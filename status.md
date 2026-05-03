# Status detail

_Updated: 2026-05-03 05:35 PDT_ — watching `iree-org/iree`, window = last 10h

## Per-label metrics

| label | type | jobs | queued | oldest queued | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/25277826968/job/74110360572) | [8s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664150) | [8s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664150) | 12% (1/8) | 0% (0/1) | 8 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | 0 | — | 2s | [3s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664145) | [3s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664147) | [3s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664147) | 0% (0/3) | — | 3 |  |
| `macos-14` | github-hosted | 2 | 0 | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664151) | [3s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664168) | [3s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664168) | 0% (0/2) | — | 2 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664165) | [2s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664170) | [2s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664170) | 0% (0/2) | — | 2 |  |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1024 | 961 | 54 | 8 | 5% | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 885 | 854 | 24 | 6 | 3% | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 799 | 784 | 11 | 4 | 1% |  | 1d07h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 610 | 570 | 38 | 2 | 6% |  | 1d07h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 237 | 225 | 5 | 7 | 2% |  | 1d07h ago |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 64 | 56 | 7 | 1 | 11% |  | 5d15h ago |

## Alerts

_No active alerts._

## Methodology

- Window: last 10 hours of job records for label metrics; last 7 days for runner metrics and SPOF.
- Timestamps rendered in `America/Los_Angeles` local time; underlying records are UTC.
- Queue time: `started_at - created_at`. Skipped jobs excluded.
- Queued: jobs with `status == queued` or `waiting` (not yet assigned a runner).
- Running: jobs with `status == in_progress` (runner assigned, executing).
- Oldest queued: `now - created_at` for the oldest still-queued job. This is the actionable signal for runner starvation — a job that's been in_progress for hours is just slow, not starved.
- All-jobs fail rate: over every completed job (PR + push + schedule).
- Main-only fail rate: subset where `head_branch == main` and `event != pull_request` — post-merge, scheduled, and workflow_dispatch runs. PR noise excluded.
- Runner type:
  - `self-hosted`: persistent physical hosts managed by the IREE infra team (shark fleet, `iree-mi308-1`, etc.). The `runners` count is the number of physical boxes.
  - `github-hosted`: GitHub's standard runner pool (`ubuntu-*`, `macos-*`, `windows-*`) and Actions Hosting partners (`ah-*`). Ephemeral — one worker per job.
  - `ossci`: org-managed autoscaler pools (`azure-*`, `*-ossci-iree-org`). Ephemeral — one worker per job, so the `runners` count here is really "pod spawns in the window" not physical capacity.
- SPOF: label has seen only one distinct `runner_name` in the last 7 days.
- Persistent runner: ran ≥ 5 jobs in the lookback window AND served at least one label with ≤ 15 distinct runners. Ephemeral auto-scaler worker names (which appear once per spawn) are excluded.
- Re-runs: `(job_id, run_attempt)` tuples are distinct; a re-run counts as a new job.

## Alert thresholds

- `queue-starved`: p95 queue > 1h00m
- `stale-queued`: oldest queued job (not yet started) > 2h00m
- `high-failure-main`: main-only failure rate > 20% with ≥ 10 completed main-only jobs
- `spof`: only one distinct runner in last 7d
