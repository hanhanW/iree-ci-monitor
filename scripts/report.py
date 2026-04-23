#!/usr/bin/env python3
"""Aggregate the last N hours of JSONL and regenerate README.md + status.md.

Reads data/YYYY/MM/DD.jsonl (today + yesterday if window crosses UTC midnight),
computes per-label stats, applies alert rules, renders Markdown.
"""

from __future__ import annotations

import collections
import json
import statistics
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
README_PATH = ROOT / "README.md"
STATUS_PATH = ROOT / "status.md"

WINDOW_HOURS = 6
SPOF_LOOKBACK_DAYS = 7
RUNNER_LOOKBACK_DAYS = 7
# Labels with more distinct runners than this over the lookback window are treated
# as auto-scaler pools (ubuntu-*, azure-*, macos-*). Per-runner rows are suppressed
# for those to keep the table readable; they're already summarized by label.
PERSISTENT_LABEL_MAX = 15
# Runners that saw fewer jobs than this over the lookback window are treated as
# ephemeral autoscaler workers (their names are per-spawn, so they don't recur).
PERSISTENT_RUNNER_MIN_JOBS = 5

DISPLAY_TZ = ZoneInfo("America/Los_Angeles")

# Alert thresholds
P95_QUEUE_ALERT_S = 3600
STALE_PENDING_S = 7200
HIGH_FAILURE_RATE = 0.20
HIGH_FAILURE_MIN_N = 10


@dataclass
class LabelStats:
    label: str
    total: int = 0
    queued: int = 0
    in_progress: int = 0
    main_total: int = 0
    main_ok: int = 0
    main_fail: int = 0
    main_cancelled: int = 0
    all_ok: int = 0
    all_fail: int = 0
    all_cancelled: int = 0
    qtimes: list[float] = field(default_factory=list)
    oldest_queued_s: float = 0.0
    oldest_in_progress_s: float = 0.0
    runners: set = field(default_factory=set)

    @property
    def pending(self) -> int:
        return self.queued + self.in_progress

    @property
    def p50(self) -> float:
        return _pct(self.qtimes, 50)

    @property
    def p95(self) -> float:
        return _pct(self.qtimes, 95)

    @property
    def avg(self) -> float:
        return statistics.mean(self.qtimes) if self.qtimes else 0.0

    @property
    def main_fail_rate(self) -> float | None:
        completed = self.main_ok + self.main_fail + self.main_cancelled
        if completed == 0:
            return None
        return self.main_fail / completed

    @property
    def all_fail_rate(self) -> float | None:
        completed = self.all_ok + self.all_fail + self.all_cancelled
        if completed == 0:
            return None
        return self.all_fail / completed


@dataclass
class RunnerStats:
    name: str
    labels: set = field(default_factory=set)
    total: int = 0
    ok: int = 0
    fail: int = 0
    cancelled: int = 0
    running: int = 0
    last_seen_at: datetime | None = None

    @property
    def completed(self) -> int:
        return self.ok + self.fail + self.cancelled

    @property
    def fail_rate(self) -> float | None:
        if self.completed == 0:
            return None
        return self.fail / self.completed


def _pct(xs: list[float], p: int) -> float:
    if not xs:
        return 0.0
    xs = sorted(xs)
    k = max(0, min(len(xs) - 1, int(round((p / 100) * (len(xs) - 1)))))
    return xs[k]


def fmt_duration(s: float) -> str:
    s = int(s)
    if s < 60:
        return f"{s}s"
    if s < 3600:
        return f"{s // 60}m{s % 60:02d}s"
    if s < 86400:
        return f"{s // 3600}h{(s % 3600) // 60:02d}m"
    return f"{s // 86400}d{(s % 86400) // 3600:02d}h"


def parse_iso(ts: str | None) -> datetime | None:
    if not ts:
        return None
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def fmt_when(now: datetime, ts: datetime | None) -> str:
    if ts is None:
        return "never"
    delta = (now - ts).total_seconds()
    if delta < 0:
        delta = 0
    return f"{fmt_duration(delta)} ago"


