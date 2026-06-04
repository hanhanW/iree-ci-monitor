# iree-ci-monitor

_Updated: 2026-06-04 12:07 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [1h55m](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448591) | [2h14m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429892) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [1h09m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536430012) | [2h13m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429798) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [44m53s](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429723) | [2h06m](https://github.com/iree-org/iree/actions/runs/26956265070/job/79537033932) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | [1h36m](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448243) | [2h06m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429720) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 0 | — | — | 0 | [51m35s](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448251) | [2h03m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429709) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 0 | — | — | 0 | [1h18m](https://github.com/iree-org/iree/actions/runs/26956282545/job/79537902662) | [2h02m](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537447935) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [1h03m](https://github.com/iree-org/iree/actions/runs/26956282545/job/79537902634) | [1h42m](https://github.com/iree-org/iree/actions/runs/26956265070/job/79537034026) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [40m00s](https://github.com/iree-org/iree/actions/runs/26956203301/job/79535830771) | [1h34m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429752) | — | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [1h05m](https://github.com/iree-org/iree/actions/runs/26956265070/job/79537034118) | [1h30m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429695) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [57m32s](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448075) | [1h14m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429924) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [42m14s](https://github.com/iree-org/iree/actions/runs/26956282545/job/79537902580) | [1h05m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429829) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 6 | 0 | — | — | 0 | [13m07s](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448320) | [46m24s](https://github.com/iree-org/iree/actions/runs/26956265070/job/79537034050) | — | `iree-mi308-1` |
| `ubuntu-24.04` | github-hosted | 134 | 0 | — | — | 0 | [6m11s](https://github.com/iree-org/iree/actions/runs/26956265070/job/79537033923) | [21m55s](https://github.com/iree-org/iree/actions/runs/26956284813/job/79535625198) | 0% (0/3) | 132 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 24 | 0 | — | — | 0 | [7m48s](https://github.com/iree-org/iree/actions/runs/26956282545/job/79537902523) | [18m27s](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448183) | — | 24 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [4m58s](https://github.com/iree-org/iree/actions/runs/26956282342/job/79534349102) | [9m51s](https://github.com/iree-org/iree/actions/runs/26956282342/job/79534349299) | — | 18 |
| `windows-2022` | github-hosted | 18 | 0 | — | — | 0 | [3m31s](https://github.com/iree-org/iree/actions/runs/26956265103/job/79536870322) | [7m15s](https://github.com/iree-org/iree/actions/runs/26956278990/job/79539095534) | — | 18 |
| `macos-14` | github-hosted | 19 | 0 | — | — | 0 | [40s](https://github.com/iree-org/iree/actions/runs/26956245614/job/79534206573) | [7m13s](https://github.com/iree-org/iree/actions/runs/26956282342/job/79534349491) | 0% (0/1) | 19 |
| `azure-linux-scale` | ossci | 32 | 0 | — | — | 0 | [45s](https://github.com/iree-org/iree/actions/runs/26956203814/job/79534018870) | [2m20s](https://github.com/iree-org/iree/actions/runs/26956282342/job/79534349203) | 0% (0/2) | 32 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26956265103/job/79536869817) | [1m49s](https://github.com/iree-org/iree/actions/runs/26956278990/job/79539095559) | — | 6 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m25s](https://github.com/iree-org/iree/actions/runs/26946175694/job/79499591877) | [1m25s](https://github.com/iree-org/iree/actions/runs/26946175694/job/79499591877) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26956265070/job/79537033890) | [4s](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537447850) | — | 6 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26960409479/job/79548905661) | [3s](https://github.com/iree-org/iree/actions/runs/26960409479/job/79548905759) | — | 9 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26946159967/job/79499538990) | [2s](https://github.com/iree-org/iree/actions/runs/26946159967/job/79499538990) | 100% (1/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [1h09m](https://github.com/iree-org/iree/actions/runs/26956203301/job/79535830770) | [2h15m](https://github.com/iree-org/iree/actions/runs/26956282545/job/79537902607) | [2h15m](https://github.com/iree-org/iree/actions/runs/26956282545/job/79537902607) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [1h55m](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448591) | [2h14m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429892) | [2h14m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429892) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [52m18s](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448166) | [2h13m](https://github.com/iree-org/iree/actions/runs/26956265070/job/79537034164) | [2h13m](https://github.com/iree-org/iree/actions/runs/26956265070/job/79537034164) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [44m53s](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429723) | [2h06m](https://github.com/iree-org/iree/actions/runs/26956265070/job/79537033932) | [2h06m](https://github.com/iree-org/iree/actions/runs/26956265070/job/79537033932) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 0 | — | — | [1h36m](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448243) | [2h06m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429720) | [2h06m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429720) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 6 | 0 | — | — | [51m35s](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448251) | [2h03m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429709) | [2h03m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429709) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 6 | 0 | — | — | [1h18m](https://github.com/iree-org/iree/actions/runs/26956282545/job/79537902662) | [2h02m](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537447935) | [2h02m](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537447935) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [1h17m](https://github.com/iree-org/iree/actions/runs/26956245057/job/79536196792) | [1h52m](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448214) | [1h52m](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448214) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [40m00s](https://github.com/iree-org/iree/actions/runs/26956203301/job/79535830771) | [1h48m](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448195) | [1h48m](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448195) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [13m26s](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448199) | [1h34m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429752) | [1h34m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429752) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 6 | 0 | — | — | [1h05m](https://github.com/iree-org/iree/actions/runs/26956265070/job/79537034118) | [1h30m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429695) | [1h30m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429695) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [44m30s](https://github.com/iree-org/iree/actions/runs/26956245057/job/79536196811) | [1h18m](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448220) | [1h18m](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448220) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [28m27s](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429721) | [1h17m](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448212) | [1h17m](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448212) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [54m03s](https://github.com/iree-org/iree/actions/runs/26956245057/job/79536196749) | [1h14m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429924) | [1h14m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429924) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [42m14s](https://github.com/iree-org/iree/actions/runs/26956282545/job/79537902580) | [1h05m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429829) | [1h05m](https://github.com/iree-org/iree/actions/runs/26956274441/job/79536429829) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 6 | 0 | — | — | [13m07s](https://github.com/iree-org/iree/actions/runs/26956279028/job/79537448320) | [46m24s](https://github.com/iree-org/iree/actions/runs/26956265070/job/79537034050) | [46m24s](https://github.com/iree-org/iree/actions/runs/26956265070/job/79537034050) | 1 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 7 | 0 | — | — | [8m34s](https://github.com/iree-org/iree/actions/runs/26956273150/job/79534348687) | [32m18s](https://github.com/iree-org/iree/actions/runs/26956282342/job/79534349161) | [32m18s](https://github.com/iree-org/iree/actions/runs/26956282342/job/79534349161) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 6 | 0 | — | — | [11m08s](https://github.com/iree-org/iree/actions/runs/26956245614/job/79534206661) | [32m14s](https://github.com/iree-org/iree/actions/runs/26956282342/job/79534349290) | [32m14s](https://github.com/iree-org/iree/actions/runs/26956282342/job/79534349290) | 6 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 6 | 0 | — | — | [10m27s](https://github.com/iree-org/iree/actions/runs/26956245614/job/79534206608) | [26m56s](https://github.com/iree-org/iree/actions/runs/26956273150/job/79534348766) | [26m56s](https://github.com/iree-org/iree/actions/runs/26956273150/job/79534348766) | 6 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 7 | 0 | — | — | [4m07s](https://github.com/iree-org/iree/actions/runs/26956282342/job/79534349025) | [24m42s](https://github.com/iree-org/iree/actions/runs/26956273150/job/79534348788) | [24m42s](https://github.com/iree-org/iree/actions/runs/26956273150/job/79534348788) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 297 | 4% (12/296) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 327 | 1% (2/327) |  | 2h36m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 228 | 1% (2/228) |  | 2h52m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 233 | 0% (0/233) |  | 3h01m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 74 | 1% (1/74) |  | 4h01m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h05m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h14m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h14m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h13m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h30m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h03m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h42m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h02m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h34m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
