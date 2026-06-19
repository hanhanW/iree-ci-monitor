# iree-ci-monitor

_Updated: 2026-06-18 18:34 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [16m23s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204213) | [21m46s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204203) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [20m31s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204164) | [20m31s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204164) | — | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [13m53s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204183) | [19m48s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204115) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [14m56s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204137) | [14m56s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204137) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [8m42s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204159) | [10m34s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204208) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204117) | [8m51s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204200) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [7m53s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204119) | [7m53s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204119) | — | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [4m50s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204184) | [4m50s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204184) | — | `shark10-ci` |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 1 | [9s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231735007) | [1m32s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231735011) | — | 5 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204166) | [8s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204211) | — | 4 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734913) | [6s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734918) | — | 3 |
| `ubuntu-24.04` | github-hosted | 19 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204122) | [3s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204233) | — | 19 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734933) | [3s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734962) | — | 3 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204113) | [2s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204113) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204134) | [2s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204134) | — | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204173) | [2s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204173) | — | `shark01-ci` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204198) | [2s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204198) | — | 1 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204231) | [2s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204231) | — | `iree-mi308-1` |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734908) | [2s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734922) | — | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231735003) | [1s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231735003) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [21m46s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204203) | [21m46s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204203) | [21m46s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204203) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [20m31s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204164) | [20m31s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204164) | [20m31s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204164) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [19m48s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204115) | [19m48s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204115) | [19m48s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204115) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [16m23s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204213) | [16m23s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204213) | [16m23s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204213) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [14m56s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204137) | [14m56s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204137) | [14m56s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204137) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [13m53s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204183) | [13m53s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204183) | [13m53s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204183) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [10m34s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204208) | [10m34s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204208) | [10m34s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204208) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [8m51s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204200) | [8m51s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204200) | [8m51s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204200) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [8m42s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204159) | [8m42s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204159) | [8m42s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204159) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [7m53s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204119) | [7m53s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204119) | [7m53s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204119) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [4m50s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204184) | [4m50s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204184) | [4m50s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204184) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m32s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231735011) | [1m32s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231735011) | [1m32s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231735011) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [13s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734996) | [13s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734996) | [13s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734996) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231735007) | [9s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231735007) | [9s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231735007) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204095) | [8s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204095) | [8s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204095) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204211) | [8s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204211) | [8s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204211) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204166) | [8s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204166) | [8s](https://github.com/iree-org/iree/actions/runs/27782623047/job/82233204166) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734918) | [6s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734918) | [6s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734918) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734878) | [5s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734878) | [5s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734878) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734913) | [5s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734913) | [5s](https://github.com/iree-org/iree/actions/runs/27782621469/job/82231734913) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 143 | 0% (0/143) |  | 4h01m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 102 | 0% (0/102) |  | 4h01m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 108 | 6% (6/108) |  | 4h06m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 116 | 0% (0/116) |  | 4h08m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 32 | 0% (0/32) |  | 4h21m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
