# iree-ci-monitor

_Updated: 2026-11-24 14:31 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [22m40s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803857) | [32m17s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803535) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [29m53s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803600) | [29m53s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803600) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [13m41s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803633) | [16m51s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803634) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [9m16s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803518) | [12m49s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803903) | — | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803472) | [3m58s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803892) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [1m46s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803544) | [1m46s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803544) | — | `shark55-ci` |
| `azure-linux-scale` | ossci | 12 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578339036) | [1m43s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682812249) | — | 12 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578337797) | [5s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682811889) | — | 6 |
| `macos-15` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682811347) | [5s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682811814) | — | 6 |
| `ubuntu-24.04` | github-hosted | 43 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682812014) | [3s](https://github.com/iree-org/iree/actions/runs/45431611272/job/138578147611) | — | 42 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45431603989/job/138578131017) | [3s](https://github.com/iree-org/iree/actions/runs/45460798163/job/138682510224) | — | 6 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578337362) | [2s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682811765) | — | 6 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [0s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682812204) | [1s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578339192) | — | 2 |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803216) | [1s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803216) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/45431611618/job/138609240465) | [32m17s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803535) | [32m17s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803535) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [29m53s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803600) | [29m53s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803600) | [29m53s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803600) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [22m40s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803857) | [22m40s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803857) | [22m40s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803857) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [16m51s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803634) | [16m51s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803634) | [16m51s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803634) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [13m41s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803633) | [13m41s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803633) | [13m41s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803633) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [12m49s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803903) | [12m49s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803903) | [12m49s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803903) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [9m16s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803518) | [9m16s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803518) | [9m16s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803518) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [3m58s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803892) | [3m58s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803892) | [3m58s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803892) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [1m46s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803544) | [1m46s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803544) | [1m46s](https://github.com/iree-org/iree/actions/runs/45460814106/job/138695803544) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578338704) | [1m43s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682812249) | [1m43s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682812249) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578338504) | [1m41s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682812252) | [1m41s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682812252) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578339280) | [1m36s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682812260) | [1m36s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682812260) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578338986) | [1m20s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682812364) | [1m20s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682812364) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [0s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682811776) | [8s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578339036) | [8s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578339036) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 2 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578337961) | [5s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682811814) | [5s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682811814) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 2 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578338053) | [5s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682811780) | [5s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682811780) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 2 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578337797) | [5s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682811889) | [5s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682811889) | 2 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578337541) | [4s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682811347) | [4s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682811347) | 2 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682811207) | [4s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578337285) | [4s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578337285) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 2 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/45431611333/job/138578337812) | [4s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682811738) | [4s](https://github.com/iree-org/iree/actions/runs/45460813818/job/138682811738) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 104 | 6% (6/104) |  | 3h02m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 139 | 4% (6/139) |  | 3h17m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
