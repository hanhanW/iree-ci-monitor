# Status detail

_Updated: 2026-07-08 18:00 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `Linux,X64,iree-r9700` | self-hosted | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659037) | 2026-07-06 06:33 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659103) | 2026-07-06 06:33 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659129) | 2026-07-06 06:33 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |
| `Linux,X64,gfx1201` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659148) | 2026-07-06 06:33 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |
| `Linux,X64,rdna3` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659151) | 2026-07-06 06:33 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 3 | 3 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659155) | 2026-07-06 06:33 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |
| `Linux,X64,gfx1100` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659172) | 2026-07-06 06:33 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659179) | 2026-07-06 06:33 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659317) | 2026-07-06 06:33 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659037) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659103) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659129) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659148) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659151) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659155) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659164) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659172) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659178) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659179) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659219) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659317) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `convert-broadcast-batch-matmul` | pull_request |
| [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620205987) | 2026-07-07 06:05 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | `integrates/llvm-20260707` | pull_request |
| [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206031) | 2026-07-07 06:05 PDT | `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | `integrates/llvm-20260707` | pull_request |
| [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206069) | 2026-07-07 06:05 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `integrates/llvm-20260707` | pull_request |
| [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206165) | 2026-07-07 06:05 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | `integrates/llvm-20260707` | pull_request |
| [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206176) | 2026-07-07 06:05 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `integrates/llvm-20260707` | pull_request |
| [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206189) | 2026-07-07 06:05 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `integrates/llvm-20260707` | pull_request |

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659317) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659179) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659129) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659155) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659103) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | self-hosted | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659037) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | self-hosted | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659164) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | self-hosted | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659178) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | self-hosted | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659148) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | self-hosted | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659151) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | self-hosted | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659172) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | self-hosted | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659219) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | self-hosted | 1 | 1 | [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206069) | 2026-07-07 06:05 PDT | 0 | 0s | 0s | 0s | 0s | 0 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 243 | 232 | 7 | 3 | 3% | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 186 | 180 | 2 | 3 | 1% | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 208 | 189 | 14 | 4 | 7% | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 177 | 172 | 2 | 2 | 1% | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 58 | 49 | 6 | 3 | 10% |  | 1d01h ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

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
