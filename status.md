# Status detail

_Updated: 2026-11-27 23:56 PST_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 1 | [2h46m](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796368) | 4s | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796338) | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796368) | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796368) | 0% (0/2) | — | 3 |  |
| `ubuntu-24.04` | github-hosted | 7 | 0 | — | — | 2 | [2h46m](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796304) | 1s | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796304) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796359) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796359) | 0% (0/5) | 0% (0/1) | 7 |  |
| `macos-15` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796321) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796410) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796410) | 0% (0/2) | — | 2 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2h46m](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796306) | 1s | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796306) | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796357) | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796357) | 0% (0/1) | — | 2 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796368) | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796368) | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796368) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796317) | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796317) | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796317) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796338) | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796338) | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796338) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796304) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796304) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796304) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796342) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796342) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796342) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796359) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796359) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796359) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796358) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796358) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796358) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796410) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796410) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796410) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796321) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796321) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796321) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873749544) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873749544) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873749544) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/46110781293/job/140873607434) | [2s](https://github.com/iree-org/iree/actions/runs/46110781293/job/140873607434) | [2s](https://github.com/iree-org/iree/actions/runs/46110781293/job/140873607434) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796306) | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796306) | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796306) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796357) | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796357) | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796357) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/46091227293/job/140812338235) | [1s](https://github.com/iree-org/iree/actions/runs/46091227293/job/140812338235) | [1s](https://github.com/iree-org/iree/actions/runs/46091227293/job/140812338235) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 91 | 89 | 1 | 1 | 1% |  | 11h33m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 76 | 69 | 6 | 1 | 8% |  | 15h20m ago |

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
