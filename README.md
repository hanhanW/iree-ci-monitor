# iree-ci-monitor

_Updated: 2026-11-09 23:25 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [2h22m](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058957) | [2h34m](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059115) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [27m35s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058798) | [2h21m](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059310) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [46m47s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058803) | [46m47s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058803) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [19m41s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059013) | [25m25s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058792) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [7m51s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059238) | [11m17s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058906) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [5m18s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058879) | [5m18s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058879) | — | `shark75-ci` |
| `macos-15` | github-hosted | 5 | 0 | — | — | 1 | [15s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363024) | [16s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363210) | — | 5 |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [11s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363314) | [15s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363420) | — | 6 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [13s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058873) | [13s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058873) | — | `shark75-ci` |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363265) | [4s](https://github.com/iree-org/iree/actions/runs/42760443092/job/129644677112) | — | 6 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363236) | [3s](https://github.com/iree-org/iree/actions/runs/42760443092/job/129644677037) | — | 5 |
| `ubuntu-24.04` | github-hosted | 37 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058949) | [2s](https://github.com/iree-org/iree/actions/runs/42760443092/job/129644677052) | 20% (1/5) | 36 |
| `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/42705092425/job/129459690548) | [2s](https://github.com/iree-org/iree/actions/runs/42705092425/job/129459690548) | 0% (0/1) | 1 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363396) | [1s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363396) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [2h34m](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059115) | [2h34m](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059115) | [2h34m](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059115) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [2h22m](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058957) | [2h22m](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058957) | [2h22m](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058957) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [2h21m](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059310) | [2h21m](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059310) | [2h21m](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059310) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [46m47s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058803) | [46m47s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058803) | [46m47s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058803) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [27m35s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058798) | [27m35s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058798) | [27m35s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058798) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [25m25s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058792) | [25m25s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058792) | [25m25s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058792) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [19m41s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059013) | [19m41s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059013) | [19m41s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059013) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [11m17s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058906) | [11m17s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058906) | [11m17s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058906) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [7m51s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059238) | [7m51s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059238) | [7m51s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059238) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [5m18s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058879) | [5m18s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058879) | [5m18s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058879) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 1 | 0 | — | — | [16s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363210) | [16s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363210) | [16s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363210) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [15s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363198) | [15s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363198) | [15s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363198) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [15s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363420) | [15s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363420) | [15s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363420) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 1 | 0 | — | — | [15s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363024) | [15s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363024) | [15s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363024) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 1 | 0 | — | — | [15s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363215) | [15s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363215) | [15s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363215) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [14s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363482) | [14s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363482) | [14s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363482) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [13s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058873) | [13s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058873) | [13s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058873) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363181) | [11s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363181) | [11s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363181) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363314) | [11s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363314) | [11s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363314) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/42760443092/job/129644677112) | [4s](https://github.com/iree-org/iree/actions/runs/42760443092/job/129644677112) | [4s](https://github.com/iree-org/iree/actions/runs/42760443092/job/129644677112) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 390 | 1% (4/390) |  | 6h52m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 299 | 1% (3/299) |  | 8h52m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h21m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h34m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
