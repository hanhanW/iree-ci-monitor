# Status detail

_Updated: 2026-08-01 00:09 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04` | github-hosted | 8 | 0 | — | — | 2 | [1h06m](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639274) | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91335039950) | [8s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639290) | [8s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639290) | 33% (2/6) | 50% (1/2) | 8 |  |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [1h06m](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639281) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639296) | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639281) | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639281) | 0% (0/1) | — | 2 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [1h06m](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639276) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639284) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639287) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639287) | 0% (0/1) | — | 3 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [1h06m](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639303) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639302) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639303) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639303) | 0% (0/1) | — | 2 |  |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 9 | 9 | [22h51m](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445151) | 2026-08-01 00:08 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [22h51m](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445151) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [21h39m](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514612) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `fix/23345-custom-op-static-loop-ranges` | pull_request |
| [21h02m](https://github.com/iree-org/iree/actions/runs/30621832279/job/91129775249) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [14h15m](https://github.com/iree-org/iree/actions/runs/30646844543/job/91217330080) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `fix-stablehlo-scatter` | pull_request |
| [14h13m](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783698) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `fix-slo-composite` | pull_request |
| [12h26m](https://github.com/iree-org/iree/actions/runs/30655580496/job/91241055463) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [11h43m](https://github.com/iree-org/iree/actions/runs/30658571489/job/91250481355) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [11h41m](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001169) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `integrates/llvm-20260731-cleanup` | pull_request |
| [11h39m](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264223) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | ossci | 9 | 9 | [22h51m](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445151) | 2026-08-01 00:08 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639290) | [8s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639290) | [8s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639290) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334616614) | [4s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334616614) | [4s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334616614) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91335039950) | [3s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91339200600) | [3s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91339200600) | 2 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639281) | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639281) | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639281) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639276) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639276) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639276) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639284) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639284) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639284) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639287) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639287) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639287) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639283) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639283) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639283) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639274) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639274) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639274) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639271) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639271) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639271) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639296) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639296) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639296) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639303) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639303) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639303) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639302) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639302) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639302) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30686947433/job/91334541438) | [2s](https://github.com/iree-org/iree/actions/runs/30686947433/job/91334541438) | [2s](https://github.com/iree-org/iree/actions/runs/30686947433/job/91334541438) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 166 | 166 | 0 | 0 | 0% |  | 10h39m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 118 | 117 | 1 | 0 | 1% |  | 10h50m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 148 | 144 | 4 | 0 | 3% |  | 10h52m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 123 | 121 | 1 | 1 | 1% |  | 10h55m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 37 | 36 | 1 | 0 | 3% |  | 11h09m ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 22h51m (> 2h00m)

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
