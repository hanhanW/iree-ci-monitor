# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Overview

**Repository:** Automated GitHub Actions runner health monitor for `iree-org/iree`.
A GitHub Actions cron (every 6h) runs `scripts/collect.py` (pulls new run+job
metadata via the REST API) and `scripts/report.py` (regenerates `README.md` +
`status.md`), then auto-commits the refresh. The dashboard *is* the committed
Markdown — readers just visit the repo.

**Audience:** Compiler engineers investigating "which runners are healthy right
now?" at a glance; IREE infra owners triaging queue starvation and bad boxes.

**Quality bar:** The dashboard is public-facing (currently private, flipping to
public when ready). Wrong numbers are worse than no numbers because they
mislead triage. Favor fewer, correct signals over many noisy ones.

## Non-Negotiables

1. **Python stdlib only.** No `requirements.txt`, no pip install step. Everything
   runs on `ubuntu-latest` with a bare `actions/setup-python@v5`.
2. **Append-only JSONL.** Never rewrite `data/YYYY/MM/DD.jsonl` files; only
   append. Dedupe on `(job_id, run_attempt)` by loading existing keys before
   writing. The collector must be idempotent — running twice in a row appends
   zero lines.
3. **Preserve the two-tier checkpoint.** `data/.state.json` tracks both
   `last_completed_run_id` (high-water mark) *and* `open_run_ids` (set of
   still-in-flight runs to re-fetch each tick). Do NOT collapse to a single
   cursor — jobs on open runs often complete across multiple ticks, and the
   single-cursor version would miss them.
4. **Keep the queued vs in_progress split.** An earlier version lumped both
   into `pending`, which fired false `stale-pending` alerts on long-running
   autoscaler jobs (the job was running fine, not starved). `stale-queued`
   only fires when `status == queued`; `in_progress` has its own counter and
   oldest-age field.
5. **Keep the main-only failure rate view.** A bad PR can spike per-label
   failure rate and look like a broken runner. The reporter tracks main-only
   failure rate (`head_branch == "main"` AND `event != "pull_request"`)
   separately. Alerts use main-only; `status.md` shows both.

## Architecture

```
iree-ci-monitor/
├── .github/workflows/monitor.yml   # 6h cron + workflow_dispatch
├── scripts/
│   ├── collect.py                  # fetch new runs+jobs, append JSONL
│   └── report.py                   # aggregate + render Markdown
├── data/
│   ├── .state.json                 # checkpoint (last_completed_run_id, open_run_ids)
│   └── YYYY/MM/DD.jsonl            # one JSON object per job, UTC day bucket
├── README.md                       # table-first dashboard (regenerated each tick)
└── status.md                       # full per-label + per-runner detail (regenerated)
```

Data flow each tick:

1. `collect.py` scans `/actions/runs?created>=now-RESCAN_HOURS` (7h, one
   tick + 1h margin), unions with `open_run_ids`, pulls
   `/actions/runs/{id}/jobs` for each, normalizes, dedupes, appends.
2. `report.py` reads the last `WINDOW_HOURS` (10h, labels) and `RUNNER_LOOKBACK_DAYS`
   (7d, per-runner + SPOF) of JSONL, computes stats, writes `README.md` +
   `status.md`. Window > tick interval gives ~4h overlap so a transient
   regression appears in two consecutive reports instead of "blink and miss".
3. The workflow commits anything under `data/`, `README.md`, `status.md`.
   Empty diffs are skipped. `CLAUDE.md` is not touched by the bot.

## Key Design Decisions

- **Aggregate by `workflow_id` not `workflow_name`.** Workflows get renamed;
  IDs stay stable. JSONL records carry both for display.
- **`event` and `head_branch` come from the run object, not the job object.**
  The collector caches them per-run and stamps onto each job record as it
  writes.
- **Day-bucket by `created_at`, UTC.** Jobs that straddle midnight UTC land
  in the bucket matching their creation time, not completion.
