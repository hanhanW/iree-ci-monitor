# Status detail

_Updated: 2026-09-09 21:48 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04` | github-hosted | 3 | 0 | — | — | 0 | — | 1s | [2s](https://github.com/iree-org/iree/actions/runs/34436975327/job/102743989937) | [2s](https://github.com/iree-org/iree/actions/runs/34436975327/job/102745844466) | [2s](https://github.com/iree-org/iree/actions/runs/34436975327/job/102745844466) | 0% (0/3) | 0% (0/3) | 3 |  |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076911) | 2026-09-08 04:24 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |
| `Linux,X64,gfx1201` | self-hosted | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076980) | 2026-09-08 04:24 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |
| `Linux,X64,rdna3` | self-hosted | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076982) | 2026-09-08 04:24 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077064) | 2026-09-08 04:24 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077123) | 2026-09-08 04:24 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076911) | 2026-09-08 04:24 PDT | `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | `users/jschuhmacher/dynamic-plugin-support-1` | pull_request |
| [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076980) | 2026-09-08 04:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `users/jschuhmacher/dynamic-plugin-support-1` | pull_request |
| [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076982) | 2026-09-08 04:24 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/jschuhmacher/dynamic-plugin-support-1` | pull_request |
| [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077064) | 2026-09-08 04:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-1` | pull_request |
| [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077123) | 2026-09-08 04:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `users/jschuhmacher/dynamic-plugin-support-1` | pull_request |

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077123) | 2026-09-08 04:24 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077064) | 2026-09-08 04:24 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | self-hosted | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076980) | 2026-09-08 04:24 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | self-hosted | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076982) | 2026-09-08 04:24 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076911) | 2026-09-08 04:24 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/34436975327/job/102743989937) | [2s](https://github.com/iree-org/iree/actions/runs/34436975327/job/102743989937) | [2s](https://github.com/iree-org/iree/actions/runs/34436975327/job/102743989937) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/34436975327/job/102745844466) | [2s](https://github.com/iree-org/iree/actions/runs/34436975327/job/102745844466) | [2s](https://github.com/iree-org/iree/actions/runs/34436975327/job/102745844466) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/34436975327/job/102743989861) | [1s](https://github.com/iree-org/iree/actions/runs/34436975327/job/102743989861) | [1s](https://github.com/iree-org/iree/actions/runs/34436975327/job/102743989861) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 137 | 134 | 2 | 1 | 1% |  | 12h06m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 113 | 105 | 6 | 2 | 5% |  | 12h11m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 100 | 1 | 1 | 1% |  | 12h12m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 93 | 93 | 0 | 0 | 0% |  | 12h12m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
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
