# iree-ci-monitor

_Updated: 2026-09-08 21:47 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/34310791080/job/102336860636) | [3s](https://github.com/iree-org/iree/actions/runs/34310791080/job/102336860817) | 0% (0/3) | 3 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076911) | 2026-09-08 04:24 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201` | self-hosted | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076980) | 2026-09-08 04:24 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076982) | 2026-09-08 04:24 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077064) | 2026-09-08 04:24 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077123) | 2026-09-08 04:24 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076911) | 2026-09-08 04:24 PDT | `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | `users/jschuhmacher/dynamic-plugin-support-1` | pull_request |
| [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076980) | 2026-09-08 04:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `users/jschuhmacher/dynamic-plugin-support-1` | pull_request |
| [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076982) | 2026-09-08 04:24 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/jschuhmacher/dynamic-plugin-support-1` | pull_request |
| [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077064) | 2026-09-08 04:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-1` | pull_request |
| [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077123) | 2026-09-08 04:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `users/jschuhmacher/dynamic-plugin-support-1` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077123) | 2026-09-08 04:24 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077064) | 2026-09-08 04:24 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076980) | 2026-09-08 04:24 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076982) | 2026-09-08 04:24 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076911) | 2026-09-08 04:24 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34310791080/job/102336860817) | [3s](https://github.com/iree-org/iree/actions/runs/34310791080/job/102336860817) | [3s](https://github.com/iree-org/iree/actions/runs/34310791080/job/102336860817) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34310791080/job/102336860636) | [3s](https://github.com/iree-org/iree/actions/runs/34310791080/job/102336860636) | [3s](https://github.com/iree-org/iree/actions/runs/34310791080/job/102336860636) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/34310791080/job/102338757108) | [1s](https://github.com/iree-org/iree/actions/runs/34310791080/job/102338757108) | [1s](https://github.com/iree-org/iree/actions/runs/34310791080/job/102338757108) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 131 | 2% (2/131) |  | 13h03m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 88 | 0% (0/88) |  | 13h06m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 111 | 5% (5/111) |  | 13h09m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 99 | 1% (1/99) |  | 13h11m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
