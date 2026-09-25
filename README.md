# iree-ci-monitor

_Updated: 2026-09-25 14:38 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [32m16s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178322066) | [57m45s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611992) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [33m24s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611730) | [43m19s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611780) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [40m57s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611809) | [42m07s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611769) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [22m14s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178321980) | [37m50s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611594) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178321974) | [26m22s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611673) | 100% (1/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [6m47s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611743) | [17m58s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178321983) | 0% (0/1) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [4m39s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178322027) | [12m43s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611761) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [8m19s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178322065) | [8m36s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611478) | 0% (0/1) | `shark75-ci` |
| `azure-linux-scale` | ossci | 11 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/36166506616/job/108175530887) | [21s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154140335) | 0% (0/6) | 11 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/36166506616/job/108175530928) | [10s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139854) | 0% (0/3) | 6 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139862) | [5s](https://github.com/iree-org/iree/actions/runs/36166506616/job/108175531028) | 0% (0/3) | 6 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139833) | [4s](https://github.com/iree-org/iree/actions/runs/36166506616/job/108175531609) | 0% (0/3) | 6 |
| `ubuntu-24.04` | github-hosted | 42 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178322240) | [3s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178322319) | 5% (1/20) | 42 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/36145819953/job/108106615431) | [3s](https://github.com/iree-org/iree/actions/runs/36166505341/job/108175462398) | 0% (0/3) | 9 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154140265) | [2s](https://github.com/iree-org/iree/actions/runs/36166506616/job/108175531036) | 0% (0/1) | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [32m16s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178322066) | [57m45s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611992) | [57m45s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611992) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [21m18s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178322277) | [43m19s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611780) | [43m19s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611780) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [11m06s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178322200) | [42m07s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611769) | [42m07s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611769) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [2m10s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178322219) | [40m57s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611809) | [40m57s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611809) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [22m14s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178321980) | [37m50s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611594) | [37m50s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611594) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [12m21s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178322164) | [33m24s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611730) | [33m24s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611730) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [22m17s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611964) | [28m03s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178322377) | [28m03s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178322377) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178321974) | [26m22s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611673) | [26m22s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611673) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 2 | 0 | — | — | [6m47s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611743) | [17m58s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178321983) | [17m58s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178321983) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [4m28s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178322089) | [12m43s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611761) | [12m43s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611761) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [8m19s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178322065) | [8m36s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611478) | [8m36s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611478) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [16s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611508) | [4m39s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178322027) | [4m39s](https://github.com/iree-org/iree/actions/runs/36166506757/job/108178322027) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36166506616/job/108175531197) | [21s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154140335) | [21s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154140335) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36166506616/job/108175531044) | [19s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139995) | [19s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139995) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/36166506616/job/108175530887) | [19s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139939) | [19s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139939) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/36166506616/job/108175531158) | [19s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154140113) | [19s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154140113) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36166506616/job/108175530928) | [10s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139854) | [10s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139854) | 2 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36166506616/job/108175530891) | [9s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139643) | [9s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139643) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139757) | [9s](https://github.com/iree-org/iree/actions/runs/36166506616/job/108175531139) | [9s](https://github.com/iree-org/iree/actions/runs/36166506616/job/108175531139) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/36166506616/job/108175531037) | [7s](https://github.com/iree-org/iree/actions/runs/36166506616/job/108175531037) | [7s](https://github.com/iree-org/iree/actions/runs/36166506616/job/108175531037) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 379 | 1% (5/379) |  | 3h28m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 290 | 3% (10/290) |  | 3h44m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
