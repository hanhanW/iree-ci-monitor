# iree-ci-monitor

_Updated: 2026-06-05 06:24 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305921) | [21m54s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715306039) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [15m52s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305969) | [15m52s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305969) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [4m56s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305979) | [14m50s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305916) | — | `shark01-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [13m44s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305746) | [13m44s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305746) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [11m15s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305939) | [12m53s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305873) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [9m27s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305962) | [9m27s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305962) | — | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305909) | [4m49s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715306024) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [4m39s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305751) | [4m39s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305751) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [4m08s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305971) | [4m08s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305971) | — | `shark10-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m30s](https://github.com/iree-org/iree/actions/runs/27009919441/job/79710711727) | [1m30s](https://github.com/iree-org/iree/actions/runs/27009919441/job/79710711727) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101729) | [9s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101786) | 0% (0/2) | 7 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305951) | [7s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305976) | — | 4 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101674) | [6s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615106) | — | 6 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/27009905341/job/79710665778) | [4s](https://github.com/iree-org/iree/actions/runs/27009905341/job/79710665778) | — | 1 |
| `ubuntu-24.04` | github-hosted | 35 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305858) | [3s](https://github.com/iree-org/iree/actions/runs/27012190395/job/79718244319) | 50% (2/4) | 35 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101656) | [3s](https://github.com/iree-org/iree/actions/runs/27009909973/job/79710680846) | 0% (0/1) | 6 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615111) | [3s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101661) | — | 5 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27012440667/job/79719110163) | [3s](https://github.com/iree-org/iree/actions/runs/27012441135/job/79719089352) | — | 6 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305706) | [1s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305706) | — | 1 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305855) | [1s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305855) | — | `iree-mi308-1` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305860) | [1s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305860) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305879) | [1s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305879) | — | `shark01-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101789) | [1s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101789) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [21m54s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715306039) | [21m54s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715306039) | [21m54s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715306039) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [15m52s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305969) | [15m52s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305969) | [15m52s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305969) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [14m50s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305916) | [14m50s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305916) | [14m50s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305916) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [13m44s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305746) | [13m44s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305746) | [13m44s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305746) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [12m53s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305873) | [12m53s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305873) | [12m53s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305873) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [11m15s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305939) | [11m15s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305939) | [11m15s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305939) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [9m27s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305962) | [9m27s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305962) | [9m27s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305962) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [4m56s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305979) | [4m56s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305979) | [4m56s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305979) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [4m49s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715306024) | [4m49s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715306024) | [4m49s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715306024) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [4m39s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305751) | [4m39s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305751) | [4m39s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305751) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [4m08s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305971) | [4m08s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305971) | [4m08s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305971) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m30s](https://github.com/iree-org/iree/actions/runs/27009919441/job/79710711727) | [1m30s](https://github.com/iree-org/iree/actions/runs/27009919441/job/79710711727) | [1m30s](https://github.com/iree-org/iree/actions/runs/27009919441/job/79710711727) | 1 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 1 | 0 | — | — | [1m29s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101567) | [1m29s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101567) | [1m29s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101567) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 1 | 0 | — | — | [1m28s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101578) | [1m28s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101578) | [1m28s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101578) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101786) | [9s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101786) | [9s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101786) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101762) | [8s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101762) | [8s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101762) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101806) | [8s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101806) | [8s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101806) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101729) | [7s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101729) | [7s](https://github.com/iree-org/iree/actions/runs/26999287537/job/79714101729) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305786) | [7s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305786) | [7s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305786) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305951) | [7s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305951) | [7s](https://github.com/iree-org/iree/actions/runs/26999287565/job/79715305951) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 278 | 0% (1/278) |  | 1h43m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 203 | 0% (0/203) |  | 1h54m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 197 | 1% (2/197) |  | 1h57m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 252 | 4% (10/252) |  | 1h57m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 63 | 0% (0/63) |  | 2h06m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
