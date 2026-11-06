# iree-ci-monitor

_Updated: 2026-11-06 11:29 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 20 | 0 | — | — | 0 | [2h38m](https://github.com/iree-org/iree/actions/runs/42238352322/job/127967702603) | [4h17m](https://github.com/iree-org/iree/actions/runs/42228755353/job/127932579164) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 20 | 0 | — | — | 0 | [2h41m](https://github.com/iree-org/iree/actions/runs/42247473631/job/127999887003) | [4h14m](https://github.com/iree-org/iree/actions/runs/42228755353/job/127932579418) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 10 | 0 | — | — | 0 | [43m36s](https://github.com/iree-org/iree/actions/runs/42238352322/job/127967702161) | [3h45m](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933120650) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 20 | 0 | — | — | 0 | [36m34s](https://github.com/iree-org/iree/actions/runs/42247473631/job/127999886888) | [2h51m](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933120865) | 0% (0/4) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [23m32s](https://github.com/iree-org/iree/actions/runs/42255850691/job/128028009411) | [2h21m](https://github.com/iree-org/iree/actions/runs/42238352322/job/127967702476) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 20 | 0 | — | — | 0 | [1h09m](https://github.com/iree-org/iree/actions/runs/42228492320/job/127931311606) | [1h59m](https://github.com/iree-org/iree/actions/runs/42225761425/job/127921853219) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [37m59s](https://github.com/iree-org/iree/actions/runs/42228755353/job/127932578918) | [1h09m](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933120974) | 0% (0/2) | `shark55-ci` |
| `ubuntu-24.04` | github-hosted | 221 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/42247473334/job/127994752421) | [2m58s](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933120991) | 2% (1/40) | 215 |
| `ubuntu-24.04-arm` | github-hosted | 33 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/42232131681/job/127940491492) | [1m54s](https://github.com/iree-org/iree/actions/runs/42228492341/job/127928078469) | 0% (0/6) | 33 |
| `macos-15` | github-hosted | 33 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/42246330855/job/127989539052) | [1m52s](https://github.com/iree-org/iree/actions/runs/42228755228/job/127929145685) | 0% (0/6) | 33 |
| `windows-2022` | github-hosted | 33 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/42255851046/job/128022816073) | [1m41s](https://github.com/iree-org/iree/actions/runs/42228755228/job/127929145439) | 0% (0/6) | 33 |
| `azure-linux-scale` | ossci | 68 | 0 | — | — | 0 | [15s](https://github.com/iree-org/iree/actions/runs/42225761355/job/127918819452) | [1m41s](https://github.com/iree-org/iree/actions/runs/42221242830/job/127903624753) | 7% (1/14) | 68 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 3 | 0 | — | — | 0 | [1m32s](https://github.com/iree-org/iree/actions/runs/42232131681/job/127940492511) | [1m37s](https://github.com/iree-org/iree/actions/runs/42246330855/job/127989539200) | — | 3 |
| `azure-windows-scale` | ossci | 11 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/42232131681/job/127940492290) | [5s](https://github.com/iree-org/iree/actions/runs/42228755228/job/127929145972) | 0% (0/2) | 11 |
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/42238350850/job/127961808130) | [3s](https://github.com/iree-org/iree/actions/runs/42231423798/job/127938089463) | 0% (0/6) | 18 |
| `Linux,X64,iree-w7900` | self-hosted | 10 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 0 | — | — | [2h59m](https://github.com/iree-org/iree/actions/runs/42247473631/job/127999887014) | [4h39m](https://github.com/iree-org/iree/actions/runs/42221242830/job/127907187756) | [4h39m](https://github.com/iree-org/iree/actions/runs/42221242830/job/127907187756) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [3h03m](https://github.com/iree-org/iree/actions/runs/42225761425/job/127921853201) | [4h31m](https://github.com/iree-org/iree/actions/runs/42221242830/job/127907187629) | [4h31m](https://github.com/iree-org/iree/actions/runs/42221242830/job/127907187629) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 0 | — | — | [2h17m](https://github.com/iree-org/iree/actions/runs/42255850691/job/128028009447) | [4h06m](https://github.com/iree-org/iree/actions/runs/42228755353/job/127932579126) | [4h06m](https://github.com/iree-org/iree/actions/runs/42228755353/job/127932579126) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [1h09m](https://github.com/iree-org/iree/actions/runs/42228492320/job/127931311606) | [3h58m](https://github.com/iree-org/iree/actions/runs/42225761425/job/127921853321) | [3h58m](https://github.com/iree-org/iree/actions/runs/42225761425/job/127921853321) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 10 | 0 | — | — | [43m36s](https://github.com/iree-org/iree/actions/runs/42238352322/job/127967702161) | [3h45m](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933120650) | [3h45m](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933120650) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [2h22m](https://github.com/iree-org/iree/actions/runs/42247473631/job/127999886940) | [3h43m](https://github.com/iree-org/iree/actions/runs/42225761425/job/127921853269) | [3h43m](https://github.com/iree-org/iree/actions/runs/42225761425/job/127921853269) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [36m34s](https://github.com/iree-org/iree/actions/runs/42247473631/job/127999886888) | [2h53m](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933120909) | [2h53m](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933120909) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [44m41s](https://github.com/iree-org/iree/actions/runs/42238352322/job/127967702441) | [2h51m](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933120865) | [2h51m](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933120865) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 10 | 0 | — | — | [23m32s](https://github.com/iree-org/iree/actions/runs/42255850691/job/128028009411) | [2h21m](https://github.com/iree-org/iree/actions/runs/42238352322/job/127967702476) | [2h21m](https://github.com/iree-org/iree/actions/runs/42238352322/job/127967702476) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [1h15m](https://github.com/iree-org/iree/actions/runs/42238352322/job/127967702501) | [1h59m](https://github.com/iree-org/iree/actions/runs/42225761425/job/127921853219) | [1h59m](https://github.com/iree-org/iree/actions/runs/42225761425/job/127921853219) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 0 | — | — | [37m59s](https://github.com/iree-org/iree/actions/runs/42228755353/job/127932578918) | [1h09m](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933120974) | [1h09m](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933120974) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42247473631/job/127999886806) | [6m16s](https://github.com/iree-org/iree/actions/runs/42228755353/job/127932579376) | [6m16s](https://github.com/iree-org/iree/actions/runs/42228755353/job/127932579376) | 10 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42238352322/job/127967702410) | [5m36s](https://github.com/iree-org/iree/actions/runs/42228755353/job/127932579629) | [5m36s](https://github.com/iree-org/iree/actions/runs/42228755353/job/127932579629) | 10 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42247473631/job/127999886921) | [5m19s](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933121143) | [5m19s](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933121143) | 10 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42255850691/job/128028009171) | [4m58s](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933120961) | [4m58s](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933120961) | 10 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42238352322/job/127967702714) | [4m55s](https://github.com/iree-org/iree/actions/runs/42228755353/job/127932579375) | [4m55s](https://github.com/iree-org/iree/actions/runs/42228755353/job/127932579375) | 10 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42247473631/job/127999886659) | [4m37s](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933120895) | [4m37s](https://github.com/iree-org/iree/actions/runs/42228298305/job/127933120895) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42255851046/job/128022816051) | [4m21s](https://github.com/iree-org/iree/actions/runs/42228298037/job/127929947273) | [4m21s](https://github.com/iree-org/iree/actions/runs/42228298037/job/127929947273) | 11 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42247473631/job/127999886740) | [4m13s](https://github.com/iree-org/iree/actions/runs/42228755353/job/127932578842) | [4m13s](https://github.com/iree-org/iree/actions/runs/42228755353/job/127932578842) | 10 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42246330855/job/127989538481) | [4m04s](https://github.com/iree-org/iree/actions/runs/42228298037/job/127929946760) | [4m04s](https://github.com/iree-org/iree/actions/runs/42228298037/job/127929946760) | 11 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 554 | 1% (8/554) |  | 5m27s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 436 | 1% (5/436) |  | 1h22m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 4h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h21m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h59m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h45m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 4h14m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h51m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
