# iree-ci-monitor

_Updated: 2026-09-01 04:43 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [32m32s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543496) | [32m32s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543496) | — | `shark01-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [21m15s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543696) | [21m15s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543696) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [14m57s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543613) | [21m02s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543558) | — | `shark01-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [6m32s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543500) | [16m52s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543563) | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [15m54s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543396) | [15m54s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543396) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543389) | [10m50s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543560) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [6m10s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543419) | [6m10s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543419) | — | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543634) | [5m42s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543561) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [5m25s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543473) | [5m25s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543473) | — | `shark10-ci` |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658475) | [1m32s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658967) | 0% (0/2) | 7 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m23s](https://github.com/iree-org/iree/actions/runs/33492423580/job/99806758045) | [1m23s](https://github.com/iree-org/iree/actions/runs/33492423580/job/99806758045) | 0% (0/1) | 1 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/33492415838/job/99806732025) | [4s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658180) | — | 6 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33496339179/job/99819360754) | [3s](https://github.com/iree-org/iree/actions/runs/33496339179/job/99819360741) | 0% (0/3) | 12 |
| `ubuntu-24.04` | github-hosted | 35 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99805803256) | [3s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543567) | 0% (0/4) | 35 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658050) | [3s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658250) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33472967958/job/99746345034) | [3s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658301) | — | 6 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658642) | [1s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658642) | — | 1 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543374) | [1s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543374) | — | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543522) | [1s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543522) | — | `shark01-ci` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [32m32s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543496) | [32m32s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543496) | [32m32s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543496) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [21m15s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543696) | [21m15s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543696) | [21m15s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543696) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [21m02s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543558) | [21m02s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543558) | [21m02s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543558) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [16m52s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543563) | [16m52s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543563) | [16m52s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543563) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [15m54s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543396) | [15m54s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543396) | [15m54s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543396) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [14m57s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543613) | [14m57s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543613) | [14m57s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543613) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [10m50s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543560) | [10m50s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543560) | [10m50s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543560) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [6m32s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543500) | [6m32s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543500) | [6m32s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543500) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [6m10s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543419) | [6m10s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543419) | [6m10s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543419) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [5m42s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543561) | [5m42s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543561) | [5m42s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543561) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [5m25s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543473) | [5m25s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543473) | [5m25s](https://github.com/iree-org/iree/actions/runs/33488023439/job/99794543473) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m32s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658967) | [1m32s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658967) | [1m32s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658967) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m23s](https://github.com/iree-org/iree/actions/runs/33492423580/job/99806758045) | [1m23s](https://github.com/iree-org/iree/actions/runs/33492423580/job/99806758045) | [1m23s](https://github.com/iree-org/iree/actions/runs/33492423580/job/99806758045) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658617) | [12s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658617) | [12s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658617) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658851) | [11s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658851) | [11s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658851) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658475) | [10s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658475) | [10s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658475) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33469915714/job/99737403236) | [4s](https://github.com/iree-org/iree/actions/runs/33496339478/job/99819317131) | [4s](https://github.com/iree-org/iree/actions/runs/33496339478/job/99819317131) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658180) | [4s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658180) | [4s](https://github.com/iree-org/iree/actions/runs/33488023678/job/99792658180) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33472967958/job/99746344869) | [3s](https://github.com/iree-org/iree/actions/runs/33472967958/job/99746344869) | [3s](https://github.com/iree-org/iree/actions/runs/33472967958/job/99746344869) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33472967958/job/99746344872) | [3s](https://github.com/iree-org/iree/actions/runs/33472967958/job/99746344872) | [3s](https://github.com/iree-org/iree/actions/runs/33472967958/job/99746344872) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 225 | 4% (10/225) |  | 2h18m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 196 | 1% (1/196) |  | 2h19m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 269 | 0% (1/269) |  | 2h30m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 188 | 0% (0/188) |  | 2h35m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
