# Status detail

_Updated: 2026-09-02 21:37 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | — | 6s | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527355) | [9s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527618) | [9s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527618) | 40% (2/5) | — | 5 |  |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527252) | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100421355362) | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100421355362) | 18% (2/11) | — | 11 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 3s | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527313) | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527253) | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527253) | 0% (0/3) | — | 3 |  |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | — | 3s | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527320) | [4s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527281) | [4s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527281) | 0% (0/3) | — | 3 |  |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527250) | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527120) | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527120) | 0% (0/3) | — | 3 |  |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | — | 1s | [1s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527389) | [1s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527389) | [1s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527389) | 0% (0/1) | — | 1 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 9s | [9s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527618) | [9s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527618) | [9s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527618) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527355) | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527355) | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527355) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527397) | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527397) | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527397) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 7s | [7s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527343) | [7s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527343) | [7s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527343) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100421355362) | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100421355362) | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100421355362) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527253) | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527253) | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527253) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527281) | [4s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527281) | [4s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527281) | 1 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527208) | [4s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527208) | [4s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527208) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527120) | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527120) | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527120) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527313) | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527313) | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527313) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527320) | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527320) | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527320) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527093) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527093) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527093) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527124) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527124) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527124) | 1 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527126) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527126) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527126) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527094) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527094) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527094) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527250) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527250) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527250) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527227) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527227) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527227) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527156) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527156) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527156) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527252) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527252) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527252) | 1 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408461483) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408461483) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408461483) | 1 |
| `.github/workflows/clang_tidy.yml` | clang-tidy | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33678321395/job/100408460841) | [2s](https://github.com/iree-org/iree/actions/runs/33678321395/job/100408460841) | [2s](https://github.com/iree-org/iree/actions/runs/33678321395/job/100408460841) | 1 |
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33678321531/job/100408461419) | [2s](https://github.com/iree-org/iree/actions/runs/33678321531/job/100408461419) | [2s](https://github.com/iree-org/iree/actions/runs/33678321531/job/100408461419) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33678321962/job/100410440236) | [2s](https://github.com/iree-org/iree/actions/runs/33678321962/job/100410440236) | [2s](https://github.com/iree-org/iree/actions/runs/33678321962/job/100410440236) | 1 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33678321962/job/100408463674) | [2s](https://github.com/iree-org/iree/actions/runs/33678321962/job/100408463674) | [2s](https://github.com/iree-org/iree/actions/runs/33678321962/job/100408463674) | 1 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527389) | [1s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527389) | [1s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527389) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/33678321962/job/100408520670) | [1s](https://github.com/iree-org/iree/actions/runs/33678321962/job/100408520670) | [1s](https://github.com/iree-org/iree/actions/runs/33678321962/job/100408520670) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 199 | 196 | 0 | 3 | 0% |  | 15h11m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 171 | 162 | 7 | 2 | 4% |  | 15h14m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 133 | 130 | 0 | 3 | 0% |  | 15h17m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 139 | 136 | 1 | 2 | 1% |  | 15h21m ago |

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
