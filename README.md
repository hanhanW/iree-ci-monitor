# iree-ci-monitor

_Updated: 2026-05-20 18:21 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 10 | 0 | — | — | 0 | [44m15s](https://github.com/iree-org/iree/actions/runs/26188574851/job/77051987709) | [1h45m](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329623) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [19m05s](https://github.com/iree-org/iree/actions/runs/26188574851/job/77051987578) | [1h44m](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046315030) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926511) | 2026-05-19 06:28 PDT | 0 | [1h06m](https://github.com/iree-org/iree/actions/runs/26188574851/job/77051988347) | [1h42m](https://github.com/iree-org/iree/actions/runs/26186906213/job/77046149340) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 10 | 0 | — | — | 0 | [50m18s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329721) | [1h29m](https://github.com/iree-org/iree/actions/runs/26186906213/job/77046149363) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926441) | 2026-05-19 06:28 PDT | 0 | [55m35s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314856) | [1h22m](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329339) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 5 | 0 | — | — | 0 | [30m24s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314996) | [1h09m](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329529) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [34m43s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329583) | [1h05m](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314861) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 5 | 0 | — | — | 0 | [25m36s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329791) | [1h04m](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046315150) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 10 | 0 | — | — | 0 | [21m09s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314871) | [59m49s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329803) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 10 | 0 | — | — | 0 | [4m31s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329936) | [27m35s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329678) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 5 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26188574851/job/77051987502) | [20m05s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314844) | 0% (0/1) | `iree-mi308-1` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [9m40s](https://github.com/iree-org/iree/actions/runs/26188574851/job/77051987534) | [13m41s](https://github.com/iree-org/iree/actions/runs/26176389715/job/77009694079) | 0% (0/1) | `shark01-ci`, `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 20 | 0 | — | — | 0 | [1m49s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046315278) | [9m24s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329372) | 0% (0/4) | 20 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26188574851/job/77051987522) | [3m55s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329348) | 0% (0/1) | 5 |
| `ubuntu-24.04` | github-hosted | 108 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/26188574851/job/77051987734) | [3m48s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329383) | 5% (1/19) | 108 |
| `macos-14` | github-hosted | 18 | 0 | — | — | 0 | [31s](https://github.com/iree-org/iree/actions/runs/26176336607/job/77007356543) | [3m16s](https://github.com/iree-org/iree/actions/runs/26186931962/job/77045177080) | 0% (0/3) | 17 |
| `ubuntu-latest` | github-hosted | 19 | 0 | — | — | 0 | [27s](https://github.com/iree-org/iree/actions/runs/26176333675/job/77007296965) | [1m58s](https://github.com/iree-org/iree/actions/runs/26176333675/job/77007296587) | 0% (0/4) | 19 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26186906254/job/77044830144) | [1m44s](https://github.com/iree-org/iree/actions/runs/26186931962/job/77045177041) | 0% (0/3) | 18 |
| `windows-2022` | github-hosted | 18 | 0 | — | — | 0 | [17s](https://github.com/iree-org/iree/actions/runs/26176336607/job/77007356535) | [1m37s](https://github.com/iree-org/iree/actions/runs/26186931962/job/77045177093) | 0% (0/3) | 17 |
| `azure-windows-scale` | ossci | 6 | 4 | [5h15m](https://github.com/iree-org/iree/actions/runs/26186906254/job/77044830168) | 2026-05-20 18:21 PDT | 0 | [52s](https://github.com/iree-org/iree/actions/runs/26176389707/job/77007813618) | [52s](https://github.com/iree-org/iree/actions/runs/26176389707/job/77007813618) | — | 1 |
| `azure-linux-scale` | ossci | 31 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/26186931962/job/77045177451) | [33s](https://github.com/iree-org/iree/actions/runs/26176389707/job/77007813561) | 0% (0/6) | 28 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [5h15m](https://github.com/iree-org/iree/actions/runs/26186906254/job/77044830168) | 2026-05-20 18:21 PDT | `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | `users/bjacob/cpu-mma-broadcast-mbcst-fold` | pull_request |
| [5h14m](https://github.com/iree-org/iree/actions/runs/26186923000/job/77044990784) | 2026-05-20 18:21 PDT | `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | `users/bjacob/cpu-flatten-transfer-before-rank-reduce` | pull_request |
| [5h13m](https://github.com/iree-org/iree/actions/runs/26186931962/job/77045177363) | 2026-05-20 18:21 PDT | `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | `users/bjacob/cpu-mma-widen-before-broadcast` | pull_request |
| [4h42m](https://github.com/iree-org/iree/actions/runs/26188574886/job/77050678076) | 2026-05-20 18:21 PDT | `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | `main` | push |
| [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926441) | 2026-05-19 06:28 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `new-lds-promotion` | pull_request |
| [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926511) | 2026-05-19 06:28 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `new-lds-promotion` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 6 | 4 | [5h15m](https://github.com/iree-org/iree/actions/runs/26186906254/job/77044830168) | 2026-05-20 18:21 PDT | [52s](https://github.com/iree-org/iree/actions/runs/26176389707/job/77007813618) | [52s](https://github.com/iree-org/iree/actions/runs/26176389707/job/77007813618) | [52s](https://github.com/iree-org/iree/actions/runs/26176389707/job/77007813618) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [44m15s](https://github.com/iree-org/iree/actions/runs/26188574851/job/77051987709) | [1h45m](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329623) | [1h45m](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329623) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 5 | 0 | — | — | [19m05s](https://github.com/iree-org/iree/actions/runs/26188574851/job/77051987578) | [1h44m](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046315030) | [1h44m](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046315030) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926511) | 2026-05-19 06:28 PDT | [1h06m](https://github.com/iree-org/iree/actions/runs/26188574851/job/77051988347) | [1h42m](https://github.com/iree-org/iree/actions/runs/26186906213/job/77046149340) | [1h42m](https://github.com/iree-org/iree/actions/runs/26186906213/job/77046149340) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [46m34s](https://github.com/iree-org/iree/actions/runs/26186906213/job/77046149334) | [1h37m](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329832) | [1h37m](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329832) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 5 | 0 | — | — | [54m16s](https://github.com/iree-org/iree/actions/runs/26188574851/job/77051987777) | [1h29m](https://github.com/iree-org/iree/actions/runs/26186906213/job/77046149363) | [1h29m](https://github.com/iree-org/iree/actions/runs/26186906213/job/77046149363) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926441) | 2026-05-19 06:28 PDT | [55m35s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314856) | [1h22m](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329339) | [1h22m](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329339) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 5 | 0 | — | — | [30m24s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314996) | [1h09m](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329529) | [1h09m](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329529) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 5 | 0 | — | — | [41m00s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329862) | [1h06m](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046315189) | [1h06m](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046315189) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 5 | 0 | — | — | [34m43s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329583) | [1h05m](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314861) | [1h05m](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314861) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 5 | 0 | — | — | [25m36s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329791) | [1h04m](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046315150) | [1h04m](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046315150) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [28m32s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046315075) | [59m49s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329803) | [59m49s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329803) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [21m09s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314871) | [50m40s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329755) | [50m40s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329755) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [17m08s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314864) | [27m35s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329678) | [27m35s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329678) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 5 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26188574851/job/77051987502) | [20m05s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314844) | [20m05s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314844) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 5 | 0 | — | — | [9m40s](https://github.com/iree-org/iree/actions/runs/26188574851/job/77051987534) | [13m41s](https://github.com/iree-org/iree/actions/runs/26176389715/job/77009694079) | [13m41s](https://github.com/iree-org/iree/actions/runs/26176389715/job/77009694079) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [4m31s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329936) | [13m04s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314957) | [13m04s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314957) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 5 | 0 | — | — | [17s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046315006) | [9m31s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329606) | [9m31s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329606) | 5 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 5 | 0 | — | — | [46s](https://github.com/iree-org/iree/actions/runs/26176389715/job/77009693488) | [9m24s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329372) | [9m24s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329372) | 5 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 5 | 0 | — | — | [3m14s](https://github.com/iree-org/iree/actions/runs/26186932032/job/77046329578) | [8m23s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314963) | [8m23s](https://github.com/iree-org/iree/actions/runs/26186922959/job/77046314963) | 5 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 553 | 2% (10/552) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 458 | 6% (27/457) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 435 | 0% (1/434) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 454 | 1% (5/453) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 139 | 1% (2/139) |  | 4h24m ago |

## Alerts

- **[stale-queued]** `azure-windows-scale` oldest queued job observed waiting 5h15m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h44m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h45m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h42m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h22m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h05m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h29m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h04m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