def fmt_updated(now: datetime) -> str:
    return now.astimezone(DISPLAY_TZ).strftime("%Y-%m-%d %H:%M %Z")


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


def files_in_window(now: datetime, window_hours: int) -> list[Path]:
    start = now - timedelta(hours=window_hours)
    days: set[tuple[int, int, int]] = set()
    cur = start.replace(hour=0, minute=0, second=0, microsecond=0)
    end = now.replace(hour=0, minute=0, second=0, microsecond=0)
    while cur <= end:
        days.add((cur.year, cur.month, cur.day))
        cur += timedelta(days=1)
    return [
        DATA_DIR / f"{y:04d}" / f"{m:02d}" / f"{d:02d}.jsonl"
        for (y, m, d) in sorted(days)
    ]


def files_in_days(now: datetime, lookback_days: int) -> list[Path]:
    start = now - timedelta(days=lookback_days)
    paths: list[Path] = []
    cur = start.replace(hour=0, minute=0, second=0, microsecond=0)
    end = now.replace(hour=0, minute=0, second=0, microsecond=0)
    while cur <= end:
        paths.append(DATA_DIR / f"{cur.year:04d}" / f"{cur.month:02d}" / f"{cur.day:02d}.jsonl")
        cur += timedelta(days=1)
    return paths


def is_main_post_merge(rec: dict) -> bool:
    return rec.get("head_branch") == "main" and rec.get("event") != "pull_request"


def aggregate(now: datetime, window_hours: int) -> dict[str, LabelStats]:
    cutoff = now - timedelta(hours=window_hours)
    by_label: dict[str, LabelStats] = {}

    for path in files_in_window(now, window_hours):
        for rec in iter_jsonl(path):
            created = parse_iso(rec.get("created_at"))
            if created is None or created < cutoff:
                continue
            labels = rec.get("labels") or []
            if not labels:
                continue
            key = ",".join(labels)
            s = by_label.setdefault(key, LabelStats(label=key))
            s.total += 1

            status = rec.get("status")
            concl = rec.get("conclusion")
            main = is_main_post_merge(rec)
            if status == "completed":
                if concl == "success":
                    s.all_ok += 1
                    if main:
                        s.main_ok += 1
                elif concl == "failure":
                    s.all_fail += 1
                    if main:
                        s.main_fail += 1
                elif concl == "cancelled":
                    s.all_cancelled += 1
                    if main:
                        s.main_cancelled += 1
                if main:
                    s.main_total += 1
            elif status == "queued" or status == "waiting":
                s.queued += 1
                wait = (now - created).total_seconds()
                s.oldest_queued_s = max(s.oldest_queued_s, wait)
            elif status == "in_progress":
                s.in_progress += 1
                wait = (now - created).total_seconds()
                s.oldest_in_progress_s = max(s.oldest_in_progress_s, wait)

            rn = rec.get("runner_name")
            if rn:
                s.runners.add(rn)

            started = parse_iso(rec.get("started_at"))
            if started and created and concl != "skipped":
                q = (started - created).total_seconds()
                if q >= 0:
                    s.qtimes.append(q)

    return by_label


def aggregate_runners(
    now: datetime, lookback_days: int
) -> tuple[dict[str, RunnerStats], dict[str, set[str]]]:
    """Aggregate per-runner stats over `lookback_days`. Also returns the
    distinct-runner set per label over the same window (used for SPOF detection
    and for filtering out auto-scaler pools from the per-runner view)."""
    runners: dict[str, RunnerStats] = {}
    label_runners: dict[str, set[str]] = collections.defaultdict(set)

    for path in files_in_days(now, lookback_days):
        for rec in iter_jsonl(path):
            rn = rec.get("runner_name")
            labels = rec.get("labels") or []
            key = ",".join(labels) if labels else ""
            if rn and labels:
                label_runners[key].add(rn)
            if not rn:
                continue
            r = runners.setdefault(rn, RunnerStats(name=rn))
            if labels:
                r.labels.add(key)
            r.total += 1
            status = rec.get("status")
            concl = rec.get("conclusion")
            if status == "completed":
                if concl == "success":
                    r.ok += 1
                elif concl == "failure":
                    r.fail += 1
                elif concl == "cancelled":
                    r.cancelled += 1
                comp = parse_iso(rec.get("completed_at"))
                if comp and (r.last_seen_at is None or comp > r.last_seen_at):
                    r.last_seen_at = comp
            elif status == "in_progress":
                r.running += 1
                started = parse_iso(rec.get("started_at"))
                if started and (r.last_seen_at is None or started > r.last_seen_at):
                    r.last_seen_at = started
    return runners, dict(label_runners)


