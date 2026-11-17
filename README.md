# iree-ci-monitor

_Updated: 2026-11-17 00:00 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 5 | [7s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643762) | [1m45s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133897647183) | — | 6 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 3 | [1s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643507) | [1m30s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643455) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/44022208103/job/133834197363) | [5s](https://github.com/iree-org/iree/actions/runs/44022208103/job/133834197336) | — | 6 |
| `ubuntu-24.04` | github-hosted | 29 | 0 | — | — | 12 | [2s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643478) | [3s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780613) | 0% (0/4) | 29 |
| `macos-15` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643436) | [2s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643489) | — | 5 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780546) | [2s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780546) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 1 | [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780551) | 2026-11-17 00:00 PST | 1 | [2s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780573) | [2s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780573) | — | `shark55-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643653) | [1s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643653) | — | 1 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 1 | [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780472) | 2026-11-17 00:00 PST | 0 | 0s | 0s | — | 0 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 2 | [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780494) | 2026-11-17 00:00 PST | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201` | self-hosted | 2 | 2 | [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780520) | 2026-11-17 00:00 PST | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780530) | 2026-11-17 00:00 PST | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 2 | 2 | [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780535) | 2026-11-17 00:00 PST | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780472) | 2026-11-17 00:00 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `schuermans/split-large-constants` | pull_request |
| [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780494) | 2026-11-17 00:00 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | `schuermans/split-large-constants` | pull_request |
| [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780520) | 2026-11-17 00:00 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `schuermans/split-large-constants` | pull_request |
| [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780530) | 2026-11-17 00:00 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `schuermans/split-large-constants` | pull_request |
| [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780535) | 2026-11-17 00:00 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `schuermans/split-large-constants` | pull_request |
| [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780551) | 2026-11-17 00:00 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `schuermans/split-large-constants` | pull_request |
| [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780580) | 2026-11-17 00:00 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `schuermans/split-large-constants` | pull_request |
| [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780592) | 2026-11-17 00:00 PST | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | `schuermans/split-large-constants` | pull_request |
| [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780600) | 2026-11-17 00:00 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `schuermans/split-large-constants` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [1m45s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133897647183) | [1m45s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133897647183) | [1m45s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133897647183) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m31s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643586) | [1m31s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643586) | [1m31s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643586) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 1 | 0 | — | — | [1m30s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643455) | [1m30s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643455) | [1m30s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643455) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [1m28s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643808) | [1m28s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643808) | [1m28s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643808) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 1 | [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780472) | 2026-11-17 00:00 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 1 | [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780530) | 2026-11-17 00:00 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 1 | [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780494) | 2026-11-17 00:00 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 1 | [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780535) | 2026-11-17 00:00 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 1 | [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780520) | 2026-11-17 00:00 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 1 | [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780551) | 2026-11-17 00:00 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 1 | [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780592) | 2026-11-17 00:00 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 1 | [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780600) | 2026-11-17 00:00 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 1 | [25s](https://github.com/iree-org/iree/actions/runs/44041701890/job/133901780580) | 2026-11-17 00:00 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643762) | [7s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643762) | [7s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643762) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643670) | [6s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643670) | [6s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643670) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/44022208103/job/133834197336) | [5s](https://github.com/iree-org/iree/actions/runs/44022208103/job/133834197336) | [5s](https://github.com/iree-org/iree/actions/runs/44022208103/job/133834197336) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44022208103/job/133834197363) | [4s](https://github.com/iree-org/iree/actions/runs/44022208103/job/133834197363) | [4s](https://github.com/iree-org/iree/actions/runs/44022208103/job/133834197363) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643482) | [4s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643482) | [4s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643482) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643587) | [4s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643587) | [4s](https://github.com/iree-org/iree/actions/runs/44041701709/job/133897643587) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/44022208103/job/133834197385) | [3s](https://github.com/iree-org/iree/actions/runs/44022208103/job/133834197385) | [3s](https://github.com/iree-org/iree/actions/runs/44022208103/job/133834197385) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 340 | 1% (4/339) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 401 | 0% (2/400) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
