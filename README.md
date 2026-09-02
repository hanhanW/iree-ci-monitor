# iree-ci-monitor

_Updated: 2026-09-02 14:06 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [19m13s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441171) | [26m00s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483583) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [10m07s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441317) | [20m26s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483451) | 0% (0/2) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [4m50s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441003) | [20m03s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483664) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [12m52s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441198) | [19m14s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483675) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [15m49s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483669) | [18m40s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441212) | 0% (0/4) | `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [8m35s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441135) | [18m18s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441211) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483159) | [14m17s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441025) | 0% (0/2) | `shark01-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441177) | [10m27s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483532) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [7m46s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441018) | [8m31s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483551) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483353) | [5m49s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255440953) | 0% (0/2) | `shark75-ci` |
| `azure-linux-scale` | ossci | 11 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527397) | [10s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603496) | 0% (0/6) | 11 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603117) | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527253) | 33% (1/3) | 6 |
| `ubuntu-24.04` | github-hosted | 42 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408461483) | [4s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483646) | 3% (1/31) | 42 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252602954) | [4s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603262) | 0% (0/3) | 6 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527126) | [4s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527281) | 0% (0/3) | 6 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33640317825/job/100281535543) | [3s](https://github.com/iree-org/iree/actions/runs/33640318512/job/100281460910) | 0% (0/3) | 15 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441276) | [2s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483543) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603507) | [1s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527389) | 0% (0/1) | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441057) | [26m00s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483583) | [26m00s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483583) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [10m07s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441317) | [20m26s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483451) | [20m26s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483451) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [4m50s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441003) | [20m03s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483664) | [20m03s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483664) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [12m52s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441198) | [19m14s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483675) | [19m14s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483675) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [7m17s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483526) | [19m13s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441171) | [19m13s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441171) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [15m49s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483669) | [18m40s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441212) | [18m40s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441212) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483652) | [18m18s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441211) | [18m18s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441211) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [14m45s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441027) | [15m16s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483610) | [15m16s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483610) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483159) | [14m17s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441025) | [14m17s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441025) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441177) | [10m27s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483532) | [10m27s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483532) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [5m45s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483368) | [8m35s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441135) | [8m35s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441135) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441196) | [8m31s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483551) | [8m31s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483551) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [5m56s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483723) | [7m46s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441018) | [7m46s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441018) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483353) | [5m49s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255440953) | [5m49s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255440953) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527343) | [10s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603469) | [10s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603469) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527618) | [10s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603461) | [10s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603461) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603496) | [10s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603496) | [10s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603496) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527355) | [9s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603445) | [9s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603445) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603568) | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527397) | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527397) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/33678321962/job/100408520670) | [8s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100252612993) | [8s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100252612993) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 220 | 0% (0/220) |  | 7h40m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 192 | 5% (9/192) |  | 7h42m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 147 | 0% (0/147) |  | 7h46m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 158 | 1% (1/158) |  | 7h50m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
