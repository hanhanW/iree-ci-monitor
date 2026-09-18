# iree-ci-monitor

_Updated: 2026-09-18 04:23 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 12 | 3 | [3h11m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529520015) | 2026-09-18 04:21 PDT | 0 | [2h14m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517051058) | [2h56m](https://github.com/iree-org/iree/actions/runs/35322330390/job/105531038633) | 0% (0/3) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [2h18m](https://github.com/iree-org/iree/actions/runs/35322330544/job/105530686235) | [2h53m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519941) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 1 | [1h43m](https://github.com/iree-org/iree/actions/runs/35322330544/job/105530686191) | [2h38m](https://github.com/iree-org/iree/actions/runs/35322331231/job/105530927321) | 0% (0/3) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [29m09s](https://github.com/iree-org/iree/actions/runs/35322330544/job/105530686192) | [2h04m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519816) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [18m20s](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519775) | [1h40m](https://github.com/iree-org/iree/actions/runs/35322330544/job/105530686048) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [54m14s](https://github.com/iree-org/iree/actions/runs/35322330390/job/105531038608) | [1h27m](https://github.com/iree-org/iree/actions/runs/35322331181/job/105530601666) | 0% (0/2) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [37m14s](https://github.com/iree-org/iree/actions/runs/35322331231/job/105530927317) | [1h09m](https://github.com/iree-org/iree/actions/runs/35322330544/job/105530686152) | 0% (0/4) | `shark55-ci`, `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 149 | 0 | — | — | 2 | [2m11s](https://github.com/iree-org/iree/actions/runs/35322331157/job/105527394004) | [12m26s](https://github.com/iree-org/iree/actions/runs/35322331231/job/105530926976) | 0% (0/41) | 141 |
| `windows-2022` | github-hosted | 20 | 0 | — | — | 0 | [1m03s](https://github.com/iree-org/iree/actions/runs/35322330742/job/105527803169) | [6m18s](https://github.com/iree-org/iree/actions/runs/35322331365/job/105529477827) | 0% (0/6) | 20 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [1m17s](https://github.com/iree-org/iree/actions/runs/35322330408/job/105529177298) | [5m28s](https://github.com/iree-org/iree/actions/runs/35322331207/job/105528281552) | 0% (0/6) | 21 |
| `macos-14` | github-hosted | 21 | 0 | — | — | 1 | [1m00s](https://github.com/iree-org/iree/actions/runs/35322330742/job/105527803114) | [5m00s](https://github.com/iree-org/iree/actions/runs/35322331365/job/105529477766) | 0% (0/6) | 21 |
| `azure-linux-scale` | ossci | 34 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/35322323187/job/105527415309) | [2m14s](https://github.com/iree-org/iree/actions/runs/35322331365/job/105529477953) | 0% (0/14) | 34 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m27s](https://github.com/iree-org/iree/actions/runs/35329565578/job/105550511911) | [1m27s](https://github.com/iree-org/iree/actions/runs/35329565578/job/105550511911) | 100% (1/1) | 1 |
| `ubuntu-latest` | github-hosted | 30 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35322326222/job/105527382373) | [3s](https://github.com/iree-org/iree/actions/runs/35322326172/job/105527383469) | 0% (0/6) | 30 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/35322330742/job/105527803584) | [2s](https://github.com/iree-org/iree/actions/runs/35322323187/job/105527415182) | 0% (0/2) | 6 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 15 | 15 | [19h10m](https://github.com/iree-org/iree/actions/runs/35244084342/job/105282772106) | 2026-09-18 04:21 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 6 | [4h00m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050682) | 2026-09-18 04:21 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [19h10m](https://github.com/iree-org/iree/actions/runs/35244084342/job/105282772106) | 2026-09-18 04:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [19h10m](https://github.com/iree-org/iree/actions/runs/35244090870/job/105282957801) | 2026-09-18 04:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/egebeysel/scalable-dist-3-unpack-distribution-hints` | pull_request |
| [19h07m](https://github.com/iree-org/iree/actions/runs/35244089937/job/105283906279) | 2026-09-18 04:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/egebeysel/scalable-dist-2-distribution-tile-sizes` | pull_request |
| [19h02m](https://github.com/iree-org/iree/actions/runs/35244090100/job/105285600898) | 2026-09-18 04:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/egebeysel/scalable-dist-5-distribution-tiling-tests` | pull_request |
| [18h38m](https://github.com/iree-org/iree/actions/runs/35245416206/job/105294110239) | 2026-09-18 04:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `integrates/llvm-20260916` | pull_request |
| [17h21m](https://github.com/iree-org/iree/actions/runs/35251598607/job/105320096896) | 2026-09-18 04:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `add-fma-math-vm-lowringg` | pull_request |
| [16h36m](https://github.com/iree-org/iree/actions/runs/35257416856/job/105335534767) | 2026-09-18 04:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [16h25m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360642) | 2026-09-18 04:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [16h23m](https://github.com/iree-org/iree/actions/runs/35259670726/job/105339834679) | 2026-09-18 04:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_canonicalize_dynamism` | pull_request |
| [4h00m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050682) | 2026-09-18 04:21 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `main` | push |
| [4h00m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050800) | 2026-09-18 04:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [3h11m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519793) | 2026-09-18 04:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [3h11m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519874) | 2026-09-18 04:21 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `main` | push |
| [3h11m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529520015) | 2026-09-18 04:21 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [3h07m](https://github.com/iree-org/iree/actions/runs/35322331181/job/105530601652) | 2026-09-18 04:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_dynamic_reduce_window_scatter` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 15 | 15 | [19h10m](https://github.com/iree-org/iree/actions/runs/35244084342/job/105282772106) | 2026-09-18 04:21 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 6 | [4h00m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050682) | 2026-09-18 04:21 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 3 | [3h11m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529520015) | 2026-09-18 04:21 PDT | [2h14m](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517051058) | [2h56m](https://github.com/iree-org/iree/actions/runs/35322330390/job/105531038633) | [2h56m](https://github.com/iree-org/iree/actions/runs/35322330390/job/105531038633) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [1h31m](https://github.com/iree-org/iree/actions/runs/35322330390/job/105531038461) | [3h08m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519963) | [3h08m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519963) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [2h11m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519908) | [2h55m](https://github.com/iree-org/iree/actions/runs/35322331181/job/105530601671) | [2h55m](https://github.com/iree-org/iree/actions/runs/35322331181/job/105530601671) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [1h35m](https://github.com/iree-org/iree/actions/runs/35322331181/job/105530601720) | [2h53m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519941) | [2h53m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519941) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [2h06m](https://github.com/iree-org/iree/actions/runs/35322330390/job/105531038507) | [2h49m](https://github.com/iree-org/iree/actions/runs/35322331181/job/105530601797) | [2h49m](https://github.com/iree-org/iree/actions/runs/35322331181/job/105530601797) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [47m48s](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517051045) | [2h33m](https://github.com/iree-org/iree/actions/runs/35322331181/job/105530601705) | [2h33m](https://github.com/iree-org/iree/actions/runs/35322331181/job/105530601705) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [29m09s](https://github.com/iree-org/iree/actions/runs/35322330544/job/105530686192) | [2h04m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519816) | [2h04m](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519816) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [18m20s](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529519775) | [1h40m](https://github.com/iree-org/iree/actions/runs/35322330544/job/105530686048) | [1h40m](https://github.com/iree-org/iree/actions/runs/35322330544/job/105530686048) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [54m14s](https://github.com/iree-org/iree/actions/runs/35322330390/job/105531038608) | [1h27m](https://github.com/iree-org/iree/actions/runs/35322331181/job/105530601666) | [1h27m](https://github.com/iree-org/iree/actions/runs/35322331181/job/105530601666) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [31m41s](https://github.com/iree-org/iree/actions/runs/35318211424/job/105517050677) | [1h18m](https://github.com/iree-org/iree/actions/runs/35322330544/job/105530686180) | [1h18m](https://github.com/iree-org/iree/actions/runs/35322330544/job/105530686180) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [37m14s](https://github.com/iree-org/iree/actions/runs/35322331231/job/105530927317) | [1h09m](https://github.com/iree-org/iree/actions/runs/35322330544/job/105530686152) | [1h09m](https://github.com/iree-org/iree/actions/runs/35322330544/job/105530686152) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 6 | 0 | — | — | [4m24s](https://github.com/iree-org/iree/actions/runs/35322331207/job/105528281362) | [17m30s](https://github.com/iree-org/iree/actions/runs/35322330408/job/105529177400) | [17m30s](https://github.com/iree-org/iree/actions/runs/35322330408/job/105529177400) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 6 | 0 | — | — | [4m01s](https://github.com/iree-org/iree/actions/runs/35322330742/job/105527803239) | [16m34s](https://github.com/iree-org/iree/actions/runs/35322330408/job/105529177341) | [16m34s](https://github.com/iree-org/iree/actions/runs/35322330408/job/105529177341) | 6 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 6 | 0 | — | — | [49s](https://github.com/iree-org/iree/actions/runs/35322330742/job/105527803035) | [14m01s](https://github.com/iree-org/iree/actions/runs/35322330408/job/105529177115) | [14m01s](https://github.com/iree-org/iree/actions/runs/35322330408/job/105529177115) | 6 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 6 | 0 | — | — | [3m23s](https://github.com/iree-org/iree/actions/runs/35322323117/job/105529520110) | [13m00s](https://github.com/iree-org/iree/actions/runs/35322331181/job/105530601699) | [13m00s](https://github.com/iree-org/iree/actions/runs/35322331181/job/105530601699) | 6 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 6 | 0 | — | — | [5m37s](https://github.com/iree-org/iree/actions/runs/35322331181/job/105530602145) | [12m53s](https://github.com/iree-org/iree/actions/runs/35322330544/job/105530686171) | [12m53s](https://github.com/iree-org/iree/actions/runs/35322330544/job/105530686171) | 6 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 6 | 0 | — | — | [5m15s](https://github.com/iree-org/iree/actions/runs/35322331231/job/105530927142) | [12m34s](https://github.com/iree-org/iree/actions/runs/35322331181/job/105530601674) | [12m34s](https://github.com/iree-org/iree/actions/runs/35322331181/job/105530601674) | 6 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 6 | 0 | — | — | [5m33s](https://github.com/iree-org/iree/actions/runs/35322330544/job/105530686220) | [12m26s](https://github.com/iree-org/iree/actions/runs/35322331231/job/105530926976) | [12m26s](https://github.com/iree-org/iree/actions/runs/35322331231/job/105530926976) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 352 | 1% (2/351) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 426 | 1% (4/426) |  | 2m37s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 310 | 2% (5/310) |  | 14h05m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 118 | 8% (9/118) |  | 3d19h ago |

## Alerts

- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job observed waiting 4h00m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 19h10m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 3h11m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h38m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h40m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h53m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h04m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h56m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h09m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
