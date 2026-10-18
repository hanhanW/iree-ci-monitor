# iree-ci-monitor

_Updated: 2026-10-18 08:55 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [22m10s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397753) | [2h41m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397843) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [1h26m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397824) | [2h37m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397868) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [37m37s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397817) | [2h31m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397776) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [1h19m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397758) | [1h19m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397758) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [55m28s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397739) | [1h02m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397909) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [50m44s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397770) | [50m44s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397770) | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [6m04s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397704) | [6m04s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397704) | — | `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 59 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39129531181/job/117681670467) | [2m09s](https://github.com/iree-org/iree/actions/runs/39129613279/job/117681917152) | 0% (0/2) | 47 |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/39129531142/job/117681713562) | [1m25s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117681713567) | — | 6 |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39134667508/job/117696639260) | [34s](https://github.com/iree-org/iree/actions/runs/39129610007/job/117681909529) | 0% (0/3) | 24 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39129531142/job/117681713313) | [31s](https://github.com/iree-org/iree/actions/runs/39129531142/job/117681713586) | — | 3 |
| `macos-15` | github-hosted | 3 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/39129531142/job/117681713533) | [10s](https://github.com/iree-org/iree/actions/runs/39129531142/job/117681713298) | — | 3 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/39129531142/job/117681713378) | [5s](https://github.com/iree-org/iree/actions/runs/39129531142/job/117681713246) | — | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/39129531142/job/117681713519) | [1s](https://github.com/iree-org/iree/actions/runs/39129531142/job/117681713519) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [2h41m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397843) | [2h41m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397843) | [2h41m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397843) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [2h37m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397868) | [2h37m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397868) | [2h37m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397868) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [2h31m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397776) | [2h31m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397776) | [2h31m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397776) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [1h26m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397824) | [1h26m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397824) | [1h26m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397824) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [1h19m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397758) | [1h19m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397758) | [1h19m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397758) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [1h02m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397909) | [1h02m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397909) | [1h02m](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397909) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [55m28s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397739) | [55m28s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397739) | [55m28s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397739) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [50m44s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397770) | [50m44s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397770) | [50m44s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397770) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [37m37s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397817) | [37m37s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397817) | [37m37s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397817) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [22m10s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397753) | [22m10s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397753) | [22m10s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397753) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [6m04s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397704) | [6m04s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397704) | [6m04s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397704) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 1 | 0 | — | — | [4m06s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397829) | [4m06s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397829) | [4m06s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397829) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 1 | 0 | — | — | [2m37s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397792) | [2m37s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397792) | [2m37s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397792) | 1 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117681670685) | [2m09s](https://github.com/iree-org/iree/actions/runs/39129613279/job/117681917152) | [2m09s](https://github.com/iree-org/iree/actions/runs/39129613279/job/117681917152) | 5 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39129531142/job/117681670444) | [2m07s](https://github.com/iree-org/iree/actions/runs/39129613307/job/117681916985) | [2m07s](https://github.com/iree-org/iree/actions/runs/39129613307/job/117681916985) | 5 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 1 | 0 | — | — | [1m56s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397709) | [1m56s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397709) | [1m56s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397709) | 1 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 1 | 0 | — | — | [1m44s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397750) | [1m44s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397750) | [1m44s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117683397750) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [1m25s](https://github.com/iree-org/iree/actions/runs/39129531142/job/117681713574) | [1m25s](https://github.com/iree-org/iree/actions/runs/39129531142/job/117681713574) | [1m25s](https://github.com/iree-org/iree/actions/runs/39129531142/job/117681713574) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [1m25s](https://github.com/iree-org/iree/actions/runs/39129531142/job/117681713623) | [1m25s](https://github.com/iree-org/iree/actions/runs/39129531142/job/117681713623) | [1m25s](https://github.com/iree-org/iree/actions/runs/39129531142/job/117681713623) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [1m25s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117681713567) | [1m25s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117681713567) | [1m25s](https://github.com/iree-org/iree/actions/runs/39129531156/job/117681713567) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 266 | 4% (11/266) |  | 2m52s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 218 | 1% (2/218) |  | 5m27s ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h41m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h37m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h02m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h31m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
