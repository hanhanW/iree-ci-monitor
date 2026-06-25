# iree-ci-monitor

_Updated: 2026-06-25 12:00 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [47m49s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333055) | [58m30s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683630) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [25m06s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161284) | [51m11s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333176) | 0% (0/4) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [25m15s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683238) | [45m25s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333044) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [31m46s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683497) | [41m40s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333144) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [25m38s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161213) | [37m29s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683587) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [15m16s](https://github.com/iree-org/iree/actions/runs/28172319267/job/83446011870) | [32m24s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683571) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [7m38s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683330) | [28m01s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332898) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [6m24s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161262) | [24m49s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683659) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [12m45s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333031) | [23m09s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683582) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [9m03s](https://github.com/iree-org/iree/actions/runs/28172319267/job/83446011589) | [20m53s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683076) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [1m02s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683111) | [16m26s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161090) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [4m05s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333013) | [5m47s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683224) | 0% (0/2) | `iree-mi308-1` |
| `azure-linux-scale` | ossci | 26 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/28162167882/job/83405148574) | [2m06s](https://github.com/iree-org/iree/actions/runs/28156378038/job/83402531337) | 0% (0/15) | 26 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/28172319267/job/83446011845) | [1m41s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333028) | 0% (0/8) | 16 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m22s](https://github.com/iree-org/iree/actions/runs/28163293944/job/83408912850) | [1m22s](https://github.com/iree-org/iree/actions/runs/28163293944/job/83408912850) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28172319473/job/83439512445) | [1m13s](https://github.com/iree-org/iree/actions/runs/28162167882/job/83405148111) | 0% (0/6) | 12 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/28167098347/job/83421719750) | [1m04s](https://github.com/iree-org/iree/actions/runs/28162167882/job/83405148102) | 0% (0/6) | 12 |
| `macos-14` | github-hosted | 13 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28163294447/job/83408914280) | [1m00s](https://github.com/iree-org/iree/actions/runs/28162167882/job/83405148099) | 0% (0/7) | 13 |
| `ubuntu-24.04` | github-hosted | 90 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28169004592/job/83428334648) | [4s](https://github.com/iree-org/iree/actions/runs/28171244220/job/83435779003) | 2% (1/40) | 88 |
| `ubuntu-latest` | github-hosted | 30 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28179659365/job/83465554419) | [4s](https://github.com/iree-org/iree/actions/runs/28179659934/job/83465515234) | 0% (0/6) | 30 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28163291752/job/83408904982) | [3s](https://github.com/iree-org/iree/actions/runs/28163291752/job/83408904982) | 0% (0/1) | 1 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28167098347/job/83421719912) | [1s](https://github.com/iree-org/iree/actions/runs/28172319473/job/83439512738) | 0% (0/2) | 4 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 4 | [9h06m](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332845) | 2026-06-25 12:00 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [9h06m](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332845) | 2026-06-25 12:00 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `fuse_multiple-slice` | pull_request |
| [8h53m](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683033) | 2026-06-25 12:00 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [6h56m](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161012) | 2026-06-25 12:00 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `integrates/llvm-20260625` | pull_request |
| [5h22m](https://github.com/iree-org/iree/actions/runs/28172319267/job/83446011596) | 2026-06-25 12:00 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 4 | 4 | [9h06m](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332845) | 2026-06-25 12:00 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [47m49s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333055) | [58m30s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683630) | [58m30s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683630) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [42m13s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683484) | [51m11s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333176) | [51m11s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333176) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [13m48s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161195) | [48m23s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683592) | [48m23s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683592) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [34m40s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683688) | [45m25s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333044) | [45m25s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333044) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [31m46s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683497) | [41m40s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333144) | [41m40s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333144) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [25m38s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161213) | [37m29s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683587) | [37m29s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683587) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [29m14s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333006) | [32m24s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683571) | [32m24s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683571) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [25m15s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683238) | [29m57s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333046) | [29m57s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333046) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [7m38s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683330) | [28m01s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332898) | [28m01s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332898) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [15m16s](https://github.com/iree-org/iree/actions/runs/28172319267/job/83446011870) | [24m52s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333164) | [24m52s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333164) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [12m18s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161176) | [24m49s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683659) | [24m49s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683659) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [12m45s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333031) | [23m09s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683582) | [23m09s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683582) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [9m03s](https://github.com/iree-org/iree/actions/runs/28172319267/job/83446011589) | [20m53s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683076) | [20m53s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683076) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [6m24s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161262) | [17m01s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683518) | [17m01s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683518) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [1m02s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683111) | [16m26s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161090) | [16m26s](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161090) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 4 | 0 | — | — | [4m05s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333013) | [5m47s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683224) | [5m47s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683224) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/28172319267/job/83446011848) | [2m27s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333149) | [2m27s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404333149) | 4 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/28162167887/job/83405150597) | [2m13s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83402537897) | [2m13s](https://github.com/iree-org/iree/actions/runs/28156378002/job/83402537897) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 4 | 0 | — | — | [1m46s](https://github.com/iree-org/iree/actions/runs/28172319473/job/83439512586) | [2m06s](https://github.com/iree-org/iree/actions/runs/28156378038/job/83402531337) | [2m06s](https://github.com/iree-org/iree/actions/runs/28156378038/job/83402531337) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 127 | 0% (0/127) |  | 4h53m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 97 | 0% (0/97) |  | 4h57m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 107 | 6% (6/107) |  | 4h58m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 89 | 0% (0/89) |  | 4h58m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 28 | 0% (0/28) |  | 5h10m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 9h06m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
