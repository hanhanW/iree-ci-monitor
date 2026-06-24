# iree-ci-monitor

_Updated: 2026-06-24 00:30 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139098012) | [10m09s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097759) | — | `shark10-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097912) | [8m15s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139098052) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 1 | [7m02s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097970) | [7m02s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097970) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 1 | [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097974) | 2026-06-24 00:30 PDT | 1 | [5m51s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139098025) | [5m51s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139098025) | — | `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [5m00s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097743) | [5m00s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097743) | — | `shark10-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097769) | [2m23s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097876) | — | 4 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [6s](https://github.com/iree-org/iree/actions/runs/28079587977/job/83131285389) | [1m29s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869744) | — | 6 |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 4 | [12s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869972) | [13s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137870000) | — | 5 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869754) | [4s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869733) | — | 5 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869735) | [4s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869641) | — | 5 |
| `ubuntu-24.04` | github-hosted | 27 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869626) | [3s](https://github.com/iree-org/iree/actions/runs/28079587977/job/83131285390) | 50% (2/4) | 27 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869959) | [1s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869959) | — | 1 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097744) | [1s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097744) | — | `iree-mi308-1` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097983) | [1s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097983) | — | `shark01-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097988) | [1s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097988) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 1 | [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097782) | 2026-06-24 00:30 PDT | 0 | 0s | 0s | — | 0 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 6 | [23h01m](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438192) | 2026-06-24 00:30 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 1 | [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097812) | 2026-06-24 00:30 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201` | self-hosted | 2 | 2 | [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097849) | 2026-06-24 00:30 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 1 | [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097852) | 2026-06-24 00:30 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [23h01m](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438192) | 2026-06-24 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `devtbi/tduf` | pull_request |
| [19h53m](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944814860) | 2026-06-24 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `integrates/llvm-20260623` | pull_request |
| [16h14m](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257221) | 2026-06-24 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [10h52m](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409541) | 2026-06-24 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/bjacob/cpu-ukernel-pipeline-test` | pull_request |
| [10h39m](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990411) | 2026-06-24 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/bjacob/cpu-ukernel-bodies` | pull_request |
| [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097782) | 2026-06-24 00:30 PDT | `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | `fix-24624-raise-special-ops-memref-crash` | pull_request |
| [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097808) | 2026-06-24 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `fix-24624-raise-special-ops-memref-crash` | pull_request |
| [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097812) | 2026-06-24 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `fix-24624-raise-special-ops-memref-crash` | pull_request |
| [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097849) | 2026-06-24 00:30 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `fix-24624-raise-special-ops-memref-crash` | pull_request |
| [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097852) | 2026-06-24 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `fix-24624-raise-special-ops-memref-crash` | pull_request |
| [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097974) | 2026-06-24 00:30 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `fix-24624-raise-special-ops-memref-crash` | pull_request |
| [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139098024) | 2026-06-24 00:30 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `fix-24624-raise-special-ops-memref-crash` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 6 | 6 | [23h01m](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438192) | 2026-06-24 00:30 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 1 | [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097812) | 2026-06-24 00:30 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 1 | [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097852) | 2026-06-24 00:30 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 1 | [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139098024) | 2026-06-24 00:30 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 1 | [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097974) | 2026-06-24 00:30 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 1 | [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097849) | 2026-06-24 00:30 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 1 | [11m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097782) | 2026-06-24 00:30 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [10m09s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097759) | [10m09s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097759) | [10m09s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097759) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [8m15s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139098052) | [8m15s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139098052) | [8m15s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139098052) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [7m02s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097970) | [7m02s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097970) | [7m02s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097970) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [5m51s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139098025) | [5m51s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139098025) | [5m51s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139098025) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [5m00s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097743) | [5m00s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097743) | [5m00s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097743) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [2m23s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097876) | [2m23s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097876) | [2m23s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097876) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1m29s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869744) | [1m29s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869744) | [1m29s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869744) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1m14s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869730) | [1m14s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869730) | [1m14s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869730) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [13s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137870000) | [13s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137870000) | [13s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137870000) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869972) | [12s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869972) | [12s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869972) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869979) | [12s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869979) | [12s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869979) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869969) | [8s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869969) | [8s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869969) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097769) | [8s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097769) | [8s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097769) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 106 | 3% (3/105) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 104 | 0% (0/103) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 132 | 0% (0/131) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 91 | 0% (0/90) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 30 | 0% (0/30) |  | 1m16s ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 23h01m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
