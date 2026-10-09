# iree-ci-monitor

_Updated: 2026-10-09 15:42 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [16m18s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175141) | [17m15s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175149) | — | `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [14m09s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175120) | [14m09s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175120) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [13m32s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175007) | [13m32s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175007) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2m45s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175138) | [8m47s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903174943) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [7m05s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175153) | [7m05s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175153) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175034) | [5m53s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175401) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [1m34s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175277) | [4m46s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175181) | — | `shark75-ci` |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083352) | [9s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083663) | — | 6 |
| `macos-15` | github-hosted | 3 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083151) | [7s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083181) | — | 3 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083171) | [5s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083176) | — | 3 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083213) | [4s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083198) | — | 3 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/37953772125/job/113898973183) | [4s](https://github.com/iree-org/iree/actions/runs/37953772125/job/113898972534) | — | 3 |
| `ubuntu-24.04` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899082896) | [2s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175184) | 50% (1/2) | 24 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175064) | [1s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175064) | — | `shark75-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083976) | [1s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083976) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [17m15s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175149) | [17m15s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175149) | [17m15s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175149) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [16m18s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175141) | [16m18s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175141) | [16m18s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175141) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 1 | 0 | — | — | [14m09s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175120) | [14m09s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175120) | [14m09s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175120) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [13m32s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175007) | [13m32s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175007) | [13m32s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175007) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [8m47s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903174943) | [8m47s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903174943) | [8m47s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903174943) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [7m05s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175153) | [7m05s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175153) | [7m05s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175153) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [5m53s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175401) | [5m53s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175401) | [5m53s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175401) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [4m46s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175181) | [4m46s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175181) | [4m46s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175181) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [2m45s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175138) | [2m45s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175138) | [2m45s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175138) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [1m34s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175277) | [1m34s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175277) | [1m34s](https://github.com/iree-org/iree/actions/runs/37953778162/job/113903175277) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083455) | [9s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083455) | [9s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083455) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083663) | [9s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083663) | [9s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083663) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083563) | [8s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083563) | [8s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083563) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083352) | [7s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083352) | [7s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083352) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083181) | [7s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083181) | [7s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083181) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083151) | [7s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083151) | [7s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083151) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083564) | [6s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083564) | [6s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083564) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083053) | [6s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083053) | [6s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083053) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083171) | [5s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083171) | [5s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083171) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083176) | [5s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083176) | [5s](https://github.com/iree-org/iree/actions/runs/37953777798/job/113899083176) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 219 | 15% (33/219) |  | 6h27m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 370 | 0% (1/370) |  | 6h32m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
