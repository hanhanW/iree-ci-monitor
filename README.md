# iree-ci-monitor

_Updated: 2026-10-06 23:06 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [16m14s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516633) | [19m10s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516653) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [3m55s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516355) | [13m34s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516474) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [10m53s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516499) | [10m53s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516499) | — | `shark75-ci` |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267801) | [1m33s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267626) | — | 6 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [7s](https://github.com/iree-org/iree/actions/runs/37575593559/job/112643708539) | [9s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267487) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267454) | [5s](https://github.com/iree-org/iree/actions/runs/37575593559/job/112643708498) | — | 6 |
| `ubuntu-24.04` | github-hosted | 30 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/37571478656/job/112630872273) | [3s](https://github.com/iree-org/iree/actions/runs/37575593559/job/112643708610) | 0% (0/4) | 29 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267510) | [3s](https://github.com/iree-org/iree/actions/runs/37575593559/job/112643708413) | — | 5 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516255) | [1s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516255) | — | `shark75-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267652) | [1s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267652) | — | 1 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 6 | [15h52m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313472) | 2026-10-06 23:06 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 6 | 6 | [15h52m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313612) | 2026-10-06 23:06 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 12 | 12 | [15h52m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313832) | 2026-10-06 23:06 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 12 | 12 | [15h52m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313855) | 2026-10-06 23:06 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [15h52m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313472) | 2026-10-06 23:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [15h52m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313612) | 2026-10-06 23:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [15h52m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313832) | 2026-10-06 23:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [15h52m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313855) | 2026-10-06 23:06 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [15h52m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313864) | 2026-10-06 23:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [15h52m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313928) | 2026-10-06 23:06 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [15h41m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051077) | 2026-10-06 23:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [15h41m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051248) | 2026-10-06 23:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [15h41m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051249) | 2026-10-06 23:06 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [15h41m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051272) | 2026-10-06 23:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [15h41m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051325) | 2026-10-06 23:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [15h41m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051395) | 2026-10-06 23:06 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [15h36m](https://github.com/iree-org/iree/actions/runs/37477997055/job/112323157558) | 2026-10-06 23:06 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [15h36m](https://github.com/iree-org/iree/actions/runs/37477997055/job/112323157752) | 2026-10-06 23:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [15h36m](https://github.com/iree-org/iree/actions/runs/37477997055/job/112323157820) | 2026-10-06 23:06 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 6 | [15h52m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313472) | 2026-10-06 23:06 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 6 | 6 | [15h52m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313612) | 2026-10-06 23:06 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 6 | [15h52m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313864) | 2026-10-06 23:06 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 6 | [15h52m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313832) | 2026-10-06 23:06 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 6 | [15h52m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313855) | 2026-10-06 23:06 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 6 | [15h52m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313928) | 2026-10-06 23:06 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [19m10s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516653) | [19m10s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516653) | [19m10s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516653) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [16m14s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516633) | [16m14s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516633) | [16m14s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516633) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [13m34s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516474) | [13m34s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516474) | [13m34s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516474) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [10m53s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516499) | [10m53s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516499) | [10m53s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516499) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [3m55s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516355) | [3m55s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516355) | [3m55s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516355) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [1m33s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267626) | [1m33s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267626) | [1m33s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267626) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m04s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267733) | [1m04s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267733) | [1m04s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267733) | 1 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 1 | 0 | — | — | [38s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516391) | [38s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516391) | [38s](https://github.com/iree-org/iree/actions/runs/37556930700/job/112587516391) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267607) | [9s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267607) | [9s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267607) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267487) | [9s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267487) | [9s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267487) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37575593559/job/112643708463) | [8s](https://github.com/iree-org/iree/actions/runs/37575593559/job/112643708463) | [8s](https://github.com/iree-org/iree/actions/runs/37575593559/job/112643708463) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267801) | [8s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267801) | [8s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267801) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37575593559/job/112643708539) | [7s](https://github.com/iree-org/iree/actions/runs/37575593559/job/112643708539) | [7s](https://github.com/iree-org/iree/actions/runs/37575593559/job/112643708539) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267669) | [7s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267669) | [7s](https://github.com/iree-org/iree/actions/runs/37556930774/job/112585267669) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 337 | 0% (1/337) |  | 4h05m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 91 | 0% (0/91) |  | 6d09h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 15h52m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 15h52m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 15h52m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 15h52m (> 2h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
