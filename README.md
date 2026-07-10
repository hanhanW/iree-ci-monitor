# iree-ci-monitor

_Updated: 2026-07-10 00:29 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364842) | [6s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364863) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364819) | [3s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300333211) | 50% (2/4) | 9 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364813) | [3s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364828) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364822) | [3s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364841) | — | 2 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 1 | [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620205987) | 2026-07-07 06:05 PDT | 0 | 0s | 0s | — | 0 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 1 | [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206031) | 2026-07-07 06:05 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201` | self-hosted | 1 | 1 | [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206069) | 2026-07-07 06:05 PDT | 0 | 0s | 0s | — | 0 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 1 | 1 | [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206165) | 2026-07-07 06:05 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 1 | [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206176) | 2026-07-07 06:05 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206189) | 2026-07-07 06:05 PDT | 0 | 0s | 0s | — | 0 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 2 | 2 | [17h12m](https://github.com/iree-org/iree/actions/runs/29023197797/job/86141233680) | 2026-07-10 00:29 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [17h12m](https://github.com/iree-org/iree/actions/runs/29023197797/job/86141233680) | 2026-07-10 00:29 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/rvv_scalable_vectorization` | pull_request |
| [17h07m](https://github.com/iree-org/iree/actions/runs/29023147299/job/86142385872) | 2026-07-10 00:29 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/rvv_tile_size_selection` | pull_request |
| [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620205987) | 2026-07-07 06:05 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | `integrates/llvm-20260707` | pull_request |
| [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206031) | 2026-07-07 06:05 PDT | `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | `integrates/llvm-20260707` | pull_request |
| [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206069) | 2026-07-07 06:05 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `integrates/llvm-20260707` | pull_request |
| [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206165) | 2026-07-07 06:05 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | `integrates/llvm-20260707` | pull_request |
| [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206176) | 2026-07-07 06:05 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `integrates/llvm-20260707` | pull_request |
| [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206189) | 2026-07-07 06:05 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `integrates/llvm-20260707` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 2 | 2 | [17h12m](https://github.com/iree-org/iree/actions/runs/29023197797/job/86141233680) | 2026-07-10 00:29 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 1 | [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206189) | 2026-07-07 06:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 1 | [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206176) | 2026-07-07 06:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 1 | [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620205987) | 2026-07-07 06:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 1 | [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206165) | 2026-07-07 06:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 1 | [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206069) | 2026-07-07 06:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 1 | [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206031) | 2026-07-07 06:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364863) | [6s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364863) | [6s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364863) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364842) | [5s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364842) | [5s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364842) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364808) | [5s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364808) | [5s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364808) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364828) | [3s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364828) | [3s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364828) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300333211) | [3s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300333211) | [3s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300333211) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364841) | [3s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364841) | [3s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364841) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364822) | [3s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364822) | [3s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364822) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364847) | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364847) | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364847) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364827) | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364827) | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364827) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364851) | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364851) | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364851) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364819) | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364819) | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364819) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364813) | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364813) | [2s](https://github.com/iree-org/iree/actions/runs/29073624408/job/86300364813) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29071349566/job/86293319652) | [2s](https://github.com/iree-org/iree/actions/runs/29071349566/job/86293319652) | [2s](https://github.com/iree-org/iree/actions/runs/29071349566/job/86293319652) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 255 | 1% (3/254) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 186 | 1% (1/185) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 208 | 6% (13/207) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 197 | 1% (1/196) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 61 | 8% (5/61) |  | 13h59m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 17h12m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