def is_persistent_runner(r: RunnerStats, label_runners: dict[str, set[str]]) -> bool:
    if r.total < PERSISTENT_RUNNER_MIN_JOBS:
        return False
    for L in r.labels:
        count = len(label_runners.get(L, set()))
        if 0 < count <= PERSISTENT_LABEL_MAX:
            return True
    return False


def fmt_labels_short(labels: set[str], limit: int = 2) -> str:
    if not labels:
        return "—"
    items = sorted(labels)
    if len(items) <= limit:
        return ", ".join(f"`{L}`" for L in items)
    head = ", ".join(f"`{L}`" for L in items[:limit])
    return f"{head}, +{len(items) - limit} more"


def spof_labels_from(label_runners: dict[str, set[str]]) -> set[str]:
    return {lab for lab, rs in label_runners.items() if len(rs) == 1}


def build_alerts(stats: dict[str, LabelStats], spof: set[str]) -> list[tuple[str, str]]:
    alerts: list[tuple[str, str]] = []
    for s in stats.values():
        if s.p95 > P95_QUEUE_ALERT_S:
            alerts.append(("queue-starved", f"`{s.label}` p95 queue {fmt_duration(s.p95)} (> {fmt_duration(P95_QUEUE_ALERT_S)})"))
        if s.oldest_queued_s > STALE_PENDING_S:
            alerts.append(("stale-queued", f"`{s.label}` oldest queued job waiting {fmt_duration(s.oldest_queued_s)} (> {fmt_duration(STALE_PENDING_S)})"))
        fr = s.main_fail_rate
        main_completed = s.main_ok + s.main_fail + s.main_cancelled
        if fr is not None and fr > HIGH_FAILURE_RATE and main_completed >= HIGH_FAILURE_MIN_N:
            alerts.append(("high-failure-main", f"`{s.label}` main-branch failure rate {fr:.0%} ({s.main_fail}/{main_completed})"))
        if s.label in spof:
            alerts.append(("spof", f"`{s.label}` single runner observed in last {SPOF_LOOKBACK_DAYS}d"))
    severity = {"stale-queued": 0, "queue-starved": 1, "high-failure-main": 2, "spof": 3}
    alerts.sort(key=lambda a: (severity.get(a[0], 99), a[1]))
    return alerts


def _runner_sort_key(r: RunnerStats):
    # Running now first, then most-recently-seen.
    last = r.last_seen_at or datetime.min.replace(tzinfo=timezone.utc)
    return (0 if r.running > 0 else 1, -last.timestamp())


