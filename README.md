# iree-ci-monitor

_Updated: 2026-06-09 18:23 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [6h29m](https://github.com/iree-org/iree/actions/runs/27226683635/job/80398435144) | [7h51m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691582) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 16 | 0 | — | — | 0 | [48m19s](https://github.com/iree-org/iree/actions/runs/27220711929/job/80376331016) | [6h55m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691565) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 8 | 0 | — | — | 0 | [38m35s](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691383) | [5h07m](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471272) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [1h30m](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471485) | [3h49m](https://github.com/iree-org/iree/actions/runs/27212736254/job/80375312214) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 8 | 0 | — | — | 0 | [1h09m](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471665) | [3h37m](https://github.com/iree-org/iree/actions/runs/27212736254/job/80375312392) | 0% (0/2) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 8 | 0 | — | — | 0 | [44m14s](https://github.com/iree-org/iree/actions/runs/27212736254/job/80375312350) | [3h12m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691589) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [48m50s](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471535) | [2h03m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691551) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 16 | 0 | — | — | 0 | [37m20s](https://github.com/iree-org/iree/actions/runs/27220711929/job/80376330884) | [1h45m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691643) | 0% (0/4) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 16 | 0 | — | — | 0 | [40m17s](https://github.com/iree-org/iree/actions/runs/27212736254/job/80375312498) | [1h33m](https://github.com/iree-org/iree/actions/runs/27220711929/job/80376330942) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 8 | 0 | — | — | 0 | [3m28s](https://github.com/iree-org/iree/actions/runs/27220711929/job/80376330668) | [1h06m](https://github.com/iree-org/iree/actions/runs/27226683635/job/80398435065) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 16 | 0 | — | — | 0 | [17m11s](https://github.com/iree-org/iree/actions/runs/27226683635/job/80398435105) | [36m34s](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691537) | 0% (0/4) | `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 32 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/27226683635/job/80398435221) | [19m39s](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691642) | 0% (0/8) | 32 |
| `azure-linux-scale` | ossci | 39 | 0 | — | — | 0 | [25s](https://github.com/iree-org/iree/actions/runs/27220864257/job/80375037898) | [14m26s](https://github.com/iree-org/iree/actions/runs/27226765079/job/80396006617) | 0% (0/12) | 39 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 8 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27217948090/job/80366246012) | [11m50s](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691556) | 0% (0/2) | `iree-mi308-1` |
| `ubuntu-24.04` | github-hosted | 148 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471412) | [2m05s](https://github.com/iree-org/iree/actions/runs/27220863694/job/80375037146) | 0% (0/36) | 148 |
| `windows-2022` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27220863694/job/80375036801) | [1m34s](https://github.com/iree-org/iree/actions/runs/27226765079/job/80396006667) | 0% (0/6) | 21 |
| `macos-14` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27220711868/job/80374520637) | [1m10s](https://github.com/iree-org/iree/actions/runs/27220711868/job/80374520689) | 0% (0/6) | 21 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/27212736143/job/80373818808) | [48s](https://github.com/iree-org/iree/actions/runs/27220711868/job/80374520587) | 0% (0/6) | 21 |
| `azure-windows-scale` | ossci | 7 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27226684424/job/80395672855) | [29s](https://github.com/iree-org/iree/actions/runs/27219158289/job/80370202260) | 0% (0/2) | 7 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27220708109/job/80374493528) | [9s](https://github.com/iree-org/iree/actions/runs/27220860406/job/80375009856) | 0% (0/6) | 9 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691470) | [2s](https://github.com/iree-org/iree/actions/runs/27226683635/job/80398435003) | 50% (1/2) | 8 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [31m28s](https://github.com/iree-org/iree/actions/runs/27220711929/job/80376330854) | [7h58m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691640) | [7h58m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691640) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 8 | 0 | — | — | [6h29m](https://github.com/iree-org/iree/actions/runs/27226683635/job/80398435144) | [7h51m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691582) | [7h51m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691582) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [50m53s](https://github.com/iree-org/iree/actions/runs/27219157774/job/80370491948) | [6h55m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691565) | [6h55m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691565) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 8 | 0 | — | — | [38m35s](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691383) | [5h07m](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471272) | [5h07m](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471272) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 8 | 0 | — | — | [1h30m](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471485) | [3h49m](https://github.com/iree-org/iree/actions/runs/27212736254/job/80375312214) | [3h49m](https://github.com/iree-org/iree/actions/runs/27212736254/job/80375312214) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 8 | 0 | — | — | [1h09m](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471665) | [3h37m](https://github.com/iree-org/iree/actions/runs/27212736254/job/80375312392) | [3h37m](https://github.com/iree-org/iree/actions/runs/27212736254/job/80375312392) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 8 | 0 | — | — | [44m14s](https://github.com/iree-org/iree/actions/runs/27212736254/job/80375312350) | [3h12m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691589) | [3h12m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691589) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 8 | 0 | — | — | [48m50s](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471535) | [2h03m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691551) | [2h03m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691551) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [48m28s](https://github.com/iree-org/iree/actions/runs/27212736254/job/80375312509) | [2h03m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691619) | [2h03m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691619) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [37m20s](https://github.com/iree-org/iree/actions/runs/27220711929/job/80376330884) | [1h45m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691643) | [1h45m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691643) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 8 | 0 | — | — | [55m13s](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471492) | [1h37m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691727) | [1h37m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691727) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 8 | 0 | — | — | [29m51s](https://github.com/iree-org/iree/actions/runs/27220711929/job/80376331079) | [1h06m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691519) | [1h06m](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691519) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 8 | 0 | — | — | [3m28s](https://github.com/iree-org/iree/actions/runs/27220711929/job/80376330668) | [1h06m](https://github.com/iree-org/iree/actions/runs/27226683635/job/80398435065) | [1h06m](https://github.com/iree-org/iree/actions/runs/27226683635/job/80398435065) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [25m53s](https://github.com/iree-org/iree/actions/runs/27220711929/job/80376330875) | [39m00s](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471290) | [39m00s](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471290) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [17m11s](https://github.com/iree-org/iree/actions/runs/27226683635/job/80398435105) | [36m34s](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691537) | [36m34s](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691537) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 8 | 0 | — | — | [12m14s](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471575) | [21m51s](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691507) | [21m51s](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691507) | 8 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 8 | 0 | — | — | [9m41s](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471349) | [19m39s](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691642) | [19m39s](https://github.com/iree-org/iree/actions/runs/27220864257/job/80376691642) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 7 | 0 | — | — | [25s](https://github.com/iree-org/iree/actions/runs/27220863694/job/80375037150) | [19m35s](https://github.com/iree-org/iree/actions/runs/27226765079/job/80396006904) | [19m35s](https://github.com/iree-org/iree/actions/runs/27226765079/job/80396006904) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 7 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/27220711868/job/80374520716) | [19m27s](https://github.com/iree-org/iree/actions/runs/27226765079/job/80396007109) | [19m27s](https://github.com/iree-org/iree/actions/runs/27226765079/job/80396007109) | 7 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 8 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27217948090/job/80366246006) | [15m26s](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471479) | [15m26s](https://github.com/iree-org/iree/actions/runs/27226765068/job/80398471479) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 315 | 3% (8/315) |  | 16m58s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 238 | 2% (4/238) |  | 2h47m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 272 | 7% (19/272) |  | 4h47m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 238 | 2% (5/238) |  | 5h29m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 74 | 1% (1/74) |  | 6h28m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h03m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h45m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 7h51m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 6h55m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 5h07m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 3h49m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 3h37m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h33m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 3h12m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
