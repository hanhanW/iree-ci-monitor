# iree-ci-monitor

_Updated: 2026-09-07 21:43 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [34m29s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201866) | [34m29s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201866) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201842) | [28m14s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201901) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [20m38s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201822) | [20m38s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201822) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [15m08s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201844) | [19m08s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874202084) | — | `shark01-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201864) | [12m43s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201849) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [11m39s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201899) | [11m39s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201899) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [6m19s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201912) | [9m43s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201857) | — | `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [7m54s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201896) | [7m54s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201896) | — | `shark01-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [5m57s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201821) | [5m57s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201821) | — | `shark10-ci` |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [1m20s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916515) | [1m26s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916633) | — | 5 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916560) | [33s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916476) | — | 3 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916511) | [5s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916525) | — | 3 |
| `ubuntu-24.04` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874202022) | [3s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101877949997) | 0% (0/3) | 23 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916514) | [3s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916547) | — | 3 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201736) | [1s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201736) | — | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201758) | [1s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201758) | — | `shark01-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916610) | [1s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916610) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [34m29s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201866) | [34m29s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201866) | [34m29s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201866) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [28m14s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201901) | [28m14s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201901) | [28m14s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201901) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [20m38s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201822) | [20m38s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201822) | [20m38s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201822) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [19m08s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874202084) | [19m08s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874202084) | [19m08s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874202084) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [15m08s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201844) | [15m08s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201844) | [15m08s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201844) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [12m43s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201849) | [12m43s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201849) | [12m43s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201849) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [11m39s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201899) | [11m39s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201899) | [11m39s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201899) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [9m43s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201857) | [9m43s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201857) | [9m43s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201857) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [7m54s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201896) | [7m54s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201896) | [7m54s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201896) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [6m19s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201912) | [6m19s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201912) | [6m19s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201912) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [5m57s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201821) | [5m57s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201821) | [5m57s](https://github.com/iree-org/iree/actions/runs/34164543372/job/101874201821) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [1m26s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916633) | [1m26s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916633) | [1m26s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916633) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [1m20s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916515) | [1m20s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916515) | [1m20s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916515) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m20s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916680) | [1m20s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916680) | [1m20s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916680) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [33s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916476) | [33s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916476) | [33s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916476) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916517) | [8s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916517) | [8s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916517) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916560) | [7s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916560) | [7s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916560) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916453) | [6s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916453) | [6s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916453) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916525) | [5s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916525) | [5s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916525) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916511) | [5s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916511) | [5s](https://github.com/iree-org/iree/actions/runs/34164543401/job/101872916511) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 115 | 2% (2/115) |  | 6h04m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 95 | 4% (4/95) |  | 6h20m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 88 | 0% (0/88) |  | 6h22m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 76 | 0% (0/76) |  | 6h23m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
