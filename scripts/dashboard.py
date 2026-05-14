#!/usr/bin/env python3
"""Generate a static main-branch benchmark dashboard.

Milestone 1 intentionally has no backend. This script reads normalized PkgCI
benchmark result rows under data/benchmarks and writes a GitHub Pages-compatible
static site under docs/.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import statistics
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable

REPO = os.environ.get("IREE_CI_MONITOR_REPO", "iree-org/iree")
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
BENCHMARK_DATA_DIR = DATA_DIR / "benchmarks"
DOCS_DIR = ROOT / "docs"
DEFAULT_LOOKBACK_DAYS = 90
DISPLAY_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
PR_TITLE_RE = re.compile(r"^(?P<title>.+?)\s+\(#(?P<number>\d+)\)$")


def parse_iso(ts: str | None) -> datetime | None:
    if not ts:
        return None
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def fmt_iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime(DISPLAY_TIME_FORMAT)


def parse_now() -> datetime:
    override = os.environ.get("IREE_CI_MONITOR_NOW")
    if not override:
        return datetime.now(timezone.utc)
    parsed = parse_iso(override)
    if parsed is None:
        raise ValueError("IREE_CI_MONITOR_NOW must be an ISO-8601 timestamp")
    return parsed.astimezone(timezone.utc)


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


def read_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError:
        return None


def files_in_days(now: datetime, lookback_days: int, data_dir: Path = DATA_DIR) -> list[Path]:
    start = now - timedelta(days=lookback_days)
    paths: list[Path] = []
    cur = start.replace(hour=0, minute=0, second=0, microsecond=0)
    end = now.replace(hour=0, minute=0, second=0, microsecond=0)
    while cur <= end:
        paths.append(data_dir / f"{cur.year:04d}" / f"{cur.month:02d}" / f"{cur.day:02d}.jsonl")
        cur += timedelta(days=1)
    return paths


def iter_latest_per_job(paths: Iterable[Path]) -> Iterable[dict]:
    latest: dict[tuple[int, int], dict] = {}
    for path in paths:
        for rec in iter_jsonl(path):
            try:
                key = (int(rec["job_id"]), int(rec.get("run_attempt", 1)))
            except (KeyError, TypeError, ValueError):
                continue
            latest[key] = rec
    yield from latest.values()


def seconds_between(start: str | None, end: str | None) -> float | None:
    start_dt = parse_iso(start)
    end_dt = parse_iso(end)
    if start_dt is None or end_dt is None:
        return None
    seconds = (end_dt - start_dt).total_seconds()
    return seconds if seconds >= 0 else None


def workflow_label(rec: dict) -> str:
    return rec.get("workflow_path") or rec.get("workflow_name") or "unknown"


def is_main_post_merge(rec: dict) -> bool:
    return rec.get("head_branch") == "main" and rec.get("event") != "pull_request"


def is_benchmark_record(rec: dict) -> bool:
    """Return true for milestone-1 benchmark-like main jobs.

    The historical data does not contain benchmark result payloads, so the first
    dashboard tracks timing/result trends for main-branch PkgCI test jobs. The
    classifier is intentionally narrow to avoid mixing setup/build jobs into the
    benchmark proxy view.
    """
    if not is_main_post_merge(rec):
        return False
    name = rec.get("name") or ""
    workflow = workflow_label(rec).lower()
    workflow_name = (rec.get("workflow_name") or "").lower()
    if "pkgci" not in workflow and "pkgci" not in workflow_name:
        return False
    return name.startswith("Test ")


def _median(values: list[float]) -> float | None:
    return statistics.median(values) if values else None


def _artifact_target(name: str | None) -> str:
    if not name:
        return "unknown"
    for suffix in ("_summary.json", ".json"):
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return name


def _commit_subject(message: str | None) -> str | None:
    if not message:
        return None
    first = message.splitlines()[0].strip()
    return first or None


def _pr_title(subject: str | None) -> str | None:
    if not subject:
        return None
    match = PR_TITLE_RE.match(subject)
    if not match:
        return None
    return match.group("title").strip()


def _suite_configs(suite_manifest: dict | None, kind: str | None = None) -> list[dict]:
    configs: list[dict] = []
    if not suite_manifest:
        return configs
    for suite in suite_manifest.get("suites") or []:
        suite_name = suite.get("name") or "unknown"
        for config in suite.get("configs") or []:
            if kind is not None and config.get("kind") != kind:
                continue
            entry = dict(config)
            entry["suite"] = suite_name
            configs.append(entry)
    return configs


def _point_matches_config(point: dict, config: dict) -> bool:
    benchmark = point.get("benchmark") or ""
    config_path = config.get("path") or ""
    config_name = config.get("name") or Path(config_path).name
    return (
        benchmark == config_path
        or benchmark == config_name
        or config_path.endswith("/" + benchmark)
    )


def _infer_suite(point: dict, suite_manifest: dict | None) -> str | None:
    suite_names = [
        suite.get("name")
        for suite in (suite_manifest or {}).get("suites", [])
        if suite.get("name")
    ]
    target = point.get("target") or point.get("labels_key") or ""
    for suite_name in sorted(suite_names, key=len, reverse=True):
        if target == suite_name or target.startswith(suite_name + "_"):
            return suite_name
    for config in _suite_configs(suite_manifest, kind="benchmark"):
        if _point_matches_config(point, config):
            return config["suite"]
    return None


def _annotate_suites(points: list[dict], suite_manifest: dict | None) -> None:
    for point in points:
        suite = _infer_suite(point, suite_manifest)
        if suite:
            point["suite"] = suite


def _suite_coverage(suite_manifest: dict | None, points: list[dict]) -> list[dict]:
    if not suite_manifest:
        return []
    rows = []
    benchmark_configs = _suite_configs(suite_manifest, kind="benchmark")
    points_by_suite: Counter[str] = Counter()
    observed_names_by_suite: dict[str, set[str]] = {}
    matched_configs_by_suite: dict[str, set[str]] = {}
    for point in points:
        suite = point.get("suite") or "unmatched"
        points_by_suite[suite] += 1
        observed_names_by_suite.setdefault(suite, set()).add(point.get("benchmark") or "unknown")
        for config in benchmark_configs:
            if config["suite"] == suite and _point_matches_config(point, config):
                matched_configs_by_suite.setdefault(suite, set()).add(config["path"])
    for suite in suite_manifest.get("suites") or []:
        suite_name = suite.get("name") or "unknown"
        configured = [
            config
            for config in suite.get("configs") or []
            if config.get("kind") == "benchmark"
        ]
        matched = matched_configs_by_suite.get(suite_name, set())
        missing = [config["path"] for config in configured if config["path"] not in matched]
        rows.append(
            {
                "suite": suite_name,
                "suite_url": suite.get("html_url"),
                "configured_benchmarks": len(configured),
                "observed_configured_benchmarks": len(matched),
                "observed_benchmark_names": len(observed_names_by_suite.get(suite_name, set())),
                "points": points_by_suite.get(suite_name, 0),
                "missing_benchmark_examples": missing[:8],
            }
        )
    if points_by_suite.get("unmatched"):
        rows.append(
            {
                "suite": "unmatched",
                "suite_url": None,
                "configured_benchmarks": 0,
                "observed_configured_benchmarks": 0,
                "observed_benchmark_names": len(observed_names_by_suite.get("unmatched", set())),
                "points": points_by_suite["unmatched"],
                "missing_benchmark_examples": [],
            }
        )
    return rows


def _benchmark_files_in_days(
    now: datetime, lookback_days: int, data_dir: Path
) -> list[Path]:
    return files_in_days(now, lookback_days, data_dir / "benchmarks")


def _benchmark_result_points(
    now: datetime,
    lookback_days: int,
    data_dir: Path,
) -> tuple[list[dict], Counter]:
    cutoff = now - timedelta(days=lookback_days)
    points: list[dict] = []
    skipped = Counter()
    for path in _benchmark_files_in_days(now, lookback_days, data_dir):
        for rec in iter_jsonl(path):
            created = (
                parse_iso(rec.get("artifact_created_at"))
                or parse_iso(rec.get("run_created_at"))
                or parse_iso(rec.get("collected_at"))
            )
            if created is None or created < cutoff or created > now:
                continue
            if rec.get("head_branch") != "main" or rec.get("event") == "pull_request":
                skipped["non_main"] += 1
                continue
            current = rec.get("current_time_ms")
            if not isinstance(current, (int, float)):
                skipped["missing_current_time_ms"] += 1
                continue
            run_id = int(rec["run_id"])
            head_sha = rec.get("head_sha")
            artifact_name = rec.get("artifact_name") or "unknown"
            target = _artifact_target(artifact_name)
            benchmark = rec.get("name") or "unknown"
            commit_subject = _commit_subject(rec.get("commit_message"))
            points.append(
                {
                    "created_at": fmt_iso(created),
                    "commit": head_sha,
                    "commit_short": head_sha[:12] if head_sha else None,
                    "commit_subject": commit_subject,
                    "commit_url": f"https://github.com/{REPO}/commit/{head_sha}" if head_sha else None,
                    "pr_title": _pr_title(commit_subject),
                    "run_id": run_id,
                    "run_url": rec.get("run_html_url") or f"https://github.com/{REPO}/actions/runs/{run_id}",
                    "artifact_id": rec.get("artifact_id"),
                    "artifact_name": artifact_name,
                    "benchmark": benchmark,
                    "labels_key": target,
                    "target": target,
                    "status": rec.get("status"),
                    "result_status": rec.get("status"),
                    "current_time_ms": round(float(current), 6),
                    "golden_time_ms": rec.get("golden_time_ms"),
                    "threshold_ms": rec.get("threshold_ms"),
                    "tolerance_factor": rec.get("tolerance_factor"),
                    "metric": "current_time_ms",
                    "unit": "ms",
                }
            )
    points.sort(key=lambda p: (p["created_at"], p["run_id"], p["benchmark"], p["labels_key"]))
    return points, skipped


def _job_timing_proxy_points(
    now: datetime,
    lookback_days: int,
    data_dir: Path,
) -> tuple[list[dict], Counter]:
    cutoff = now - timedelta(days=lookback_days)
    points: list[dict] = []
    skipped = Counter()
    for rec in iter_latest_per_job(files_in_days(now, lookback_days, data_dir)):
        created = parse_iso(rec.get("created_at"))
        if created is None or created < cutoff or created > now:
            continue
        if not is_benchmark_record(rec):
            skipped["non_benchmark_or_non_main"] += 1
            continue
        if not rec.get("labels"):
            skipped["unlabeled"] += 1
            continue
        if rec.get("status") != "completed" or rec.get("conclusion") == "skipped":
            skipped["not_completed_benchmark"] += 1
            continue
        duration_s = seconds_between(rec.get("started_at"), rec.get("completed_at"))
        queue_s = seconds_between(rec.get("created_at"), rec.get("started_at"))
        total_s = seconds_between(rec.get("created_at"), rec.get("completed_at"))
        if duration_s is None or queue_s is None or total_s is None:
            skipped["missing_timing"] += 1
            continue

        run_id = int(rec["run_id"])
        job_id = int(rec["job_id"])
        head_sha = rec.get("head_sha")
        labels = list(rec.get("labels") or [])
        labels_key = ",".join(labels) if labels else "unlabeled"
        workflow = workflow_label(rec)
        job = rec.get("name") or "unknown"
        run_url = rec.get("run_html_url") or f"https://github.com/{REPO}/actions/runs/{run_id}"
        commit_subject = _commit_subject(rec.get("commit_message"))

        points.append(
            {
                "created_at": fmt_iso(created),
                "completed_at": rec.get("completed_at"),
                "commit": head_sha,
                "commit_short": head_sha[:12] if head_sha else None,
                "commit_subject": commit_subject,
                "commit_url": f"https://github.com/{REPO}/commit/{head_sha}" if head_sha else None,
                "pr_title": _pr_title(commit_subject),
                "run_id": run_id,
                "run_attempt": int(rec.get("run_attempt", 1)),
                "run_url": run_url,
                "job_id": job_id,
                "job_url": f"https://github.com/{REPO}/actions/runs/{run_id}/job/{job_id}",
                "workflow": workflow,
                "job": job,
                "benchmark": job,
                "labels": labels,
                "labels_key": labels_key,
                "runner_name": rec.get("runner_name"),
                "status": rec.get("status"),
                "conclusion": rec.get("conclusion"),
                "queue_s": round(queue_s, 3),
                "duration_s": round(duration_s, 3),
                "total_s": round(total_s, 3),
                "metric": "duration_s",
                "unit": "s",
            }
        )
    points.sort(key=lambda p: (p["created_at"], p["run_id"], p.get("job_id", 0)))
    return points, skipped


def build_dashboard_data(
    now: datetime,
    lookback_days: int = DEFAULT_LOOKBACK_DAYS,
    data_dir: Path = DATA_DIR,
) -> dict:
    points, skipped = _benchmark_result_points(now, lookback_days, data_dir)
    suite_manifest = read_json(data_dir / "benchmark_suites.json")
    current_level = "benchmark_result"
    metrics = ["current_time_ms", "golden_time_ms", "threshold_ms"]
    primary_metric = "current_time_ms"
    if not points:
        points, skipped = _job_timing_proxy_points(now, lookback_days, data_dir)
        current_level = "job_timing_proxy"
        metrics = ["duration_s", "queue_s", "total_s"]
        primary_metric = "duration_s"
    _annotate_suites(points, suite_manifest)

    group_values: dict[tuple[str, str], list[float]] = {}
    for p in points:
        value = p.get(primary_metric)
        if isinstance(value, (int, float)):
            group_values.setdefault((p["benchmark"], p["labels_key"]), []).append(value)
    groups = [
        {
            "benchmark": benchmark,
            "labels_key": labels_key,
            "points": len(values),
            f"median_{primary_metric}": round(_median(values) or 0.0, 6),
        }
        for (benchmark, labels_key), values in sorted(group_values.items())
    ]

    commit_points = sum(1 for p in points if p["commit"])
    suite_coverage = _suite_coverage(suite_manifest, points)
    configured_benchmarks = sum(row["configured_benchmarks"] for row in suite_coverage)
    return {
        "schema_version": 1,
        "generated_at": fmt_iso(now),
        "repo": REPO,
        "lookback_days": lookback_days,
        "metric_contract": {
            "current_level": current_level,
            "metrics": metrics,
            "main_filter": "head_branch == main and event != pull_request",
            "benchmark_filter": "PkgCI summary artifact benchmark rows",
            "commit_identity": "head_sha when present; older records may only have run/job ids",
        },
        "summary": {
            "points": len(points),
            "groups": len(groups),
            "points_with_commit": commit_points,
            "points_without_commit": len(points) - commit_points,
            "configured_benchmarks": configured_benchmarks,
            "suites": len(suite_coverage),
            "skipped": dict(skipped),
        },
        "suite_manifest": {
            "generated_at": suite_manifest.get("generated_at"),
            "suite_root_url": suite_manifest.get("suite_root_url"),
        } if suite_manifest else None,
        "suite_coverage": suite_coverage,
        "groups": groups,
        "points": points,
    }


def render_html(data_filename: str = "benchmark-data.json", embedded_data: dict | None = None) -> str:
    escaped_data_filename = html.escape(data_filename, quote=True)
    embedded_json = ""
    if embedded_data is not None:
        # Escape '<' so the JSON cannot accidentally terminate the script tag.
        embedded_json = (
            '<script type="application/json" id="embedded-data">'
            + json.dumps(embedded_data, separators=(",", ":"), sort_keys=True).replace("<", "\\u003c")
            + "</script>\n  "
        )
    data_url_js = "null" if embedded_data is not None else f'"{escaped_data_filename}"'
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>IREE Main Benchmark Dashboard</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f7f8fa;
      --panel: #ffffff;
      --text: #1f2933;
      --muted: #667085;
      --border: #d9dee7;
      --accent: #0f766e;
      --accent-2: #7c3aed;
      --bad: #b42318;
      --good: #027a48;
      --warn: #b54708;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: var(--bg);
      color: var(--text);
    }}
    header {{
      border-bottom: 1px solid var(--border);
      background: var(--panel);
      padding: 16px 20px 12px;
    }}
    h1 {{
      margin: 0 0 6px;
      font-size: 22px;
      font-weight: 650;
      letter-spacing: 0;
    }}
    .subhead {{
      color: var(--muted);
      font-size: 13px;
      line-height: 1.4;
    }}
    main {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 16px 20px 28px;
    }}
    .toolbar {{
      display: grid;
      grid-template-columns: minmax(220px, 2fr) minmax(220px, 1.5fr) minmax(120px, 0.8fr) minmax(110px, 0.6fr) auto;
      gap: 10px;
      align-items: end;
      margin-bottom: 14px;
    }}
    label {{
      display: grid;
      gap: 4px;
      color: var(--muted);
      font-size: 12px;
      font-weight: 600;
    }}
    select, input[type="number"] {{
      width: 100%;
      height: 34px;
      border: 1px solid var(--border);
      border-radius: 6px;
      background: var(--panel);
      color: var(--text);
      padding: 0 9px;
      font: inherit;
      font-size: 13px;
    }}
    .toggle {{
      height: 34px;
      display: flex;
      align-items: center;
      gap: 8px;
      color: var(--text);
      font-size: 13px;
      font-weight: 500;
      border: 1px solid var(--border);
      border-radius: 6px;
      background: var(--panel);
      padding: 0 10px;
      white-space: nowrap;
    }}
    .summary {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 10px;
      margin-bottom: 14px;
    }}
    .stat {{
      border: 1px solid var(--border);
      border-radius: 8px;
      background: var(--panel);
      padding: 10px 12px;
      min-height: 66px;
    }}
    .stat .label {{
      color: var(--muted);
      font-size: 12px;
      font-weight: 600;
    }}
    .stat .value {{
      margin-top: 5px;
      font-size: 20px;
      font-weight: 700;
    }}
    .stat .hint {{
      margin-top: 2px;
      color: var(--muted);
      font-size: 12px;
    }}
    .chart-wrap {{
      border: 1px solid var(--border);
      border-radius: 8px;
      background: var(--panel);
      padding: 12px;
      margin-bottom: 14px;
    }}
    .chart-legend {{
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      align-items: center;
      color: var(--muted);
      font-size: 12px;
      margin: 0 0 8px 46px;
    }}
    .legend-item {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .legend-line {{
      width: 22px;
      height: 0;
      border-top: 3px solid var(--accent);
    }}
    .legend-line.rolling {{
      border-top-color: var(--accent-2);
    }}
    canvas {{
      display: block;
      width: 100%;
      height: 420px;
    }}
    .tooltip {{
      position: fixed;
      display: none;
      max-width: 420px;
      padding: 9px 10px;
      border: 1px solid var(--border);
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.98);
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.16);
      color: var(--text);
      font-size: 12px;
      line-height: 1.35;
      pointer-events: none;
      z-index: 10;
    }}
    .tooltip.pinned {{
      pointer-events: auto;
    }}
    .tooltip .muted {{ color: var(--muted); }}
    .tooltip a {{ font-weight: 650; }}
    .tooltip .actions {{
      display: flex;
      gap: 10px;
      margin-top: 7px;
    }}
    .grid {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) minmax(360px, 0.45fr);
      gap: 14px;
      margin-bottom: 14px;
    }}
    section {{
      border: 1px solid var(--border);
      border-radius: 8px;
      background: var(--panel);
      overflow: hidden;
    }}
    section h2 {{
      margin: 0;
      padding: 10px 12px;
      border-bottom: 1px solid var(--border);
      font-size: 14px;
      letter-spacing: 0;
    }}
    .table-scroll {{
      overflow: auto;
      max-height: 420px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
    }}
    th, td {{
      padding: 8px 10px;
      border-bottom: 1px solid #edf0f5;
      text-align: left;
      vertical-align: top;
      white-space: nowrap;
    }}
    th {{
      position: sticky;
      top: 0;
      background: #fbfcfe;
      color: var(--muted);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0;
      z-index: 1;
    }}
    a {{ color: var(--accent); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .pill {{
      display: inline-block;
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 2px 7px;
      font-size: 11px;
      color: var(--muted);
      background: #fbfcfe;
    }}
    .good {{ color: var(--good); }}
    .bad {{ color: var(--bad); }}
    .warn {{ color: var(--warn); }}
    .empty {{
      padding: 18px 12px;
      color: var(--muted);
      font-size: 13px;
    }}
    @media (max-width: 980px) {{
      .toolbar, .summary, .grid {{ grid-template-columns: 1fr; }}
      main {{ padding: 12px; }}
      canvas {{ height: 320px; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>IREE Main Benchmark Dashboard</h1>
    <div id="subtitle" class="subhead">Loading benchmark data...</div>
  </header>
  <main>
    <div class="toolbar">
      <label>Benchmark
        <select id="benchmark"></select>
      </label>
      <label>Hardware / labels
        <select id="labels"></select>
      </label>
      <label>Metric
        <select id="metric"></select>
      </label>
      <label>Rolling window
        <input id="window" type="number" min="1" max="25" value="5">
      </label>
      <label class="toggle"><input id="successOnly" type="checkbox" checked> Success only</label>
    </div>

    <div class="summary">
      <div class="stat"><div class="label">Points</div><div id="statPoints" class="value">0</div><div id="statLookback" class="hint"></div></div>
      <div class="stat"><div class="label">Median</div><div id="statMedian" class="value">-</div><div class="hint">selected metric</div></div>
      <div class="stat"><div class="label">Recent range</div><div id="statRecent" class="value">-</div><div class="hint">last rolling window</div></div>
      <div class="stat"><div class="label">Commit coverage</div><div id="statCommits" class="value">-</div><div class="hint">points with head_sha</div></div>
    </div>

    <div class="chart-wrap">
      <div class="chart-legend">
        <span class="legend-item"><span class="legend-line"></span>Points and raw metric</span>
        <span class="legend-item"><span class="legend-line rolling"></span>Rolling median</span>
      </div>
      <canvas id="chart" width="1200" height="420"></canvas>
      <div id="tooltip" class="tooltip"></div>
    </div>

    <div class="grid">
      <section>
        <h2>Recent Points</h2>
        <div class="table-scroll">
          <table>
            <thead><tr><th>time</th><th>value</th><th>result</th><th>commit/run</th><th>job</th></tr></thead>
            <tbody id="pointsBody"></tbody>
          </table>
        </div>
      </section>
      <section>
        <h2>Candidate Ranges</h2>
        <div class="table-scroll">
          <table>
            <thead><tr><th>range</th><th>change</th><th>from</th><th>to</th></tr></thead>
            <tbody id="rangesBody"></tbody>
          </table>
        </div>
      </section>
    </div>

    <section>
      <h2>Suite Coverage</h2>
      <div class="table-scroll">
        <table>
          <thead><tr><th>suite</th><th>observed points</th><th>observed configs</th><th>configured benchmarks</th><th>missing examples</th></tr></thead>
          <tbody id="suiteBody"></tbody>
        </table>
      </div>
    </section>
  </main>

  {embedded_json}<script>
    const DATA_URL = {data_url_js};
    const STORAGE_KEY = "iree-ci-monitor.dashboard.controls.v1";
    const state = {{ data: null, points: [], hitPoints: [], activePoints: [], activeMetric: "", pinned: false, pinnedHit: null }};

    function metricLabel(metric) {{
      return {{
        current_time_ms: "Current Time",
        golden_time_ms: "Golden Time",
        threshold_ms: "Threshold",
        duration_s: "Duration",
        queue_s: "Queue",
        total_s: "Total"
      }}[metric] || metric;
    }}

    function fmtValue(value, metric) {{
      if (!Number.isFinite(value)) return "-";
      if (metric && metric.endsWith("_ms")) return `${{value.toFixed(3)}}ms`;
      if (value < 60) return `${{value.toFixed(1)}}s`;
      if (value < 3600) return `${{Math.floor(value / 60)}}m${{String(Math.round(value % 60)).padStart(2, "0")}}s`;
      return `${{Math.floor(value / 3600)}}h${{String(Math.round((value % 3600) / 60)).padStart(2, "0")}}m`;
    }}

    function median(values) {{
      const xs = values.filter(Number.isFinite).slice().sort((a, b) => a - b);
      if (!xs.length) return NaN;
      const mid = Math.floor(xs.length / 2);
      return xs.length % 2 ? xs[mid] : (xs[mid - 1] + xs[mid]) / 2;
    }}

    function rolling(points, metric, width) {{
      return points.map((point, index) => {{
        const start = Math.max(0, index - width + 1);
        const window = points.slice(start, index + 1).map(p => p[metric]);
        return {{ point, value: median(window) }};
      }});
    }}

    function optionText(text, max = 96) {{
      return text.length > max ? text.slice(0, max - 1) + "..." : text;
    }}

    function setSelectValue(id, value) {{
      if (value === undefined || value === null) return false;
      const select = document.getElementById(id);
      if (![...select.options].some(option => option.value === value)) return false;
      select.value = value;
      return true;
    }}

    function loadSavedControls() {{
      try {{
        const raw = window.localStorage.getItem(STORAGE_KEY);
        return raw ? JSON.parse(raw) : {{}};
      }} catch (error) {{
        return {{}};
      }}
    }}

    function saveControls() {{
      try {{
        window.localStorage.setItem(STORAGE_KEY, JSON.stringify({{
          benchmark: document.getElementById("benchmark").value,
          labels: document.getElementById("labels").value,
          metric: document.getElementById("metric").value,
          window: document.getElementById("window").value,
          successOnly: document.getElementById("successOnly").checked
        }}));
      }} catch (error) {{
        // Some browser privacy modes disable localStorage; the dashboard still works.
      }}
    }}

    function restoreControls() {{
      const saved = loadSavedControls();
      if (setSelectValue("benchmark", saved.benchmark)) populateLabels();
      setSelectValue("labels", saved.labels);
      setSelectValue("metric", saved.metric);
      const width = Number.parseInt(saved.window, 10);
      if (Number.isInteger(width) && width >= 1 && width <= 25) {{
        document.getElementById("window").value = String(width);
      }}
      if (typeof saved.successOnly === "boolean") {{
        document.getElementById("successOnly").checked = saved.successOnly;
      }}
    }}

    function populateControls() {{
      const benchmarks = [...new Set(state.data.points.map(p => p.benchmark))].sort();
      const benchmarkSelect = document.getElementById("benchmark");
      benchmarkSelect.innerHTML = benchmarks.map(b => `<option value="${{escapeHtml(b)}}">${{escapeHtml(optionText(b))}}</option>`).join("");
      populateLabels();
    }}

    function populateMetrics() {{
      const metrics = state.data.metric_contract.metrics || ["current_time_ms"];
      const metricSelect = document.getElementById("metric");
      metricSelect.innerHTML = metrics.map(m => `<option value="${{escapeHtml(m)}}">${{escapeHtml(metricLabel(m))}}</option>`).join("");
    }}

    function populateLabels() {{
      const selectedBenchmark = document.getElementById("benchmark").value;
      const labels = [...new Set(state.data.points.filter(p => p.benchmark === selectedBenchmark).map(p => p.labels_key))].sort();
      const labelsSelect = document.getElementById("labels");
      labelsSelect.innerHTML = labels.map(l => `<option value="${{escapeHtml(l)}}">${{escapeHtml(optionText(l, 72))}}</option>`).join("");
    }}

    function escapeHtml(value) {{
      return String(value).replace(/[&<>"']/g, ch => ({{"&":"&amp;","<":"&lt;",">":"&gt;","\\"":"&quot;","'":"&#39;"}}[ch]));
    }}

    function escapeAttr(value) {{
      return escapeHtml(value || "#");
    }}

    function linkAttrs(url) {{
      return `href="${{escapeAttr(url)}}" rel="noopener noreferrer"`;
    }}

    function commitSubject(p) {{
      const subject = p.commit_subject || (p.commit_message || "").split(/\\r?\\n/)[0];
      return subject ? subject.trim() : "";
    }}

    function prTitleFromSubject(subject) {{
      const match = subject.match(/^(.*?)\\s+\\(#\\d+\\)$/);
      return match ? match[1].trim() : "";
    }}

    function pointTitle(p) {{
      const subject = commitSubject(p);
      const title = p.pr_title || prTitleFromSubject(subject) || subject;
      return title ? title.trim() : "";
    }}

    function pointTitleLabel(p) {{
      return p.pr_title || prTitleFromSubject(commitSubject(p)) ? "PR title" : "commit subject";
    }}

    function selectedPoints() {{
      const benchmark = document.getElementById("benchmark").value;
      const labels = document.getElementById("labels").value;
      const successOnly = document.getElementById("successOnly").checked;
      return state.data.points.filter(p =>
        p.benchmark === benchmark &&
        p.labels_key === labels &&
        (!successOnly || ["PASSED", "success", "completed", "REPORTED"].includes(p.result_status || p.conclusion || p.status))
      );
    }}

    function selectedMetricPoints(metric) {{
      return selectedPoints().filter(p => Number.isFinite(p[metric]));
    }}

    function drawChart(points, metric, width) {{
      const canvas = document.getElementById("chart");
      const ctx = canvas.getContext("2d");
      state.hitPoints = [];
      const dpr = window.devicePixelRatio || 1;
      const rect = canvas.getBoundingClientRect();
      canvas.width = Math.max(600, Math.floor(rect.width * dpr));
      canvas.height = Math.max(280, Math.floor(rect.height * dpr));
      ctx.scale(dpr, dpr);
      const w = canvas.width / dpr;
      const h = canvas.height / dpr;
      ctx.clearRect(0, 0, w, h);
      const pad = {{ left: 58, right: 18, top: 18, bottom: 44 }};
      const plotW = w - pad.left - pad.right;
      const plotH = h - pad.top - pad.bottom;
      ctx.strokeStyle = "#d9dee7";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(pad.left, pad.top);
      ctx.lineTo(pad.left, pad.top + plotH);
      ctx.lineTo(pad.left + plotW, pad.top + plotH);
      ctx.stroke();

      const values = points.map(p => p[metric]).filter(Number.isFinite);
      if (points.length < 2 || values.length < 2) {{
        ctx.fillStyle = "#667085";
        ctx.font = "13px system-ui";
        ctx.fillText("Not enough points for a chart.", pad.left + 12, pad.top + 28);
        return;
      }}

      const minY = Math.min(...values);
      const maxY = Math.max(...values);
      const spanY = Math.max(1, maxY - minY);
      const yMin = Math.max(0, minY - spanY * 0.08);
      const yMax = maxY + spanY * 0.12;
      const x = i => pad.left + (i / Math.max(1, points.length - 1)) * plotW;
      const y = v => pad.top + plotH - ((v - yMin) / Math.max(1, yMax - yMin)) * plotH;

      ctx.fillStyle = "#667085";
      ctx.font = "12px system-ui";
      for (let t = 0; t <= 4; t++) {{
        const value = yMin + ((yMax - yMin) * t / 4);
        const yy = y(value);
        ctx.strokeStyle = "#edf0f5";
        ctx.beginPath();
        ctx.moveTo(pad.left, yy);
        ctx.lineTo(pad.left + plotW, yy);
        ctx.stroke();
        ctx.fillText(fmtValue(value, metric), 8, yy + 4);
      }}

      ctx.strokeStyle = "#0f766e";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      points.forEach((p, i) => {{
        const xx = x(i), yy = y(p[metric]);
        if (i === 0) ctx.moveTo(xx, yy); else ctx.lineTo(xx, yy);
      }});
      ctx.stroke();

      ctx.fillStyle = "#0f766e";
      points.forEach((p, i) => {{
        const xx = x(i);
        const yy = y(p[metric]);
        state.hitPoints.push({{ x: xx, y: yy, point: p }});
        ctx.beginPath();
        ctx.arc(xx, yy, 2.5, 0, Math.PI * 2);
        ctx.fill();
      }});

      const rolled = rolling(points, metric, width);
      ctx.strokeStyle = "#7c3aed";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      rolled.forEach((entry, i) => {{
        const xx = x(i), yy = y(entry.value);
        if (i === 0) ctx.moveTo(xx, yy); else ctx.lineTo(xx, yy);
      }});
      ctx.stroke();

      ctx.fillStyle = "#667085";
      const first = new Date(points[0].created_at).toISOString().slice(0, 10);
      const last = new Date(points[points.length - 1].created_at).toISOString().slice(0, 10);
      ctx.fillText(first, pad.left, h - 14);
      ctx.textAlign = "right";
      ctx.fillText(last, pad.left + plotW, h - 14);
      ctx.textAlign = "left";
    }}

    function pointCommitHtml(p) {{
      if (p.commit && p.commit_url) {{
        return `<a ${{linkAttrs(p.commit_url)}}>${{escapeHtml(p.commit_short)}}</a>`;
      }}
      return `<a ${{linkAttrs(p.run_url)}}>run ${{p.run_id}}</a>`;
    }}

    function positionTooltip(event) {{
      const tip = document.getElementById("tooltip");
      const margin = 14;
      const width = 420;
      const height = tip.offsetHeight || 160;
      tip.style.left = `${{Math.max(8, Math.min(event.clientX + margin, window.innerWidth - width - 8))}}px`;
      tip.style.top = `${{Math.max(8, Math.min(event.clientY + margin, window.innerHeight - height - 8))}}px`;
    }}

    function showTooltip(event, hit, pinned = false) {{
      const tip = document.getElementById("tooltip");
      const p = hit.point;
      const metric = state.activeMetric;
      const status = p.result_status || p.conclusion || p.status || "-";
      const title = pointTitle(p);
      const titleLabel = pointTitleLabel(p);
      tip.innerHTML = `
        <strong>${{escapeHtml(p.benchmark)}}</strong><br>
        ${{escapeHtml(metricLabel(metric))}}: <strong>${{fmtValue(p[metric], metric)}}</strong><br>
        <span class="muted">commit/run:</span> ${{pointCommitHtml(p)}}<br>
        ${{title ? `<span class="muted">${{titleLabel}}:</span> ${{escapeHtml(title)}}<br>` : ""}}
        <span class="muted">target:</span> ${{escapeHtml(p.labels_key || "-")}}<br>
        <span class="muted">time:</span> ${{escapeHtml((p.created_at || "").replace("T", " ").replace("Z", " UTC"))}}<br>
        <span class="muted">status:</span> ${{escapeHtml(status)}}
        <div class="actions">
          ${{p.commit_url ? `<a ${{linkAttrs(p.commit_url)}}>commit</a>` : ""}}
          <a ${{linkAttrs(p.run_url)}}>run</a>
          ${{p.job_url ? `<a ${{linkAttrs(p.job_url)}}>job</a>` : ""}}
          ${{p.artifact_id ? `<span class="muted">artifact ${{p.artifact_id}}</span>` : ""}}
        </div>
      `;
      tip.classList.toggle("pinned", pinned);
      positionTooltip(event);
      tip.style.display = "block";
    }}

    function hideTooltip(force = false) {{
      if (state.pinned && !force) return;
      const tip = document.getElementById("tooltip");
      tip.style.display = "none";
      tip.classList.remove("pinned");
      if (force) {{
        state.pinned = false;
        state.pinnedHit = null;
      }}
    }}

    function nearestHit(event) {{
      const canvas = document.getElementById("chart");
      const rect = canvas.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      let best = null;
      let bestDist = 64;
      for (const hit of state.hitPoints) {{
        const dx = hit.x - x;
        const dy = hit.y - y;
        const dist = dx * dx + dy * dy;
        if (dist < bestDist) {{
          bestDist = dist;
          best = hit;
        }}
      }}
      return best;
    }}

    function onChartMove(event) {{
      const canvas = document.getElementById("chart");
      const best = nearestHit(event);
      if (best) {{
        canvas.style.cursor = "crosshair";
        if (!state.pinned) showTooltip(event, best, false);
      }} else {{
        canvas.style.cursor = "default";
        hideTooltip(false);
      }}
    }}

    function onChartClick(event) {{
      const best = nearestHit(event);
      if (!best) {{
        hideTooltip(true);
        return;
      }}
      state.pinned = true;
      state.pinnedHit = best;
      showTooltip(event, best, true);
    }}

    function detectRanges(points, metric, width) {{
      if (points.length < Math.max(4, width * 2)) return [];
      const rolled = rolling(points, metric, width);
      const ranges = [];
      for (let i = width * 2 - 1; i < rolled.length; i++) {{
        const before = median(rolled.slice(i - width * 2 + 1, i - width + 1).map(r => r.value));
        const after = median(rolled.slice(i - width + 1, i + 1).map(r => r.value));
        if (!Number.isFinite(before) || before === 0 || !Number.isFinite(after)) continue;
        const delta = (after - before) / before;
        if (Math.abs(delta) >= 0.10) {{
          ranges.push({{
            start: points[i - width + 1],
            end: points[i],
            before,
            after,
            delta
          }});
        }}
      }}
      return ranges.sort((a, b) => Math.abs(b.delta) - Math.abs(a.delta)).slice(0, 10);
    }}

    function renderTables(points, metric, width) {{
      const rows = points.slice(-80).reverse().map(p => {{
        const commit = p.commit ? `<a ${{linkAttrs(p.commit_url)}}>${{p.commit_short}}</a>` : `<a ${{linkAttrs(p.run_url)}}>run ${{p.run_id}}</a>`;
        const status = p.result_status || p.conclusion || p.status || "-";
        const resultClass = ["PASSED", "success", "completed"].includes(status) ? "good" : (["FAILED", "failure"].includes(status) ? "bad" : "warn");
        return `<tr>
          <td>${{escapeHtml(p.created_at.replace("T", " ").replace("Z", " UTC"))}}</td>
          <td>${{fmtValue(p[metric], metric)}}</td>
          <td><span class="${{resultClass}}">${{escapeHtml(status)}}</span></td>
          <td>${{commit}}</td>
          <td><a ${{linkAttrs(p.job_url || p.run_url)}}>${{p.job_url ? "job" : "run"}}</a></td>
        </tr>`;
      }}).join("");
      document.getElementById("pointsBody").innerHTML = rows || `<tr><td colspan="5" class="empty">No points match the current filters.</td></tr>`;

      const rangeRows = detectRanges(points, metric, width).map(r => {{
        const cls = r.delta > 0 ? "bad" : "good";
        const label = r.delta > 0 ? "regression" : "improvement";
        const start = r.start.commit ? `<a ${{linkAttrs(r.start.commit_url)}}>${{r.start.commit_short}}</a>` : `<a ${{linkAttrs(r.start.run_url)}}>run ${{r.start.run_id}}</a>`;
        const end = r.end.commit ? `<a ${{linkAttrs(r.end.commit_url)}}>${{r.end.commit_short}}</a>` : `<a ${{linkAttrs(r.end.run_url)}}>run ${{r.end.run_id}}</a>`;
        return `<tr>
          <td><span class="pill">${{label}}</span></td>
          <td class="${{cls}}">${{(r.delta * 100).toFixed(1)}}%</td>
          <td>${{start}}<br>${{fmtValue(r.before, metric)}}</td>
          <td>${{end}}<br>${{fmtValue(r.after, metric)}}</td>
        </tr>`;
      }}).join("");
      document.getElementById("rangesBody").innerHTML = rangeRows || `<tr><td colspan="4" class="empty">No >=10% rolling-window changes in this selection.</td></tr>`;
    }}

    function renderSuiteCoverage() {{
      const rows = state.data.suite_coverage || [];
      const html = rows.map(row => {{
        const suite = row.suite_url
          ? `<a ${{linkAttrs(row.suite_url)}}>${{escapeHtml(row.suite)}}</a>`
          : escapeHtml(row.suite);
        const missing = (row.missing_benchmark_examples || []).map(escapeHtml).join("<br>");
        const observed = `${{Number(row.observed_configured_benchmarks || 0).toLocaleString()}} / ${{Number(row.observed_benchmark_names || 0).toLocaleString()}}`;
        return `<tr>
          <td>${{suite}}</td>
          <td>${{Number(row.points || 0).toLocaleString()}}</td>
          <td>${{observed}}</td>
          <td>${{Number(row.configured_benchmarks || 0).toLocaleString()}}</td>
          <td>${{missing || '<span class="muted">none</span>'}}</td>
        </tr>`;
      }}).join("");
      document.getElementById("suiteBody").innerHTML = html || `<tr><td colspan="5" class="empty">No benchmark suite manifest was generated.</td></tr>`;
    }}

    function update() {{
      const metric = document.getElementById("metric").value;
      const width = Math.max(1, Number.parseInt(document.getElementById("window").value, 10) || 5);
      const points = selectedMetricPoints(metric);
      hideTooltip(true);
      const values = points.map(p => p[metric]);
      const med = median(values);
      const recent = median(values.slice(-width));
      state.activePoints = points;
      state.activeMetric = metric;
      document.getElementById("statPoints").textContent = points.length.toLocaleString();
      document.getElementById("statMedian").textContent = fmtValue(med, metric);
      document.getElementById("statRecent").textContent = fmtValue(recent, metric);
      document.getElementById("statLookback").textContent = `${{state.data.lookback_days}} day source window`;
      drawChart(points, metric, width);
      renderTables(points, metric, width);
      saveControls();
    }}

    async function main() {{
      try {{
        const embedded = document.getElementById("embedded-data");
        if (embedded) {{
          state.data = JSON.parse(embedded.textContent);
        }} else {{
          const response = await fetch(DATA_URL);
          if (!response.ok) throw new Error(`HTTP ${{response.status}}`);
          state.data = await response.json();
        }}
      }} catch (error) {{
        document.getElementById("subtitle").textContent = `Unable to load ${{DATA_URL || "embedded data"}}. Serve docs/ with a static server when running locally, or open standalone.html.`;
        return;
      }}

      const summary = state.data.summary;
      document.getElementById("subtitle").textContent =
        `Generated ${{state.data.generated_at}} from ${{state.data.repo}}; ${{summary.points.toLocaleString()}} main-branch benchmark result points across ${{summary.groups.toLocaleString()}} groups.`;
      document.getElementById("statCommits").textContent =
        `${{summary.points_with_commit.toLocaleString()}} / ${{summary.points.toLocaleString()}}`;
      populateMetrics();
      populateControls();
      restoreControls();
      renderSuiteCoverage();
      update();
      for (const id of ["benchmark", "labels", "metric", "window", "successOnly"]) {{
        document.getElementById(id).addEventListener("change", () => {{
          if (id === "benchmark") populateLabels();
          update();
        }});
      }}
      document.getElementById("chart").addEventListener("mousemove", onChartMove);
      document.getElementById("chart").addEventListener("click", onChartClick);
      document.getElementById("chart").addEventListener("mouseleave", () => hideTooltip(false));
      document.addEventListener("click", event => {{
        const tip = document.getElementById("tooltip");
        const chart = document.getElementById("chart");
        if (!state.pinned) return;
        if (tip.contains(event.target) || chart.contains(event.target)) return;
        hideTooltip(true);
      }});
      document.addEventListener("keydown", event => {{
        if (event.key === "Escape") hideTooltip(true);
      }});
      window.addEventListener("resize", update);
    }}

    main();
  </script>
</body>
</html>
"""


