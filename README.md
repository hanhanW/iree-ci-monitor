# iree-ci-monitor

_Updated: 2026-07-27 00:28 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 1 | [9m10s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992216) | [9m10s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992216) | — | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 2 | [6m16s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992376) | [7m51s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992462) | — | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992327) | [6m09s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992437) | — | `shark01-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [4m39s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992349) | [4m39s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992349) | — | `shark10-ci` |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 4 | [1m33s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293565) | [2m21s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89910298712) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293403) | [1m10s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293450) | — | 6 |
| `ubuntu-24.04` | github-hosted | 27 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992418) | [4s](https://github.com/iree-org/iree/actions/runs/30239628748/job/89895625979) | 0% (0/4) | 27 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293417) | [3s](https://github.com/iree-org/iree/actions/runs/30241943964/job/89900888113) | — | 5 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293470) | [3s](https://github.com/iree-org/iree/actions/runs/30241943964/job/89900888094) | — | 5 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992171) | [2s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992171) | — | 1 |
| `Linux,X64,rdna3` | self-hosted | 2 | 1 | [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992405) | 2026-07-27 00:28 PDT | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992285) | [2s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992285) | — | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992318) | [2s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992318) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992375) | [2s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992375) | — | `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992409) | [2s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992409) | — | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293536) | [1s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293536) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 1 | [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992231) | 2026-07-27 00:28 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 1 | [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992271) | 2026-07-27 00:28 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201` | self-hosted | 2 | 2 | [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992310) | 2026-07-27 00:28 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 1 | [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992390) | 2026-07-27 00:28 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992231) | 2026-07-27 00:28 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `fix/dynamic-argsort-stack-allocation` | pull_request |
| [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992271) | 2026-07-27 00:28 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `fix/dynamic-argsort-stack-allocation` | pull_request |
| [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992310) | 2026-07-27 00:28 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `fix/dynamic-argsort-stack-allocation` | pull_request |
| [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992390) | 2026-07-27 00:28 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `fix/dynamic-argsort-stack-allocation` | pull_request |
| [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992405) | 2026-07-27 00:28 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `fix/dynamic-argsort-stack-allocation` | pull_request |
| [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992472) | 2026-07-27 00:28 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `fix/dynamic-argsort-stack-allocation` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 1 | [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992271) | 2026-07-27 00:28 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 1 | [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992231) | 2026-07-27 00:28 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 1 | [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992390) | 2026-07-27 00:28 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 1 | [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992472) | 2026-07-27 00:28 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 1 | [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992405) | 2026-07-27 00:28 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 1 | [10m27s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992310) | 2026-07-27 00:28 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [9m10s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992216) | [9m10s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992216) | [9m10s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992216) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [7m51s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992462) | [7m51s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992462) | [7m51s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992462) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [6m16s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992376) | [6m16s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992376) | [6m16s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992376) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [6m09s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992437) | [6m09s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992437) | [6m09s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992437) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [4m39s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992349) | [4m39s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992349) | [4m39s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992349) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [2m21s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89910298712) | [2m21s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89910298712) | [2m21s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89910298712) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [1m53s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293824) | [1m53s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293824) | [1m53s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293824) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [1m33s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293565) | [1m33s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293565) | [1m33s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293565) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 1 | 0 | — | — | [1m20s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293473) | [1m20s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293473) | [1m20s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293473) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1m10s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293450) | [1m10s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293450) | [1m10s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293450) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [14s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293477) | [14s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293477) | [14s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293477) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293415) | [4s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293415) | [4s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293415) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/30239628748/job/89895625979) | [4s](https://github.com/iree-org/iree/actions/runs/30239628748/job/89895625979) | [4s](https://github.com/iree-org/iree/actions/runs/30239628748/job/89895625979) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30241943964/job/89900888094) | [3s](https://github.com/iree-org/iree/actions/runs/30241943964/job/89900888094) | [3s](https://github.com/iree-org/iree/actions/runs/30241943964/job/89900888094) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 303 | 5% (14/302) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 283 | 1% (2/282) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 271 | 1% (3/270) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 370 | 1% (5/369) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 85 | 2% (2/85) |  | 2m21s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
