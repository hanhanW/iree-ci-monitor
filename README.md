# iree-ci-monitor

_Updated: 2026-10-26 22:11 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [14m01s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873651175) | [21m26s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650986) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [19m54s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650883) | [19m54s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650883) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [15m58s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650478) | [15m58s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650478) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650853) | [8m09s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650942) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2m27s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650920) | [7m36s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650817) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [5m12s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650810) | [5m12s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650810) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650890) | [2m25s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873651011) | — | `shark55-ci` |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012722) | [9s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012912) | — | 6 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870013031) | [5s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870013082) | — | 3 |
| `macos-15` | github-hosted | 4 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012625) | [3s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012947) | — | 4 |
| `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/40406662286/job/121866059753) | [3s](https://github.com/iree-org/iree/actions/runs/40406662286/job/121866059753) | 0% (0/1) | 1 |
| `ubuntu-24.04` | github-hosted | 26 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650834) | [2s](https://github.com/iree-org/iree/actions/runs/40449411942/job/122010998376) | 0% (0/3) | 25 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012708) | [2s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012796) | — | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870013229) | [1s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870013229) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [21m26s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650986) | [21m26s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650986) | [21m26s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650986) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [19m54s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650883) | [19m54s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650883) | [19m54s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650883) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [15m58s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650478) | [15m58s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650478) | [15m58s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650478) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [14m01s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873651175) | [14m01s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873651175) | [14m01s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873651175) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [8m09s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650942) | [8m09s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650942) | [8m09s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650942) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [7m36s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650817) | [7m36s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650817) | [7m36s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650817) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [5m12s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650810) | [5m12s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650810) | [5m12s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650810) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [2m27s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650920) | [2m27s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650920) | [2m27s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873650920) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [2m25s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873651011) | [2m25s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873651011) | [2m25s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121873651011) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012837) | [9s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012837) | [9s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012837) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012912) | [9s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012912) | [9s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012912) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012722) | [8s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012722) | [8s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012722) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012927) | [8s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012927) | [8s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012927) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012785) | [7s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012785) | [7s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012785) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40407790045/job/121883706641) | [6s](https://github.com/iree-org/iree/actions/runs/40380420062/job/121800890284) | [6s](https://github.com/iree-org/iree/actions/runs/40380420062/job/121800890284) | 2 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870013082) | [5s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870013082) | [5s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870013082) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870013031) | [4s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870013031) | [4s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870013031) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012666) | [4s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012666) | [4s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012666) | 1 |
| `.github/workflows/ci.yml` | macos_arm64_clang / macos_arm64_clang | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012947) | [3s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012947) | [3s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012947) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012625) | [3s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012625) | [3s](https://github.com/iree-org/iree/actions/runs/40407790130/job/121870012625) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 302 | 0% (0/302) |  | 6h49m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 243 | 3% (7/243) |  | 6h53m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
