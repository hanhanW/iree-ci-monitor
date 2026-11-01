# iree-ci-monitor

_Updated: 2026-11-01 05:35 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [1h28m](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262778) | [2h12m](https://github.com/iree-org/iree/actions/runs/41283061346/job/124780357135) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [1h00m](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196941) | [2h07m](https://github.com/iree-org/iree/actions/runs/41283061346/job/124780357169) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [47m39s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196800) | [2h06m](https://github.com/iree-org/iree/actions/runs/41283061346/job/124780357171) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [33m38s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196935) | [2h02m](https://github.com/iree-org/iree/actions/runs/41278083479/job/124765688158) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [1h27m](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262876) | [2h02m](https://github.com/iree-org/iree/actions/runs/41283061346/job/124780357185) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [11m40s](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262731) | [1h10m](https://github.com/iree-org/iree/actions/runs/41278083479/job/124765688102) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [33m21s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196972) | [49m59s](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262788) | — | `shark55-ci` |
| `ubuntu-24.04` | github-hosted | 106 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/41278083479/job/124765688089) | [4m28s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196834) | 0% (0/1) | 102 |
| `macos-15` | github-hosted | 17 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/41283061354/job/124778788683) | [3m09s](https://github.com/iree-org/iree/actions/runs/41276164000/job/124758684343) | — | 17 |
| `windows-2022` | github-hosted | 17 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/41278083478/job/124764789224) | [2m54s](https://github.com/iree-org/iree/actions/runs/41276164000/job/124758684286) | — | 17 |
| `azure-linux-scale` | ossci | 30 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/41283061354/job/124778788751) | [2m43s](https://github.com/iree-org/iree/actions/runs/41277566847/job/124762762733) | — | 30 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/41278083478/job/124764789197) | [1m32s](https://github.com/iree-org/iree/actions/runs/41277566847/job/124762762610) | — | 18 |
| `azure-windows-scale` | ossci | 5 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/41283061354/job/124778788859) | [44s](https://github.com/iree-org/iree/actions/runs/41276164000/job/124758684441) | — | 5 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/41311804331/job/124863563652) | [3s](https://github.com/iree-org/iree/actions/runs/41311804331/job/124863563644) | 0% (0/3) | 3 |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [1h28m](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262778) | [2h12m](https://github.com/iree-org/iree/actions/runs/41283061346/job/124780357135) | [2h12m](https://github.com/iree-org/iree/actions/runs/41283061346/job/124780357135) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [48m06s](https://github.com/iree-org/iree/actions/runs/41278083479/job/124765688216) | [2h07m](https://github.com/iree-org/iree/actions/runs/41283061346/job/124780357169) | [2h07m](https://github.com/iree-org/iree/actions/runs/41283061346/job/124780357169) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [59m21s](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262774) | [2h06m](https://github.com/iree-org/iree/actions/runs/41283061346/job/124780357171) | [2h06m](https://github.com/iree-org/iree/actions/runs/41283061346/job/124780357171) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [11m52s](https://github.com/iree-org/iree/actions/runs/41283061346/job/124780357153) | [2h02m](https://github.com/iree-org/iree/actions/runs/41278083479/job/124765688158) | [2h02m](https://github.com/iree-org/iree/actions/runs/41278083479/job/124765688158) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [1h49m](https://github.com/iree-org/iree/actions/runs/41278083479/job/124765688164) | [2h02m](https://github.com/iree-org/iree/actions/runs/41283061346/job/124780357185) | [2h02m](https://github.com/iree-org/iree/actions/runs/41283061346/job/124780357185) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [1h13m](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262860) | [1h59m](https://github.com/iree-org/iree/actions/runs/41278083479/job/124765688188) | [1h59m](https://github.com/iree-org/iree/actions/runs/41278083479/job/124765688188) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [47m39s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196800) | [1h56m](https://github.com/iree-org/iree/actions/runs/41283061346/job/124780357081) | [1h56m](https://github.com/iree-org/iree/actions/runs/41283061346/job/124780357081) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [30m09s](https://github.com/iree-org/iree/actions/runs/41278083479/job/124765688159) | [1h32m](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262807) | [1h32m](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262807) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [34m49s](https://github.com/iree-org/iree/actions/runs/41283061346/job/124780357066) | [1h11m](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262939) | [1h11m](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262939) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [11m40s](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262731) | [1h10m](https://github.com/iree-org/iree/actions/runs/41278083479/job/124765688102) | [1h10m](https://github.com/iree-org/iree/actions/runs/41278083479/job/124765688102) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [33m21s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196972) | [49m59s](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262788) | [49m59s](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262788) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 4 | 0 | — | — | [2m14s](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262825) | [5m52s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196978) | [5m52s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196978) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 4 | 0 | — | — | [2m20s](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262846) | [5m32s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196859) | [5m32s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196859) | 4 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 4 | 0 | — | — | [3m14s](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262755) | [5m02s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196945) | [5m02s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196945) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41278083478/job/124764789243) | [4m53s](https://github.com/iree-org/iree/actions/runs/41276164000/job/124758684327) | [4m53s](https://github.com/iree-org/iree/actions/runs/41276164000/job/124758684327) | 5 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 4 | 0 | — | — | [3m21s](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262779) | [4m49s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196782) | [4m49s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196782) | 4 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 4 | 0 | — | — | [1m01s](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262781) | [4m28s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196834) | [4m28s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196834) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 5 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/41278083478/job/124764789242) | [4m09s](https://github.com/iree-org/iree/actions/runs/41276164000/job/124758684345) | [4m09s](https://github.com/iree-org/iree/actions/runs/41276164000/job/124758684345) | 5 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 4 | 0 | — | — | [20s](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262763) | [4m05s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196739) | [4m05s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196739) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 4 | 0 | — | — | [2m34s](https://github.com/iree-org/iree/actions/runs/41276164200/job/124760262851) | [3m59s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196925) | [3m59s](https://github.com/iree-org/iree/actions/runs/41275818547/job/124759196925) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 238 | 3% (7/238) |  | 4h08m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 282 | 3% (8/282) |  | 4h09m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h07m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h12m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h10m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h02m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h06m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
