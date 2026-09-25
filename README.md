# iree-ci-monitor

_Updated: 2026-09-24 22:02 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [44m35s](https://github.com/iree-org/iree/actions/runs/36056908901/job/107829897800) | [1h38m](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830561104) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [1h05m](https://github.com/iree-org/iree/actions/runs/36056908901/job/107829897659) | [1h27m](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830561268) | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [1m22s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171752) | [1h07m](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830560864) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [34m40s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171699) | [1h05m](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171812) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [56m36s](https://github.com/iree-org/iree/actions/runs/36056908901/job/107829897823) | [1h01m](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171276) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [31m54s](https://github.com/iree-org/iree/actions/runs/36056908901/job/107829897601) | [59m16s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171528) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [4m04s](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830561164) | [52m58s](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830560880) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [27m15s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171667) | [48m48s](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830560769) | — | `shark55-ci` |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 0 | [42s](https://github.com/iree-org/iree/actions/runs/36057081794/job/107827088096) | [4m20s](https://github.com/iree-org/iree/actions/runs/36057079799/job/107827112171) | — | 9 |
| `ubuntu-24.04` | github-hosted | 81 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171588) | [3m21s](https://github.com/iree-org/iree/actions/runs/36057079799/job/107827112036) | 0% (0/3) | 75 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/36057081794/job/107827088145) | [3m06s](https://github.com/iree-org/iree/actions/runs/36057079799/job/107827112177) | — | 9 |
| `macos-14` | github-hosted | 9 | 0 | — | — | 0 | [1m22s](https://github.com/iree-org/iree/actions/runs/36057081794/job/107827088248) | [2m54s](https://github.com/iree-org/iree/actions/runs/36057079799/job/107827112228) | — | 9 |
| `azure-linux-scale` | ossci | 15 | 0 | — | — | 0 | [43s](https://github.com/iree-org/iree/actions/runs/36057081794/job/107827088535) | [1m25s](https://github.com/iree-org/iree/actions/runs/36056908901/job/107826186843) | — | 15 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/36057073652/job/107826635145) | [40s](https://github.com/iree-org/iree/actions/runs/36057076096/job/107826643742) | — | 12 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36057081794/job/107827088533) | [4s](https://github.com/iree-org/iree/actions/runs/36057079799/job/107827112521) | — | 3 |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [1h32m](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171641) | [1h38m](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830561104) | [1h38m](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830561104) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [39m31s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171732) | [1h27m](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830561268) | [1h27m](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830561268) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [1h12m](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171691) | [1h19m](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830560976) | [1h19m](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830560976) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [1m22s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171752) | [1h07m](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830560864) | [1h07m](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830560864) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [48m52s](https://github.com/iree-org/iree/actions/runs/36056908901/job/107829897915) | [1h05m](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171812) | [1h05m](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171812) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [34m46s](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830561242) | [1h02m](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171746) | [1h02m](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171746) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [56m36s](https://github.com/iree-org/iree/actions/runs/36056908901/job/107829897823) | [1h01m](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171276) | [1h01m](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171276) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [31m54s](https://github.com/iree-org/iree/actions/runs/36056908901/job/107829897601) | [59m16s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171528) | [59m16s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171528) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [52m56s](https://github.com/iree-org/iree/actions/runs/36056908901/job/107829897644) | [52m58s](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830560880) | [52m58s](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830560880) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 3 | 0 | — | — | [27m15s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171667) | [48m48s](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830560769) | [48m48s](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830560769) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [25m38s](https://github.com/iree-org/iree/actions/runs/36056908901/job/107829897781) | [34m40s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171699) | [34m40s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171699) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 3 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/36057081794/job/107827088131) | [4m22s](https://github.com/iree-org/iree/actions/runs/36057079799/job/107827112131) | [4m22s](https://github.com/iree-org/iree/actions/runs/36057079799/job/107827112131) | 3 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 3 | 0 | — | — | [2m57s](https://github.com/iree-org/iree/actions/runs/36057081794/job/107827088230) | [4m20s](https://github.com/iree-org/iree/actions/runs/36057079799/job/107827112171) | [4m20s](https://github.com/iree-org/iree/actions/runs/36057079799/job/107827112171) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [3m05s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171574) | [4m04s](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830561164) | [4m04s](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830561164) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 3 | 0 | — | — | [2m13s](https://github.com/iree-org/iree/actions/runs/36057081794/job/107827088295) | [3m55s](https://github.com/iree-org/iree/actions/runs/36057079799/job/107827112211) | [3m55s](https://github.com/iree-org/iree/actions/runs/36057079799/job/107827112211) | 3 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 3 | 0 | — | — | [2m58s](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830561291) | [3m53s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171475) | [3m53s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171475) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 3 | 0 | — | — | [1m12s](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830561211) | [3m33s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171642) | [3m33s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171642) | 3 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36057081794/job/107827087900) | [3m21s](https://github.com/iree-org/iree/actions/runs/36057079799/job/107827112036) | [3m21s](https://github.com/iree-org/iree/actions/runs/36057079799/job/107827112036) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 3 | 0 | — | — | [1m10s](https://github.com/iree-org/iree/actions/runs/36057081794/job/107827088233) | [3m17s](https://github.com/iree-org/iree/actions/runs/36057079799/job/107827112202) | [3m17s](https://github.com/iree-org/iree/actions/runs/36057079799/job/107827112202) | 3 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 3 | 0 | — | — | [30s](https://github.com/iree-org/iree/actions/runs/36057082290/job/107830171429) | [3m09s](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830561412) | [3m09s](https://github.com/iree-org/iree/actions/runs/36057079852/job/107830561412) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 357 | 1% (5/357) |  | 6h20m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 276 | 3% (9/276) |  | 6h54m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h07m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h05m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h38m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
