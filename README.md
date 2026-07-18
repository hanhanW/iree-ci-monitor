# iree-ci-monitor

_Updated: 2026-07-17 23:58 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [27m14s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549691) | [27m14s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549691) | — | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [14m18s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549663) | [26m20s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549667) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [10m49s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549752) | [21m44s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549692) | — | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [13m43s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549734) | [16m10s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549683) | — | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549646) | [9m20s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549679) | — | `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [7m45s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549681) | [7m45s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549681) | — | `shark01-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [6m36s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549574) | [6m36s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549574) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [4m30s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549580) | [4m30s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549580) | — | `shark10-ci` |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [1m38s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059088) | [1m48s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88004060018) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059139) | [6s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823755) | — | 6 |
| `ubuntu-24.04` | github-hosted | 33 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549715) | [3s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823764) | 0% (0/2) | 30 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823741) | [3s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059097) | — | 5 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549610) | [3s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549610) | — | 1 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059125) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823756) | — | 5 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059099) | [1s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059099) | — | 1 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549628) | [1s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549628) | — | `iree-mi308-1` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549629) | [1s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549629) | — | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549645) | [1s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549645) | — | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549651) | [1s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549651) | — | `shark75-ci` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [27m14s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549691) | [27m14s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549691) | [27m14s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549691) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [26m20s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549667) | [26m20s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549667) | [26m20s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549667) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [21m44s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549692) | [21m44s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549692) | [21m44s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549692) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [16m10s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549683) | [16m10s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549683) | [16m10s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549683) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [14m18s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549663) | [14m18s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549663) | [14m18s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549663) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [13m43s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549734) | [13m43s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549734) | [13m43s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549734) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [10m49s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549752) | [10m49s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549752) | [10m49s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549752) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [9m20s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549679) | [9m20s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549679) | [9m20s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549679) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [7m45s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549681) | [7m45s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549681) | [7m45s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549681) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [6m36s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549574) | [6m36s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549574) | [6m36s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549574) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [4m30s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549580) | [4m30s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549580) | [4m30s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549580) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [1m48s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88004060018) | [1m48s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88004060018) | [1m48s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88004060018) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m41s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059128) | [1m41s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059128) | [1m41s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059128) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [1m38s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059088) | [1m38s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059088) | [1m38s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059088) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [1m37s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059054) | [1m37s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059054) | [1m37s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059054) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [1m36s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059061) | [1m36s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059061) | [1m36s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059061) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823755) | [6s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823755) | [6s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823755) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823754) | [5s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823754) | [5s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823754) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823731) | [5s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823731) | [5s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823731) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059042) | [5s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059042) | [5s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059042) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 175 | 1% (1/175) |  | 8h08m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 141 | 9% (13/141) |  | 8h09m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 150 | 1% (2/150) |  | 8h15m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 137 | 0% (0/137) |  | 8h18m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 41 | 0% (0/41) |  | 8h28m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
