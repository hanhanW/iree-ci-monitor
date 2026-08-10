# iree-ci-monitor

_Updated: 2026-08-10 06:47 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [34m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417803) | [34m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417803) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [31m03s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417910) | [31m03s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417910) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [28m04s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417643) | [28m04s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417643) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [13m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417842) | [25m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417649) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [13m45s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417841) | [20m05s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417611) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [7m12s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417685) | [10m20s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417804) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [5m14s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417686) | [7m27s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417782) | 50% (1/2) | `shark10-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 8 | 0 | — | — | 0 | [1m45s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164172) | [1m57s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93436187790) | 0% (0/8) | 8 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m24s](https://github.com/iree-org/iree/actions/runs/31376153146/job/93415725104) | [1m24s](https://github.com/iree-org/iree/actions/runs/31376153146/job/93415725104) | 0% (0/1) | 1 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31382674321/job/93436112366) | [10s](https://github.com/iree-org/iree/actions/runs/31380851322/job/93430539622) | 0% (0/3) | 9 |
| `ubuntu-24.04` | github-hosted | 33 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436163842) | [9s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417509) | 5% (1/22) | 33 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436163989) | [8s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164003) | 0% (0/3) | 6 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436163929) | [4s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958672) | 0% (0/4) | 6 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436163923) | [3s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164004) | 0% (0/3) | 5 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164223) | [2s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164223) | 0% (0/1) | 1 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417468) | [2s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417468) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417522) | [2s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417522) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417642) | [2s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417642) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417648) | [2s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417648) | 100% (1/1) | `shark55-ci` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [34m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417803) | [34m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417803) | [34m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417803) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [31m03s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417910) | [31m03s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417910) | [31m03s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417910) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [28m04s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417643) | [28m04s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417643) | [28m04s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417643) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [25m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417649) | [25m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417649) | [25m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417649) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [20m05s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417611) | [20m05s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417611) | [20m05s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417611) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [13m45s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417841) | [13m45s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417841) | [13m45s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417841) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [13m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417842) | [13m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417842) | [13m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417842) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [10m20s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417804) | [10m20s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417804) | [10m20s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417804) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [7m27s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417782) | [7m27s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417782) | [7m27s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417782) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [7m12s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417685) | [7m12s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417685) | [7m12s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417685) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [5m14s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417686) | [5m14s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417686) | [5m14s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417686) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [1m57s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93436187790) | [1m57s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93436187790) | [1m57s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93436187790) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [1m48s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164166) | [1m48s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164166) | [1m48s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164166) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [1m48s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164228) | [1m48s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164228) | [1m48s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164228) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m45s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164172) | [1m45s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164172) | [1m45s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164172) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m24s](https://github.com/iree-org/iree/actions/runs/31376153146/job/93415725104) | [1m24s](https://github.com/iree-org/iree/actions/runs/31376153146/job/93415725104) | [1m24s](https://github.com/iree-org/iree/actions/runs/31376153146/job/93415725104) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/31380851322/job/93430539622) | [10s](https://github.com/iree-org/iree/actions/runs/31380851322/job/93430539622) | [10s](https://github.com/iree-org/iree/actions/runs/31380851322/job/93430539622) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164129) | [9s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164129) | [9s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164129) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417865) | [9s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417865) | [9s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417865) | 1 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417511) | [9s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417511) | [9s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417511) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 119 | 4% (5/119) |  | 1h41m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 136 | 0% (0/136) |  | 1h43m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 106 | 3% (3/106) |  | 1h44m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 103 | 6% (6/103) |  | 1h55m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
