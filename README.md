# iree-ci-monitor

_Updated: 2026-07-30 11:49 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [27m53s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756427) | [29m29s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925867) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [15m10s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862699) | [26m08s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925824) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [5m07s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862957) | [25m41s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925894) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [18m57s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863261) | [25m13s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925849) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [20m12s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756230) | [23m27s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925721) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [6m14s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863040) | [23m22s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925848) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [14m47s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756304) | [22m42s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925702) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [7m20s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863419) | [22m00s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925788) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [8m22s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863171) | [21m14s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925938) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [19m50s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756549) | [20m40s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925866) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 1 | [2m38s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756342) | [16m27s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756323) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863218) | [13m08s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925761) | 0% (0/1) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30531204475/job/90833772288) | [11m23s](https://github.com/iree-org/iree/actions/runs/30527500179/job/90834067270) | 0% (0/1) | 3 |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236609) | [1m54s](https://github.com/iree-org/iree/actions/runs/30527500179/job/90834067124) | 0% (0/3) | 9 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236606) | [1m50s](https://github.com/iree-org/iree/actions/runs/30527500179/job/90834067154) | 0% (0/3) | 9 |
| `ubuntu-24.04` | github-hosted | 66 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862762) | [1m47s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925810) | 0% (0/23) | 65 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m29s](https://github.com/iree-org/iree/actions/runs/30533088476/job/90839779304) | [1m29s](https://github.com/iree-org/iree/actions/runs/30533088476/job/90839779304) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 18 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/30527500179/job/90834067121) | [20s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236669) | 0% (0/8) | 18 |
| `macos-14` | github-hosted | 10 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30555399091/job/90922236350) | [17s](https://github.com/iree-org/iree/actions/runs/30527500179/job/90834067214) | 0% (0/4) | 10 |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30531200019/job/90833706812) | [8s](https://github.com/iree-org/iree/actions/runs/30531550219/job/90834823481) | 0% (0/3) | 24 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30533049204/job/90839650929) | [2s](https://github.com/iree-org/iree/actions/runs/30533049204/job/90839650929) | 0% (0/1) | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925772) | [2s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862809) | 0% (0/1) | 3 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [27m53s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756427) | [29m29s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925867) | [29m29s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925867) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [15m10s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862699) | [26m08s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925824) | [26m08s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925824) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [8m16s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863326) | [25m41s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925894) | [25m41s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925894) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [18m57s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863261) | [25m13s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925849) | [25m13s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925849) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [20m12s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756230) | [23m27s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925721) | [23m27s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925721) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [6m14s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863040) | [23m22s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925848) | [23m22s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925848) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [14m47s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756304) | [22m42s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925702) | [22m42s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925702) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [10m18s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863262) | [22m00s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925788) | [22m00s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925788) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [8m22s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863171) | [21m14s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925938) | [21m14s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925938) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [19m50s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756549) | [20m40s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925866) | [20m40s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925866) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [8m18s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756430) | [16m41s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925883) | [16m41s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925883) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [9m14s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925818) | [16m27s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756323) | [16m27s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756323) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [2m38s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756342) | [16m24s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925878) | [16m24s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925878) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 3 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863218) | [13m08s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925761) | [13m08s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925761) | 1 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30531204475/job/90833772288) | [11m23s](https://github.com/iree-org/iree/actions/runs/30527500179/job/90834067270) | [11m23s](https://github.com/iree-org/iree/actions/runs/30527500179/job/90834067270) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [7m20s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863419) | [8m27s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925950) | [8m27s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925950) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [2m38s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925862) | [5m07s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862957) | [5m07s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862957) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 3 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756273) | [2m14s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925859) | [2m14s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925859) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924863323) | [2m04s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925933) | [2m04s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925933) | 3 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/30555399727/job/90924862675) | [2m01s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925816) | [2m01s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925816) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 156 | 0% (0/155) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 190 | 5% (9/190) |  | 2h37m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 209 | 1% (2/209) |  | 2h46m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 47 | 2% (1/47) |  | 2h50m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 149 | 1% (2/149) |  | 2h50m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