def render_readme(
    now: datetime,
    stats: dict[str, LabelStats],
    alerts: list[tuple[str, str]],
    runners: dict[str, RunnerStats],
    label_runners: dict[str, set[str]],
) -> str:
    lines: list[str] = []
    lines.append("# iree-ci-monitor")
    lines.append("")
    lines.append(f"_Updated: {fmt_updated(now)}_ — `iree-org/iree`, last {WINDOW_HOURS}h")
    lines.append("")
    lines.append("Automated tracker of GitHub Actions runner health for the IREE project. ")
    lines.append("Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.")
    lines.append("")

    lines.append(f"## Top of queue (sorted by p95, last {WINDOW_HOURS}h)")
    lines.append("")
    lines.append("| label | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for s in sorted(stats.values(), key=lambda s: -s.p95):
        fr = s.main_fail_rate
        fr_s = f"{fr:.0%} ({s.main_fail}/{s.main_ok + s.main_fail + s.main_cancelled})" if fr is not None else "—"
        lines.append(
            f"| `{s.label}` | {s.total} | {s.queued} | "
            f"{fmt_duration(s.oldest_queued_s) if s.queued else '—'} | "
            f"{s.in_progress} | "
            f"{fmt_duration(s.p50)} | {fmt_duration(s.p95)} | "
            f"{fr_s} | {len(s.runners)} |"
        )
    lines.append("")

    persistent = sorted(
        (r for r in runners.values() if is_persistent_runner(r, label_runners)),
        key=_runner_sort_key,
    )
    lines.append(f"## Self-hosted runners (last {RUNNER_LOOKBACK_DAYS}d)")
    lines.append("")
    if not persistent:
        lines.append("_No persistent runners observed yet._")
    else:
        lines.append("| runner | labels | jobs | fail rate | running | last seen |")
        lines.append("|---|---|---:|---:|:---:|---:|")
        for r in persistent:
            fr = r.fail_rate
            fr_s = f"{fr:.0%} ({r.fail}/{r.completed})" if fr is not None else "—"
            running = "yes" if r.running > 0 else ""
            last_s = "running" if r.running > 0 else fmt_when(now, r.last_seen_at)
            lines.append(
                f"| `{r.name}` | {fmt_labels_short(r.labels)} | {r.total} | "
                f"{fr_s} | {running} | {last_s} |"
            )
    lines.append("")

    lines.append("## Alerts")
    if not alerts:
        lines.append("")
        lines.append("_No active alerts._")
    else:
        lines.append("")
        for tag, msg in alerts:
            lines.append(f"- **[{tag}]** {msg}")
    lines.append("")

    lines.append("See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds.")
    lines.append("")
    return "\n".join(lines)


def render_status(
    now: datetime,
    stats: dict[str, LabelStats],
    alerts: list[tuple[str, str]],
    spof: set[str],
    runners: dict[str, RunnerStats],
    label_runners: dict[str, set[str]],
) -> str:
    lines: list[str] = []
    lines.append("# Status detail")
    lines.append("")
    lines.append(f"_Updated: {fmt_updated(now)}_ — watching `iree-org/iree`, window = last {WINDOW_HOURS}h")
    lines.append("")

    lines.append("## Per-label metrics")
    lines.append("")
    lines.append("| label | jobs | queued | oldest queued | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|")
    for s in sorted(stats.values(), key=lambda s: -s.p95):
        fr_all = s.all_fail_rate
        fr_main = s.main_fail_rate
        fr_all_s = (
            f"{fr_all:.0%} ({s.all_fail}/{s.all_ok + s.all_fail + s.all_cancelled})"
            if fr_all is not None else "—"
        )
        fr_main_s = (
            f"{fr_main:.0%} ({s.main_fail}/{s.main_ok + s.main_fail + s.main_cancelled})"
            if fr_main is not None else "—"
        )
        max_q = max(s.qtimes) if s.qtimes else 0
        lines.append(
            f"| `{s.label}` | {s.total} | {s.queued} | "
            f"{fmt_duration(s.oldest_queued_s) if s.queued else '—'} | "
            f"{s.in_progress} | "
            f"{fmt_duration(s.oldest_in_progress_s) if s.in_progress else '—'} | "
            f"{fmt_duration(s.avg)} | {fmt_duration(s.p50)} | {fmt_duration(s.p95)} | "
            f"{fmt_duration(max_q)} | {fr_all_s} | {fr_main_s} | "
            f"{len(s.runners)} | {'yes' if s.label in spof else ''} |"
        )
    lines.append("")

    persistent = sorted(
        (r for r in runners.values() if is_persistent_runner(r, label_runners)),
        key=_runner_sort_key,
    )
    lines.append(f"## Per-runner metrics (self-hosted, last {RUNNER_LOOKBACK_DAYS}d)")
    lines.append("")
    lines.append(
        f"Only runners that served at least one label with ≤ {PERSISTENT_LABEL_MAX} distinct runners in the lookback window are listed. "
        "Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above."
    )
    lines.append("")
    if not persistent:
        lines.append("_No persistent runners observed yet._")
    else:
        lines.append("| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |")
        lines.append("|---|---|---:|---:|---:|---:|---:|:---:|---:|")
        for r in persistent:
            labels_s = ", ".join(f"`{L}`" for L in sorted(r.labels)) if r.labels else "—"
            fr = r.fail_rate
            fr_s = f"{fr:.0%}" if fr is not None else "—"
            running = "yes" if r.running > 0 else ""
            last_s = "running" if r.running > 0 else fmt_when(now, r.last_seen_at)
            lines.append(
                f"| `{r.name}` | {labels_s} | {r.total} | {r.ok} | {r.fail} | {r.cancelled} | "
                f"{fr_s} | {running} | {last_s} |"
            )
    lines.append("")

    lines.append("## Alerts")
    if not alerts:
        lines.append("")
        lines.append("_No active alerts._")
    else:
        lines.append("")
        for tag, msg in alerts:
            lines.append(f"- **[{tag}]** {msg}")
    lines.append("")

    lines.append("## Methodology")
    lines.append("")
    lines.append(f"- Window: last {WINDOW_HOURS} hours of job records for label metrics; last {RUNNER_LOOKBACK_DAYS} days for runner metrics and SPOF.")
    lines.append(f"- Timestamps rendered in `{DISPLAY_TZ.key}` local time; underlying records are UTC.")
    lines.append("- Queue time: `started_at - created_at`. Skipped jobs excluded.")
    lines.append("- Queued: jobs with `status == queued` or `waiting` (not yet assigned a runner).")
    lines.append("- Running: jobs with `status == in_progress` (runner assigned, executing).")
    lines.append("- Oldest queued: `now - created_at` for the oldest still-queued job. This is the actionable signal for runner starvation — a job that's been in_progress for hours is just slow, not starved.")
    lines.append("- All-jobs fail rate: over every completed job (PR + push + schedule).")
    lines.append("- Main-only fail rate: subset where `head_branch == main` and `event != pull_request` — post-merge, scheduled, and workflow_dispatch runs. PR noise excluded.")
    lines.append(f"- SPOF: label has seen only one distinct `runner_name` in the last {SPOF_LOOKBACK_DAYS} days.")
    lines.append(f"- Persistent runner: ran ≥ {PERSISTENT_RUNNER_MIN_JOBS} jobs in the lookback window AND served at least one label with ≤ {PERSISTENT_LABEL_MAX} distinct runners. Ephemeral auto-scaler worker names (which appear once per spawn) are excluded.")
    lines.append("- Re-runs: `(job_id, run_attempt)` tuples are distinct; a re-run counts as a new job.")
    lines.append("")

    lines.append("## Alert thresholds")
    lines.append("")
    lines.append(f"- `queue-starved`: p95 queue > {fmt_duration(P95_QUEUE_ALERT_S)}")
    lines.append(f"- `stale-queued`: oldest queued job (not yet started) > {fmt_duration(STALE_PENDING_S)}")
    lines.append(f"- `high-failure-main`: main-only failure rate > {HIGH_FAILURE_RATE:.0%} with ≥ {HIGH_FAILURE_MIN_N} completed main-only jobs")
    lines.append(f"- `spof`: only one distinct runner in last {SPOF_LOOKBACK_DAYS}d")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    now = datetime.now(timezone.utc)
    stats = aggregate(now, WINDOW_HOURS)
    runners, label_runners = aggregate_runners(now, RUNNER_LOOKBACK_DAYS)
    spof = spof_labels_from(label_runners)
    alerts = build_alerts(stats, spof)

    README_PATH.write_text(render_readme(now, stats, alerts, runners, label_runners))
    STATUS_PATH.write_text(render_status(now, stats, alerts, spof, runners, label_runners))
    print(
        f"[report] labels={len(stats)} alerts={len(alerts)} "
        f"spof={len(spof)} runners={len(runners)}",
        flush=True,
    )


if __name__ == "__main__":
    main()
