# Status detail

_Updated: 2026-10-04 05:27 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 5s | [4s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943099) | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943088) | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943088) | 33% (1/3) | — | 3 |  |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | — | 6s | [6s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943107) | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943087) | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943087) | 0% (0/2) | — | 2 |  |
| `ubuntu-24.04` | github-hosted | 7 | 0 | — | — | 1 | [5h30m](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943092) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943077) | [3s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943092) | [3s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943092) | 17% (1/6) | 0% (0/1) | 7 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943082) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943113) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943113) | 0% (0/2) | — | 2 |  |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 1 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721930) | 2026-10-04 05:27 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 1 | 1 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721946) | 2026-10-04 05:27 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |
| `Linux,X64,rdna3` | self-hosted | 2 | 2 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721988) | 2026-10-04 05:27 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |
| `Linux,X64,gfx1100` | self-hosted | 2 | 2 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722024) | 2026-10-04 05:27 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721930) | 2026-10-04 05:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |
| [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721946) | 2026-10-04 05:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |
| [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721988) | 2026-10-04 05:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |
| [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722024) | 2026-10-04 05:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |
| [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722031) | 2026-10-04 05:27 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |
| [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722066) | 2026-10-04 05:27 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 1 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721930) | 2026-10-04 05:27 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | self-hosted | 1 | 1 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721946) | 2026-10-04 05:27 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | self-hosted | 1 | 1 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722024) | 2026-10-04 05:27 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | self-hosted | 1 | 1 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721988) | 2026-10-04 05:27 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | self-hosted | 1 | 1 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722066) | 2026-10-04 05:27 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | self-hosted | 1 | 1 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722031) | 2026-10-04 05:27 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 7s | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943088) | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943088) | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943088) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 7s | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943087) | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943087) | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943087) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 6s | [6s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943107) | [6s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943107) | [6s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943107) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943099) | [4s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943099) | [4s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943099) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943046) | [4s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943046) | [4s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943046) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943092) | [3s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943092) | [3s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943092) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943096) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943096) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943096) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943083) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943083) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943083) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943077) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943077) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943077) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382915478) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382915478) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382915478) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943113) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943113) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943113) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943082) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943082) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943082) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111376769824) | [2s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111376769824) | [2s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111376769824) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37184259141/job/111382816759) | [2s](https://github.com/iree-org/iree/actions/runs/37184259141/job/111382816759) | [2s](https://github.com/iree-org/iree/actions/runs/37184259141/job/111382816759) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 296 | 284 | 4 | 8 | 1% |  | 15h42m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 206 | 203 | 2 | 1 | 1% |  | 3d15h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 16h04m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 16h04m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 16h04m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 16h04m (> 2h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

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
