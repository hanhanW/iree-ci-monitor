# Status detail

_Updated: 2026-06-19 01:14 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `azure-linux-scale` | ossci | 4 | 0 | — | — | 1 | [10m51s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82309121156) | 30s | [30s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82309121156) | [30s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82309121156) | [30s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82309121156) | 0% (0/3) | — | 4 |  |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [1h26m](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770683) | 5s | [5s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770724) | [6s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770681) | [6s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770681) | 0% (0/4) | — | 6 |  |
| `ubuntu-24.04` | github-hosted | 15 | 0 | — | — | 2 | [1h26m](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770675) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27810236676/job/82298658231) | [3s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770679) | [3s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770679) | 15% (2/13) | 50% (2/4) | 15 |  |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [1h26m](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770671) | 3s | [3s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770671) | [3s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770677) | [3s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770677) | 0% (0/4) | — | 5 |  |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [1h26m](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770697) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770674) | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770697) | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770697) | 0% (0/4) | — | 5 |  |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | — | 0s | 0s | 0s | 0s | 0% (0/1) | — | 1 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | ossci | 1 | 0 | — | — | 1 | 30s | [30s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82309121156) | [30s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82309121156) | [30s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82309121156) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 6s | [6s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770681) | [6s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770681) | [6s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770681) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770724) | [5s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770724) | [5s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770724) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770683) | [5s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770683) | [5s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770683) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770679) | [3s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770679) | [3s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770679) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770671) | [3s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770671) | [3s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770671) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770677) | [3s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770677) | [3s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770677) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770682) | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770682) | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770682) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770675) | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770675) | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770675) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770664) | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770664) | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770664) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770697) | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770697) | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770697) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770674) | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770674) | [2s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298770674) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27808266933/job/82292631113) | [2s](https://github.com/iree-org/iree/actions/runs/27808266933/job/82292631113) | [2s](https://github.com/iree-org/iree/actions/runs/27808266933/job/82292631113) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27808266933/job/82292631133) | [2s](https://github.com/iree-org/iree/actions/runs/27808266933/job/82292631133) | [2s](https://github.com/iree-org/iree/actions/runs/27808266933/job/82292631133) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27808266933/job/82293703303) | [2s](https://github.com/iree-org/iree/actions/runs/27808266933/job/82293703303) | [2s](https://github.com/iree-org/iree/actions/runs/27808266933/job/82293703303) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27810236676/job/82298658231) | [2s](https://github.com/iree-org/iree/actions/runs/27810236676/job/82298658231) | [2s](https://github.com/iree-org/iree/actions/runs/27810236676/job/82298658231) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298748963) | [1s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298748963) | [1s](https://github.com/iree-org/iree/actions/runs/27810264571/job/82298748963) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 143 | 142 | 0 | 1 | 0% |  | 10h41m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 102 | 101 | 0 | 1 | 0% |  | 10h42m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 108 | 101 | 6 | 1 | 6% |  | 10h47m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 116 | 115 | 0 | 1 | 0% |  | 10h49m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 32 | 31 | 0 | 1 | 0% |  | 11h02m ago |

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
