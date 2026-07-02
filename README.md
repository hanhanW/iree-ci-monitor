# iree-ci-monitor

_Updated: 2026-07-02 11:50 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 9 | 0 | — | — | 0 | [19m00s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039770) | [48m27s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772665882) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 9 | 0 | — | — | 1 | [7m17s](https://github.com/iree-org/iree/actions/runs/28579686349/job/84741335712) | [43m46s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772666011) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 18 | 0 | — | — | 0 | [13m03s](https://github.com/iree-org/iree/actions/runs/28586459413/job/84762114436) | [39m58s](https://github.com/iree-org/iree/actions/runs/28588299940/job/84770551817) | 0% (0/4) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 9 | 0 | — | — | 0 | [20m48s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257910) | [38m14s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772666002) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 18 | 0 | — | — | 0 | [10m28s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039832) | [34m55s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772665979) | 25% (1/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [6m38s](https://github.com/iree-org/iree/actions/runs/28586459413/job/84762114445) | [32m32s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257651) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [8m42s](https://github.com/iree-org/iree/actions/runs/28594381200/job/84787867146) | [27m40s](https://github.com/iree-org/iree/actions/runs/28588299940/job/84770551755) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [19m41s](https://github.com/iree-org/iree/actions/runs/28597990344/job/84804764256) | [23m53s](https://github.com/iree-org/iree/actions/runs/28586459413/job/84762114439) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 18 | 0 | — | — | 0 | [14m36s](https://github.com/iree-org/iree/actions/runs/28597990344/job/84804764450) | [21m14s](https://github.com/iree-org/iree/actions/runs/28588299940/job/84770551795) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 9 | 0 | — | — | 0 | [10m44s](https://github.com/iree-org/iree/actions/runs/28586459413/job/84762114340) | [20m05s](https://github.com/iree-org/iree/actions/runs/28597990344/job/84804764059) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 18 | 0 | — | — | 0 | [7m07s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257859) | [18m12s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257983) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 58 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/28597990774/job/84802215992) | [2m09s](https://github.com/iree-org/iree/actions/runs/28588299427/job/84765353232) | 7% (1/15) | 58 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m36s](https://github.com/iree-org/iree/actions/runs/28582467604/job/84745840996) | [1m36s](https://github.com/iree-org/iree/actions/runs/28582467604/job/84745840996) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 30 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28589961158/job/84770790782) | [1m32s](https://github.com/iree-org/iree/actions/runs/28584377118/job/84752225405) | 0% (0/6) | 30 |
| `ubuntu-24.04-arm` | github-hosted | 30 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836780927) | [1m27s](https://github.com/iree-org/iree/actions/runs/28584377118/job/84752225379) | 0% (0/6) | 30 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28594381200/job/84787867708) | [52s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772665968) | 0% (0/2) | `iree-mi308-1` |
| `macos-14` | github-hosted | 31 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28584377118/job/84752225390) | [40s](https://github.com/iree-org/iree/actions/runs/28584377118/job/84752225295) | 0% (0/7) | 31 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 36 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/28588299940/job/84770551816) | [38s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039923) | 12% (1/8) | 36 |
| `ubuntu-24.04` | github-hosted | 194 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28594381258/job/84785877814) | [6s](https://github.com/iree-org/iree/actions/runs/28597990344/job/84804764407) | 5% (2/40) | 194 |
| `ubuntu-latest` | github-hosted | 30 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28599269313/job/84802840792) | [3s](https://github.com/iree-org/iree/actions/runs/28599269313/job/84802878974) | 0% (0/6) | 30 |
| `azure-windows-scale` | ossci | 10 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28597990774/job/84802215952) | [2s](https://github.com/iree-org/iree/actions/runs/28594381258/job/84785878015) | 0% (0/2) | 10 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28582450676/job/84745786715) | [2s](https://github.com/iree-org/iree/actions/runs/28582450676/job/84745786715) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 9 | 0 | — | — | [19m00s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039770) | [48m27s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772665882) | [48m27s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772665882) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 9 | 0 | — | — | [7m17s](https://github.com/iree-org/iree/actions/runs/28579686349/job/84741335712) | [43m46s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772666011) | [43m46s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772666011) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [11m30s](https://github.com/iree-org/iree/actions/runs/28579686349/job/84741335731) | [42m40s](https://github.com/iree-org/iree/actions/runs/28588299940/job/84770551682) | [42m40s](https://github.com/iree-org/iree/actions/runs/28588299940/job/84770551682) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [27m11s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039943) | [41m31s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772666057) | [41m31s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772666057) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [13m03s](https://github.com/iree-org/iree/actions/runs/28586459413/job/84762114436) | [39m58s](https://github.com/iree-org/iree/actions/runs/28588299940/job/84770551817) | [39m58s](https://github.com/iree-org/iree/actions/runs/28588299940/job/84770551817) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 9 | 0 | — | — | [20m48s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257910) | [38m14s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772666002) | [38m14s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772666002) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [10m28s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039832) | [34m55s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772665979) | [34m55s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772665979) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 9 | 0 | — | — | [6m38s](https://github.com/iree-org/iree/actions/runs/28586459413/job/84762114445) | [32m32s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257651) | [32m32s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257651) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 9 | 0 | — | — | [8m42s](https://github.com/iree-org/iree/actions/runs/28594381200/job/84787867146) | [27m40s](https://github.com/iree-org/iree/actions/runs/28588299940/job/84770551755) | [27m40s](https://github.com/iree-org/iree/actions/runs/28588299940/job/84770551755) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 9 | 0 | — | — | [14m36s](https://github.com/iree-org/iree/actions/runs/28597990344/job/84804764450) | [26m08s](https://github.com/iree-org/iree/actions/runs/28594381200/job/84787867191) | [26m08s](https://github.com/iree-org/iree/actions/runs/28594381200/job/84787867191) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 9 | 0 | — | — | [19m41s](https://github.com/iree-org/iree/actions/runs/28597990344/job/84804764256) | [23m53s](https://github.com/iree-org/iree/actions/runs/28586459413/job/84762114439) | [23m53s](https://github.com/iree-org/iree/actions/runs/28586459413/job/84762114439) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 9 | 0 | — | — | [16m53s](https://github.com/iree-org/iree/actions/runs/28594381200/job/84787867148) | [21m14s](https://github.com/iree-org/iree/actions/runs/28588299940/job/84770551795) | [21m14s](https://github.com/iree-org/iree/actions/runs/28588299940/job/84770551795) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [6m57s](https://github.com/iree-org/iree/actions/runs/28586459413/job/84762114467) | [21m07s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772666130) | [21m07s](https://github.com/iree-org/iree/actions/runs/28589961150/job/84772666130) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 9 | 0 | — | — | [10m44s](https://github.com/iree-org/iree/actions/runs/28586459413/job/84762114340) | [20m05s](https://github.com/iree-org/iree/actions/runs/28597990344/job/84804764059) | [20m05s](https://github.com/iree-org/iree/actions/runs/28597990344/job/84804764059) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [8m33s](https://github.com/iree-org/iree/actions/runs/28588299940/job/84770551903) | [18m12s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257983) | [18m12s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257983) | 3 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 10 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/28594381258/job/84785878090) | [2m34s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836781020) | [2m34s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836781020) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 10 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/28589961158/job/84770791201) | [2m22s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836781114) | [2m22s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836781114) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 10 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/28594381258/job/84785878028) | [2m14s](https://github.com/iree-org/iree/actions/runs/28588299427/job/84765353239) | [2m14s](https://github.com/iree-org/iree/actions/runs/28588299427/job/84765353239) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 10 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/28579686334/job/84737062435) | [1m59s](https://github.com/iree-org/iree/actions/runs/28588299427/job/84765353228) | [1m59s](https://github.com/iree-org/iree/actions/runs/28588299427/job/84765353228) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 5 | 0 | — | — | [40s](https://github.com/iree-org/iree/actions/runs/28584377118/job/84752225504) | [1m58s](https://github.com/iree-org/iree/actions/runs/28588299427/job/84765353231) | [1m58s](https://github.com/iree-org/iree/actions/runs/28588299427/job/84765353231) | 5 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 247 | 8% (19/246) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 194 | 2% (3/194) |  | 6m16s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 274 | 3% (7/274) |  | 8m23s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 218 | 1% (3/218) |  | 18m06s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 63 | 2% (1/63) |  | 31m13s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
