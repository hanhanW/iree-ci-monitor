# iree-ci-monitor

_Updated: 2026-07-01 00:50 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [40m57s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105814) | [40m57s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105814) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [11m24s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105752) | [24m22s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105821) | — | `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [22m51s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105822) | [22m51s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105822) | — | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [15m47s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105760) | [22m06s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105852) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [16m56s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105824) | [16m56s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105824) | — | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [7m02s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105856) | [15m23s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105768) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [8m53s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105762) | [8m53s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105762) | — | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [8m23s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105788) | [8m23s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105788) | — | `shark75-ci` |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [1m30s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467243913) | [1m39s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467244034) | — | 5 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [37s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105767) | [56s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105784) | — | 4 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467243850) | [5s](https://github.com/iree-org/iree/actions/runs/28498435050/job/84469805790) | — | 6 |
| `ubuntu-24.04` | github-hosted | 30 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105801) | [4s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105785) | 50% (2/4) | 30 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467243916) | [4s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467243808) | — | 5 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467243799) | [3s](https://github.com/iree-org/iree/actions/runs/28498435050/job/84469805795) | — | 5 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105581) | [2s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105581) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105595) | [2s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105595) | — | `shark01-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105825) | [2s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105758) | — | `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105761) | [2s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105761) | — | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467243942) | [2s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467243942) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 3 | 3 | [15h42m](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981214) | 2026-07-01 00:49 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [15h42m](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981214) | 2026-07-01 00:49 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/overload_iree_tiling_interface_ops` | pull_request |
| [15h38m](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954579) | 2026-07-01 00:49 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/scalable_vector_level_tiling` | pull_request |
| [15h34m](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707596) | 2026-07-01 00:49 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/scalable_distribution_tiling` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 3 | 3 | [15h42m](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981214) | 2026-07-01 00:49 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [40m57s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105814) | [40m57s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105814) | [40m57s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105814) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [24m22s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105821) | [24m22s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105821) | [24m22s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105821) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [22m51s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105822) | [22m51s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105822) | [22m51s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105822) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [22m06s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105852) | [22m06s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105852) | [22m06s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105852) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [16m56s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105824) | [16m56s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105824) | [16m56s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105824) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [15m47s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105760) | [15m47s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105760) | [15m47s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105760) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [15m23s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105768) | [15m23s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105768) | [15m23s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105768) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [11m24s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105752) | [11m24s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105752) | [11m24s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105752) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [8m53s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105762) | [8m53s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105762) | [8m53s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105762) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [8m23s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105788) | [8m23s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105788) | [8m23s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105788) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [7m02s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105856) | [7m02s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105856) | [7m02s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105856) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m39s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467244034) | [1m39s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467244034) | [1m39s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467244034) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [1m32s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467244023) | [1m32s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467244023) | [1m32s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467244023) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [1m30s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467243913) | [1m30s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467243913) | [1m30s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467243913) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [56s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105784) | [56s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105784) | [56s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105784) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [37s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105767) | [37s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105767) | [37s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105767) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [30s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105544) | [30s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105544) | [30s](https://github.com/iree-org/iree/actions/runs/28495168049/job/84468105544) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467243901) | [7s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467243901) | [7s](https://github.com/iree-org/iree/actions/runs/28495167998/job/84467243901) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28498435050/job/84469805790) | [5s](https://github.com/iree-org/iree/actions/runs/28498435050/job/84469805790) | [5s](https://github.com/iree-org/iree/actions/runs/28498435050/job/84469805790) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 181 | 8% (15/181) |  | 41m30s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 209 | 0% (0/209) |  | 54m49s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 173 | 0% (0/173) |  | 56m44s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 147 | 0% (0/147) |  | 58m14s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 48 | 0% (0/48) |  | 1h17m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 15h42m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
