#!/usr/bin/env python3
"""Collect benchmark result rows from PkgCI summary artifacts.

PkgCI jobs upload small artifacts such as
`torch_models_amdgpu_mi325_summary.json` containing `job_summary.json`. Those
files contain the actual benchmark rows shown in the GitHub Actions run summary,
for example `sdxl/clip_benchmark_mi325.json` with `Current Time (ms)`.

The IREE test suites currently emit two time-result schemas:

* Torch models: `{"benchmark": {"headers": [...], "rows": [...]}}`
* Sharktank models: `{"time_summary": [[model, submodel, current, golden], ...]}`
"""

from __future__ import annotations

import argparse
import io
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable

REPO = os.environ.get("IREE_CI_MONITOR_REPO", "iree-org/iree")
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
BENCHMARK_DATA_DIR = DATA_DIR / "benchmarks"
DEFAULT_LOOKBACK_DAYS = 90
RATE_LIMIT_MAX_SLEEP_S = 300
MAX_PAGES = 60
_TOKEN: str | None = None


def log(msg: str) -> None:
    print(f"[benchmark_collect] {msg}", flush=True)


def parse_iso(ts: str | None) -> datetime | None:
    if not ts:
        return None
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def fmt_iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def parse_now() -> datetime:
    override = os.environ.get("IREE_CI_MONITOR_NOW")
    if not override:
        return datetime.now(timezone.utc)
    parsed = parse_iso(override)
    if parsed is None:
        raise ValueError("IREE_CI_MONITOR_NOW must be an ISO-8601 timestamp")
    return parsed.astimezone(timezone.utc)


def token() -> str:
    global _TOKEN
    if _TOKEN:
        return _TOKEN
    env_token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if env_token:
        _TOKEN = env_token
        return _TOKEN
    try:
        _TOKEN = subprocess.check_output(
            ["gh", "auth", "token"], text=True, stderr=subprocess.DEVNULL
        ).strip()
        return _TOKEN
    except (FileNotFoundError, subprocess.CalledProcessError):
        sys.exit("GITHUB_TOKEN not set and `gh auth token` failed")


def _rate_limit_wait(e: urllib.error.HTTPError) -> int | None:
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
    if not link_header:
        return None
    for part in link_header.split(","):
        segs = [s.strip() for s in part.split(";")]
        if len(segs) < 2 or not (segs[0].startswith("<") and segs[0].endswith(">")):
            continue
        if any(rel == 'rel="next"' for rel in segs[1:]):
            return segs[0][1:-1]
    return None


def gh_response(
    path_or_url: str, params: dict | None = None, *, raw: bool = False
) -> tuple[dict | bytes, dict]:
    if path_or_url.startswith("http"):
        url = path_or_url
    else:
        url = f"https://api.github.com{path_or_url}"
    if params:
        sep = "&" if "?" in url else "?"
        url += sep + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token()}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "iree-ci-monitor",
        },
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                body = resp.read()
                headers = {k.lower(): v for k, v in resp.headers.items()}
                return (body if raw else json.loads(body)), headers
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


def gh_request(path_or_url: str, params: dict | None = None, *, raw: bool = False):
    body, _ = gh_response(path_or_url, params, raw=raw)
    return body


