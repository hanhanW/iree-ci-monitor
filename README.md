# iree-ci-monitor

_Updated: 2026-09-29 15:20 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [16m42s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459318) | [2h23m](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892764) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [22m52s](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892642) | [1h32m](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892786) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [10m51s](https://github.com/iree-org/iree/actions/runs/36606098587/job/109538342476) | [1h24m](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892714) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [6m24s](https://github.com/iree-org/iree/actions/runs/36606098587/job/109538342532) | [1h02m](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892460) | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [17m04s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459251) | [27m44s](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892362) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [13m11s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459144) | [25m22s](https://github.com/iree-org/iree/actions/runs/36606098587/job/109538342426) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [9m17s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459075) | [17m05s](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892520) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [2m57s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459252) | [9m59s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459220) | — | `shark55-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 15 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/36590684833/job/109483927111) | [26s](https://github.com/iree-org/iree/actions/runs/36570441486/job/109412923499) | — | 15 |
| `macos-14` | github-hosted | 9 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/36590684833/job/109483926623) | [11s](https://github.com/iree-org/iree/actions/runs/36606098442/job/109535472003) | — | 9 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/36590684833/job/109483926551) | [6s](https://github.com/iree-org/iree/actions/runs/36606098442/job/109535472034) | — | 9 |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36590684833/job/109483926491) | [5s](https://github.com/iree-org/iree/actions/runs/36606098442/job/109535472017) | — | 9 |
| `ubuntu-24.04` | github-hosted | 72 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892624) | [4s](https://github.com/iree-org/iree/actions/runs/36606098587/job/109538342345) | — | 72 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/36590677602/job/109482649796) | [3s](https://github.com/iree-org/iree/actions/runs/36590677602/job/109482650013) | — | 3 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/36590684833/job/109483927147) | [2s](https://github.com/iree-org/iree/actions/runs/36606098442/job/109535472218) | — | 3 |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [21m59s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459694) | [2h23m](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892764) | [2h23m](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892764) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [16m42s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459318) | [2h15m](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892589) | [2h15m](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892589) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [32m26s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459793) | [1h32m](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892786) | [1h32m](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892786) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [14m31s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459991) | [1h24m](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892714) | [1h24m](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892714) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [6m24s](https://github.com/iree-org/iree/actions/runs/36606098587/job/109538342532) | [1h02m](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892460) | [1h02m](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892460) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [10m51s](https://github.com/iree-org/iree/actions/runs/36606098587/job/109538342476) | [50m31s](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892732) | [50m31s](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892732) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [17m04s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459251) | [27m44s](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892362) | [27m44s](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892362) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 3 | 0 | — | — | [13m11s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459144) | [25m22s](https://github.com/iree-org/iree/actions/runs/36606098587/job/109538342426) | [25m22s](https://github.com/iree-org/iree/actions/runs/36606098587/job/109538342426) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [22m52s](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892642) | [25m02s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459489) | [25m02s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459489) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [9m17s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459075) | [17m05s](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892520) | [17m05s](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892520) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [2m46s](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892645) | [9m59s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459220) | [9m59s](https://github.com/iree-org/iree/actions/runs/36590684245/job/109487459220) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [8m44s](https://github.com/iree-org/iree/actions/runs/36570441286/job/109415892703) | [8m55s](https://github.com/iree-org/iree/actions/runs/36606098587/job/109538342516) | [8m55s](https://github.com/iree-org/iree/actions/runs/36606098587/job/109538342516) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 3 | 0 | — | — | [26s](https://github.com/iree-org/iree/actions/runs/36570441486/job/109412923499) | [31s](https://github.com/iree-org/iree/actions/runs/36606098442/job/109535472451) | [31s](https://github.com/iree-org/iree/actions/runs/36606098442/job/109535472451) | 3 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36590684833/job/109483927111) | [26s](https://github.com/iree-org/iree/actions/runs/36570441486/job/109412923354) | [26s](https://github.com/iree-org/iree/actions/runs/36570441486/job/109412923354) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 3 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/36590684833/job/109483927357) | [20s](https://github.com/iree-org/iree/actions/runs/36606098442/job/109535472334) | [20s](https://github.com/iree-org/iree/actions/runs/36606098442/job/109535472334) | 3 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 3 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36606098587/job/109535471055) | [13s](https://github.com/iree-org/iree/actions/runs/36570441286/job/109413116080) | [13s](https://github.com/iree-org/iree/actions/runs/36570441286/job/109413116080) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36570441486/job/109412923222) | [11s](https://github.com/iree-org/iree/actions/runs/36606098442/job/109535472003) | [11s](https://github.com/iree-org/iree/actions/runs/36606098442/job/109535472003) | 3 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 3 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/36606098442/job/109535471884) | [10s](https://github.com/iree-org/iree/actions/runs/36590684833/job/109483926508) | [10s](https://github.com/iree-org/iree/actions/runs/36590684833/job/109483926508) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36590684833/job/109483927033) | [8s](https://github.com/iree-org/iree/actions/runs/36606098442/job/109535472390) | [8s](https://github.com/iree-org/iree/actions/runs/36606098442/job/109535472390) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 3 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36590684833/job/109483926623) | [8s](https://github.com/iree-org/iree/actions/runs/36606098442/job/109535471954) | [8s](https://github.com/iree-org/iree/actions/runs/36606098442/job/109535471954) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 391 | 2% (6/391) |  | 4h09m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 297 | 4% (13/297) |  | 4h17m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h24m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h23m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
