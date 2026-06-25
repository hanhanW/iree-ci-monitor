# Status detail

_Updated: 2026-06-25 00:31 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [1h04m](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402024) | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402049) | [6s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402024) | [6s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402024) | 0% (0/1) | — | 3 |  |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [1h04m](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402073) | 1s | [2s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83362517534) | [3s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402047) | [3s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402047) | 29% (2/7) | 50% (2/4) | 9 |  |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [1h04m](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402058) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402058) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402108) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402108) | 0% (0/1) | — | 2 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [1h04m](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402110) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402094) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402110) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402110) | 0% (0/1) | — | 2 |  |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 6 | [20h06m](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261695) | 2026-06-25 00:30 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [20h06m](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261695) | 2026-06-25 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `flow_empty_fold` | pull_request |
| [19h25m](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554091) | 2026-06-25 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [17h51m](https://github.com/iree-org/iree/actions/runs/28102210744/job/83208735459) | 2026-06-25 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [17h44m](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184300) | 2026-06-25 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/bjacob/cpu-ukernel-bodies` | pull_request |
| [16h59m](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582315) | 2026-06-25 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `fix-24624-raise-special-ops-memref-crash` | pull_request |
| [16h24m](https://github.com/iree-org/iree/actions/runs/28107886109/job/83228908779) | 2026-06-25 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 6 | [20h06m](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261695) | 2026-06-25 00:30 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 6s | [6s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402024) | [6s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402024) | [6s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402024) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402049) | [5s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402049) | [5s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402049) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402038) | [5s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402038) | [5s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402038) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402047) | [3s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402047) | [3s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402047) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369376612) | [3s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369376612) | [3s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369376612) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402070) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402070) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402070) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402058) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402058) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402058) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402108) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402108) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402108) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402110) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402110) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402110) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402094) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402094) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402094) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83362517534) | [2s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83362517534) | [2s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83362517534) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83362517517) | [2s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83362517517) | [2s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83362517517) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28151259678/job/83369276881) | [2s](https://github.com/iree-org/iree/actions/runs/28151259678/job/83369276881) | [2s](https://github.com/iree-org/iree/actions/runs/28151259678/job/83369276881) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402078) | [1s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402078) | [1s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402078) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402073) | [1s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402073) | [1s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402073) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83363567561) | [1s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83363567561) | [1s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83363567561) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 87 | 81 | 6 | 0 | 7% |  | 15h52m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 76 | 76 | 0 | 0 | 0% |  | 16h01m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 111 | 110 | 0 | 1 | 0% |  | 16h04m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 86 | 85 | 0 | 1 | 0% |  | 16h07m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 24 | 24 | 0 | 0 | 0% |  | 16h14m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 20h06m (> 2h00m)

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
