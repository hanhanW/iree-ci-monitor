# iree-ci-monitor

_Updated: 2026-09-18 13:58 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [1h32m](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362587) | [2h44m](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841179) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [1h05m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304531) | [2h29m](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362591) | — | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [1h38m](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361400) | [2h21m](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362629) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [1h33m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304696) | [2h11m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304727) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [1h18m](https://github.com/iree-org/iree/actions/runs/35358845541/job/105647952249) | [1h42m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304521) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [22m37s](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361178) | [50m14s](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841348) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [15m52s](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361146) | [48m02s](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362380) | — | `shark75-ci` |
| `windows-2022` | github-hosted | 18 | 0 | — | — | 0 | [56s](https://github.com/iree-org/iree/actions/runs/35360858649/job/105651548237) | [10m00s](https://github.com/iree-org/iree/actions/runs/35360855800/job/105651545087) | — | 18 |
| `macos-14` | github-hosted | 18 | 0 | — | — | 0 | [2m27s](https://github.com/iree-org/iree/actions/runs/35360867517/job/105651573252) | [8m34s](https://github.com/iree-org/iree/actions/runs/35360855800/job/105651545109) | — | 18 |
| `ubuntu-24.04` | github-hosted | 138 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744363010) | [8m21s](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841335) | 75% (3/4) | 138 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35388676347/job/105741717154) | [7m02s](https://github.com/iree-org/iree/actions/runs/35360870368/job/105651921337) | — | 6 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [1m04s](https://github.com/iree-org/iree/actions/runs/35360867517/job/105651573225) | [5m09s](https://github.com/iree-org/iree/actions/runs/35360858649/job/105651548266) | — | 18 |
| `azure-linux-scale` | ossci | 30 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/35360858649/job/105651548382) | [3m21s](https://github.com/iree-org/iree/actions/runs/35360870368/job/105651921277) | — | 30 |
| `ubuntu-latest` | github-hosted | 27 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/35358838395/job/105644772767) | [6s](https://github.com/iree-org/iree/actions/runs/35360867933/job/105651510679) | — | 27 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 8 | 8 | [13h36m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050800) | 2026-09-18 13:57 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 8 | 8 | [13h36m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050682) | 2026-09-18 13:57 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [13h36m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050682) | 2026-09-18 13:57 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `main` | push |
| [13h36m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050800) | 2026-09-18 13:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [12h47m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519793) | 2026-09-18 13:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [12h47m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519874) | 2026-09-18 13:57 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `main` | push |
| [5h56m](https://github.com/iree-org/iree/actions/runs/35358845541/job/105647952101) | 2026-09-18 13:57 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/ziereis/qdq-integer-contractions` | pull_request |
| [5h56m](https://github.com/iree-org/iree/actions/runs/35358845541/job/105647952198) | 2026-09-18 13:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/ziereis/qdq-integer-contractions` | pull_request |
| [5h35m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304560) | 2026-09-18 13:57 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/jschuhmacher/stablehlo_dynamic_pad_conv` | pull_request |
| [5h35m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304588) | 2026-09-18 13:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_dynamic_pad_conv` | pull_request |
| [5h35m](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361198) | 2026-09-18 13:57 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/jschuhmacher/stablehlo_dynamic_gather_broadcast` | pull_request |
| [5h35m](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361457) | 2026-09-18 13:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_dynamic_gather_broadcast` | pull_request |
| [5h35m](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362358) | 2026-09-18 13:57 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/jschuhmacher/stablehlo_lower_bounds` | pull_request |
| [5h35m](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362593) | 2026-09-18 13:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_lower_bounds` | pull_request |
| [5h33m](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841111) | 2026-09-18 13:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_dynamic_reduce_window_scatter` | pull_request |
| [5h33m](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841119) | 2026-09-18 13:57 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/jschuhmacher/stablehlo_dynamic_reduce_window_scatter` | pull_request |
| [52m17s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361380) | 2026-09-18 13:57 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/jschuhmacher/dynamic-plugin-support-2` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 8 | 8 | [13h36m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050682) | 2026-09-18 13:57 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 8 | 8 | [13h36m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050800) | 2026-09-18 13:57 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [1h17m](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361481) | [2h58m](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841258) | [2h58m](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841258) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [26m30s](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361420) | [2h53m](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841256) | [2h53m](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841256) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [29m10s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105744361731) | [2h44m](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841179) | [2h44m](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841179) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [1h05m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304531) | [2h29m](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362591) | [2h29m](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362591) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [1h33m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304696) | [2h28m](https://github.com/iree-org/iree/actions/runs/35358845541/job/105647952361) | [2h28m](https://github.com/iree-org/iree/actions/runs/35358845541/job/105647952361) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [1h38m](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361400) | [2h21m](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362629) | [2h21m](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362629) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [1h02m](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361380) | [2h11m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304727) | [2h11m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304727) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [1h18m](https://github.com/iree-org/iree/actions/runs/35358845541/job/105647952249) | [1h42m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304521) | [1h42m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304521) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [2m33s](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361475) | [1h00m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304621) | [1h00m](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304621) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [22m37s](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361178) | [50m14s](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841348) | [50m14s](https://github.com/iree-org/iree/actions/runs/35360870302/job/105655841348) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [15m52s](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361146) | [48m02s](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362380) | [48m02s](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362380) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 6 | 0 | — | — | [5m48s](https://github.com/iree-org/iree/actions/runs/35360867517/job/105651573315) | [10m11s](https://github.com/iree-org/iree/actions/runs/35360858649/job/105651548281) | [10m11s](https://github.com/iree-org/iree/actions/runs/35360858649/job/105651548281) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 6 | 0 | — | — | [1m05s](https://github.com/iree-org/iree/actions/runs/35360867517/job/105651573210) | [10m06s](https://github.com/iree-org/iree/actions/runs/35360855800/job/105651545169) | [10m06s](https://github.com/iree-org/iree/actions/runs/35360855800/job/105651545169) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 6 | 0 | — | — | [56s](https://github.com/iree-org/iree/actions/runs/35360858649/job/105651548237) | [10m00s](https://github.com/iree-org/iree/actions/runs/35360855800/job/105651545087) | [10m00s](https://github.com/iree-org/iree/actions/runs/35360855800/job/105651545087) | 6 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 6 | 0 | — | — | [14s](https://github.com/iree-org/iree/actions/runs/35360855800/job/105651544760) | [9m03s](https://github.com/iree-org/iree/actions/runs/35360870368/job/105651920880) | [9m03s](https://github.com/iree-org/iree/actions/runs/35360870368/job/105651920880) | 6 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 6 | 0 | — | — | [48s](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304574) | [9m02s](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361356) | [9m02s](https://github.com/iree-org/iree/actions/runs/35360867550/job/105655361356) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 6 | 0 | — | — | [3m45s](https://github.com/iree-org/iree/actions/runs/35360870368/job/105651920890) | [8m40s](https://github.com/iree-org/iree/actions/runs/35360855800/job/105651545059) | [8m40s](https://github.com/iree-org/iree/actions/runs/35360855800/job/105651545059) | 6 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 6 | 0 | — | — | [2m24s](https://github.com/iree-org/iree/actions/runs/35360858699/job/105655304573) | [8m36s](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362580) | [8m36s](https://github.com/iree-org/iree/actions/runs/35360855757/job/105655362580) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 392 | 1% (2/392) |  | 15m46s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 455 | 1% (4/455) |  | 17m58s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 310 | 2% (5/310) |  | 23h41m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 118 | 8% (9/118) |  | 4d05h ago |

## Alerts

- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job observed waiting 13h36m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 13h36m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h29m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h44m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h42m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h11m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h21m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
