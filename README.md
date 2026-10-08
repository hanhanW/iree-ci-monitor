# iree-ci-monitor

_Updated: 2026-10-07 23:12 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [17m30s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869907) | [24m26s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869911) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869799) | [15m26s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869813) | 0% (0/2) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869624) | [12m01s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869938) | 0% (0/1) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [8m47s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869825) | [8m47s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869825) | 100% (1/1) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [6m00s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151870036) | [6m00s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151870036) | 0% (0/1) | `shark55-ci` |
| `macos-15` | github-hosted | 3 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163761) | [11s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163789) | 0% (0/3) | 3 |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113150164732) | [9s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163802) | 0% (0/7) | 7 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [5s](https://github.com/iree-org/iree/actions/runs/37731675631/job/113162040832) | [7s](https://github.com/iree-org/iree/actions/runs/37731675631/job/113162040863) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163705) | [4s](https://github.com/iree-org/iree/actions/runs/37731675631/job/113162040751) | 0% (0/3) | 6 |
| `ubuntu-24.04` | github-hosted | 41 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869714) | [3s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163666) | 25% (7/28) | 41 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/37731675631/job/113162040797) | [3s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163709) | 33% (1/3) | 5 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37727892538/job/113150120473) | [3s](https://github.com/iree-org/iree/actions/runs/37727892538/job/113150120411) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163803) | [1s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163803) | 0% (0/1) | 1 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 1 | [1h33m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869658) | 2026-10-07 23:11 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201` | self-hosted | 2 | 2 | [1h33m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869866) | 2026-10-07 23:11 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [1h33m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869951) | 2026-10-07 23:11 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [1h33m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869658) | 2026-10-07 23:11 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `main` | push |
| [1h33m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869866) | 2026-10-07 23:11 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [1h33m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869951) | 2026-10-07 23:11 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `main` | push |
| [1h33m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151870328) | 2026-10-07 23:11 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 1 | [1h33m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869658) | 2026-10-07 23:11 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 1 | [1h33m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869951) | 2026-10-07 23:11 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 1 | [1h33m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869866) | 2026-10-07 23:11 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 1 | [1h33m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151870328) | 2026-10-07 23:11 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [24m26s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869911) | [24m26s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869911) | [24m26s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869911) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [17m30s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869907) | [17m30s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869907) | [17m30s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869907) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [15m26s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869813) | [15m26s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869813) | [15m26s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869813) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [12m01s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869938) | [12m01s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869938) | [12m01s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869938) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 1 | 0 | — | — | [8m47s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869825) | [8m47s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869825) | [8m47s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869825) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [6m00s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151870036) | [6m00s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151870036) | [6m00s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151870036) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 1 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163789) | [11s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163789) | [11s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163789) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163661) | [10s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163661) | [10s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163661) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163761) | [10s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163761) | [10s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163761) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163802) | [9s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163802) | [9s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163802) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163752) | [9s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163752) | [9s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163752) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163788) | [9s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163788) | [9s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163788) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113150164732) | [9s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113150164732) | [9s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113150164732) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163879) | [8s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163879) | [8s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163879) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37731675631/job/113162040863) | [7s](https://github.com/iree-org/iree/actions/runs/37731675631/job/113162040863) | [7s](https://github.com/iree-org/iree/actions/runs/37731675631/job/113162040863) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163843) | [7s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163843) | [7s](https://github.com/iree-org/iree/actions/runs/37727893406/job/113150163843) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 341 | 0% (1/340) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 99 | 15% (15/99) |  | 1h06m ago |

## Alerts

- **[high-failure-main]** `ubuntu-24.04` main-branch failure rate 25% (7/28)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
