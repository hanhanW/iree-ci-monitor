# Status detail

_Updated: 2026-08-20 00:08 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 1 | [1h34m](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869830) | 5s | [5s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869835) | [6s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869844) | [6s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869844) | 50% (1/2) | — | 3 |  |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 2 | [1h34m](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869855) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869855) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869935) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869935) | 22% (2/9) | 0% (0/4) | 11 |  |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [1h34m](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869893) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870009) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869893) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869893) | 0% (0/1) | — | 2 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [1h34m](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870005) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870005) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869928) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869928) | 0% (0/1) | — | 2 |  |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759524) | 2026-08-19 00:07 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |
| `Linux,X64,rdna3` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759599) | 2026-08-19 00:07 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759660) | 2026-08-19 00:07 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |
| `Linux,X64,gfx1100` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759688) | 2026-08-19 00:07 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759971) | 2026-08-19 00:07 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759524) | 2026-08-19 00:07 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `main` | push |
| [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759599) | 2026-08-19 00:07 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759660) | 2026-08-19 00:07 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `main` | push |
| [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759688) | 2026-08-19 00:07 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759971) | 2026-08-19 00:07 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | `main` | push |

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759524) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759660) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759599) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759971) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759688) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 6s | [6s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869844) | [6s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869844) | [6s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869844) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869835) | [5s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869835) | [5s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869835) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869830) | [4s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869830) | [4s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869830) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869881) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869881) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869881) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869815) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869815) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869815) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869935) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869935) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869935) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869893) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869893) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869893) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869928) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869928) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869928) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/32274087599/job/96243015344) | [3s](https://github.com/iree-org/iree/actions/runs/32274087599/job/96243015344) | [3s](https://github.com/iree-org/iree/actions/runs/32274087599/job/96243015344) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/32332975306/job/96317020402) | [3s](https://github.com/iree-org/iree/actions/runs/32332975306/job/96317020402) | [3s](https://github.com/iree-org/iree/actions/runs/32332975306/job/96317020402) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869855) | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869855) | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869855) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870009) | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870009) | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870009) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325839192) | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325839192) | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325839192) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870005) | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870005) | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870005) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32274087453/job/96244813282) | [2s](https://github.com/iree-org/iree/actions/runs/32274087453/job/96244813282) | [2s](https://github.com/iree-org/iree/actions/runs/32274087453/job/96244813282) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32332975306/job/96317020545) | [2s](https://github.com/iree-org/iree/actions/runs/32332975306/job/96317020545) | [2s](https://github.com/iree-org/iree/actions/runs/32332975306/job/96317020545) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32332975306/job/96318339839) | [2s](https://github.com/iree-org/iree/actions/runs/32332975306/job/96318339839) | [2s](https://github.com/iree-org/iree/actions/runs/32332975306/job/96318339839) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32336047733/job/96325719201) | [2s](https://github.com/iree-org/iree/actions/runs/32336047733/job/96325719201) | [2s](https://github.com/iree-org/iree/actions/runs/32336047733/job/96325719201) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 212 | 207 | 1 | 3 | 0% | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 158 | 152 | 0 | 5 | 0% | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 192 | 183 | 6 | 2 | 3% | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 150 | 146 | 0 | 3 | 0% | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d

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
