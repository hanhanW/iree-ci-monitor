# Status detail

_Updated: 2026-11-11 23:18 PST_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [2h07m](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316566) | 4s | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316570) | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316764) | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316764) | 0% (0/1) | — | 3 |  |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2h07m](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316545) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/43159487021/job/130987035658) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316622) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316622) | 0% (0/7) | 0% (0/4) | 9 |  |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [2h07m](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316657) | 3s | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316620) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316657) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316657) | 0% (0/1) | — | 2 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2h07m](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316790) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316775) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316790) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316790) | 0% (0/1) | — | 2 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316570) | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316570) | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316570) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316764) | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316764) | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316764) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316566) | [4s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316566) | [4s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316566) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316622) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316622) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316622) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316657) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316657) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316657) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316620) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316620) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316620) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316790) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316790) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316790) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316678) | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316678) | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316678) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316545) | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316545) | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316545) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316592) | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316592) | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316592) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316775) | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316775) | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316775) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130968017954) | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130968017954) | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130968017954) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130968018181) | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130968018181) | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130968018181) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130971162447) | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130971162447) | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130971162447) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/43159487021/job/130987035658) | [2s](https://github.com/iree-org/iree/actions/runs/43159487021/job/130987035658) | [2s](https://github.com/iree-org/iree/actions/runs/43159487021/job/130987035658) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987237139) | [1s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987237139) | [1s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987237139) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 314 | 310 | 2 | 2 | 1% |  | 11h15m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 266 | 263 | 2 | 1 | 1% |  | 11h30m ago |

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
