# Status detail

_Updated: 2026-10-24 21:49 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | — | 1h20m | [1h18m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163846) | [1h22m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163827) | [1h22m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163827) | 0% (0/2) | 0% (0/2) | 1 | yes |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | — | 50m04s | [50m04s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163745) | [50m04s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163745) | [50m04s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163745) | 0% (0/1) | 0% (0/1) | 1 | yes |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | — | 35m55s | [27m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163883) | [44m40s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163872) | [44m40s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163872) | 0% (0/2) | 0% (0/2) | 1 | yes |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | — | 39m16s | [39m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163718) | [39m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163718) | [39m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163718) | 0% (0/1) | 0% (0/1) | 1 | yes |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | — | 14m45s | [7m17s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163866) | [22m13s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163890) | [22m13s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163890) | 0% (0/2) | 0% (0/2) | 1 | yes |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | — | 3m43s | [2m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163755) | [5m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163695) | [5m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163695) | 0% (0/2) | 0% (0/2) | 2 |  |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | — | 22s | [22s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163807) | [22s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163807) | [22s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163807) | 0% (0/1) | 0% (0/1) | 1 | yes |
| `ubuntu-24.04` | github-hosted | 12 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163823) | [2s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120968860330) | [3s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120981696483) | 0% (0/12) | 0% (0/12) | 12 |  |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | self-hosted | 1 | 0 | — | — | 0 | 1h22m | [1h22m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163827) | [1h22m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163827) | [1h22m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163827) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | self-hosted | 1 | 0 | — | — | 0 | 1h18m | [1h18m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163846) | [1h18m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163846) | [1h18m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163846) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | 50m04s | [50m04s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163745) | [50m04s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163745) | [50m04s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163745) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | self-hosted | 1 | 0 | — | — | 0 | 44m40s | [44m40s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163872) | [44m40s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163872) | [44m40s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163872) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | 39m16s | [39m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163718) | [39m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163718) | [39m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163718) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | self-hosted | 1 | 0 | — | — | 0 | 27m10s | [27m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163883) | [27m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163883) | [27m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163883) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | self-hosted | 1 | 0 | — | — | 0 | 22m13s | [22m13s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163890) | [22m13s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163890) | [22m13s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163890) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | self-hosted | 1 | 0 | — | — | 0 | 7m17s | [7m17s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163866) | [7m17s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163866) | [7m17s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163866) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | self-hosted | 1 | 0 | — | — | 0 | 5m10s | [5m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163695) | [5m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163695) | [5m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163695) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | self-hosted | 1 | 0 | — | — | 0 | 2m16s | [2m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163755) | [2m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163755) | [2m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163755) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | 22s | [22s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163807) | [22s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163807) | [22s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163807) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120981696483) | [3s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120981696483) | [3s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120981696483) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120968860330) | [2s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120968860330) | [2s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120968860330) | 1 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163720) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163720) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163720) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163776) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163776) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163776) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163848) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163848) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163848) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163865) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163865) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163865) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163804) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163804) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163804) | 1 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163736) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163736) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163736) | 1 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163713) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163713) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163713) | 1 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163823) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163823) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163823) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163849) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163849) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163849) | 1 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163672) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163672) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163672) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 0 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 408 | 406 | 0 | 2 | 0% |  | 8h10m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 338 | 329 | 7 | 2 | 2% |  | 8h44m ago |

## Alerts

- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h22m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
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
