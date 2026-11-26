# iree-ci-monitor

_Updated: 2026-11-26 13:39 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [8m23s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567594) | [36m39s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567467) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [4m22s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567330) | [29m18s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567462) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [23m51s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567550) | [26m52s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567373) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [19m36s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567451) | [19m36s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567451) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567235) | [14m30s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567465) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [9m01s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567454) | [9m01s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567454) | — | `shark55-ci` |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [20s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620686) | [3m49s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140160638198) | — | 6 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620701) | [4s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620751) | — | 3 |
| `ubuntu-24.04` | github-hosted | 22 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620410) | [3s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567445) | — | 22 |
| `macos-15` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620731) | [2s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620759) | — | 3 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567247) | [2s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567247) | — | `shark75-ci` |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620728) | [1s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160621271) | — | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620988) | [1s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620988) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [36m39s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567467) | [36m39s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567467) | [36m39s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567467) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [29m18s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567462) | [29m18s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567462) | [29m18s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567462) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [26m52s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567373) | [26m52s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567373) | [26m52s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567373) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [23m51s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567550) | [23m51s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567550) | [23m51s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567550) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [19m36s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567451) | [19m36s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567451) | [19m36s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567451) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [14m30s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567465) | [14m30s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567465) | [14m30s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567465) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [9m01s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567454) | [9m01s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567454) | [9m01s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567454) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [8m23s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567594) | [8m23s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567594) | [8m23s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567594) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [4m22s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567330) | [4m22s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567330) | [4m22s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567330) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [3m49s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140160638198) | [3m49s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140160638198) | [3m49s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140160638198) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m16s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620937) | [1m16s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620937) | [1m16s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620937) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [26s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160621001) | [26s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160621001) | [26s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160621001) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [20s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620686) | [20s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620686) | [20s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620686) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160621013) | [7s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160621013) | [7s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160621013) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620524) | [4s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620524) | [4s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620524) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620751) | [4s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620751) | [4s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620751) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620701) | [4s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620701) | [4s](https://github.com/iree-org/iree/actions/runs/45877362554/job/140160620701) | 1 |
| `.github/workflows/clang_tidy.yml` | clang-tidy | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/45877362390/job/140160531804) | [3s](https://github.com/iree-org/iree/actions/runs/45877362390/job/140160531804) | [3s](https://github.com/iree-org/iree/actions/runs/45877362390/job/140160531804) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567371) | [3s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567371) | [3s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567371) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567444) | [3s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567444) | [3s](https://github.com/iree-org/iree/actions/runs/45877362451/job/140164567444) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 60 | 12% (7/60) |  | 2m19s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 83 | 6% (5/83) |  | 8m44s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
