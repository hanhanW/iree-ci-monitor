# iree-ci-monitor

_Updated: 2026-07-30 05:53 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [27m53s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756427) | [29m29s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925867) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [5m44s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756407) | [27m16s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312276) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [18m28s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312341) | [26m08s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925824) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [6m58s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756261) | [25m13s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925849) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [20m12s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756230) | [23m27s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925721) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [8m18s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756430) | [23m22s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925848) | 0% (0/4) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [14m47s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756304) | [22m42s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925702) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756361) | [22m00s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925788) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [6m29s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312170) | [21m14s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925938) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [19m50s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756549) | [20m40s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925866) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [13m22s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312401) | [16m27s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756323) | 0% (0/4) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756242) | [13m08s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925761) | 0% (0/2) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30531204475/job/90833772288) | [11m23s](https://github.com/iree-org/iree/actions/runs/30527500179/job/90834067270) | 0% (0/3) | 4 |
| `windows-2022` | github-hosted | 14 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/30531204475/job/90833772224) | [1m54s](https://github.com/iree-org/iree/actions/runs/30527500179/job/90834067124) | 0% (0/9) | 14 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/30518079435/job/90792289152) | [1m39s](https://github.com/iree-org/iree/actions/runs/30527500179/job/90834067099) | 0% (0/9) | 15 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m29s](https://github.com/iree-org/iree/actions/runs/30533088476/job/90839779304) | [1m29s](https://github.com/iree-org/iree/actions/runs/30533088476/job/90839779304) | 0% (0/1) | 1 |
| `ubuntu-24.04` | github-hosted | 82 | 0 | — | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756139) | [1m20s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925819) | 0% (0/50) | 80 |
| `azure-linux-scale` | ossci | 24 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90834078226) | [17s](https://github.com/iree-org/iree/actions/runs/30533023612/job/90839567848) | 0% (0/19) | 24 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/30531204475/job/90833772201) | [17s](https://github.com/iree-org/iree/actions/runs/30527500179/job/90834067214) | 0% (0/9) | 15 |
| `ubuntu-latest` | github-hosted | 27 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30538765834/job/90858333807) | [8s](https://github.com/iree-org/iree/actions/runs/30531550219/job/90834823481) | 0% (0/6) | 27 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756129) | [2s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925772) | 0% (0/2) | 3 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30533049204/job/90839650929) | [2s](https://github.com/iree-org/iree/actions/runs/30533049204/job/90839650929) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [27m53s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756427) | [29m29s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925867) | [29m29s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925867) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [25m41s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925894) | [27m16s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312276) | [27m16s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312276) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [18m28s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312341) | [26m08s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925824) | [26m08s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925824) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [6m58s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756261) | [25m13s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925849) | [25m13s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925849) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [20m12s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756230) | [23m27s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925721) | [23m27s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925721) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [5m44s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756311) | [23m22s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925848) | [23m22s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925848) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [14m47s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756304) | [22m42s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925702) | [22m42s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925702) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756271) | [22m00s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925788) | [22m00s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925788) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [2m38s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925862) | [21m36s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312228) | [21m36s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312228) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [6m29s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312170) | [21m14s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925938) | [21m14s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925938) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [19m50s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756549) | [20m40s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925866) | [20m40s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925866) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [15m01s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312244) | [16m41s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925883) | [16m41s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925883) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [13m22s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312401) | [16m27s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756323) | [16m27s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756323) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [14m27s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312177) | [16m24s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925878) | [16m24s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925878) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756242) | [13m08s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925761) | [13m08s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925761) | 1 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30531204475/job/90833772288) | [11m23s](https://github.com/iree-org/iree/actions/runs/30527500179/job/90834067270) | [11m23s](https://github.com/iree-org/iree/actions/runs/30527500179/job/90834067270) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [6m54s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312213) | [8m27s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925950) | [8m27s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925950) | 3 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 3 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756273) | [2m14s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925859) | [2m14s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925859) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756354) | [2m04s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925933) | [2m04s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925933) | 3 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30527500120/job/90835756139) | [2m01s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925816) | [2m01s](https://github.com/iree-org/iree/actions/runs/30531201947/job/90835925816) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 205 | 1% (2/205) |  | 2h35m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 184 | 5% (9/184) |  | 2h36m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 155 | 0% (0/155) |  | 2h38m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 145 | 1% (2/145) |  | 2h42m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 46 | 2% (1/46) |  | 2h44m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
