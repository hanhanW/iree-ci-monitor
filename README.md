# iree-ci-monitor

_Updated: 2026-08-04 05:59 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [6m12s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647927) | [25m17s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647942) | — | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [21m21s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648128) | [21m21s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648128) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [7m14s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648191) | [20m50s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648265) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [18m13s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648054) | [18m13s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648054) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [15m35s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647814) | [15m35s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647814) | — | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [12m08s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648166) | [14m10s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648193) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [5m27s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647981) | [6m26s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648178) | — | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 12 | 0 | — | — | 5 | [1m25s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187673) | [1m40s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248949) | 50% (1/2) | 12 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m30s](https://github.com/iree-org/iree/actions/runs/30899387048/job/91959852511) | [1m30s](https://github.com/iree-org/iree/actions/runs/30899387048/job/91959852511) | 0% (0/1) | 1 |
| `ubuntu-24.04` | github-hosted | 45 | 0 | — | — | 4 | [3s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648034) | [9s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248713) | 0% (0/4) | 43 |
| `macos-14` | github-hosted | 9 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187474) | [9s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187540) | — | 9 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248879) | [5s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697644) | — | 9 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [5s](https://github.com/iree-org/iree/actions/runs/30899337842/job/91959692349) | [5s](https://github.com/iree-org/iree/actions/runs/30899337842/job/91959692349) | — | 1 |
| `windows-2022` | github-hosted | 8 | 0 | — | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187519) | [3s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248730) | — | 8 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30907023766/job/91984425081) | [3s](https://github.com/iree-org/iree/actions/runs/30907024153/job/91984388956) | — | 6 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187637) | [2s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998249092) | — | 2 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647810) | [2s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647810) | — | `shark01-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647825) | [1s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647825) | — | `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647871) | [1s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647871) | — | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647888) | [1s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647888) | — | `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 1 | 1 | [23h56m](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209322) | 2026-08-04 05:59 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [23h56m](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209322) | 2026-08-04 05:59 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `integrates/llvm-20260731-cleanup` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 1 | [23h56m](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209322) | 2026-08-04 05:59 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [25m17s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647942) | [25m17s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647942) | [25m17s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647942) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [21m21s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648128) | [21m21s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648128) | [21m21s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648128) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [20m50s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648265) | [20m50s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648265) | [20m50s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648265) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [18m13s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648054) | [18m13s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648054) | [18m13s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648054) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [15m35s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647814) | [15m35s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647814) | [15m35s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647814) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [14m10s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648193) | [14m10s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648193) | [14m10s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648193) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [12m08s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648166) | [12m08s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648166) | [12m08s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648166) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [7m14s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648191) | [7m14s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648191) | [7m14s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648191) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [6m26s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648178) | [6m26s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648178) | [6m26s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648178) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [6m12s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647927) | [6m12s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647927) | [6m12s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647927) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [5m27s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647981) | [5m27s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647981) | [5m27s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647981) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91979175916) | [1m54s](https://github.com/iree-org/iree/actions/runs/30911221979/job/91998330308) | [1m54s](https://github.com/iree-org/iree/actions/runs/30911221979/job/91998330308) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [1m27s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187652) | [1m40s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248853) | [1m40s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248853) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [1m25s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187673) | [1m40s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248945) | [1m40s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248945) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [36s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187710) | [1m40s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248949) | [1m40s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248949) | 2 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m30s](https://github.com/iree-org/iree/actions/runs/30899387048/job/91959852511) | [1m30s](https://github.com/iree-org/iree/actions/runs/30899387048/job/91959852511) | [1m30s](https://github.com/iree-org/iree/actions/runs/30899387048/job/91959852511) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248785) | [10s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187596) | [10s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187596) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647847) | [10s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647847) | [10s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647847) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187497) | [9s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248713) | [9s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248713) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 161 | 0% (0/161) |  | 46m00s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 115 | 0% (0/115) |  | 46m45s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 143 | 2% (3/143) |  | 51m41s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 121 | 1% (1/121) |  | 52m28s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 35 | 0% (0/35) |  | 23h45m ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 23h56m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
