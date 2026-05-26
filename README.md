# iree-ci-monitor

_Updated: 2026-05-26 00:32 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [10m32s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639658) | [20m39s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639733) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [19m44s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639652) | [19m44s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639652) | — | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [13m28s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639641) | [13m28s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639641) | — | `shark01-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [5m19s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639760) | [13m13s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639680) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [8m41s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639757) | [9m13s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639666) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [5m59s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639667) | [5m59s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639667) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639678) | [4m33s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639648) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [4m11s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639670) | [4m11s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639670) | — | `shark01-ci` |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [12s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951914) | [25s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77801955744) | — | 5 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639755) | [7s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639817) | — | 4 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26436121568/job/77819292669) | [3s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951848) | — | 5 |
| `ubuntu-24.04` | github-hosted | 34 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639606) | [2s](https://github.com/iree-org/iree/actions/runs/26436121568/job/77819292763) | 40% (2/5) | 34 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951861) | [2s](https://github.com/iree-org/iree/actions/runs/26436121568/job/77819292730) | — | 6 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951884) | [2s](https://github.com/iree-org/iree/actions/runs/26436121568/job/77819292695) | — | 5 |
| `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26430106863/job/77801415968) | [2s](https://github.com/iree-org/iree/actions/runs/26430106863/job/77801415968) | 0% (0/1) | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639612) | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639612) | — | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639632) | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639632) | — | `shark75-ci` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639634) | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639634) | — | 1 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639644) | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639644) | — | `iree-mi308-1` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639699) | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639699) | — | `shark01-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951927) | [1s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951927) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [20m39s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639733) | [20m39s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639733) | [20m39s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639733) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [19m44s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639652) | [19m44s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639652) | [19m44s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639652) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [13m28s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639641) | [13m28s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639641) | [13m28s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639641) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [13m13s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639680) | [13m13s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639680) | [13m13s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639680) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [10m32s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639658) | [10m32s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639658) | [10m32s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639658) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [9m13s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639666) | [9m13s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639666) | [9m13s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639666) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [8m41s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639757) | [8m41s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639757) | [8m41s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639757) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [5m59s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639667) | [5m59s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639667) | [5m59s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639667) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [5m19s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639760) | [5m19s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639760) | [5m19s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639760) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [4m33s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639648) | [4m33s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639648) | [4m33s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639648) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [4m11s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639670) | [4m11s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639670) | [4m11s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639670) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [25s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77801955744) | [25s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77801955744) | [25s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77801955744) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951914) | [12s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951914) | [12s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951914) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951948) | [12s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951948) | [12s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951948) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951909) | [10s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951909) | [10s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951909) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639817) | [7s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639817) | [7s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639817) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639755) | [7s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639755) | [7s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639755) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639657) | [6s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639657) | [6s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639657) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26436121568/job/77819292654) | [3s](https://github.com/iree-org/iree/actions/runs/26436121568/job/77819292654) | [3s](https://github.com/iree-org/iree/actions/runs/26436121568/job/77819292654) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951848) | [3s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951848) | [3s](https://github.com/iree-org/iree/actions/runs/26430274091/job/77801951848) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 284 | 7% (20/283) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 306 | 2% (7/305) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 226 | 1% (2/225) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 236 | 4% (9/235) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 75 | 3% (2/75) |  | 3h54m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