def write_dashboard(
    output_dir: Path = DOCS_DIR,
    lookback_days: int = DEFAULT_LOOKBACK_DAYS,
    now: datetime | None = None,
    data_dir: Path = DATA_DIR,
) -> dict:
    now = now or parse_now()
    output_dir.mkdir(parents=True, exist_ok=True)
    data = build_dashboard_data(now, lookback_days, data_dir)
    (output_dir / "benchmark-data.json").write_text(
        json.dumps(data, separators=(",", ":"), sort_keys=True) + "\n"
    )
    (output_dir / "index.html").write_text(render_html())
    (output_dir / "standalone.html").write_text(render_html(embedded_data=data))
    (output_dir / ".nojekyll").write_text("")
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--lookback-days",
        type=int,
        default=int(os.environ.get("IREE_BENCHMARK_LOOKBACK_DAYS", DEFAULT_LOOKBACK_DAYS)),
        help="Historical window to include in generated dashboard data.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DOCS_DIR,
        help="Output directory for static dashboard assets.",
    )
    args = parser.parse_args()
    data = write_dashboard(output_dir=args.output_dir, lookback_days=args.lookback_days)
    print(
        f"[dashboard] wrote {args.output_dir} with "
        f"{data['summary']['points']} points across {data['summary']['groups']} groups"
    )


if __name__ == "__main__":
    main()