def paginate(path: str, params: dict | None = None, list_key: str | None = None):
    params = dict(params or {})
    params.setdefault("per_page", 100)
    next_url: str | None = None
    detected_key = list_key
    for _ in range(MAX_PAGES):
        if next_url is None:
            body, headers = gh_response(path, params)
        else:
            body, headers = gh_response(next_url)
        if detected_key is None:
            if isinstance(body, list):
                yield from body
                return
            for candidate in ("artifacts", "workflow_runs", "jobs"):
                if isinstance(body, dict) and candidate in body:
                    detected_key = candidate
                    break
        if detected_key is None:
            return
        yield from body.get(detected_key, [])
        next_url = _parse_next_link(headers.get("link"))
        if not next_url:
            return
    raise RuntimeError(f"hit MAX_PAGES={MAX_PAGES} on {path}; refusing to truncate")


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def download_artifact_zip(archive_download_url: str) -> bytes:
    """Download an Actions artifact without forwarding GitHub auth to blob storage."""
    req = urllib.request.Request(
        archive_download_url,
        headers={
            "Authorization": f"Bearer {token()}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "iree-ci-monitor",
        },
    )
    opener = urllib.request.build_opener(_NoRedirect)
    try:
        with opener.open(req, timeout=60) as resp:
            location = resp.headers.get("Location")
            if not location:
                return resp.read()
    except urllib.error.HTTPError as e:
        if e.code not in (301, 302, 303, 307, 308):
            raise
        location = e.headers.get("Location")
        if not location:
            raise
    raw_req = urllib.request.Request(
        location,
        headers={"User-Agent": "iree-ci-monitor"},
    )
    with urllib.request.urlopen(raw_req, timeout=120) as resp:
        return resp.read()


def iter_jsonl(path: Path) -> Iterable[dict]:
    if not path.exists():
        return
    with path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def files_in_days(now: datetime, lookback_days: int, data_dir: Path = DATA_DIR) -> list[Path]:
    start = now - timedelta(days=lookback_days)
    paths: list[Path] = []
    cur = start.replace(hour=0, minute=0, second=0, microsecond=0)
    end = now.replace(hour=0, minute=0, second=0, microsecond=0)
    while cur <= end:
        paths.append(data_dir / f"{cur.year:04d}" / f"{cur.month:02d}" / f"{cur.day:02d}.jsonl")
        cur += timedelta(days=1)
    return paths


def discover_main_pkgci_runs(
    now: datetime, lookback_days: int, data_dir: Path = DATA_DIR
) -> dict[int, dict]:
    cutoff = now - timedelta(days=lookback_days)
    runs: dict[int, dict] = {}
    for path in files_in_days(now, lookback_days, data_dir):
        for rec in iter_jsonl(path):
            created = parse_iso(rec.get("created_at"))
            if created is None or created < cutoff or created > now:
                continue
            if rec.get("workflow_name") != "PkgCI":
                continue
            if rec.get("head_branch") != "main" or rec.get("event") == "pull_request":
                continue
            try:
                run_id = int(rec["run_id"])
            except (KeyError, TypeError, ValueError):
                continue
            info = runs.setdefault(
                run_id,
                {
                    "run_id": run_id,
                    "workflow_name": rec.get("workflow_name"),
                    "workflow_path": rec.get("workflow_path"),
                    "head_branch": rec.get("head_branch"),
                    "event": rec.get("event"),
                    "head_sha": rec.get("head_sha"),
                    "commit_message": rec.get("commit_message"),
                    "run_attempt": rec.get("run_attempt"),
                    "run_html_url": rec.get("run_html_url"),
                    "created_at": rec.get("created_at"),
                },
            )
            if rec.get("head_sha"):
                info["head_sha"] = rec.get("head_sha")
            if rec.get("commit_message"):
                info["commit_message"] = rec.get("commit_message")
            if rec.get("run_attempt"):
                info["run_attempt"] = rec.get("run_attempt")
            if rec.get("run_html_url"):
                info["run_html_url"] = rec.get("run_html_url")
    return runs


def is_summary_artifact(artifact: dict) -> bool:
    name = artifact.get("name") or ""
    return name.endswith("_summary.json") and not artifact.get("expired")


