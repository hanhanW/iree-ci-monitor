# iree-ci-monitor

_Updated: 2026-08-05 20:42 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [16m34s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542920) | [17m32s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542908) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [12m23s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542977) | [16m57s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542899) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [16m36s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542885) | [16m36s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542885) | — | `shark01-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [13m20s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542831) | [13m20s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542831) | — | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [4m01s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542995) | [11m25s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426543090) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [9m34s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542833) | [9m34s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542833) | — | `shark01-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [5m36s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542839) | [5m36s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542839) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [5m32s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542782) | [5m32s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542782) | — | `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 21 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258816) | [9s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542749) | — | 20 |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258937) | [8s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424259027) | — | 5 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258678) | [3s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258902) | — | 3 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258673) | [3s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258888) | — | 3 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258686) | [2s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258805) | — | 3 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542769) | [2s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542812) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542771) | [2s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542771) | — | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542772) | [2s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542772) | — | `shark75-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258942) | [1s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258942) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [17m32s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542908) | [17m32s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542908) | [17m32s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542908) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [16m57s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542899) | [16m57s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542899) | [16m57s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542899) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [16m36s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542885) | [16m36s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542885) | [16m36s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542885) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [16m34s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542920) | [16m34s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542920) | [16m34s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542920) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [13m20s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542831) | [13m20s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542831) | [13m20s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542831) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [12m23s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542977) | [12m23s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542977) | [12m23s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542977) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [11m25s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426543090) | [11m25s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426543090) | [11m25s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426543090) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [9m34s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542833) | [9m34s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542833) | [9m34s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542833) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [5m36s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542839) | [5m36s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542839) | [5m36s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542839) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [5m32s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542782) | [5m32s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542782) | [5m32s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542782) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [4m01s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542995) | [4m01s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542995) | [4m01s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542995) | 1 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 1 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542865) | [11s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542865) | [11s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542865) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258713) | [9s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258713) | [9s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258713) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258659) | [9s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258659) | [9s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258659) | 1 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542749) | [9s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542749) | [9s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92426542749) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424259015) | [8s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424259015) | [8s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424259015) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258937) | [8s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258937) | [8s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424258937) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424259027) | [8s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424259027) | [8s](https://github.com/iree-org/iree/actions/runs/31036221789/job/92424259027) | 1 |
| `.github/workflows/clang_tidy.yml` | clang-tidy | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31036221592/job/92424208311) | [8s](https://github.com/iree-org/iree/actions/runs/31036221592/job/92424208311) | [8s](https://github.com/iree-org/iree/actions/runs/31036221592/job/92424208311) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92433771679) | [8s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92433771679) | [8s](https://github.com/iree-org/iree/actions/runs/31036222014/job/92433771679) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 119 | 0% (0/119) |  | 7h21m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 103 | 2% (2/103) |  | 7h21m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 93 | 1% (1/93) |  | 7h26m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 90 | 0% (0/90) |  | 7h26m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 17 | 0% (0/17) |  | 2d14h ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
