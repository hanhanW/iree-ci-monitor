# iree-ci-monitor

_Updated: 2026-06-25 06:06 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [47m49s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333055) | [58m30s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683630) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [25m06s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161284) | [51m11s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333176) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [25m15s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683238) | [45m25s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333044) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [31m46s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683497) | [41m40s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333144) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [25m38s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161213) | [37m29s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683587) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [14m50s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161212) | [32m24s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683571) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [7m38s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683330) | [28m01s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332898) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [6m24s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161262) | [24m49s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683659) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [12m45s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333031) | [23m09s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683582) | 0% (0/1) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [5m56s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332822) | [20m53s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683076) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [1m02s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683111) | [16m26s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161090) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 3 | 0 | — | — | 0 | [4m05s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333013) | [5m47s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683224) | 0% (0/1) | `iree-mi308-1` |
| `azure-linux-scale` | ossci | 19 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/28162167882/job/83405148478) | [2m06s](https://github.com/iree-org/iree/actions/runs/28156378038/job/83402531337) | 0% (0/8) | 19 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 12 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161294) | [1m41s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333028) | 0% (0/4) | 12 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m22s](https://github.com/iree-org/iree/actions/runs/28163293944/job/83408912850) | [1m22s](https://github.com/iree-org/iree/actions/runs/28163293944/job/83408912850) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28167098347/job/83421719773) | [1m18s](https://github.com/iree-org/iree/actions/runs/28156378038/job/83402531185) | 0% (0/3) | 11 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/28167098347/job/83421719772) | [1m04s](https://github.com/iree-org/iree/actions/runs/28162167882/job/83405148102) | 0% (0/3) | 12 |
| `macos-14` | github-hosted | 12 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/28163294447/job/83408914280) | [1m00s](https://github.com/iree-org/iree/actions/runs/28162167882/job/83405148099) | 0% (0/3) | 12 |
| `ubuntu-24.04` | github-hosted | 80 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/28167098151/job/83421687756) | [4s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333123) | 9% (2/23) | 78 |
| `ubuntu-latest` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28162445611/job/83406040295) | [4s](https://github.com/iree-org/iree/actions/runs/28169112465/job/83428467728) | 0% (0/3) | 21 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/28163291752/job/83408904982) | [3s](https://github.com/iree-org/iree/actions/runs/28163291752/job/83408904982) | — | 1 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28162167882/job/83405148509) | [1s](https://github.com/iree-org/iree/actions/runs/28167098347/job/83421719912) | 0% (0/1) | 3 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 7 | 7 | [23h26m](https://github.com/iree-org/iree/actions/runs/28102210744/job/83208735459) | 2026-06-25 06:06 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [23h26m](https://github.com/iree-org/iree/actions/runs/28102210744/job/83208735459) | 2026-06-25 06:06 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [23h19m](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184300) | 2026-06-25 06:06 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/bjacob/cpu-ukernel-bodies` | pull_request |
| [22h34m](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582315) | 2026-06-25 06:06 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `fix-24624-raise-special-ops-memref-crash` | pull_request |
| [21h59m](https://github.com/iree-org/iree/actions/runs/28107886109/job/83228908779) | 2026-06-25 06:06 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [3h12m](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332845) | 2026-06-25 06:06 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `fuse_multiple-slice` | pull_request |
| [2h59m](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683033) | 2026-06-25 06:06 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [1h02m](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161012) | 2026-06-25 06:06 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `integrates/llvm-20260625` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 7 | 7 | [23h26m](https://github.com/iree-org/iree/actions/runs/28102210744/job/83208735459) | 2026-06-25 06:06 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [47m49s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333055) | [58m30s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683630) | [58m30s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683630) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [42m13s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683484) | [51m11s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333176) | [51m11s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333176) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [13m48s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161195) | [48m23s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683592) | [48m23s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683592) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [34m40s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683688) | [45m25s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333044) | [45m25s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333044) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [31m46s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683497) | [41m40s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333144) | [41m40s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333144) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [25m38s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161213) | [37m29s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683587) | [37m29s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683587) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [29m14s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333006) | [32m24s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683571) | [32m24s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683571) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [25m15s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683238) | [29m57s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333046) | [29m57s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333046) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [7m38s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683330) | [28m01s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332898) | [28m01s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332898) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [12m59s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683564) | [24m52s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333164) | [24m52s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333164) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [12m18s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161176) | [24m49s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683659) | [24m49s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683659) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [12m45s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333031) | [23m09s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683582) | [23m09s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683582) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [5m56s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332822) | [20m53s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683076) | [20m53s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683076) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [6m24s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161262) | [17m01s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683518) | [17m01s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683518) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [1m02s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683111) | [16m26s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161090) | [16m26s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161090) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 3 | 0 | — | — | [4m05s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333013) | [5m47s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683224) | [5m47s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683224) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 3 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161294) | [2m27s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333149) | [2m27s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333149) | 3 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83405150597) | [2m13s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83402537897) | [2m13s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83402537897) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 3 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/28167098347/job/83421719914) | [2m06s](https://github.com/iree-org/iree/actions/runs/28156378038/job/83402531337) | [2m06s](https://github.com/iree-org/iree/actions/runs/28156378038/job/83402531337) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 6% (6/102) |  | 32m31s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 123 | 0% (0/123) |  | 32m52s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 94 | 0% (0/94) |  | 40m10s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 86 | 0% (0/86) |  | 41m32s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 27 | 0% (0/27) |  | 52m23s ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 23h26m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
