# iree-ci-monitor

_Updated: 2026-10-14 10:17 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 22 | 0 | — | — | 0 | [37m09s](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742876717) | [1h35m](https://github.com/iree-org/iree/actions/runs/38580865113/job/115915243686) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 22 | 0 | — | — | 0 | [22m08s](https://github.com/iree-org/iree/actions/runs/38580865113/job/115915243919) | [1h28m](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875661) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 22 | 0 | — | — | 0 | [28m16s](https://github.com/iree-org/iree/actions/runs/38529169306/job/115739584348) | [1h17m](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875484) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 11 | 0 | — | — | 0 | [20m00s](https://github.com/iree-org/iree/actions/runs/38580865113/job/115915243691) | [1h04m](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875262) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [19m04s](https://github.com/iree-org/iree/actions/runs/38568140188/job/115869592105) | [52m13s](https://github.com/iree-org/iree/actions/runs/38584157562/job/115926104493) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [19m57s](https://github.com/iree-org/iree/actions/runs/38568140188/job/115869591935) | [42m29s](https://github.com/iree-org/iree/actions/runs/38580865113/job/115915243653) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 22 | 0 | — | — | 0 | [13m48s](https://github.com/iree-org/iree/actions/runs/38571380424/job/115885486552) | [40m23s](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875736) | 0% (0/4) | `shark55-ci`, `shark75-ci` |
| `windows-2022` | github-hosted | 42 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38584413127/job/115922560353) | [3m12s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105162) | 0% (0/6) | 42 |
| `azure-linux-scale` | ossci | 89 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/38568140146/job/115866106173) | [2m13s](https://github.com/iree-org/iree/actions/runs/38589209784/job/115939380725) | 0% (0/16) | 89 |
| `ubuntu-24.04-arm` | github-hosted | 42 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/38571380298/job/115899291825) | [2m05s](https://github.com/iree-org/iree/actions/runs/38580865396/job/115910190855) | 0% (0/6) | 41 |
| `macos-15` | github-hosted | 43 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/38583560850/job/115919560235) | [1m56s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105160) | 0% (0/7) | 43 |
| `ubuntu-24.04` | github-hosted | 274 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38580865113/job/115910088230) | [1m29s](https://github.com/iree-org/iree/actions/runs/38529169445/job/115736669265) | 5% (2/44) | 266 |
| `ubuntu-latest` | github-hosted | 45 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/38529168661/job/115736607641) | [1m28s](https://github.com/iree-org/iree/actions/runs/38530094390/job/115739645021) | 0% (0/6) | 45 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m26s](https://github.com/iree-org/iree/actions/runs/38542595656/job/115780762052) | [1m26s](https://github.com/iree-org/iree/actions/runs/38542595656/job/115780762052) | 100% (1/1) | 1 |
| `azure-windows-scale` | ossci | 14 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/38568140146/job/115866106250) | [1s](https://github.com/iree-org/iree/actions/runs/38589209784/job/115939381261) | 0% (0/2) | 14 |
| `Linux,X64,iree-w7900` | self-hosted | 11 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 11 | 0 | — | — | [37m25s](https://github.com/iree-org/iree/actions/runs/38583560735/job/115923522367) | [1h46m](https://github.com/iree-org/iree/actions/runs/38527942546/job/115735218542) | [1h46m](https://github.com/iree-org/iree/actions/runs/38527942546/job/115735218542) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 11 | 0 | — | — | [29m16s](https://github.com/iree-org/iree/actions/runs/38589209812/job/115944179316) | [1h40m](https://github.com/iree-org/iree/actions/runs/38527942546/job/115735218222) | [1h40m](https://github.com/iree-org/iree/actions/runs/38527942546/job/115735218222) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 11 | 0 | — | — | [24m19s](https://github.com/iree-org/iree/actions/runs/38563091727/job/115852450408) | [1h35m](https://github.com/iree-org/iree/actions/runs/38580865113/job/115915243686) | [1h35m](https://github.com/iree-org/iree/actions/runs/38580865113/job/115915243686) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 11 | 0 | — | — | [16m29s](https://github.com/iree-org/iree/actions/runs/38584157562/job/115926104644) | [1h22m](https://github.com/iree-org/iree/actions/runs/38529169306/job/115739584284) | [1h22m](https://github.com/iree-org/iree/actions/runs/38529169306/job/115739584284) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 11 | 0 | — | — | [17m46s](https://github.com/iree-org/iree/actions/runs/38584157562/job/115926104777) | [1h09m](https://github.com/iree-org/iree/actions/runs/38529169306/job/115739584234) | [1h09m](https://github.com/iree-org/iree/actions/runs/38529169306/job/115739584234) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 11 | 0 | — | — | [20m00s](https://github.com/iree-org/iree/actions/runs/38580865113/job/115915243691) | [1h04m](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875262) | [1h04m](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875262) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 11 | 0 | — | — | [31m56s](https://github.com/iree-org/iree/actions/runs/38589209812/job/115944179654) | [59m11s](https://github.com/iree-org/iree/actions/runs/38584157562/job/115926104749) | [59m11s](https://github.com/iree-org/iree/actions/runs/38584157562/job/115926104749) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 11 | 0 | — | — | [19m04s](https://github.com/iree-org/iree/actions/runs/38568140188/job/115869592105) | [52m13s](https://github.com/iree-org/iree/actions/runs/38584157562/job/115926104493) | [52m13s](https://github.com/iree-org/iree/actions/runs/38584157562/job/115926104493) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 11 | 0 | — | — | [15m38s](https://github.com/iree-org/iree/actions/runs/38571380424/job/115885486384) | [49m06s](https://github.com/iree-org/iree/actions/runs/38527942546/job/115735218221) | [49m06s](https://github.com/iree-org/iree/actions/runs/38527942546/job/115735218221) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 11 | 0 | — | — | [19m57s](https://github.com/iree-org/iree/actions/runs/38568140188/job/115869591935) | [42m29s](https://github.com/iree-org/iree/actions/runs/38580865113/job/115915243653) | [42m29s](https://github.com/iree-org/iree/actions/runs/38580865113/job/115915243653) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 11 | 0 | — | — | [8m50s](https://github.com/iree-org/iree/actions/runs/38578799425/job/115907418114) | [30m09s](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875381) | [30m09s](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875381) | 2 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 14 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38584413127/job/115922560131) | [3m49s](https://github.com/iree-org/iree/actions/runs/38584157641/job/115923335603) | [3m49s](https://github.com/iree-org/iree/actions/runs/38584157641/job/115923335603) | 13 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38571380424/job/115885486051) | [3m38s](https://github.com/iree-org/iree/actions/runs/38583560735/job/115923521820) | [3m38s](https://github.com/iree-org/iree/actions/runs/38583560735/job/115923521820) | 11 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 14 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38584413127/job/115922560353) | [3m12s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105162) | [3m28s](https://github.com/iree-org/iree/actions/runs/38584157641/job/115923335250) | 14 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38578799425/job/115907417836) | [3m07s](https://github.com/iree-org/iree/actions/runs/38583560735/job/115923522134) | [3m07s](https://github.com/iree-org/iree/actions/runs/38583560735/job/115923522134) | 11 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38571380424/job/115885486883) | [2m46s](https://github.com/iree-org/iree/actions/runs/38583560735/job/115923522007) | [2m46s](https://github.com/iree-org/iree/actions/runs/38583560735/job/115923522007) | 11 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 14 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/38571380298/job/115899291825) | [2m43s](https://github.com/iree-org/iree/actions/runs/38584157641/job/115923335185) | [3m19s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105271) | 14 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 14 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/38583560850/job/115919561312) | [2m39s](https://github.com/iree-org/iree/actions/runs/38589209784/job/115939381208) | [3m23s](https://github.com/iree-org/iree/actions/runs/38578799246/job/115902989324) | 14 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38571380424/job/115885486427) | [2m37s](https://github.com/iree-org/iree/actions/runs/38583560735/job/115923521332) | [2m37s](https://github.com/iree-org/iree/actions/runs/38583560735/job/115923521332) | 11 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 14 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38584413127/job/115922560349) | [2m35s](https://github.com/iree-org/iree/actions/runs/38529169445/job/115736669350) | [2m56s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105130) | 14 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 404 | 11% (44/404) |  | 47m22s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 317 | 1% (2/317) |  | 1h01m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h35m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h04m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h28m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
