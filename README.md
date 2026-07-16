# iree-ci-monitor

_Updated: 2026-07-15 20:40 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [29m20s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036042) | [29m20s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036042) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036068) | [23m20s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036081) | — | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [23m14s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035823) | [23m14s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035823) | — | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [21m30s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035979) | [21m30s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035979) | — | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [16m16s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035800) | [16m16s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035800) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [15m17s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035969) | [15m17s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035969) | — | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [7m14s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036102) | [12m17s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036091) | — | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [5m37s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035848) | [10m35s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035939) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036080) | [4m42s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036183) | — | `shark10-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [14s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892136) | [1m23s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87444894476) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892000) | [6s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444891931) | — | 3 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035842) | [4s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035842) | — | 1 |
| `ubuntu-24.04` | github-hosted | 20 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035762) | [3s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87454676152) | — | 20 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035904) | [3s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035904) | — | `iree-mi308-1` |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444891872) | [3s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892021) | — | 3 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892001) | [3s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892010) | — | 3 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035925) | [2s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035925) | — | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035996) | [2s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035996) | — | `shark01-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892196) | [1s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892196) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [29m20s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036042) | [29m20s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036042) | [29m20s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036042) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [23m20s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036081) | [23m20s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036081) | [23m20s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036081) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [23m14s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035823) | [23m14s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035823) | [23m14s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035823) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [21m30s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035979) | [21m30s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035979) | [21m30s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035979) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [16m16s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035800) | [16m16s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035800) | [16m16s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035800) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [15m17s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035969) | [15m17s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035969) | [15m17s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035969) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [12m17s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036091) | [12m17s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036091) | [12m17s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036091) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [10m35s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035939) | [10m35s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035939) | [10m35s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035939) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [7m14s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036102) | [7m14s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036102) | [7m14s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036102) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [5m37s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035848) | [5m37s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035848) | [5m37s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035848) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [4m42s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036183) | [4m42s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036183) | [4m42s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036183) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [1m23s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87444894476) | [1m23s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87444894476) | [1m23s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87444894476) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [15s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892221) | [15s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892221) | [15s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892221) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [14s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892136) | [14s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892136) | [14s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892136) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444891963) | [7s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444891963) | [7s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444891963) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444891931) | [6s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444891931) | [6s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444891931) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444891976) | [5s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444891976) | [5s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444891976) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892000) | [5s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892000) | [5s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892000) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035842) | [4s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035842) | [4s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035842) | 1 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035990) | [4s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035990) | [4s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035990) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 159 | 1% (2/159) |  | 7h59m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 134 | 1% (1/134) |  | 8h05m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 132 | 10% (13/132) |  | 8h08m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 116 | 1% (1/116) |  | 8h20m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 37 | 0% (0/37) |  | 8h24m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
