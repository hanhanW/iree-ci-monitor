# iree-ci-monitor

_Updated: 2026-10-16 14:15 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [17m07s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474251) | [31m31s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474410) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [5m53s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474122) | [28m56s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474187) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [9m40s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474050) | [26m51s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474283) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [22m55s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474373) | [22m55s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474373) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474194) | [18m57s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474031) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [4m32s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474095) | [4m32s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474095) | — | `shark55-ci` |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456775) | [10s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456908) | — | 7 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456600) | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456816) | — | 3 |
| `macos-15` | github-hosted | 3 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456601) | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456612) | — | 3 |
| `ubuntu-24.04` | github-hosted | 22 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474026) | [3s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117075782759) | 100% (1/1) | 22 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456636) | [3s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456750) | — | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456874) | [2s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456874) | — | 1 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474001) | [2s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474001) | — | `shark75-ci` |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38922987677/job/117047346174) | [2s](https://github.com/iree-org/iree/actions/runs/38922987677/job/117047346284) | — | 3 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [31m31s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474410) | [31m31s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474410) | [31m31s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474410) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [28m56s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474187) | [28m56s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474187) | [28m56s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474187) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [26m51s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474283) | [26m51s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474283) | [26m51s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474283) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [22m55s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474373) | [22m55s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474373) | [22m55s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474373) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [18m57s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474031) | [18m57s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474031) | [18m57s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474031) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [17m07s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474251) | [17m07s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474251) | [17m07s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474251) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [9m40s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474050) | [9m40s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474050) | [9m40s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474050) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [5m53s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474122) | [5m53s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474122) | [5m53s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474122) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [4m32s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474095) | [4m32s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474095) | [4m32s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117057474095) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456908) | [10s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456908) | [10s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456908) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456814) | [9s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456814) | [9s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456814) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047457620) | [9s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047457620) | [9s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047457620) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456590) | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456590) | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456590) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456775) | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456775) | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456775) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456612) | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456612) | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456612) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456601) | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456601) | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456601) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456816) | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456816) | [8s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456816) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456663) | [7s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456663) | [7s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456663) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117047487946) | [6s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117047487946) | [6s](https://github.com/iree-org/iree/actions/runs/38922992316/job/117047487946) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456600) | [5s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456600) | [5s](https://github.com/iree-org/iree/actions/runs/38922992121/job/117047456600) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 309 | 6% (18/309) |  | 4h54m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 248 | 1% (2/248) |  | 5h00m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
