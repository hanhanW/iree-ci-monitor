# iree-ci-monitor

_Updated: 2026-10-12 17:46 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645789) | [15m06s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874646313) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [11m36s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645885) | [14m54s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645914) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [13m35s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645909) | [13m35s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645909) | 100% (1/1) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [5m47s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645952) | [8m49s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874646309) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [7m12s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645996) | [7m12s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645996) | 0% (0/1) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [4m36s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874646021) | [6m23s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645874) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [1m35s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645619) | [1m35s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645619) | 0% (0/1) | `shark75-ci` |
| `azure-linux-scale` | ossci | 8 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047568) | [10s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047661) | 12% (1/8) | 8 |
| `macos-15` | github-hosted | 3 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866046968) | [9s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047098) | 0% (0/3) | 3 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866046926) | [5s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047070) | 0% (0/3) | 3 |
| `ubuntu-24.04` | github-hosted | 22 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114885444220) | [3s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866046886) | 10% (2/20) | 21 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866046740) | [3s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047108) | 0% (0/3) | 3 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38265334886/job/114865962713) | [3s](https://github.com/iree-org/iree/actions/runs/38265334886/job/114865963258) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047445) | [2s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047445) | 0% (0/1) | 1 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645967) | [1s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645967) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [15m06s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874646313) | [15m06s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874646313) | [15m06s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874646313) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [14m54s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645914) | [14m54s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645914) | [14m54s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645914) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 1 | 0 | — | — | [13m35s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645909) | [13m35s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645909) | [13m35s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645909) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [11m36s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645885) | [11m36s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645885) | [11m36s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645885) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [8m49s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874646309) | [8m49s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874646309) | [8m49s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874646309) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [7m12s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645996) | [7m12s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645996) | [7m12s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645996) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [6m23s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645874) | [6m23s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645874) | [6m23s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645874) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [5m47s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645952) | [5m47s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645952) | [5m47s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645952) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [4m36s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874646021) | [4m36s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874646021) | [4m36s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874646021) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [1m35s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645619) | [1m35s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645619) | [1m35s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645619) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [52s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114883508174) | [52s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114883508174) | [52s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114883508174) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047661) | [10s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047661) | [10s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047661) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047648) | [9s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047648) | [9s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047648) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047568) | [9s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047568) | [9s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047568) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047741) | [9s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047741) | [9s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047741) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047098) | [9s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047098) | [9s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047098) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114866050870) | [9s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114866050870) | [9s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114866050870) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047400) | [8s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047400) | [8s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047400) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866046680) | [7s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866046680) | [7s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866046680) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866046968) | [7s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866046968) | [7s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866046968) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 238 | 0% (0/238) |  | 9h17m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 254 | 15% (38/254) |  | 9h22m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
