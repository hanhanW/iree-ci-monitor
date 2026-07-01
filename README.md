# iree-ci-monitor

_Updated: 2026-07-01 11:59 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 10 | 0 | — | — | 0 | [17m43s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292663) | [1h51m](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397520) | 20% (1/5) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 20 | 0 | — | — | 0 | [29m37s](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397504) | [1h23m](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526636) | 0% (0/10) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 10 | 0 | — | — | 0 | [48m14s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748510) | [1h23m](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397540) | 0% (0/5) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 10 | 0 | — | — | 0 | [21m50s](https://github.com/iree-org/iree/actions/runs/28514016318/job/84522402882) | [1h09m](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397372) | 0% (0/5) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 10 | 0 | — | — | 0 | [18m17s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292808) | [1h08m](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526366) | 0% (0/5) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 20 | 0 | — | — | 0 | [16m46s](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397521) | [1h03m](https://github.com/iree-org/iree/actions/runs/28514016318/job/84522402978) | 0% (0/10) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [11m52s](https://github.com/iree-org/iree/actions/runs/28509966963/job/84523275635) | [55m48s](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526548) | 20% (1/5) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 20 | 0 | — | — | 0 | [26m35s](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397462) | [46m27s](https://github.com/iree-org/iree/actions/runs/28509966963/job/84523275882) | 0% (0/10) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [11m10s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748467) | [37m49s](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526561) | 0% (0/5) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [13m20s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292796) | [26m54s](https://github.com/iree-org/iree/actions/runs/28521369523/job/84548105206) | 0% (0/5) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 20 | 0 | — | — | 0 | [9m45s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292775) | [26m34s](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397434) | 10% (1/10) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28521369523/job/84548105150) | [16m13s](https://github.com/iree-org/iree/actions/runs/28509966963/job/84523275643) | 0% (0/5) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 40 | 0 | — | — | 0 | [14s](https://github.com/iree-org/iree/actions/runs/28521369523/job/84548105113) | [7m46s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748396) | 5% (1/20) | 40 |
| `ubuntu-24.04-arm` | github-hosted | 30 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/28524767522/job/84560217383) | [6m29s](https://github.com/iree-org/iree/actions/runs/28509966981/job/84521498155) | 0% (0/15) | 30 |
| `ubuntu-24.04` | github-hosted | 206 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292827) | [5m06s](https://github.com/iree-org/iree/actions/runs/28509966963/job/84523275577) | 5% (5/95) | 204 |
| `windows-2022` | github-hosted | 30 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28524767522/job/84560217453) | [2m47s](https://github.com/iree-org/iree/actions/runs/28509966981/job/84521498296) | 0% (0/15) | 30 |
| `azure-linux-scale` | ossci | 57 | 0 | — | — | 0 | [51s](https://github.com/iree-org/iree/actions/runs/28525494129/job/84560729328) | [2m15s](https://github.com/iree-org/iree/actions/runs/28521369502/job/84546167936) | 0% (0/32) | 57 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m32s](https://github.com/iree-org/iree/actions/runs/28511166404/job/84511558252) | [1m32s](https://github.com/iree-org/iree/actions/runs/28511166404/job/84511558252) | 0% (0/1) | 1 |
| `ubuntu-latest` | github-hosted | 42 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28527105591/job/84566410484) | [1m22s](https://github.com/iree-org/iree/actions/runs/28514319401/job/84522104449) | 0% (0/15) | 42 |
| `macos-14` | github-hosted | 31 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28521369502/job/84546167744) | [1m15s](https://github.com/iree-org/iree/actions/runs/28514016312/job/84521108653) | 0% (0/16) | 31 |
| `azure-windows-scale` | ossci | 10 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28521369502/job/84546167887) | [4s](https://github.com/iree-org/iree/actions/runs/28525494129/job/84560729446) | 0% (0/5) | 10 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28511136564/job/84511465091) | [2s](https://github.com/iree-org/iree/actions/runs/28511136564/job/84511465091) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 10 | 0 | — | — | [17m43s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292663) | [1h51m](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397520) | [1h51m](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397520) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [34m16s](https://github.com/iree-org/iree/actions/runs/28521369523/job/84548105375) | [1h25m](https://github.com/iree-org/iree/actions/runs/28509966963/job/84523275870) | [1h25m](https://github.com/iree-org/iree/actions/runs/28509966963/job/84523275870) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 10 | 0 | — | — | [48m14s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748510) | [1h23m](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397540) | [1h23m](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397540) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [29m37s](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397504) | [1h12m](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526536) | [1h12m](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526536) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 10 | 0 | — | — | [21m50s](https://github.com/iree-org/iree/actions/runs/28514016318/job/84522402882) | [1h09m](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397372) | [1h09m](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397372) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 10 | 0 | — | — | [18m17s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292808) | [1h08m](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526366) | [1h08m](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526366) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 0 | — | — | [19m23s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748424) | [1h05m](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526552) | [1h05m](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526552) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [29m24s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748631) | [1h00m](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526623) | [1h00m](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526623) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 10 | 0 | — | — | [11m52s](https://github.com/iree-org/iree/actions/runs/28509966963/job/84523275635) | [55m48s](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526548) | [55m48s](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526548) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 0 | — | — | [16m46s](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397521) | [45m36s](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526553) | [45m36s](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526553) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [18m38s](https://github.com/iree-org/iree/actions/runs/28524767794/job/84561953229) | [41m28s](https://github.com/iree-org/iree/actions/runs/28509966963/job/84523275860) | [41m28s](https://github.com/iree-org/iree/actions/runs/28509966963/job/84523275860) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 0 | — | — | [11m10s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748467) | [37m49s](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526561) | [37m49s](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526561) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [13m21s](https://github.com/iree-org/iree/actions/runs/28509966963/job/84523275833) | [28m31s](https://github.com/iree-org/iree/actions/runs/28524767794/job/84561953262) | [28m31s](https://github.com/iree-org/iree/actions/runs/28524767794/job/84561953262) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 10 | 0 | — | — | [13m20s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292796) | [26m54s](https://github.com/iree-org/iree/actions/runs/28521369523/job/84548105206) | [26m54s](https://github.com/iree-org/iree/actions/runs/28521369523/job/84548105206) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [9m24s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748483) | [26m34s](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397434) | [26m34s](https://github.com/iree-org/iree/actions/runs/28525494138/job/84562397434) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28521369523/job/84548105150) | [16m13s](https://github.com/iree-org/iree/actions/runs/28509966963/job/84523275643) | [16m13s](https://github.com/iree-org/iree/actions/runs/28509966963/job/84523275643) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28530040692/job/84592216813) | [16m09s](https://github.com/iree-org/iree/actions/runs/28509966981/job/84521498150) | [16m09s](https://github.com/iree-org/iree/actions/runs/28509966981/job/84521498150) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28530040692/job/84592216780) | [16m01s](https://github.com/iree-org/iree/actions/runs/28509966981/job/84521498264) | [16m01s](https://github.com/iree-org/iree/actions/runs/28509966981/job/84521498264) | 10 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28530040692/job/84592216623) | [13m59s](https://github.com/iree-org/iree/actions/runs/28509966981/job/84521497977) | [13m59s](https://github.com/iree-org/iree/actions/runs/28509966981/job/84521497977) | 10 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 10 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28521369523/job/84548105340) | [12m00s](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526644) | [12m00s](https://github.com/iree-org/iree/actions/runs/28513921659/job/84522526644) | 10 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 220 | 9% (20/220) |  | 1h05m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 257 | 1% (2/257) |  | 1h19m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 186 | 1% (1/186) |  | 1h19m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 210 | 0% (1/210) |  | 1h26m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 59 | 0% (0/59) |  | 1h27m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h23m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h51m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h23m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h03m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h08m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
