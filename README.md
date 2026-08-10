# iree-ci-monitor

_Updated: 2026-08-10 12:18 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665308) | [34m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417803) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [12m38s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665289) | [31m03s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417910) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [7m27s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665298) | [28m04s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417643) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [13m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417842) | [25m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417649) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [13m45s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417841) | [20m05s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417611) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417642) | [17m17s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665479) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417468) | [16m08s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665130) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [10m20s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417804) | [10m46s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665379) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [8m02s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665271) | [9m29s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665505) | 50% (1/2) | `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417522) | [4m44s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665451) | 0% (0/1) | `shark10-ci` |
| `azure-linux-scale` | ossci | 13 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/31399257540/job/93496627688) | [1m48s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164228) | 0% (0/8) | 13 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m24s](https://github.com/iree-org/iree/actions/runs/31376153146/job/93415725104) | [1m24s](https://github.com/iree-org/iree/actions/runs/31376153146/job/93415725104) | 0% (0/1) | 1 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31398533116/job/93487414286) | [10s](https://github.com/iree-org/iree/actions/runs/31380851322/job/93430539622) | 0% (0/3) | 15 |
| `ubuntu-24.04` | github-hosted | 45 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436112379) | [9s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665384) | 5% (1/21) | 45 |
| `macos-14` | github-hosted | 7 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436163972) | [9s](https://github.com/iree-org/iree/actions/runs/31399257540/job/93496627642) | 0% (0/4) | 7 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31399257540/job/93496627520) | [8s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164003) | 0% (0/3) | 6 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164004) | [3s](https://github.com/iree-org/iree/actions/runs/31399257540/job/93496627759) | 0% (0/3) | 6 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31399257540/job/93496627999) | [2s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164223) | 0% (0/1) | 2 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665315) | [2s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417648) | 100% (1/1) | `shark55-ci` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665308) | [34m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417803) | [34m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417803) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [12m38s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665289) | [31m03s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417910) | [31m03s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417910) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [7m27s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665298) | [28m04s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417643) | [28m04s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417643) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [10m59s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665511) | [25m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417649) | [25m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417649) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [4m56s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665823) | [20m05s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417611) | [20m05s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417611) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417642) | [17m17s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665479) | [17m17s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665479) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417468) | [16m08s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665130) | [16m08s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665130) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [11m29s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665429) | [13m45s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417841) | [13m45s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417841) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665303) | [13m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417842) | [13m41s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417842) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [10m20s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417804) | [10m46s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665379) | [10m46s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665379) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [5m14s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417686) | [9m29s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665505) | [9m29s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665505) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [7m27s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417782) | [8m02s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665271) | [8m02s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665271) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665692) | [7m12s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417685) | [7m12s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417685) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93438417522) | [4m44s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665451) | [4m44s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93499665451) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/31399257999/job/93496660401) | [1m57s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93436187790) | [1m57s](https://github.com/iree-org/iree/actions/runs/31382675388/job/93436187790) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31399257540/job/93496627830) | [1m48s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164166) | [1m48s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164166) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/31399257540/job/93496628075) | [1m48s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164228) | [1m48s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164228) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31399257540/job/93496627920) | [1m45s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164172) | [1m45s](https://github.com/iree-org/iree/actions/runs/31382675428/job/93436164172) | 2 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m24s](https://github.com/iree-org/iree/actions/runs/31376153146/job/93415725104) | [1m24s](https://github.com/iree-org/iree/actions/runs/31376153146/job/93415725104) | [1m24s](https://github.com/iree-org/iree/actions/runs/31376153146/job/93415725104) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31382674321/job/93436112435) | [22s](https://github.com/iree-org/iree/actions/runs/31398533116/job/93487414504) | [22s](https://github.com/iree-org/iree/actions/runs/31398533116/job/93487414504) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 140 | 0% (0/140) |  | 3h46m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 123 | 4% (5/123) |  | 3h46m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 111 | 3% (3/111) |  | 3h46m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 105 | 7% (7/105) |  | 3h52m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
