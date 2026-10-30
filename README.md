# iree-ci-monitor

_Updated: 2026-10-29 22:55 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 1 | [4m30s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236630) | [4m30s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236630) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 1 | [1m28s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236615) | [3m09s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236601) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 1 | [5m38s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236682) | 2026-10-29 22:55 PDT | 0 | [1m53s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236637) | [1m53s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236637) | — | `shark55-ci` |
| `macos-15` | github-hosted | 5 | 0 | — | — | 1 | [9s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949392) | [1m27s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949544) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/41007051985/job/123904281302) | [1m04s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949522) | — | 6 |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 5 | [12s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949686) | [14s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123912952818) | — | 6 |
| `ubuntu-24.04` | github-hosted | 34 | 0 | — | — | 4 | [2s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949304) | [3s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236868) | 0% (0/9) | 34 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949518) | [3s](https://github.com/iree-org/iree/actions/runs/41007051985/job/123904281359) | — | 5 |
| `Linux,X64,gfx1100` | self-hosted | 2 | 1 | [5m38s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236771) | 2026-10-29 22:55 PDT | 0 | [2s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236594) | [2s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236594) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 1 | [5m38s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236749) | 2026-10-29 22:55 PDT | 0 | [2s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236638) | [2s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236638) | — | `shark75-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949667) | [1s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949667) | — | 1 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 1 | [5m38s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236724) | 2026-10-29 22:55 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [5m38s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236742) | 2026-10-29 22:55 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [5m38s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236682) | 2026-10-29 22:55 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/yalong/register-restructure-non-constant-axes` | pull_request |
| [5m38s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236724) | 2026-10-29 22:55 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/yalong/register-restructure-non-constant-axes` | pull_request |
| [5m38s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236742) | 2026-10-29 22:55 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `users/yalong/register-restructure-non-constant-axes` | pull_request |
| [5m38s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236749) | 2026-10-29 22:55 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `users/yalong/register-restructure-non-constant-axes` | pull_request |
| [5m38s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236771) | 2026-10-29 22:55 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/yalong/register-restructure-non-constant-axes` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 1 | [5m38s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236724) | 2026-10-29 22:55 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 1 | [5m38s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236742) | 2026-10-29 22:55 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 1 | [5m38s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236771) | 2026-10-29 22:55 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 1 | [5m38s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236749) | 2026-10-29 22:55 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 1 | [5m38s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236682) | 2026-10-29 22:55 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [4m30s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236630) | [4m30s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236630) | [4m30s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236630) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [3m09s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236601) | [3m09s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236601) | [3m09s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236601) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [1m53s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236637) | [1m53s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236637) | [1m53s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236637) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [1m28s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236615) | [1m28s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236615) | [1m28s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236615) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 1 | 0 | — | — | [1m27s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949544) | [1m27s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949544) | [1m27s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949544) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 1 | 0 | — | — | [1m23s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949437) | [1m23s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949437) | [1m23s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949437) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1m04s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949522) | [1m04s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949522) | [1m04s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949522) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [14s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123912952818) | [14s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123912952818) | [14s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123912952818) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [13s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949650) | [13s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949650) | [13s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949650) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [13s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912950052) | [13s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912950052) | [13s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912950052) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949686) | [12s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949686) | [12s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949686) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949604) | [10s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949604) | [10s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949604) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/41007051985/job/123904281385) | [9s](https://github.com/iree-org/iree/actions/runs/41007051985/job/123904281385) | [9s](https://github.com/iree-org/iree/actions/runs/41007051985/job/123904281385) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949392) | [9s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949392) | [9s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949392) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949536) | [9s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949536) | [9s](https://github.com/iree-org/iree/actions/runs/41007453988/job/123912949536) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 233 | 2% (5/232) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 280 | 1% (4/279) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
