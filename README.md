# iree-ci-monitor

_Updated: 2026-09-19 04:06 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [8m34s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672659) | [15m42s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672640) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [1m38s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672700) | [14m44s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672601) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [12m46s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672629) | [12m46s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672629) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [12m28s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672681) | [12m28s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672681) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [10m43s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672714) | [10m43s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672714) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672607) | [7m40s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672716) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672606) | [1m44s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672749) | 0% (0/2) | `shark75-ci` |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729147) | [9s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729259) | 0% (0/7) | 7 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826728967) | [8s](https://github.com/iree-org/iree/actions/runs/35423426403/job/105845145387) | 0% (0/3) | 5 |
| `ubuntu-24.04` | github-hosted | 31 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/35423426403/job/105845122956) | [4s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729078) | 9% (2/22) | 31 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729103) | [4s](https://github.com/iree-org/iree/actions/runs/35423426403/job/105845145406) | 0% (0/3) | 6 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/35439111188/job/105886743891) | [3s](https://github.com/iree-org/iree/actions/runs/35416966947/job/105827399845) | 0% (0/3) | 12 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35423426403/job/105845145348) | [3s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729004) | 0% (0/3) | 5 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729312) | [1s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729312) | 0% (0/1) | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 7 | 7 | [20h04m](https://github.com/iree-org/iree/actions/runs/35358845541/job/105647952101) | 2026-09-19 04:05 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 7 | 7 | [20h04m](https://github.com/iree-org/iree/actions/runs/35358845541/job/105647952198) | 2026-09-19 04:05 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [20h04m](https://github.com/iree-org/iree/actions/runs/35358845541/job/105647952101) | 2026-09-19 04:05 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/ziereis/qdq-integer-contractions` | pull_request |
| [20h04m](https://github.com/iree-org/iree/actions/runs/35358845541/job/105647952198) | 2026-09-19 04:05 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/ziereis/qdq-integer-contractions` | pull_request |
| [19h43m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304560) | 2026-09-19 04:05 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/jschuhmacher/stablehlo_dynamic_pad_conv` | pull_request |
| [19h43m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304588) | 2026-09-19 04:05 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_dynamic_pad_conv` | pull_request |
| [19h43m](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361198) | 2026-09-19 04:05 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/jschuhmacher/stablehlo_dynamic_gather_broadcast` | pull_request |
| [19h43m](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361457) | 2026-09-19 04:05 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_dynamic_gather_broadcast` | pull_request |
| [19h43m](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362358) | 2026-09-19 04:05 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/jschuhmacher/stablehlo_lower_bounds` | pull_request |
| [19h43m](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362593) | 2026-09-19 04:05 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_lower_bounds` | pull_request |
| [19h41m](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841111) | 2026-09-19 04:05 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_dynamic_reduce_window_scatter` | pull_request |
| [19h41m](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841119) | 2026-09-19 04:05 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/jschuhmacher/stablehlo_dynamic_reduce_window_scatter` | pull_request |
| [15h00m](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361380) | 2026-09-19 04:05 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/jschuhmacher/dynamic-plugin-support-2` | pull_request |
| [15h00m](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361595) | 2026-09-19 04:05 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-2` | pull_request |
| [7h47m](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672695) | 2026-09-19 04:05 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `main` | push |
| [7h47m](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672722) | 2026-09-19 04:05 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 7 | 7 | [20h04m](https://github.com/iree-org/iree/actions/runs/35358845541/job/105647952101) | 2026-09-19 04:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 7 | 7 | [20h04m](https://github.com/iree-org/iree/actions/runs/35358845541/job/105647952198) | 2026-09-19 04:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [15m42s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672640) | [15m42s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672640) | [15m42s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672640) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [14m44s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672601) | [14m44s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672601) | [14m44s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672601) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [12m46s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672629) | [12m46s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672629) | [12m46s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672629) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [12m28s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672681) | [12m28s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672681) | [12m28s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672681) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [10m43s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672714) | [10m43s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672714) | [10m43s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672714) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [8m34s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672659) | [8m34s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672659) | [8m34s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672659) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [7m40s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672716) | [7m40s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672716) | [7m40s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672716) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [1m44s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672749) | [1m44s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672749) | [1m44s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672749) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [1m38s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672700) | [1m38s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672700) | [1m38s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672700) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729175) | [9s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729175) | [9s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729175) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729259) | [9s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729259) | [9s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729259) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35423426403/job/105845145387) | [8s](https://github.com/iree-org/iree/actions/runs/35423426403/job/105845145387) | [8s](https://github.com/iree-org/iree/actions/runs/35423426403/job/105845145387) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729147) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729147) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729147) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729185) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729185) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729185) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826728967) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826728967) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826728967) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729151) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729151) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729151) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729170) | [7s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729170) | [7s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729170) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672645) | [7s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672645) | [7s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672645) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 354 | 1% (3/354) |  | 7h26m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 316 | 0% (1/316) |  | 7h31m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 230 | 2% (4/230) |  | 1d13h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 17 | 12% (2/17) |  | 4d19h ago |

## Alerts

- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job observed waiting 20h04m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 20h04m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
