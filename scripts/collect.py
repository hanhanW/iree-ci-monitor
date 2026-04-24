#!/usr/bin/env python3
"""Collect GitHub Actions runs+jobs for iree-org/iree and append to JSONL.

Run order each tick:
  1. Scan recent runs (2h re-scan window, unions with open runs from state).
  2. Pull jobs for each run.
  3. Dedupe against today's JSONL, append new records.
  4. Update .state.json.

Usage: python scripts/collect.py

Env:
  GITHUB_TOKEN (required) - used for authenticated API access.
  IREE_CI_MONITOR_REPO (optional) - override watched repo (default: iree-org/iree).
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = os.environ.get("IREE_CI_MONITOR_REPO", "iree-org/iree")
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
STATE_PATH = DATA_DIR / ".state.json"

RESCAN_HOURS = 7
INITIAL_BACKFILL_HOURS = 24
MAX_PAGES = 60  # safety cap on pagination depth; raises on hit
MAX_OPEN_AGE_DAYS = 3  # drop tracked open runs older than this
RATE_LIMIT_MAX_SLEEP_S = 300  # cap any single rate-limit wait


def log(msg: str) -> None:
    print(f"[collect] {msg}", flush=True)


def _rate_limit_wait(e: urllib.error.HTTPError) -> int | None:
    """Return seconds to wait if `e` is a GitHub rate-limit response, else None.

    GitHub uses 403 with `X-RateLimit-Remaining: 0` for the primary limit and
    may use 429 (or 403 with `Retry-After`) for secondary/abuse limits."""
    if e.code not in (403, 429):
        return None
    retry_after = e.headers.get("Retry-After")
    if retry_after:
        try:
            return min(max(1, int(retry_after)), RATE_LIMIT_MAX_SLEEP_S)
        except ValueError:
            return 60
    if e.headers.get("X-RateLimit-Remaining") == "0":
        reset = e.headers.get("X-RateLimit-Reset")
        if reset:
            try:
                wait = int(reset) - int(time.time())
                return max(1, min(wait, RATE_LIMIT_MAX_SLEEP_S))
            except ValueError:
                return 60
    return None


def _parse_next_link(link_header: str | None) -> str | None:
    """Extract the rel=next URL from a GitHub `Link` header, if any."""
    if not link_header:
        return None
    for part in link_header.split(","):
        segs = [s.strip() for s in part.split(";")]
        if len(segs) < 2 or not (segs[0].startswith("<") and segs[0].endswith(">")):
            continue
        url = segs[0][1:-1]
        if any(rel == 'rel="next"' for rel in segs[1:]):
            return url
    return None


def gh_request(path_or_url: str, params: dict | None = None) -> tuple[dict, dict]:
    if path_or_url.startswith("http"):
        url = path_or_url
    else:
        url = f"https://api.github.com{path_or_url}"
    if params:
        sep = "&" if "?" in url else "?"
        url += sep + urllib.parse.urlencode(params)
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN not set")
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "iree-ci-monitor",
        },
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                body = json.loads(resp.read())
                # Lowercase keys so callers don't depend on server's header case.
                headers = {k.lower(): v for k, v in resp.headers.items()}
                return body, headers
        except urllib.error.HTTPError as e:
            wait = _rate_limit_wait(e)
            if wait is not None and attempt < 2:
                log(f"rate limited ({e.code}); sleeping {wait}s")
                time.sleep(wait)
                continue
            if e.code in (502, 503, 504) and attempt < 2:
                time.sleep(2 ** attempt)
                continue
            raise
        except urllib.error.URLError:
            if attempt < 2:
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError("unreachable")


def paginate(path: str, params: dict | None = None):
    params = dict(params or {})
    params.setdefault("per_page", 100)
    next_url: str | None = None
    list_key: str | None = None
    for _ in range(MAX_PAGES):
        if next_url is None:
            body, headers = gh_request(path, params)
        else:
            body, headers = gh_request(next_url)
        if list_key is None:
            for candidate in ("workflow_runs", "jobs"):
                if isinstance(body, dict) and candidate in body:
                    list_key = candidate
                    break
            if list_key is None:
                if isinstance(body, list):
                    yield from body
                return
        yield from body.get(list_key, [])
        next_url = _parse_next_link(headers.get("link"))
        if not next_url:
            return
    raise RuntimeError(
        f"hit MAX_PAGES={MAX_PAGES} on {path}; refusing to truncate. "
        "Bump MAX_PAGES or narrow the query window."
    )


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {"last_completed_run_id": 0, "open_run_ids": []}
    with STATE_PATH.open() as f:
        s = json.load(f)
    s.setdefault("last_completed_run_id", 0)
    s.setdefault("open_run_ids", [])
    return s


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(state, f, indent=2, sort_keys=True)
    tmp.replace(STATE_PATH)


def jsonl_path_for(dt: datetime) -> Path:
    return DATA_DIR / f"{dt.year:04d}" / f"{dt.month:02d}" / f"{dt.day:02d}.jsonl"


def existing_keys_for_day(path: Path) -> set[tuple[int, int, str]]:
    """Return (job_id, run_attempt, status) tuples already recorded for this day.

    Status is part of the key so state transitions (queued -> in_progress ->
    completed) each produce a new JSONL line, while re-running collect with no
    state change appends zero lines. Without status in the key, the first
    snapshot (often queued) would lock the record forever — making the reader
    believe a long-completed job is still queued.
    """
    keys: set[tuple[int, int, str]] = set()
    if not path.exists():
        return keys
    with path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            k = (
                int(obj["job_id"]),
                int(obj.get("run_attempt", 1)),
                str(obj.get("status", "")),
            )
            keys.add(k)
    return keys


def append_jsonl(path: Path, records: list[dict]) -> None:
    if not records:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        for r in records:
            f.write(json.dumps(r, sort_keys=True))
            f.write("\n")


def parse_iso(ts: str | None) -> datetime | None:
    if not ts:
        return None
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def day_bucket(ts: str | None, fallback: datetime) -> datetime:
    dt = parse_iso(ts) or fallback
    return dt.astimezone(timezone.utc)


def normalize_job(job: dict, run: dict) -> dict:
    return {
        "run_id": int(job["run_id"]),
        "run_attempt": int(job.get("run_attempt", 1)),
        "job_id": int(job["id"]),
        "workflow_id": int(run.get("workflow_id", 0)) or None,
        "workflow_name": run.get("name") or job.get("workflow_name"),
        "name": job.get("name"),
        "labels": list(job.get("labels") or []),
        "runner_name": job.get("runner_name"),
        "status": job.get("status"),
        "conclusion": job.get("conclusion"),
        "event": run.get("event"),
        "head_branch": run.get("head_branch"),
        "created_at": job.get("created_at"),
        "started_at": job.get("started_at"),
        "completed_at": job.get("completed_at"),
    }


def collect() -> None:
    now = datetime.now(timezone.utc)
    state = load_state()

    if not state["last_completed_run_id"] and not state["open_run_ids"]:
        window_hours = INITIAL_BACKFILL_HOURS
        log(f"cold start: backfilling {window_hours}h")
    else:
        window_hours = RESCAN_HOURS

    since = (now - timedelta(hours=window_hours)).strftime("%Y-%m-%dT%H:%M:%SZ")
    log(f"scanning /repos/{REPO}/actions/runs?created=>{since}")

    seen_run_ids: set[int] = set()
    runs_by_id: dict[int, dict] = {}
    for run in paginate(f"/repos/{REPO}/actions/runs", {"created": f">={since}"}):
        rid = int(run["id"])
        seen_run_ids.add(rid)
        runs_by_id[rid] = run

    # Union with previously-open runs.
    for rid in state["open_run_ids"]:
        if rid in seen_run_ids:
            continue
        try:
            body, _ = gh_request(f"/repos/{REPO}/actions/runs/{rid}")
            runs_by_id[int(body["id"])] = body
            seen_run_ids.add(int(body["id"]))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                log(f"open run {rid} vanished (404); dropping")
            else:
                raise

    log(f"runs to process: {len(runs_by_id)}")

    # Pull jobs per run, grouped by day-bucket.
    by_day: dict[Path, list[dict]] = {}
    still_open: list[int] = []
    dropped_stale = 0
    max_completed_id = state["last_completed_run_id"]
    open_age_cutoff = now - timedelta(days=MAX_OPEN_AGE_DAYS)

    for rid, run in runs_by_id.items():
        jobs = list(
            paginate(f"/repos/{REPO}/actions/runs/{rid}/jobs", {"filter": "latest"})
        )
        fallback_dt = parse_iso(run.get("created_at")) or now
        for job in jobs:
            rec = normalize_job(job, run)
            bucket = day_bucket(rec["created_at"], fallback_dt)
            path = jsonl_path_for(bucket)
            by_day.setdefault(path, []).append(rec)
        if run.get("status") == "completed":
            max_completed_id = max(max_completed_id, rid)
        else:
            run_created = parse_iso(run.get("created_at"))
            # Drop if missing created_at too — otherwise the run sticks in
            # open_run_ids forever, defeating the age cap.
            if run_created is None or run_created < open_age_cutoff:
                dropped_stale += 1
            else:
                still_open.append(rid)

    # Dedupe + append per day file.
    total_new = 0
    for path, recs in by_day.items():
        existing = existing_keys_for_day(path)
        fresh = [
            r for r in recs
            if (r["job_id"], r["run_attempt"], r.get("status", "")) not in existing
        ]
        append_jsonl(path, fresh)
        total_new += len(fresh)
        log(f"{path.relative_to(ROOT)}: +{len(fresh)} (had {len(existing)})")
    log(f"total new job records: {total_new}")

    state = {
        "last_completed_run_id": max_completed_id,
        "open_run_ids": sorted(set(still_open)),
    }
    save_state(state)
    log(
        f"state: last_completed={max_completed_id} open={len(still_open)} "
        f"dropped_stale={dropped_stale}"
    )


if __name__ == "__main__":
    collect()
