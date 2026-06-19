# iree-ci-monitor

_Updated: 2026-06-19 11:58 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [14m48s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364389) | [28m55s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329396) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [21m10s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329182) | [26m50s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633004) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [8m07s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364288) | [25m00s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329350) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [19m58s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364289) | [20m36s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329306) | 0% (0/3) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [9m06s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633076) | [20m20s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364260) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [14m10s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633041) | [18m02s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329382) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [9m17s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329305) | [16m43s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364342) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [5m08s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329222) | [15m58s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364153) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [8m34s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633241) | [15m23s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329431) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [5m42s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633150) | [14m42s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329322) | 0% (0/6) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [9m05s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633152) | [11m22s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329281) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216923) | [2m52s](https://github.com/iree-org/iree/actions/runs/27822682153/job/82339360247) | 0% (0/3) | 6 |
| `azure-linux-scale` | ossci | 37 | 0 | — | — | 0 | [1m48s](https://github.com/iree-org/iree/actions/runs/27830737442/job/82366611484) | [2m36s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573757) | 0% (0/21) | 37 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 2 | 0 | — | — | 0 | [1m25s](https://github.com/iree-org/iree/actions/runs/27821372395/job/82335062227) | [1m36s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216877) | 0% (0/1) | 2 |
| `macos-14` | github-hosted | 19 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216809) | [1m14s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573566) | 0% (0/10) | 19 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/27830737442/job/82366611443) | [1m05s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573510) | 0% (0/9) | 18 |
| `windows-2022` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216673) | [40s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573530) | 0% (0/9) | 18 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633216) | [18s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329423) | 17% (2/12) | 16 |
| `ubuntu-24.04` | github-hosted | 119 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27822682121/job/82339328799) | [6s](https://github.com/iree-org/iree/actions/runs/27830737442/job/82366611366) | 5% (3/59) | 115 |
| `ubuntu-latest` | github-hosted | 30 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27831001076/job/82367492884) | [3s](https://github.com/iree-org/iree/actions/runs/27833466771/job/82375685761) | 0% (0/9) | 30 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27821345075/job/82334972343) | [3s](https://github.com/iree-org/iree/actions/runs/27821345075/job/82334972343) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342632989) | [2s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364146) | 33% (1/3) | 4 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633050) | [2s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364294) | 0% (0/3) | `iree-mi308-1` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [15m37s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633210) | [28m55s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329396) | [28m55s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329396) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [21m10s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329182) | [26m50s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633004) | [26m50s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633004) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [8m07s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364288) | [25m00s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329350) | [25m00s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329350) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [12m35s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329421) | [21m53s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364321) | [21m53s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364321) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [19m58s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364289) | [20m36s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329306) | [20m36s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329306) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [9m06s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633076) | [20m20s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364260) | [20m20s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364260) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [14m10s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633041) | [18m02s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329382) | [18m02s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329382) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [13m58s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329397) | [16m43s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364342) | [16m43s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364342) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [5m08s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329222) | [15m58s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364153) | [15m58s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364153) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [8m34s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633241) | [15m23s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329431) | [15m23s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329431) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [9m17s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329305) | [14m46s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633182) | [14m46s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633182) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [13m59s](https://github.com/iree-org/iree/actions/runs/27830737457/job/82368364243) | [14m42s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329322) | [14m42s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329322) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [8m35s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329326) | [14m12s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633202) | [14m12s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633202) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [9m05s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633152) | [11m22s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329281) | [11m22s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329281) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [5m42s](https://github.com/iree-org/iree/actions/runs/27822441074/job/82342633150) | [9m51s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329360) | [9m51s](https://github.com/iree-org/iree/actions/runs/27818270648/job/82326329360) | 3 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 6 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216923) | [2m52s](https://github.com/iree-org/iree/actions/runs/27822682153/job/82339360247) | [2m52s](https://github.com/iree-org/iree/actions/runs/27822682153/job/82339360247) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 6 | 0 | — | — | [2m03s](https://github.com/iree-org/iree/actions/runs/27830737442/job/82366611653) | [2m45s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573724) | [2m45s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573724) | 6 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 6 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27822682153/job/82339360128) | [2m43s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573612) | [2m43s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573612) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 4 | 0 | — | — | [2m03s](https://github.com/iree-org/iree/actions/runs/27817114355/job/82321015404) | [2m36s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573757) | [2m36s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573757) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 6 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27822682153/job/82339360308) | [2m34s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573655) | [2m34s](https://github.com/iree-org/iree/actions/runs/27822441133/job/82338573655) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 166 | 0% (0/166) |  | 4h13m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 126 | 5% (6/126) |  | 4h14m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 135 | 0% (0/135) |  | 4h14m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 117 | 0% (0/117) |  | 4h17m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 37 | 0% (0/37) |  | 4h26m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
