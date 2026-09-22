# iree-ci-monitor

_Updated: 2026-09-22 14:23 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 10 | 0 | — | — | 0 | [1h04m](https://github.com/iree-org/iree/actions/runs/35736869090/job/106779440775) | [2h00m](https://github.com/iree-org/iree/actions/runs/35735357842/job/106774904553) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 10 | 0 | — | — | 0 | [49m02s](https://github.com/iree-org/iree/actions/runs/35735357842/job/106774903102) | [1h48m](https://github.com/iree-org/iree/actions/runs/35735357842/job/106774904360) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [36m16s](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202189) | [1h32m](https://github.com/iree-org/iree/actions/runs/35736869090/job/106779440558) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [42m52s](https://github.com/iree-org/iree/actions/runs/35736869090/job/106779440545) | [1h31m](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202608) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 10 | 0 | — | — | 0 | [44m48s](https://github.com/iree-org/iree/actions/runs/35738551719/job/106798882126) | [1h30m](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202338) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 10 | 0 | — | — | 0 | [21m42s](https://github.com/iree-org/iree/actions/runs/35692625135/job/106729985552) | [1h17m](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202936) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 5 | 0 | — | — | 0 | [8m59s](https://github.com/iree-org/iree/actions/runs/35735357842/job/106774901802) | [54m59s](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775201821) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [30m37s](https://github.com/iree-org/iree/actions/runs/35692625135/job/106729985212) | [52m36s](https://github.com/iree-org/iree/actions/runs/35738551719/job/106798882361) | 0% (0/1) | `shark75-ci` |
| `windows-2022` | github-hosted | 15 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/35738551748/job/106795916033) | [2m24s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204678) | 0% (0/3) | 15 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/35735358112/job/106771170154) | [1m41s](https://github.com/iree-org/iree/actions/runs/35736869082/job/106776352679) | 0% (0/3) | 15 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/35735358112/job/106771170076) | [1m38s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204531) | 0% (0/3) | 15 |
| `ubuntu-24.04` | github-hosted | 107 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775201955) | [1m24s](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202089) | 0% (0/21) | 106 |
| `azure-linux-scale` | ossci | 26 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/35735358112/job/106771170588) | [1m19s](https://github.com/iree-org/iree/actions/runs/35738551748/job/106795916437) | 0% (0/6) | 26 |
| `azure-windows-scale` | ossci | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35738551748/job/106795916310) | [6s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204652) | 0% (0/1) | 5 |
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35738467411/job/106781696238) | [3s](https://github.com/iree-org/iree/actions/runs/35738467456/job/106781696582) | 0% (0/3) | 18 |
| `Linux,X64,iree-w7900` | self-hosted | 5 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 5 | 0 | — | — | [1h04m](https://github.com/iree-org/iree/actions/runs/35736869090/job/106779440775) | [2h00m](https://github.com/iree-org/iree/actions/runs/35735357842/job/106774904553) | [2h00m](https://github.com/iree-org/iree/actions/runs/35735357842/job/106774904553) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [54m44s](https://github.com/iree-org/iree/actions/runs/35738551719/job/106798882115) | [1h48m](https://github.com/iree-org/iree/actions/runs/35735357842/job/106774904360) | [1h48m](https://github.com/iree-org/iree/actions/runs/35735357842/job/106774904360) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 5 | 0 | — | — | [1h34m](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202836) | [1h45m](https://github.com/iree-org/iree/actions/runs/35735357842/job/106774903200) | [1h45m](https://github.com/iree-org/iree/actions/runs/35735357842/job/106774903200) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 5 | 0 | — | — | [36m16s](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202189) | [1h32m](https://github.com/iree-org/iree/actions/runs/35736869090/job/106779440558) | [1h32m](https://github.com/iree-org/iree/actions/runs/35736869090/job/106779440558) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 5 | 0 | — | — | [42m52s](https://github.com/iree-org/iree/actions/runs/35736869090/job/106779440545) | [1h31m](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202608) | [1h31m](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202608) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [44m48s](https://github.com/iree-org/iree/actions/runs/35738551719/job/106798882126) | [1h30m](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202338) | [1h30m](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202338) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [50m24s](https://github.com/iree-org/iree/actions/runs/35735357842/job/106774903135) | [1h26m](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202782) | [1h26m](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202782) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [8m14s](https://github.com/iree-org/iree/actions/runs/35738551719/job/106798882009) | [1h17m](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202936) | [1h17m](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202936) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [35m29s](https://github.com/iree-org/iree/actions/runs/35692625135/job/106729985277) | [1h11m](https://github.com/iree-org/iree/actions/runs/35736869090/job/106779440517) | [1h11m](https://github.com/iree-org/iree/actions/runs/35736869090/job/106779440517) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [49m02s](https://github.com/iree-org/iree/actions/runs/35735357842/job/106774903102) | [1h09m](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202716) | [1h09m](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775202716) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 5 | 0 | — | — | [8m59s](https://github.com/iree-org/iree/actions/runs/35735357842/job/106774901802) | [54m59s](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775201821) | [54m59s](https://github.com/iree-org/iree/actions/runs/35735366913/job/106775201821) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 5 | 0 | — | — | [30m37s](https://github.com/iree-org/iree/actions/runs/35692625135/job/106729985212) | [52m36s](https://github.com/iree-org/iree/actions/runs/35738551719/job/106798882361) | [52m36s](https://github.com/iree-org/iree/actions/runs/35738551719/job/106798882361) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 5 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/35738551748/job/106795915875) | [2m40s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204675) | [2m40s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204675) | 5 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 5 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/35735358112/job/106771170116) | [2m37s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204588) | [2m37s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204588) | 5 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 5 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/35735358112/job/106771170221) | [2m29s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204661) | [2m29s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204661) | 5 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 5 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/35738551748/job/106795916033) | [2m24s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204678) | [2m24s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204678) | 5 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 5 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/35738551748/job/106795915522) | [2m07s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204567) | [2m07s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204567) | 5 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 5 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/35735358112/job/106771169911) | [1m59s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204639) | [1m59s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204639) | 5 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 5 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/35738551748/job/106795915816) | [1m57s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204599) | [1m57s](https://github.com/iree-org/iree/actions/runs/35735367024/job/106771204599) | 5 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 5 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/35735358112/job/106771170154) | [1m41s](https://github.com/iree-org/iree/actions/runs/35736869082/job/106776352679) | [1m41s](https://github.com/iree-org/iree/actions/runs/35736869082/job/106776352679) | 5 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 368 | 1% (4/368) |  | 5h20m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 382 | 1% (4/382) |  | 5h35m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 214 | 1% (3/214) |  | 5d00h ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h48m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h30m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache` p95 queue 1h31m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h00m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h17m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-w7900` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
