# iree-ci-monitor

_Updated: 2026-07-24 17:55 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [13m18s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934630) | [24m19s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934610) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [21m44s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934369) | [21m44s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934369) | — | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [11m33s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934453) | [20m37s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934620) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [13m40s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934618) | [16m58s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934624) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [7m31s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934278) | [7m31s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934278) | — | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [6m46s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934319) | [6m46s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934319) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934302) | [6m36s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934360) | — | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [5m52s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934471) | [5m52s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934471) | — | `shark10-ci` |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376528) | [25s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376846) | — | 3 |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [15s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89526378313) | [18s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376810) | — | 5 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376797) | [4s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376793) | — | 3 |
| `ubuntu-24.04` | github-hosted | 44 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934213) | [3s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376488) | — | 36 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376756) | [2s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376765) | — | 3 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934168) | [2s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934168) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934170) | [2s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934170) | — | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934313) | [2s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934313) | — | `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934342) | [2s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934342) | — | 1 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934419) | [2s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934419) | — | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376811) | [1s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376811) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [24m19s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934610) | [24m19s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934610) | [24m19s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934610) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [21m44s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934369) | [21m44s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934369) | [21m44s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934369) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [20m37s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934620) | [20m37s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934620) | [20m37s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934620) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [16m58s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934624) | [16m58s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934624) | [16m58s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934624) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [13m40s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934618) | [13m40s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934618) | [13m40s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934618) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [13m18s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934630) | [13m18s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934630) | [13m18s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934630) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [11m33s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934453) | [11m33s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934453) | [11m33s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934453) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [7m31s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934278) | [7m31s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934278) | [7m31s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934278) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [6m46s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934319) | [6m46s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934319) | [6m46s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934319) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [6m36s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934360) | [6m36s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934360) | [6m36s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934360) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [5m52s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934471) | [5m52s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934471) | [5m52s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934471) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [25s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376846) | [25s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376846) | [25s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376846) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [18s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376810) | [18s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376810) | [18s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376810) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [15s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376840) | [15s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376840) | [15s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376840) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [15s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89526378313) | [15s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89526378313) | [15s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89526378313) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [14s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376673) | [14s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376673) | [14s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376673) | 1 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30106792091/job/89526056864) | [4s](https://github.com/iree-org/iree/actions/runs/30106827488/job/89526174145) | [4s](https://github.com/iree-org/iree/actions/runs/30106827488/job/89526174145) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376793) | [4s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376793) | [4s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376793) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30106827488/job/89526237648) | [3s](https://github.com/iree-org/iree/actions/runs/30093017654/job/89534698044) | [3s](https://github.com/iree-org/iree/actions/runs/30093017654/job/89534698044) | 5 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376488) | [3s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376488) | [3s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376488) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 269 | 1% (3/269) |  | 8h31m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 368 | 1% (5/368) |  | 8h33m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 300 | 5% (14/300) |  | 8h34m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 281 | 1% (2/281) |  | 8h35m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 84 | 1% (1/84) |  | 8h48m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
