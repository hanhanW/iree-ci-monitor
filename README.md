# iree-ci-monitor

_Updated: 2026-09-17 21:52 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [1h59m](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342033229) | [2h35m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360868) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [1h28m](https://github.com/iree-org/iree/actions/runs/35259670726/job/105339834969) | [2h19m](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342032886) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [53m10s](https://github.com/iree-org/iree/actions/runs/35259694388/job/105344024436) | [2h19m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360862) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | [1h18m](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964723) | [2h15m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360649) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [37m56s](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360638) | [1h51m](https://github.com/iree-org/iree/actions/runs/35259670726/job/105339834755) | 0% (0/1) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [1h13m](https://github.com/iree-org/iree/actions/runs/35259670726/job/105339834801) | [1h42m](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964412) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [1h19m](https://github.com/iree-org/iree/actions/runs/35259694388/job/105344024427) | [1h36m](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342033221) | 0% (0/2) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [1h03m](https://github.com/iree-org/iree/actions/runs/35259694388/job/105344024592) | [1h26m](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458687) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `ubuntu-24.04` | github-hosted | 69 | 0 | — | — | 0 | [1m08s](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360908) | [3m30s](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342032615) | 0% (0/14) | 69 |
| `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/35259691182/job/105339288231) | [1s](https://github.com/iree-org/iree/actions/runs/35259691182/job/105339288231) | — | 1 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 14 | 14 | [21h24m](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602166) | 2026-09-17 21:51 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [21h24m](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602166) | 2026-09-17 21:51 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/egebeysel/scalable-dist-1-vscale-range-target-field` | pull_request |
| [12h40m](https://github.com/iree-org/iree/actions/runs/35244084342/job/105282772106) | 2026-09-17 21:51 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [12h39m](https://github.com/iree-org/iree/actions/runs/35244090870/job/105282957801) | 2026-09-17 21:51 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/egebeysel/scalable-dist-3-unpack-distribution-hints` | pull_request |
| [12h37m](https://github.com/iree-org/iree/actions/runs/35244089937/job/105283906279) | 2026-09-17 21:51 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/egebeysel/scalable-dist-2-distribution-tile-sizes` | pull_request |
| [12h32m](https://github.com/iree-org/iree/actions/runs/35244090100/job/105285600898) | 2026-09-17 21:51 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/egebeysel/scalable-dist-5-distribution-tiling-tests` | pull_request |
| [12h08m](https://github.com/iree-org/iree/actions/runs/35245416206/job/105294110239) | 2026-09-17 21:51 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `integrates/llvm-20260916` | pull_request |
| [10h51m](https://github.com/iree-org/iree/actions/runs/35251598607/job/105320096896) | 2026-09-17 21:51 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `add-fma-math-vm-lowringg` | pull_request |
| [10h06m](https://github.com/iree-org/iree/actions/runs/35257416856/job/105335534767) | 2026-09-17 21:51 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [9h54m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360642) | 2026-09-17 21:51 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [9h53m](https://github.com/iree-org/iree/actions/runs/35259670726/job/105339834679) | 2026-09-17 21:51 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_canonicalize_dynamism` | pull_request |
| [9h51m](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458710) | 2026-09-17 21:51 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_dynamic_gather_broadcast` | pull_request |
| [9h47m](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964508) | 2026-09-17 21:51 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_lower_bounds` | pull_request |
| [9h47m](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342032894) | 2026-09-17 21:51 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_dynamic_pad_conv` | pull_request |
| [9h41m](https://github.com/iree-org/iree/actions/runs/35259694388/job/105344024519) | 2026-09-17 21:51 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_dynamic_reduce_window_scatter` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 14 | 14 | [21h24m](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602166) | 2026-09-17 21:51 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [1h35m](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458959) | [2h38m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360869) | [2h38m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360869) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [1h59m](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342033229) | [2h35m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360868) | [2h35m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360868) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [1h28m](https://github.com/iree-org/iree/actions/runs/35259670726/job/105339834969) | [2h19m](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342032886) | [2h19m](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342032886) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [53m10s](https://github.com/iree-org/iree/actions/runs/35259694388/job/105344024436) | [2h19m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360862) | [2h19m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360862) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 0 | — | — | [1h18m](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964723) | [2h15m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360649) | [2h15m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360649) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [37m56s](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360638) | [1h51m](https://github.com/iree-org/iree/actions/runs/35259670726/job/105339834755) | [1h51m](https://github.com/iree-org/iree/actions/runs/35259670726/job/105339834755) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [1h15m](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964563) | [1h47m](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458734) | [1h47m](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458734) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [52m40s](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360838) | [1h47m](https://github.com/iree-org/iree/actions/runs/35259694388/job/105344024793) | [1h47m](https://github.com/iree-org/iree/actions/runs/35259694388/job/105344024793) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [1h06m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360844) | [1h42m](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964412) | [1h42m](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964412) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [57m26s](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360632) | [1h39m](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964640) | [1h39m](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964640) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [1h19m](https://github.com/iree-org/iree/actions/runs/35259694388/job/105344024427) | [1h36m](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342033221) | [1h36m](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342033221) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [1h01m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360706) | [1h26m](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458687) | [1h26m](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458687) | 2 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 6 | 0 | — | — | [2m03s](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458733) | [3m53s](https://github.com/iree-org/iree/actions/runs/35259670726/job/105339834865) | [3m53s](https://github.com/iree-org/iree/actions/runs/35259670726/job/105339834865) | 6 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 6 | 0 | — | — | [53s](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964450) | [3m48s](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342033414) | [3m48s](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342033414) | 6 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 6 | 0 | — | — | [1m18s](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964540) | [3m46s](https://github.com/iree-org/iree/actions/runs/35259670726/job/105339834872) | [3m46s](https://github.com/iree-org/iree/actions/runs/35259670726/job/105339834872) | 6 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 6 | 0 | — | — | [1m37s](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458417) | [3m30s](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342032615) | [3m30s](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342032615) | 6 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 6 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458372) | [3m07s](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360521) | [3m07s](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360521) | 6 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 6 | 0 | — | — | [1m13s](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360776) | [3m00s](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458702) | [3m00s](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458702) | 6 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 6 | 0 | — | — | [1m07s](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964530) | [2m55s](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342033534) | [2m55s](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342033534) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 395 | 1% (4/395) |  | 7h00m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 310 | 2% (5/310) |  | 7h34m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 320 | 1% (2/320) |  | 7h52m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 118 | 8% (9/118) |  | 3d13h ago |

## Alerts

- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 21h24m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h51m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h26m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h35m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h15m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h42m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h36m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
