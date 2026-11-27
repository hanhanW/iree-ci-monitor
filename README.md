# iree-ci-monitor

_Updated: 2026-11-27 13:24 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [4h40m](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581969093) | [5h17m](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581969561) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [4h51m](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581969119) | [5h11m](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581969363) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [3h45m](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619233828) | [4h22m](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581968873) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [8m36s](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619233958) | [16m28s](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581969360) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [12m21s](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581968741) | [15m59s](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619233857) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581968770) | [14m36s](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619233824) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619233681) | [13m59s](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581968420) | — | `shark75-ci` |
| `azure-linux-scale` | ossci | 12 | 0 | — | — | 0 | [1m23s](https://github.com/iree-org/iree/actions/runs/46020053502/job/140577307828) | [2m20s](https://github.com/iree-org/iree/actions/runs/46029992315/job/140611556685) | — | 12 |
| `ubuntu-24.04` | github-hosted | 91 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/46029992471/job/140611547984) | [1m07s](https://github.com/iree-org/iree/actions/runs/46029992516/job/140611662556) | — | 66 |
| `macos-15` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/46020053502/job/140577307565) | [1m02s](https://github.com/iree-org/iree/actions/runs/46029992315/job/140611556592) | — | 6 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/46020053502/job/140577307615) | [16s](https://github.com/iree-org/iree/actions/runs/46029992315/job/140611556714) | — | 6 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/46020053502/job/140577307524) | [10s](https://github.com/iree-org/iree/actions/runs/46029992315/job/140611556728) | — | 6 |
| `ubuntu-latest` | github-hosted | 21 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/46029983009/job/140611027923) | [2s](https://github.com/iree-org/iree/actions/runs/46029985000/job/140611034595) | — | 21 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/46020053502/job/140577307843) | [1s](https://github.com/iree-org/iree/actions/runs/46029992315/job/140611556918) | — | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [3h56m](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619234115) | [5h17m](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581969561) | [5h17m](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581969561) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [4h04m](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619234155) | [5h11m](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581969363) | [5h11m](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581969363) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [3h58m](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619233940) | [4h51m](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581969119) | [4h51m](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581969119) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [3h10m](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619233989) | [4h40m](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581969093) | [4h40m](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581969093) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [3h45m](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619233828) | [4h22m](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581968873) | [4h22m](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581968873) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [7m44s](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619234097) | [16m28s](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581969360) | [16m28s](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581969360) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [12m21s](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581968741) | [15m59s](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619233857) | [15m59s](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619233857) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581968770) | [14m36s](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619233824) | [14m36s](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619233824) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619233681) | [13m59s](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581968420) | [13m59s](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581968420) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [6m23s](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581969138) | [8m36s](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619233958) | [8m36s](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619233958) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [0s](https://github.com/iree-org/iree/actions/runs/46020053220/job/140577229318) | [3m02s](https://github.com/iree-org/iree/actions/runs/46029992353/job/140611618045) | [3m02s](https://github.com/iree-org/iree/actions/runs/46029992353/job/140611618045) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [1m28s](https://github.com/iree-org/iree/actions/runs/46020053220/job/140581968945) | [2m51s](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619234047) | [2m51s](https://github.com/iree-org/iree/actions/runs/46029992353/job/140619234047) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/46020053502/job/140577307585) | [2m20s](https://github.com/iree-org/iree/actions/runs/46029992315/job/140611556685) | [2m20s](https://github.com/iree-org/iree/actions/runs/46029992315/job/140611556685) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/46029992315/job/140611556876) | [2m14s](https://github.com/iree-org/iree/actions/runs/46020053502/job/140577307793) | [2m14s](https://github.com/iree-org/iree/actions/runs/46020053502/job/140577307793) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/46020053502/job/140577307870) | [1m53s](https://github.com/iree-org/iree/actions/runs/46029992315/job/140611556922) | [1m53s](https://github.com/iree-org/iree/actions/runs/46029992315/job/140611556922) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/46029992315/job/140611556832) | [1m27s](https://github.com/iree-org/iree/actions/runs/46020053502/job/140577307775) | [1m27s](https://github.com/iree-org/iree/actions/runs/46020053502/job/140577307775) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 2 | 0 | — | — | [57s](https://github.com/iree-org/iree/actions/runs/46029992315/job/140611556719) | [1m23s](https://github.com/iree-org/iree/actions/runs/46020053502/job/140577307828) | [1m23s](https://github.com/iree-org/iree/actions/runs/46020053502/job/140577307828) | 2 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 8 | 0 | — | — | [48s](https://github.com/iree-org/iree/actions/runs/46029992125/job/140611633654) | [1m18s](https://github.com/iree-org/iree/actions/runs/46029992698/job/140611674147) | [1m18s](https://github.com/iree-org/iree/actions/runs/46029992698/job/140611674147) | 8 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/46020053502/job/140577307264) | [1m12s](https://github.com/iree-org/iree/actions/runs/46029992315/job/140611556258) | [1m12s](https://github.com/iree-org/iree/actions/runs/46029992315/job/140611556258) | 2 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 8 | 0 | — | — | [41s](https://github.com/iree-org/iree/actions/runs/46029991611/job/140611059255) | [1m07s](https://github.com/iree-org/iree/actions/runs/46029992516/job/140611662556) | [1m07s](https://github.com/iree-org/iree/actions/runs/46029992516/job/140611662556) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 98 | 2% (2/98) |  | 1h01m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 80 | 9% (7/80) |  | 4h48m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 4h22m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 5h11m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 5h17m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
