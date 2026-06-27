# Status detail

_Updated: 2026-06-27 00:24 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [1h09m](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369803) | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369806) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369808) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369808) | 0% (0/1) | — | 3 |  |
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 2 | [1h09m](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369813) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28280892242/job/83796313502) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369820) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369820) | 0% (0/4) | 0% (0/1) | 6 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [1h09m](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369894) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369809) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369894) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369894) | 0% (0/1) | — | 2 |  |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [1h09m](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369815) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369815) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369816) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369816) | 0% (0/1) | — | 2 |  |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 3 | 3 | [13h06m](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447477) | 2026-06-27 00:24 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [13h06m](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447477) | 2026-06-27 00:24 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/scalable_distribution_tiling` | pull_request |
| [13h05m](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677804) | 2026-06-27 00:24 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/scalable_vector_level_tiling` | pull_request |
| [13h03m](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722939709) | 2026-06-27 00:24 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/overload_iree_tiling_interface_ops` | pull_request |

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | ossci | 3 | 3 | [13h06m](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447477) | 2026-06-27 00:24 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369808) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369808) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369808) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369803) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369803) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369803) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369806) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369806) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369806) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369820) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369820) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369820) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796353903) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796353903) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796353903) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369813) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369813) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369813) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369815) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369815) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369815) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369816) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369816) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369816) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369894) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369894) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369894) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369809) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369809) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369809) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28280892242/job/83796313502) | [2s](https://github.com/iree-org/iree/actions/runs/28280892242/job/83796313502) | [2s](https://github.com/iree-org/iree/actions/runs/28280892242/job/83796313502) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369818) | [1s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369818) | [1s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369818) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369819) | [1s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369819) | [1s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369819) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 119 | 119 | 0 | 0 | 0% |  | 12h14m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 95 | 87 | 8 | 0 | 8% |  | 12h24m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 91 | 91 | 0 | 0 | 0% |  | 12h26m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 85 | 85 | 0 | 0 | 0% |  | 12h27m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 26 | 26 | 0 | 0 | 0% |  | 12h35m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 13h06m (> 2h00m)

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
