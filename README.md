# iree-ci-monitor

_Updated: 2026-06-23 06:18 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [21m20s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330325) | [34m31s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438178) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330097) | [28m12s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438250) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [12m46s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438397) | [27m41s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330276) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [13m13s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438285) | [23m23s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815011) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [8m47s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438402) | [21m22s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815151) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438224) | [20m57s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330160) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [7m35s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815095) | [20m18s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438390) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [5m20s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438531) | [19m15s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438173) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [6m53s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438218) | [17m08s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815081) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [10m28s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330230) | [17m00s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815057) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [6m39s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330288) | [14m23s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438132) | 0% (0/1) | `shark10-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 19 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/28008559577/job/82896103076) | [5m12s](https://github.com/iree-org/iree/actions/runs/28012486123/job/82908816280) | 0% (0/8) | 19 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m32s](https://github.com/iree-org/iree/actions/runs/28019544193/job/82932124574) | [1m32s](https://github.com/iree-org/iree/actions/runs/28019544193/job/82932124574) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 11 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28012486123/job/82908815982) | [1m25s](https://github.com/iree-org/iree/actions/runs/28012486123/job/82908816518) | 0% (0/3) | 11 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/28021790536/job/82939682878) | [1m12s](https://github.com/iree-org/iree/actions/runs/28008559577/job/82896102986) | 0% (0/3) | 12 |
| `macos-14` | github-hosted | 12 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/28021790536/job/82939682833) | [39s](https://github.com/iree-org/iree/actions/runs/28008559577/job/82896102987) | 0% (0/3) | 12 |
| `ubuntu-24.04` | github-hosted | 73 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/28012486123/job/82908816054) | [10s](https://github.com/iree-org/iree/actions/runs/28019552400/job/82932148559) | 9% (2/22) | 73 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 12 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815158) | [8s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815112) | 0% (0/4) | 12 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [6s](https://github.com/iree-org/iree/actions/runs/28019510129/job/82932022905) | [6s](https://github.com/iree-org/iree/actions/runs/28019510129/job/82932022905) | — | 1 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28025861136/job/82953406399) | [4s](https://github.com/iree-org/iree/actions/runs/28021785021/job/82939626495) | 0% (0/3) | 15 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330198) | [2s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438416) | 0% (0/1) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28012486123/job/82908816322) | [2s](https://github.com/iree-org/iree/actions/runs/28021790536/job/82939683067) | 0% (0/1) | 3 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 6 | [22h05m](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317105) | 2026-06-23 06:17 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [22h05m](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317105) | 2026-06-23 06:17 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `add-gpu-ada-known-target` | pull_request |
| [16h51m](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161046) | 2026-06-23 06:17 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [15h18m](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228625) | 2026-06-23 06:17 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `dependabot/github_actions/github-actions-ad4787fcfd` | pull_request |
| [6h05m](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330192) | 2026-06-23 06:17 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [4h48m](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438192) | 2026-06-23 06:17 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `devtbi/tduf` | pull_request |
| [1h41m](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944814860) | 2026-06-23 06:17 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `integrates/llvm-20260623` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 6 | 6 | [22h05m](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317105) | 2026-06-23 06:17 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [21m20s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330325) | [34m31s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438178) | [34m31s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438178) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330097) | [28m12s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438250) | [28m12s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438250) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [18m04s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438200) | [27m41s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330276) | [27m41s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330276) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [13m13s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438285) | [23m23s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815011) | [23m23s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815011) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [12m46s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438397) | [22m35s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815140) | [22m35s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815140) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [16m54s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330370) | [21m22s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815151) | [21m22s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815151) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438224) | [20m57s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330160) | [20m57s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330160) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [12m36s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330342) | [20m18s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438390) | [20m18s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438390) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [15m18s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815088) | [19m15s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438173) | [19m15s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438173) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [6m53s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438218) | [17m08s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815081) | [17m08s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815081) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [10m28s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330230) | [17m00s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815057) | [17m00s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815057) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [6m39s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330288) | [14m23s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438132) | [14m23s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438132) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [5m20s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438531) | [11m37s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330176) | [11m37s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330176) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [5m33s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815103) | [10m19s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330283) | [10m19s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330283) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438165) | [7m35s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815095) | [7m35s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815095) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 3 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/28008559577/job/82896102915) | [5m46s](https://github.com/iree-org/iree/actions/runs/28012486123/job/82908816215) | [5m46s](https://github.com/iree-org/iree/actions/runs/28012486123/job/82908816215) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 3 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/28008559577/job/82896103076) | [5m12s](https://github.com/iree-org/iree/actions/runs/28012486123/job/82908816280) | [5m12s](https://github.com/iree-org/iree/actions/runs/28012486123/job/82908816280) | 3 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 3 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/28008559577/job/82896103050) | [2m05s](https://github.com/iree-org/iree/actions/runs/28012486123/job/82908816218) | [2m05s](https://github.com/iree-org/iree/actions/runs/28012486123/job/82908816218) | 3 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | 1 | 0 | — | — | [1m46s](https://github.com/iree-org/iree/actions/runs/28019530869/job/82932085450) | [1m46s](https://github.com/iree-org/iree/actions/runs/28019530869/job/82932085450) | [1m46s](https://github.com/iree-org/iree/actions/runs/28019530869/job/82932085450) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 129 | 0% (0/129) |  | 1h13m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 163 | 0% (0/163) |  | 1h13m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 111 | 0% (0/111) |  | 1h15m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 126 | 5% (6/126) |  | 1h20m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 36 | 0% (0/36) |  | 1h31m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 22h05m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
