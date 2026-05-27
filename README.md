# iree-ci-monitor

_Updated: 2026-05-27 12:06 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [30m04s](https://github.com/iree-org/iree/actions/runs/26527576961/job/78140276389) | [1h51m](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065370903) | 0% (0/6) | `shark75-ci` |
| `azure-linux-scale` | ossci | 33 | 0 | — | — | 0 | [13s](https://github.com/iree-org/iree/actions/runs/26527578823/job/78135328433) | [1h33m](https://github.com/iree-org/iree/actions/runs/26502359002/job/78045847050) | 0% (0/15) | 33 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 0 | — | — | 0 | [11m46s](https://github.com/iree-org/iree/actions/runs/26514269732/job/78089125415) | [1h15m](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371065) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | [5m20s](https://github.com/iree-org/iree/actions/runs/26514269732/job/78089125480) | [55m03s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065370905) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [16m13s](https://github.com/iree-org/iree/actions/runs/26514269732/job/78089125587) | [47m20s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371020) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 0 | — | — | 0 | [9m57s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065370912) | [41m03s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772225) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [9m25s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772202) | [34m32s](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054136825) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [6m24s](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054136892) | [33m08s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772434) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [7m22s](https://github.com/iree-org/iree/actions/runs/26511684004/job/78104847602) | [31m13s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772366) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [9m12s](https://github.com/iree-org/iree/actions/runs/26527576961/job/78140276499) | [20m48s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772377) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [9m32s](https://github.com/iree-org/iree/actions/runs/26511684004/job/78104847534) | [19m29s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772363) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [6m07s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772394) | [17m47s](https://github.com/iree-org/iree/actions/runs/26511684004/job/78104847578) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `azure-windows-scale` | ossci | 5 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26527578823/job/78135328763) | [3m07s](https://github.com/iree-org/iree/actions/runs/26514270484/job/78086877942) | 0% (0/2) | 5 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m23s](https://github.com/iree-org/iree/actions/runs/26506124202/job/78058846260) | [1m23s](https://github.com/iree-org/iree/actions/runs/26506124202/job/78058846260) | 100% (1/1) | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 24 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/26527576961/job/78140276100) | [1m15s](https://github.com/iree-org/iree/actions/runs/26514269732/job/78089125472) | 8% (1/12) | 24 |
| `ubuntu-24.04` | github-hosted | 119 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26527576961/job/78140276249) | [1m14s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371070) | 4% (2/51) | 118 |
| `macos-14` | github-hosted | 16 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26527578823/job/78135328399) | [1m03s](https://github.com/iree-org/iree/actions/runs/26511684263/job/78077690258) | 0% (0/7) | 16 |
| `windows-2022` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26514270484/job/78086878006) | [54s](https://github.com/iree-org/iree/actions/runs/26502359002/job/78045846830) | 0% (0/6) | 15 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26507618167/job/78064044831) | [46s](https://github.com/iree-org/iree/actions/runs/26502359002/job/78045846812) | 0% (0/6) | 15 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065370848) | [15s](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054136885) | 0% (0/3) | 6 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26511684004/job/78104847867) | [13s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772326) | 0% (0/3) | `iree-mi308-1` |
| `ubuntu-latest` | github-hosted | 33 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26502355083/job/78045799600) | [4s](https://github.com/iree-org/iree/actions/runs/26511679174/job/78077681390) | 0% (0/6) | 33 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26506087959/job/78058718749) | [2s](https://github.com/iree-org/iree/actions/runs/26506087959/job/78058718749) | 100% (1/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [30m04s](https://github.com/iree-org/iree/actions/runs/26527576961/job/78140276389) | [1h51m](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065370903) | [1h51m](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065370903) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [22m19s](https://github.com/iree-org/iree/actions/runs/26514269732/job/78089125528) | [1h40m](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371049) | [1h40m](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371049) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 5 | 0 | — | — | [17s](https://github.com/iree-org/iree/actions/runs/26527578823/job/78135328794) | [1h36m](https://github.com/iree-org/iree/actions/runs/26502359002/job/78045846996) | [1h36m](https://github.com/iree-org/iree/actions/runs/26502359002/job/78045846996) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 5 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/26527578823/job/78135328535) | [1h36m](https://github.com/iree-org/iree/actions/runs/26502359002/job/78045846865) | [1h36m](https://github.com/iree-org/iree/actions/runs/26502359002/job/78045846865) | 5 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 5 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/26511684263/job/78077690436) | [1h33m](https://github.com/iree-org/iree/actions/runs/26502359002/job/78045847050) | [1h33m](https://github.com/iree-org/iree/actions/runs/26502359002/job/78045847050) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 5 | 0 | — | — | [14s](https://github.com/iree-org/iree/actions/runs/26527578823/job/78135328766) | [1h32m](https://github.com/iree-org/iree/actions/runs/26502359002/job/78045847030) | [1h32m](https://github.com/iree-org/iree/actions/runs/26502359002/job/78045847030) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 4 | 0 | — | — | [17s](https://github.com/iree-org/iree/actions/runs/26527578823/job/78135328813) | [1h21m](https://github.com/iree-org/iree/actions/runs/26502359002/job/78045846927) | [1h21m](https://github.com/iree-org/iree/actions/runs/26502359002/job/78045846927) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 6 | 0 | — | — | [11m46s](https://github.com/iree-org/iree/actions/runs/26514269732/job/78089125415) | [1h15m](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371065) | [1h15m](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371065) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 0 | — | — | [5m20s](https://github.com/iree-org/iree/actions/runs/26514269732/job/78089125480) | [55m03s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065370905) | [55m03s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065370905) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 6 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/26527576961/job/78135324762) | [51m32s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78045840208) | [51m32s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78045840208) | 6 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 6 | 0 | — | — | [16m13s](https://github.com/iree-org/iree/actions/runs/26514269732/job/78089125587) | [47m20s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371020) | [47m20s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371020) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [8m15s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772371) | [41m43s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371091) | [41m43s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371091) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 6 | 0 | — | — | [9m57s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065370912) | [41m03s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772225) | [41m03s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772225) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [9m37s](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054137034) | [38m40s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371097) | [38m40s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371097) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [6m00s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065370960) | [37m11s](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054137153) | [37m11s](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054137153) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [9m25s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772202) | [34m32s](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054136825) | [34m32s](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054136825) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [6m21s](https://github.com/iree-org/iree/actions/runs/26514269732/job/78089125412) | [33m08s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772434) | [33m08s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772434) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [7m22s](https://github.com/iree-org/iree/actions/runs/26511684004/job/78104847602) | [31m13s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772366) | [31m13s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772366) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [8m56s](https://github.com/iree-org/iree/actions/runs/26511684004/job/78104847855) | [20m48s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772377) | [20m48s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772377) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054136939) | [19m29s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772363) | [19m29s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772363) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 316 | 2% (6/316) |  | 34m23s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 287 | 6% (17/287) |  | 47m41s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 231 | 3% (8/231) |  | 50m08s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 233 | 1% (2/233) |  | 55m45s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 75 | 3% (2/75) |  | 59m24s ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h51m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h15m (> 1h00m)
- **[queue-starved]** `azure-linux-scale` p95 queue 1h33m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