def number_or_none(value):
    if value in (None, "N/A", ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def row_dict(headers: list, row: list) -> dict:
    return {str(h): row[i] if i < len(row) else None for i, h in enumerate(headers)}


def infer_backend_from_artifact_name(name: str | None) -> str | None:
    """Infer Sharktank backend suffixes from PkgCI summary artifact names."""
    if not name:
        return None
    lowered = name.lower()
    if any(token in lowered for token in ("rocm", "amdgpu", "hip")):
        return "rocm"
    if "cpu" in lowered:
        return "cpu"
    return None


def sharktank_benchmark_name(
    model_name: str | None, submodel_name: str | None, artifact_name: str | None
) -> str | None:
    if not model_name or not submodel_name:
        return None
    backend = infer_backend_from_artifact_name(artifact_name)
    stem = submodel_name
    if backend and not stem.endswith(f"_{backend}"):
        stem = f"{stem}_{backend}"
    return f"{model_name}/{stem}.json"


def normalized_record(
    *,
    run: dict,
    artifact: dict,
    collected_at: datetime,
    section: str,
    name: str,
    current_time_ms: float,
    golden_time_ms: float | None = None,
    tolerance_factor: float | None = None,
    threshold_ms: float | None = None,
    status: str | None = None,
) -> dict:
    artifact_created = artifact.get("created_at")
    return {
        "schema_version": 1,
        "repo": REPO,
        "run_id": int(run["run_id"]),
        "run_attempt": run.get("run_attempt"),
        "run_html_url": run.get("run_html_url")
        or f"https://github.com/{REPO}/actions/runs/{run['run_id']}",
        "workflow_name": run.get("workflow_name"),
        "workflow_path": run.get("workflow_path"),
        "head_branch": run.get("head_branch"),
        "event": run.get("event"),
        "head_sha": run.get("head_sha"),
        "commit_message": run.get("commit_message"),
        "run_created_at": run.get("created_at"),
        "artifact_id": int(artifact["id"]),
        "artifact_name": artifact.get("name"),
        "artifact_created_at": artifact_created,
        "collected_at": fmt_iso(collected_at),
        "section": section,
        "name": name,
        "current_time_ms": current_time_ms,
        "golden_time_ms": golden_time_ms,
        "tolerance_factor": tolerance_factor,
        "threshold_ms": threshold_ms,
        "status": status,
        "source_file": "job_summary.json",
    }


def normalized_records_from_summary(
    summary: dict,
    *,
    run: dict,
    artifact: dict,
    collected_at: datetime,
) -> list[dict]:
    records: list[dict] = []
    benchmark = summary.get("benchmark")
    if isinstance(benchmark, dict):
        headers = list(benchmark.get("headers") or [])
        for row in benchmark.get("rows") or []:
            values = row_dict(headers, list(row))
            name = values.get("Name")
            current = number_or_none(values.get("Current Time (ms)"))
            if not name or current is None:
                continue
            records.append(
                normalized_record(
                    run=run,
                    artifact=artifact,
                    collected_at=collected_at,
                    section="benchmark",
                    name=name,
                    current_time_ms=current,
                    golden_time_ms=number_or_none(values.get("Golden Time (ms)")),
                    tolerance_factor=number_or_none(values.get("Tolerance Factor")),
                    threshold_ms=number_or_none(values.get("Threshold (ms)")),
                    status=values.get("Status"),
                )
            )

    for row in summary.get("time_summary") or []:
        values = list(row)
        if len(values) < 4:
            continue
        name = sharktank_benchmark_name(values[0], values[1], artifact.get("name"))
        current = number_or_none(values[2])
        if not name or current is None:
            continue
        records.append(
            normalized_record(
                run=run,
                artifact=artifact,
                collected_at=collected_at,
                section="time_summary",
                name=name,
                current_time_ms=current,
                golden_time_ms=number_or_none(values[3]),
                status="REPORTED",
            )
        )
    return records


def records_from_artifact(run: dict, artifact: dict, collected_at: datetime) -> list[dict]:
    blob = download_artifact_zip(artifact["archive_download_url"])
    records: list[dict] = []
    with zipfile.ZipFile(io.BytesIO(blob)) as archive:
        for member in archive.namelist():
            if member.endswith("job_summary.json"):
                with archive.open(member) as f:
                    summary = json.load(f)
                records.extend(
                    normalized_records_from_summary(
                        summary, run=run, artifact=artifact, collected_at=collected_at
                    )
                )
    return records


def output_path_for(ts: str | None, fallback: datetime) -> Path:
    dt = parse_iso(ts) or fallback
    dt = dt.astimezone(timezone.utc)
    return BENCHMARK_DATA_DIR / f"{dt.year:04d}" / f"{dt.month:02d}" / f"{dt.day:02d}.jsonl"


def existing_keys(path: Path) -> set[tuple[int, int, str]]:
    keys: set[tuple[int, int, str]] = set()
    if not path.exists():
        return keys
    for rec in iter_jsonl(path):
        try:
            keys.add((int(rec["run_id"]), int(rec["artifact_id"]), str(rec["name"])))
        except (KeyError, TypeError, ValueError):
            continue
    return keys


def existing_artifact_ids(data_dir: Path = BENCHMARK_DATA_DIR) -> set[int]:
    ids: set[int] = set()
    for path in data_dir.glob("**/*.jsonl"):
        for rec in iter_jsonl(path):
            try:
                ids.add(int(rec["artifact_id"]))
            except (KeyError, TypeError, ValueError):
                continue
    return ids


def append_jsonl(path: Path, records: list[dict]) -> int:
    if not records:
        return 0
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = existing_keys(path)
    fresh = [
        r
        for r in records
        if (int(r["run_id"]), int(r["artifact_id"]), str(r["name"])) not in existing
    ]
    if not fresh:
        return 0
    with path.open("a") as f:
        for rec in fresh:
            f.write(json.dumps(rec, sort_keys=True))
            f.write("\n")
    return len(fresh)


def enrich_run_from_api(run: dict) -> dict:
    if (
        run.get("head_sha")
        and run.get("run_html_url")
        and run.get("commit_message")
        and run.get("run_attempt")
    ):
        return run
    body = gh_request(f"/repos/{REPO}/actions/runs/{run['run_id']}")
    run = dict(run)
    run["head_sha"] = run.get("head_sha") or body.get("head_sha")
    head_commit = body.get("head_commit") or {}
    run["commit_message"] = run.get("commit_message") or head_commit.get("message")
    run["run_attempt"] = run.get("run_attempt") or body.get("run_attempt")
    run["run_html_url"] = run.get("run_html_url") or body.get("html_url")
    run["created_at"] = run.get("created_at") or body.get("created_at")
    run["event"] = run.get("event") or body.get("event")
    run["head_branch"] = run.get("head_branch") or body.get("head_branch")
    run["workflow_name"] = run.get("workflow_name") or body.get("name")
    run["workflow_path"] = run.get("workflow_path") or body.get("path")
    return run


def collect_benchmarks(lookback_days: int, now: datetime | None = None) -> int:
    now = now or parse_now()
    runs = discover_main_pkgci_runs(now, lookback_days)
    log(f"runs to inspect: {len(runs)}")
    seen_artifact_ids = existing_artifact_ids()
    total = 0
    for run_id in sorted(runs):
        run = enrich_run_from_api(runs[run_id])
        artifacts = [
            a
            for a in paginate(
                f"/repos/{REPO}/actions/runs/{run_id}/artifacts",
                list_key="artifacts",
            )
            if is_summary_artifact(a)
        ]
        if not artifacts:
            continue
        log(f"run {run_id}: {len(artifacts)} summary artifacts")
        for artifact in artifacts:
            try:
                artifact_id = int(artifact["id"])
            except (KeyError, TypeError, ValueError):
                continue
            if artifact_id in seen_artifact_ids:
                continue
            try:
                records = records_from_artifact(run, artifact, now)
            except (urllib.error.HTTPError, zipfile.BadZipFile, json.JSONDecodeError) as e:
                log(f"run {run_id} artifact {artifact.get('name')}: skipped ({e})")
                continue
            path = output_path_for(artifact.get("created_at"), now)
            count = append_jsonl(path, records)
            total += count
            if count:
                seen_artifact_ids.add(artifact_id)
            if count:
                log(f"{path.relative_to(ROOT)}: +{count} from {artifact.get('name')}")
    log(f"total new benchmark records: {total}")
    return total


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--lookback-days",
        type=int,
        default=int(os.environ.get("IREE_BENCHMARK_LOOKBACK_DAYS", DEFAULT_LOOKBACK_DAYS)),
    )
    args = parser.parse_args()
    collect_benchmarks(args.lookback_days)


if __name__ == "__main__":
    main()
