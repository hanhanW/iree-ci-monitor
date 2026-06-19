# iree-ci-monitor

_Updated: 2026-06-19 06:31 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [14m25s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199802) | [28m55s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329396) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [21m10s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329182) | [26m50s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633004) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [5m08s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329222) | [25m49s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199789) | 0% (0/2) | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199827) | [25m00s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329350) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [13m14s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199797) | [21m35s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199899) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199791) | [20m36s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329306) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [14m10s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633041) | [18m02s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329382) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [5m42s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633150) | [15m25s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199896) | 0% (0/4) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [9m17s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329305) | [14m46s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633182) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [9m05s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633152) | [11m22s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329281) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [5m36s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316200039) | [9m06s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633076) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27818270629/job/82324865157) | [2m52s](https://github.com/iree-org/iree/actions/runs/27822682153/job/82339360247) | 0% (0/2) | 6 |
| `azure-linux-scale` | ossci | 36 | 0 | — | — | 0 | [22s](https://github.com/iree-org/iree/actions/runs/27822682153/job/82339360446) | [2m36s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573757) | 0% (0/15) | 36 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m25s](https://github.com/iree-org/iree/actions/runs/27821372395/job/82335062227) | [1m25s](https://github.com/iree-org/iree/actions/runs/27821372395/job/82335062227) | 0% (0/1) | 1 |
| `macos-14` | github-hosted | 21 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/27814329807/job/82311731186) | [1m14s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573566) | 0% (0/6) | 21 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573556) | [1m05s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573510) | 0% (0/6) | 21 |
| `ubuntu-24.04` | github-hosted | 121 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633018) | [42s](https://github.com/iree-org/iree/actions/runs/27818270629/job/82324865081) | 10% (4/41) | 117 |
| `windows-2022` | github-hosted | 20 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573587) | [39s](https://github.com/iree-org/iree/actions/runs/27814329807/job/82311731222) | 0% (0/6) | 20 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633048) | [18s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329423) | 12% (1/8) | 16 |
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27817112465/job/82320976100) | [3s](https://github.com/iree-org/iree/actions/runs/27825963542/job/82350352849) | 0% (0/6) | 18 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/27821345075/job/82334972343) | [3s](https://github.com/iree-org/iree/actions/runs/27821345075/job/82334972343) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342632989) | [2s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199785) | 0% (0/2) | 4 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633050) | [2s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199929) | 0% (0/2) | `iree-mi308-1` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [15m37s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633210) | [28m55s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329396) | [28m55s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329396) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [21m10s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329182) | [26m50s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633004) | [26m50s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633004) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [12m35s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329421) | [26m23s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199909) | [26m23s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199909) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [5m08s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329222) | [25m49s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199789) | [25m49s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199789) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199827) | [25m00s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329350) | [25m00s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329350) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [15m23s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329431) | [21m35s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199899) | [21m35s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199899) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199791) | [20m36s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329306) | [20m36s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329306) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [14m10s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633041) | [18m02s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329382) | [18m02s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329382) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [14m42s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329322) | [15m25s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199896) | [15m25s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199896) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [10m49s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199795) | [14m46s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633182) | [14m46s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633182) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [13m14s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199797) | [14m12s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633202) | [14m12s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633202) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [6m30s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316199903) | [13m58s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329397) | [13m58s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329397) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [9m05s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633152) | [11m22s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329281) | [11m22s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329281) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [5m42s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633150) | [9m51s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329360) | [9m51s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329360) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [5m36s](https://github.com/iree-org/iree/actions/runs/27814329802/job/82316200039) | [9m06s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633076) | [9m06s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633076) | 2 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 6 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27818270629/job/82324865157) | [2m52s](https://github.com/iree-org/iree/actions/runs/27822682153/job/82339360247) | [2m52s](https://github.com/iree-org/iree/actions/runs/27822682153/job/82339360247) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 6 | 0 | — | — | [2m04s](https://github.com/iree-org/iree/actions/runs/27818270629/job/82324865168) | [2m45s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573724) | [2m45s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573724) | 6 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 6 | 0 | — | — | [13s](https://github.com/iree-org/iree/actions/runs/27814329807/job/82311731269) | [2m43s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573612) | [2m43s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573612) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 4 | 0 | — | — | [2m03s](https://github.com/iree-org/iree/actions/runs/27817114355/job/82321015404) | [2m36s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573757) | [2m36s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573757) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 6 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/27814329807/job/82311731263) | [2m34s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573655) | [2m34s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573655) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 162 | 0% (0/162) |  | 1h14m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 114 | 0% (0/114) |  | 1h23m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 131 | 0% (0/131) |  | 1h23m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 122 | 5% (6/122) |  | 1h28m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 36 | 0% (0/36) |  | 1h37m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