- **Store UTC; display Pacific.** Timestamps are UTC in JSONL. The reporter
  renders the `_Updated: …_` header in `America/Los_Angeles` via `DISPLAY_TZ`
  and `fmt_updated()`. Don't mix zones in storage.
- **SPOF uses last 7d of observed runners.** A label whose second runner has
  been offline the whole week will false-flag as SPOF. Acceptable for v1;
  documented in `status.md` methodology rather than hidden.
- **Persistent-runner filter is two-gate.** A `runner_name` appears in the
  per-runner table only if (a) it served at least one label with
  ≤ `PERSISTENT_LABEL_MAX` distinct runners in the lookback window AND
  (b) it saw ≥ `PERSISTENT_RUNNER_MIN_JOBS` jobs. Label gate excludes
  auto-scaler pools; the job-count gate catches small-pool autoscalers
  (`macos-15-intel`, `ah-ubuntu_22_04-c7g_4x-50`) whose names are per-spawn.

## Alert thresholds

Hardcoded at the top of `scripts/report.py`:

| alert               | threshold                                                                         |
|---------------------|-----------------------------------------------------------------------------------|
| `queue-starved`     | p95 queue > `P95_QUEUE_ALERT_S` (1h)                                              |
| `stale-queued`      | oldest queued job > `STALE_PENDING_S` (2h)                                        |
| `high-failure-main` | main-only fail rate > `HIGH_FAILURE_RATE` (20%) with ≥ `HIGH_FAILURE_MIN_N` (10) completed main-only jobs |
| `spof`              | only one distinct runner observed in last `SPOF_LOOKBACK_DAYS` (7d)               |

If you add a new alert, update the methodology + thresholds sections in
`render_status()` so readers know how it fires.

## Testing

Before pushing a change to `scripts/`:

1. **Run report locally** — fast, no network:
   ```bash
   python3 scripts/report.py
   git diff README.md status.md
   ```
   Eyeball the diff. Numbers should move sensibly; Markdown tables should
   still render.

2. **Run collect locally** (needs a token):
   ```bash
   GITHUB_TOKEN=$(gh auth token) python3 scripts/collect.py
   python3 scripts/collect.py      # second run should append 0 lines
   ```
   Verify `data/YYYY/MM/DD.jsonl` only grew on the first run.

3. **Trigger the workflow in CI** rather than waiting for the 6h cron:
   ```bash
   gh workflow run monitor.yml
   gh run list --workflow=monitor.yml --limit 3
   gh run watch <run-id>
   ```

## GHA and rate-limit constraints

- Currently private. Personal accounts get 2,000 free GHA minutes/mo for
  private repos. Each tick is ~1 min; 6h cadence burns ~120 min/mo —
  plenty of headroom. If the job grows to threaten that budget, flip the
  repo to public (unlimited on public repos) or trim cadence.
- `GITHUB_TOKEN` inside the workflow has a 1,000/hr primary rate limit. One
  tick makes ~100–200 API calls with the 7h rescan window (one paginated
  `/actions/runs` scan + one `/jobs` call per run). Well under the cap.
- `concurrency: monitor` prevents scheduled + manual dispatches from
  overlapping.

## Dependencies

- Python 3.11+ (stdlib: `urllib.request`, `json`, `statistics`, `datetime`,
  `pathlib`, `zoneinfo`, `collections`, `dataclasses`).
- No external Python packages, no Node toolchain.
- `gh` CLI locally for workflow triggering + repo management.

## When in doubt

- **Don't silently add/remove JSONL fields.** Readers use `json.loads`, so
  adding new fields is safe. Renaming or removing old ones breaks historical
  records. If you must rename, read both for several weeks.
- **Don't change the commit cadence or message format** without reason —
  the bot author email and the `monitor: refresh TIMESTAMP` commit subject
  are load-bearing for filtering the refresh commits out of `git log`.
- **Don't delete old JSONL.** Retention plan is gzip-in-place after 30
  days; deleting loses SPOF signal retroactively.
- **Don't bypass dedupe** to "simplify" the collector. The idempotency
  property is what makes re-runs after failed pushes safe.
