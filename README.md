# iree-ci-monitor

_Updated: 2026-09-28 16:19 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [7m55s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279857) | [19m34s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154280242) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [14m23s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154280095) | [17m33s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279946) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279888) | [16m11s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154280087) | — | `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [13m03s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279843) | [13m03s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279843) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279815) | [11m30s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279926) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [7m41s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279678) | [7m41s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279678) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [5m39s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279806) | [5m39s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279806) | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [5m12s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279889) | [5m12s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279889) | — | `shark75-ci` |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833213) | [10s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833284) | — | 3 |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833802) | [8s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109151842539) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833216) | [6s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833242) | — | 3 |
| `ubuntu-latest` | github-hosted | 13 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36451633964/job/109027571212) | [4s](https://github.com/iree-org/iree/actions/runs/36451633678/job/109027571578) | 0% (0/1) | 13 |
| `ubuntu-24.04` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279981) | [3s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279939) | 50% (1/2) | 23 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833146) | [2s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833147) | — | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833775) | [1s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833775) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [19m34s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154280242) | [19m34s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154280242) | [19m34s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154280242) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [17m33s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279946) | [17m33s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279946) | [17m33s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279946) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [16m11s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154280087) | [16m11s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154280087) | [16m11s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154280087) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [14m23s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154280095) | [14m23s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154280095) | [14m23s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154280095) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 1 | 0 | — | — | [13m03s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279843) | [13m03s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279843) | [13m03s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279843) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [11m30s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279926) | [11m30s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279926) | [11m30s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279926) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [7m55s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279857) | [7m55s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279857) | [7m55s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279857) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [7m41s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279678) | [7m41s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279678) | [7m41s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279678) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [5m39s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279806) | [5m39s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279806) | [5m39s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279806) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [5m12s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279889) | [5m12s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279889) | [5m12s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109154279889) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833284) | [10s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833284) | [10s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833284) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833948) | [8s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833948) | [8s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833948) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833802) | [8s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833802) | [8s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833802) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109151842539) | [8s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109151842539) | [8s](https://github.com/iree-org/iree/actions/runs/36488686361/job/109151842539) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833649) | [7s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833649) | [7s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833649) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833105) | [6s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833105) | [6s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833105) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833213) | [6s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833213) | [6s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833213) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833242) | [6s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833242) | [6s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833242) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151832987) | [5s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151832987) | [5s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151832987) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833216) | [5s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833216) | [5s](https://github.com/iree-org/iree/actions/runs/36488686101/job/109151833216) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 254 | 4% (10/254) |  | 54m53s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 339 | 1% (5/339) |  | 58m41s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
