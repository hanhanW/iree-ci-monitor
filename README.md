# iree-ci-monitor

_Updated: 2026-09-08 09:42 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 20 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076980) | 2026-09-08 04:24 PDT | 0 | [2h19m](https://github.com/iree-org/iree/actions/runs/34215592216/job/102046199371) | [4h08m](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012190506) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 10 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077123) | 2026-09-08 04:24 PDT | 0 | [2h25m](https://github.com/iree-org/iree/actions/runs/34209521784/job/102010505891) | [3h43m](https://github.com/iree-org/iree/actions/runs/34209530445/job/102014447382) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 10 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077064) | 2026-09-08 04:24 PDT | 0 | [2h42m](https://github.com/iree-org/iree/actions/runs/34209521784/job/102010505998) | [3h25m](https://github.com/iree-org/iree/actions/runs/34209508728/job/102009793946) | — | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 10 | 0 | — | — | 0 | [1h50m](https://github.com/iree-org/iree/actions/runs/34209508728/job/102009794193) | [3h11m](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012189976) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [2h29m](https://github.com/iree-org/iree/actions/runs/34209521784/job/102010506049) | [3h02m](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012190063) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 20 | 0 | — | — | 0 | [43m32s](https://github.com/iree-org/iree/actions/runs/34209508728/job/102009793980) | [2h53m](https://github.com/iree-org/iree/actions/runs/34209521784/job/102010506138) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 10 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076911) | 2026-09-08 04:24 PDT | 0 | [1h13m](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012190196) | [2h34m](https://github.com/iree-org/iree/actions/runs/34209521784/job/102010506057) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 20 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076982) | 2026-09-08 04:24 PDT | 0 | [1h18m](https://github.com/iree-org/iree/actions/runs/34209501648/job/102009899355) | [2h00m](https://github.com/iree-org/iree/actions/runs/34209516346/job/102010306733) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 10 | 0 | — | — | 0 | [16m48s](https://github.com/iree-org/iree/actions/runs/34209516346/job/102010306920) | [1h39m](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012190008) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [33m50s](https://github.com/iree-org/iree/actions/runs/34209530445/job/102014447283) | [1h35m](https://github.com/iree-org/iree/actions/runs/34209521784/job/102010506117) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 20 | 0 | — | — | 0 | [26m44s](https://github.com/iree-org/iree/actions/runs/34215592216/job/102046199111) | [1h29m](https://github.com/iree-org/iree/actions/runs/34209501648/job/102009899173) | — | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 235 | 0 | — | — | 0 | [4m45s](https://github.com/iree-org/iree/actions/runs/34209508778/job/102006940155) | [33m47s](https://github.com/iree-org/iree/actions/runs/34209508778/job/102006940020) | 67% (2/3) | 216 |
| `macos-14` | github-hosted | 34 | 0 | — | — | 0 | [2m32s](https://github.com/iree-org/iree/actions/runs/34209494730/job/102006897129) | [21m19s](https://github.com/iree-org/iree/actions/runs/34209530517/job/102008925050) | 0% (0/1) | 34 |
| `windows-2022` | github-hosted | 33 | 0 | — | — | 0 | [3m48s](https://github.com/iree-org/iree/actions/runs/34209501565/job/102006922145) | [12m43s](https://github.com/iree-org/iree/actions/runs/34209538076/job/102008493848) | — | 33 |
| `ubuntu-latest` | github-hosted | 39 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/34209544664/job/102007003931) | [11m09s](https://github.com/iree-org/iree/actions/runs/34209545121/job/102007004827) | — | 36 |
| `azure-windows-scale` | ossci | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34215592417/job/102044276831) | [9m50s](https://github.com/iree-org/iree/actions/runs/34209538076/job/102008494141) | — | 11 |
| `ubuntu-24.04-arm` | github-hosted | 33 | 0 | — | — | 0 | [43s](https://github.com/iree-org/iree/actions/runs/34209516499/job/102008423818) | [8m08s](https://github.com/iree-org/iree/actions/runs/34209530517/job/102008925100) | — | 33 |
| `azure-linux-scale` | ossci | 63 | 0 | — | — | 0 | [1m34s](https://github.com/iree-org/iree/actions/runs/34209521831/job/102009119314) | [3m14s](https://github.com/iree-org/iree/actions/runs/34209530517/job/102008925271) | 0% (0/2) | 61 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m37s](https://github.com/iree-org/iree/actions/runs/34210070981/job/102008693346) | [1m37s](https://github.com/iree-org/iree/actions/runs/34210070981/job/102008693346) | 0% (0/1) | 1 |

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
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 10 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076980) | 2026-09-08 04:24 PDT | [3h15m](https://github.com/iree-org/iree/actions/runs/34209508728/job/102009794168) | [4h20m](https://github.com/iree-org/iree/actions/runs/34209530445/job/102014447446) | [4h20m](https://github.com/iree-org/iree/actions/runs/34209530445/job/102014447446) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 10 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077123) | 2026-09-08 04:24 PDT | [2h25m](https://github.com/iree-org/iree/actions/runs/34209521784/job/102010505891) | [3h43m](https://github.com/iree-org/iree/actions/runs/34209530445/job/102014447382) | [3h43m](https://github.com/iree-org/iree/actions/runs/34209530445/job/102014447382) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [1h21m](https://github.com/iree-org/iree/actions/runs/34209521784/job/102010506142) | [3h41m](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012190297) | [3h41m](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012190297) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 10 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077064) | 2026-09-08 04:24 PDT | [2h42m](https://github.com/iree-org/iree/actions/runs/34209521784/job/102010505998) | [3h25m](https://github.com/iree-org/iree/actions/runs/34209508728/job/102009793946) | [3h25m](https://github.com/iree-org/iree/actions/runs/34209508728/job/102009793946) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 10 | 0 | — | — | [1h50m](https://github.com/iree-org/iree/actions/runs/34209508728/job/102009794193) | [3h11m](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012189976) | [3h11m](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012189976) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 10 | 0 | — | — | [2h29m](https://github.com/iree-org/iree/actions/runs/34209521784/job/102010506049) | [3h02m](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012190063) | [3h02m](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012190063) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [54m10s](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076972) | [2h56m](https://github.com/iree-org/iree/actions/runs/34209501648/job/102009899259) | [2h56m](https://github.com/iree-org/iree/actions/runs/34209501648/job/102009899259) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [35m47s](https://github.com/iree-org/iree/actions/runs/34215592216/job/102046199228) | [2h53m](https://github.com/iree-org/iree/actions/runs/34209521784/job/102010506138) | [2h53m](https://github.com/iree-org/iree/actions/runs/34209521784/job/102010506138) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 10 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076911) | 2026-09-08 04:24 PDT | [1h13m](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012190196) | [2h34m](https://github.com/iree-org/iree/actions/runs/34209521784/job/102010506057) | [2h34m](https://github.com/iree-org/iree/actions/runs/34209521784/job/102010506057) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 0 | — | — | [1h18m](https://github.com/iree-org/iree/actions/runs/34209501648/job/102009899355) | [2h30m](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012190337) | [2h30m](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012190337) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076982) | 2026-09-08 04:24 PDT | [1h22m](https://github.com/iree-org/iree/actions/runs/34209530445/job/102014447266) | [2h00m](https://github.com/iree-org/iree/actions/runs/34209501648/job/102009899347) | [2h00m](https://github.com/iree-org/iree/actions/runs/34209501648/job/102009899347) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 10 | 0 | — | — | [16m48s](https://github.com/iree-org/iree/actions/runs/34209516346/job/102010306920) | [1h39m](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012190008) | [1h39m](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012190008) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 0 | — | — | [33m50s](https://github.com/iree-org/iree/actions/runs/34209530445/job/102014447283) | [1h35m](https://github.com/iree-org/iree/actions/runs/34209521784/job/102010506117) | [1h35m](https://github.com/iree-org/iree/actions/runs/34209521784/job/102010506117) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [36m45s](https://github.com/iree-org/iree/actions/runs/34209538099/job/102012190532) | [1h33m](https://github.com/iree-org/iree/actions/runs/34209516346/job/102010306794) | [1h33m](https://github.com/iree-org/iree/actions/runs/34209516346/job/102010306794) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [19m35s](https://github.com/iree-org/iree/actions/runs/34209508728/job/102009793829) | [1h10m](https://github.com/iree-org/iree/actions/runs/34209530445/job/102014447486) | [1h10m](https://github.com/iree-org/iree/actions/runs/34209530445/job/102014447486) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 11 | 0 | — | — | [3m51s](https://github.com/iree-org/iree/actions/runs/34209501565/job/102006922200) | [38m46s](https://github.com/iree-org/iree/actions/runs/34209516499/job/102008423870) | [38m46s](https://github.com/iree-org/iree/actions/runs/34209516499/job/102008423870) | 11 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 11 | 0 | — | — | [4m45s](https://github.com/iree-org/iree/actions/runs/34209508778/job/102006940155) | [37m53s](https://github.com/iree-org/iree/actions/runs/34209521831/job/102009118758) | [37m53s](https://github.com/iree-org/iree/actions/runs/34209521831/job/102009118758) | 11 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 11 | 0 | — | — | [5m15s](https://github.com/iree-org/iree/actions/runs/34209501565/job/102006922150) | [37m17s](https://github.com/iree-org/iree/actions/runs/34209508778/job/102006940026) | [37m17s](https://github.com/iree-org/iree/actions/runs/34209508778/job/102006940026) | 11 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 11 | 0 | — | — | [44s](https://github.com/iree-org/iree/actions/runs/34209530517/job/102008924995) | [36m15s](https://github.com/iree-org/iree/actions/runs/34209521831/job/102009118362) | [36m15s](https://github.com/iree-org/iree/actions/runs/34209521831/job/102009118362) | 11 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 11 | 0 | — | — | [9m44s](https://github.com/iree-org/iree/actions/runs/34209501565/job/102006922110) | [35m51s](https://github.com/iree-org/iree/actions/runs/34209530517/job/102008924978) | [35m51s](https://github.com/iree-org/iree/actions/runs/34209530517/job/102008924978) | 11 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 160 | 1% (2/160) |  | 57m42s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 106 | 0% (0/106) |  | 1h00m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 130 | 5% (6/130) |  | 1h04m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 123 | 1% (1/123) |  | 1h06m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h35m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h53m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 3h43m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 4h08m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h39m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 3h11m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 3h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 3h25m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h00m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h34m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h29m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
