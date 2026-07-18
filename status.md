# Status detail

_Updated: 2026-07-18 11:36 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29648122758/job/88089706172) | [3s](https://github.com/iree-org/iree/actions/runs/29648122626/job/88089705809) | [3s](https://github.com/iree-org/iree/actions/runs/29648122758/job/88089706173) | 33% (4/12) | — | 12 |  |
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074634926) | [2s](https://github.com/iree-org/iree/actions/runs/29647947257/job/88089236098) | [2s](https://github.com/iree-org/iree/actions/runs/29647947257/job/88089236098) | 0% (0/6) | 0% (0/2) | 6 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29642447636/job/88075083613) | [3s](https://github.com/iree-org/iree/actions/runs/29648122758/job/88089706173) | [3s](https://github.com/iree-org/iree/actions/runs/29648122758/job/88089706173) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29648122758/job/88089706159) | [3s](https://github.com/iree-org/iree/actions/runs/29642447636/job/88075083603) | [3s](https://github.com/iree-org/iree/actions/runs/29642447636/job/88075083603) | 2 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29642447320/job/88075082911) | [3s](https://github.com/iree-org/iree/actions/runs/29648122626/job/88089705809) | [3s](https://github.com/iree-org/iree/actions/runs/29648122626/job/88089705809) | 2 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29648122626/job/88089720878) | [3s](https://github.com/iree-org/iree/actions/runs/29642447320/job/88075098537) | [3s](https://github.com/iree-org/iree/actions/runs/29642447320/job/88075098537) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [1s](https://github.com/iree-org/iree/actions/runs/29648122626/job/88089720859) | [3s](https://github.com/iree-org/iree/actions/runs/29642447320/job/88075098531) | [3s](https://github.com/iree-org/iree/actions/runs/29642447320/job/88075098531) | 2 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29642278730/job/88074641463) | [2s](https://github.com/iree-org/iree/actions/runs/29647947257/job/88089236098) | [2s](https://github.com/iree-org/iree/actions/runs/29647947257/job/88089236098) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/29642447636/job/88075083598) | [2s](https://github.com/iree-org/iree/actions/runs/29648122758/job/88089706172) | [2s](https://github.com/iree-org/iree/actions/runs/29648122758/job/88089706172) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88074470123) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88074470123) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88074470123) | 1 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29642912538/job/88076264915) | [2s](https://github.com/iree-org/iree/actions/runs/29642912538/job/88076264915) | [2s](https://github.com/iree-org/iree/actions/runs/29642912538/job/88076264915) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074634926) | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074634926) | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074634926) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074477306) | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074477306) | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074477306) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 175 | 173 | 1 | 1 | 1% |  | 19h46m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 141 | 127 | 13 | 1 | 9% |  | 19h46m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 150 | 147 | 2 | 1 | 1% |  | 19h52m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 137 | 136 | 0 | 1 | 0% |  | 19h55m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 41 | 40 | 0 | 1 | 0% |  | 20h06m ago |

## Alerts

_No active alerts._

## Methodology

- Window: last 10 hours of job records for queue-time percentiles and failure metrics; queued observations are scanned for 3 days; last 7 days for runner metrics and SPOF.
- Timestamps rendered in `America/Los_Angeles` local time; underlying records are UTC.
- Queue time: `started_at - created_at`. Skipped jobs excluded.
- Queued: jobs with `status == queued` or `waiting` (not yet assigned a runner).
- Running: jobs with `status == in_progress` (runner assigned, executing).
- Oldest queued: `collected_at - created_at` for the oldest job observed with `status == queued` or `waiting`. This is only updated by collection; rerunning the reporter does not inflate stale queued snapshots.
- Workflow/job waiting time: same queue-time definition, grouped by stable workflow id/name + job name + exact label set. Older records collected before `workflow_path` was stored fall back to `workflow_name`.
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
- `stale-queued`: oldest observed queued job (not yet started) > 2h00m
- `high-failure-main`: main-only failure rate > 20% with ≥ 10 completed main-only jobs
- `spof`: only one distinct runner in last 7d
