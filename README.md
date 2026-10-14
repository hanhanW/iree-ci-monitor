# iree-ci-monitor

_Updated: 2026-10-14 14:46 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 24 | 0 | — | — | 0 | [20m59s](https://github.com/iree-org/iree/actions/runs/38568140188/job/115869592141) | [1h31m](https://github.com/iree-org/iree/actions/runs/38580865113/job/115915243895) | 0% (0/6) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 24 | 0 | — | — | 0 | [14m36s](https://github.com/iree-org/iree/actions/runs/38578799425/job/115907418279) | [47m48s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768747) | 0% (0/6) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 24 | 0 | — | — | 0 | [11m02s](https://github.com/iree-org/iree/actions/runs/38563091727/job/115852450371) | [44m42s](https://github.com/iree-org/iree/actions/runs/38580865113/job/115915243641) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [15m17s](https://github.com/iree-org/iree/actions/runs/38563091727/job/115852450402) | [35m36s](https://github.com/iree-org/iree/actions/runs/38584157562/job/115926104672) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 12 | 0 | — | — | 0 | [11m30s](https://github.com/iree-org/iree/actions/runs/38597287966/job/116010993923) | [32m02s](https://github.com/iree-org/iree/actions/runs/38584157562/job/115926104981) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [10m46s](https://github.com/iree-org/iree/actions/runs/38635008547/job/116099046254) | [28m44s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768508) | 0% (0/3) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 24 | 0 | — | — | 0 | [11m05s](https://github.com/iree-org/iree/actions/runs/38616406026/job/116037116458) | [17m43s](https://github.com/iree-org/iree/actions/runs/38589209812/job/115944179799) | 0% (0/6) | `shark55-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 83 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/38597288263/job/116006855823) | [2m13s](https://github.com/iree-org/iree/actions/runs/38589209784/job/115939380725) | 0% (0/21) | 83 |
| `windows-2022` | github-hosted | 39 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38589209784/job/115939380160) | [1m38s](https://github.com/iree-org/iree/actions/runs/38584157641/job/115923335187) | 0% (0/9) | 39 |
| `ubuntu-24.04` | github-hosted | 262 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38597287580/job/116006751818) | [1m05s](https://github.com/iree-org/iree/actions/runs/38580865396/job/115910190213) | 2% (1/59) | 258 |
| `ubuntu-24.04-arm` | github-hosted | 39 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/38568140146/job/115866105851) | [47s](https://github.com/iree-org/iree/actions/runs/38578799246/job/115902987604) | 11% (1/9) | 39 |
| `macos-15` | github-hosted | 39 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/38578799246/job/115902987676) | [42s](https://github.com/iree-org/iree/actions/runs/38580865396/job/115910190525) | 0% (0/9) | 39 |
| `azure-windows-scale` | ossci | 13 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/38589209784/job/115939381261) | [3s](https://github.com/iree-org/iree/actions/runs/38597288263/job/116006856089) | 0% (0/3) | 13 |
| `ubuntu-latest` | github-hosted | 39 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38635852311/job/116098803511) | [3s](https://github.com/iree-org/iree/actions/runs/38617229920/job/116035330327) | 0% (0/9) | 39 |
| `Linux,X64,iree-w7900` | self-hosted | 12 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 12 | 0 | — | — | [20m35s](https://github.com/iree-org/iree/actions/runs/38563091727/job/115852450333) | [1h31m](https://github.com/iree-org/iree/actions/runs/38580865113/job/115915243895) | [1h31m](https://github.com/iree-org/iree/actions/runs/38580865113/job/115915243895) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 12 | 0 | — | — | [20m13s](https://github.com/iree-org/iree/actions/runs/38563091727/job/115852450524) | [59m11s](https://github.com/iree-org/iree/actions/runs/38584157562/job/115926104749) | [59m11s](https://github.com/iree-org/iree/actions/runs/38584157562/job/115926104749) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 12 | 0 | — | — | [5m30s](https://github.com/iree-org/iree/actions/runs/38597287966/job/116010994196) | [47m48s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768747) | [47m48s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768747) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 12 | 0 | — | — | [24m19s](https://github.com/iree-org/iree/actions/runs/38563091727/job/115852450408) | [45m40s](https://github.com/iree-org/iree/actions/runs/38583560735/job/115923522534) | [1h35m](https://github.com/iree-org/iree/actions/runs/38580865113/job/115915243686) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 12 | 0 | — | — | [14m44s](https://github.com/iree-org/iree/actions/runs/38563091727/job/115852450499) | [36m12s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768495) | [59m36s](https://github.com/iree-org/iree/actions/runs/38584157562/job/115926104855) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 12 | 0 | — | — | [15m17s](https://github.com/iree-org/iree/actions/runs/38563091727/job/115852450402) | [35m36s](https://github.com/iree-org/iree/actions/runs/38584157562/job/115926104672) | [42m29s](https://github.com/iree-org/iree/actions/runs/38580865113/job/115915243653) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 12 | 0 | — | — | [11m30s](https://github.com/iree-org/iree/actions/runs/38597287966/job/116010993923) | [32m02s](https://github.com/iree-org/iree/actions/runs/38584157562/job/115926104981) | [32m36s](https://github.com/iree-org/iree/actions/runs/38616406026/job/116037116625) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 12 | 0 | — | — | [10m46s](https://github.com/iree-org/iree/actions/runs/38635008547/job/116099046254) | [28m44s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768508) | [52m13s](https://github.com/iree-org/iree/actions/runs/38584157562/job/115926104493) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 12 | 0 | — | — | [5m54s](https://github.com/iree-org/iree/actions/runs/38568140188/job/115869591810) | [26m28s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768790) | [39m15s](https://github.com/iree-org/iree/actions/runs/38589209812/job/115944179409) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 12 | 0 | — | — | [12m11s](https://github.com/iree-org/iree/actions/runs/38635008547/job/116099046337) | [17m43s](https://github.com/iree-org/iree/actions/runs/38589209812/job/115944179799) | [17m43s](https://github.com/iree-org/iree/actions/runs/38589209812/job/115944179799) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 12 | 0 | — | — | [8m50s](https://github.com/iree-org/iree/actions/runs/38578799425/job/115907418114) | [16m24s](https://github.com/iree-org/iree/actions/runs/38616406026/job/116037115788) | [20m35s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768458) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 13 | 0 | — | — | [21s](https://github.com/iree-org/iree/actions/runs/38578799246/job/115902988594) | [4m05s](https://github.com/iree-org/iree/actions/runs/38563091943/job/115849472785) | [4m05s](https://github.com/iree-org/iree/actions/runs/38563091943/job/115849472785) | 13 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 13 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38635008537/job/116095892433) | [3m49s](https://github.com/iree-org/iree/actions/runs/38584157641/job/115923335603) | [3m49s](https://github.com/iree-org/iree/actions/runs/38584157641/job/115923335603) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 13 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38584413127/job/115922560353) | [3m28s](https://github.com/iree-org/iree/actions/runs/38584157641/job/115923335250) | [3m28s](https://github.com/iree-org/iree/actions/runs/38584157641/job/115923335250) | 13 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 13 | 0 | — | — | [1m23s](https://github.com/iree-org/iree/actions/runs/38584157641/job/115923335196) | [3m23s](https://github.com/iree-org/iree/actions/runs/38578799246/job/115902989324) | [3m23s](https://github.com/iree-org/iree/actions/runs/38578799246/job/115902989324) | 13 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 13 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/38597288263/job/116006855899) | [3m07s](https://github.com/iree-org/iree/actions/runs/38563091943/job/115849472722) | [3m07s](https://github.com/iree-org/iree/actions/runs/38563091943/job/115849472722) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 13 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/38635008537/job/116095893116) | [2m37s](https://github.com/iree-org/iree/actions/runs/38584157641/job/115923335343) | [2m37s](https://github.com/iree-org/iree/actions/runs/38584157641/job/115923335343) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 13 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38616406095/job/116032614470) | [2m15s](https://github.com/iree-org/iree/actions/runs/38580865396/job/115910190999) | [2m15s](https://github.com/iree-org/iree/actions/runs/38580865396/job/115910190999) | 13 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 13 | 0 | — | — | [15s](https://github.com/iree-org/iree/actions/runs/38580865396/job/115910190657) | [2m13s](https://github.com/iree-org/iree/actions/runs/38589209784/job/115939380725) | [2m13s](https://github.com/iree-org/iree/actions/runs/38589209784/job/115939380725) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 13 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38635008537/job/116095893206) | [2m09s](https://github.com/iree-org/iree/actions/runs/38580865396/job/115910190724) | [2m09s](https://github.com/iree-org/iree/actions/runs/38580865396/job/115910190724) | 13 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 428 | 10% (44/428) |  | 32m36s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 337 | 1% (2/337) |  | 37m52s ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h31m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
