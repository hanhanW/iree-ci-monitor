# iree-ci-monitor

_Updated: 2026-09-18 21:42 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [14m52s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361931) | [29m10s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361731) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [12m46s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672629) | [28m19s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361452) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [7m40s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672716) | [25m52s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361784) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [12m28s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672681) | [19m14s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361527) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [1m44s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672749) | [19m02s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361796) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [8m34s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672659) | [15m42s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672640) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [10m43s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672714) | [12m46s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361545) | 0% (0/1) | `shark75-ci` |
| `azure-linux-scale` | ossci | 12 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/35388676347/job/105741717142) | [9s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729259) | 0% (0/7) | 12 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/35388676347/job/105741716691) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729151) | 0% (0/3) | 6 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729103) | [5s](https://github.com/iree-org/iree/actions/runs/35388676347/job/105741716898) | 0% (0/3) | 6 |
| `ubuntu-24.04` | github-hosted | 42 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/35260594164/job/105723669699) | [4s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729078) | 10% (2/21) | 42 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/35388676347/job/105741716887) | [3s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729004) | 0% (0/3) | 6 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35416967377/job/105827372373) | [3s](https://github.com/iree-org/iree/actions/runs/35416966947/job/105827399845) | 0% (0/3) | 12 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729312) | [2s](https://github.com/iree-org/iree/actions/runs/35388676347/job/105741717154) | 0% (0/1) | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 9 | 9 | [21h20m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050682) | 2026-09-18 21:42 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 9 | 9 | [21h20m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050800) | 2026-09-18 21:42 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [21h20m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050682) | 2026-09-18 21:42 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `main` | push |
| [21h20m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050800) | 2026-09-18 21:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [20h32m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519793) | 2026-09-18 21:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [20h32m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519874) | 2026-09-18 21:42 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `main` | push |
| [13h41m](https://github.com/iree-org/iree/actions/runs/35358845541/job/105647952101) | 2026-09-18 21:42 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/ziereis/qdq-integer-contractions` | pull_request |
| [13h41m](https://github.com/iree-org/iree/actions/runs/35358845541/job/105647952198) | 2026-09-18 21:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/ziereis/qdq-integer-contractions` | pull_request |
| [13h19m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304560) | 2026-09-18 21:42 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/jschuhmacher/stablehlo_dynamic_pad_conv` | pull_request |
| [13h19m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304588) | 2026-09-18 21:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_dynamic_pad_conv` | pull_request |
| [13h19m](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361198) | 2026-09-18 21:42 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/jschuhmacher/stablehlo_dynamic_gather_broadcast` | pull_request |
| [13h19m](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361457) | 2026-09-18 21:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_dynamic_gather_broadcast` | pull_request |
| [13h19m](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362358) | 2026-09-18 21:42 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/jschuhmacher/stablehlo_lower_bounds` | pull_request |
| [13h19m](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362593) | 2026-09-18 21:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_lower_bounds` | pull_request |
| [13h18m](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841111) | 2026-09-18 21:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_dynamic_reduce_window_scatter` | pull_request |
| [13h18m](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841119) | 2026-09-18 21:42 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/jschuhmacher/stablehlo_dynamic_reduce_window_scatter` | pull_request |
| [8h36m](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361380) | 2026-09-18 21:42 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/jschuhmacher/dynamic-plugin-support-2` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 9 | 9 | [21h20m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050682) | 2026-09-18 21:42 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 9 | 9 | [21h20m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050800) | 2026-09-18 21:42 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [1m38s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672700) | [29m10s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361731) | [29m10s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361731) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [12m46s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672629) | [28m19s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361452) | [28m19s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361452) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672607) | [25m52s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361784) | [25m52s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361784) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [12m28s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672681) | [19m14s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361527) | [19m14s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361527) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [1m44s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672749) | [19m02s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361796) | [19m02s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361796) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [5m02s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361569) | [15m42s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672640) | [15m42s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672640) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [14m44s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672601) | [14m52s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361931) | [14m52s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361931) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [10m43s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672714) | [12m46s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361545) | [12m46s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361545) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361535) | [8m34s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672659) | [8m34s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672659) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [5m53s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361726) | [7m40s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672716) | [7m40s](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672716) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729170) | [21s](https://github.com/iree-org/iree/actions/runs/35388676347/job/105741717122) | [21s](https://github.com/iree-org/iree/actions/runs/35388676347/job/105741717122) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35388676347/job/105741717067) | [9s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729175) | [9s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729175) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35388676347/job/105741717142) | [9s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729259) | [9s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729259) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/35388676347/job/105741716917) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729147) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729147) | 2 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35388676347/job/105741716691) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826728967) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826728967) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/35388676347/job/105741716912) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729151) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729151) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 2 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729093) | [8s](https://github.com/iree-org/iree/actions/runs/35388676347/job/105741716938) | [8s](https://github.com/iree-org/iree/actions/runs/35388676347/job/105741716938) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729185) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729185) | [8s](https://github.com/iree-org/iree/actions/runs/35416725131/job/105826729185) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 354 | 1% (3/354) |  | 1h03m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 316 | 0% (1/316) |  | 1h07m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 230 | 2% (4/230) |  | 1d07h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 17 | 12% (2/17) |  | 4d12h ago |

## Alerts

- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job observed waiting 21h20m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 21h20m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
