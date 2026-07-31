# iree-ci-monitor

_Updated: 2026-07-30 17:56 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [21m18s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863202) | [21m18s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863202) | — | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [18m57s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863261) | [18m57s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863261) | — | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [15m10s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862699) | [15m10s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862699) | — | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [7m20s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863419) | [10m18s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863262) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [8m22s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863171) | [8m22s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863171) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [5m07s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862957) | [8m16s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863326) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863658) | [6m14s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863040) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [3m59s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862783) | [3m59s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862783) | — | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [3m04s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863289) | [3m04s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863289) | — | `shark75-ci` |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236734) | [24s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90922242951) | — | 5 |
| `ubuntu-24.04` | github-hosted | 25 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30589702237/job/91029074334) | [9s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862991) | 0% (0/2) | 23 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236606) | [6s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236356) | — | 3 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236609) | [6s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236746) | — | 3 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863218) | [4s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863218) | — | `iree-mi308-1` |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236464) | [3s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236564) | — | 3 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862809) | [2s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862809) | — | 1 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862994) | [2s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862994) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863403) | [2s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863407) | — | `shark01-ci`, `shark10-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236658) | [1s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236658) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [21m18s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863202) | [21m18s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863202) | [21m18s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863202) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [18m57s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863261) | [18m57s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863261) | [18m57s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863261) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [15m10s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862699) | [15m10s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862699) | [15m10s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862699) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [10m18s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863262) | [10m18s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863262) | [10m18s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863262) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [8m22s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863171) | [8m22s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863171) | [8m22s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863171) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [8m16s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863326) | [8m16s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863326) | [8m16s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863326) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [7m20s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863419) | [7m20s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863419) | [7m20s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863419) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [6m14s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863040) | [6m14s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863040) | [6m14s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863040) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [5m07s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862957) | [5m07s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862957) | [5m07s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862957) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [3m59s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862783) | [3m59s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862783) | [3m59s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862783) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [3m04s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863289) | [3m04s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863289) | [3m04s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863289) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [24s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90922242951) | [24s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90922242951) | [24s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90922242951) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [20s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236669) | [20s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236669) | [20s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236669) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236734) | [10s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236734) | [10s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236734) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236659) | [9s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236659) | [9s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236659) | 1 |
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/30555398910/job/90922183235) | [9s](https://github.com/iree-org/iree/actions/runs/30555398910/job/90922183235) | [9s](https://github.com/iree-org/iree/actions/runs/30555398910/job/90922183235) | 1 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862675) | [9s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862675) | [9s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862675) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863888) | [9s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863888) | [9s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863888) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862991) | [9s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862991) | [9s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862991) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236474) | [8s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236474) | [8s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236474) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 109 | 0% (0/109) |  | 3h08m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 143 | 3% (4/143) |  | 8h44m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 152 | 0% (0/152) |  | 8h53m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 34 | 3% (1/34) |  | 8h57m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 106 | 1% (1/106) |  | 8h57m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
