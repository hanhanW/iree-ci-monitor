# iree-ci-monitor

_Updated: 2026-09-03 09:30 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 10 | 0 | — | — | 0 | [16m51s](https://github.com/iree-org/iree/actions/runs/33723404289/job/100548968195) | [1h21m](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661130993) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [12m55s](https://github.com/iree-org/iree/actions/runs/33766944727/job/100691703644) | [1h05m](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252233) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 20 | 0 | — | — | 0 | [21m40s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747884) | [59m03s](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661131325) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [10m46s](https://github.com/iree-org/iree/actions/runs/33766944727/job/100691704064) | [39m17s](https://github.com/iree-org/iree/actions/runs/33736882103/job/100599397350) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 10 | 0 | — | — | 0 | [7m12s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747759) | [36m26s](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661130918) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 10 | 0 | — | — | 0 | [19m05s](https://github.com/iree-org/iree/actions/runs/33751321379/job/100638003503) | [34m10s](https://github.com/iree-org/iree/actions/runs/33736882103/job/100599397398) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [5m14s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747741) | [25m39s](https://github.com/iree-org/iree/actions/runs/33736882103/job/100599397285) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33751321379/job/100638003401) | [22m14s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476462) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 20 | 0 | — | — | 0 | [6m21s](https://github.com/iree-org/iree/actions/runs/33736967065/job/100592635656) | [19m18s](https://github.com/iree-org/iree/actions/runs/33736882103/job/100599397489) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 20 | 0 | — | — | 0 | [10m00s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747690) | [18m45s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252626) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 20 | 0 | — | — | 0 | [6m02s](https://github.com/iree-org/iree/actions/runs/33751321379/job/100638003541) | [15m32s](https://github.com/iree-org/iree/actions/runs/33723404289/job/100548968407) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m30s](https://github.com/iree-org/iree/actions/runs/33738976555/job/100596176846) | [1m30s](https://github.com/iree-org/iree/actions/runs/33738976555/job/100596176846) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 68 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/33766944749/job/100687209033) | [1m29s](https://github.com/iree-org/iree/actions/runs/33760490301/job/100665364749) | 0% (0/15) | 68 |
| `ubuntu-24.04-arm` | github-hosted | 33 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/33748202197/job/100626318528) | [1m19s](https://github.com/iree-org/iree/actions/runs/33758667370/job/100659304829) | 0% (0/6) | 33 |
| `macos-14` | github-hosted | 34 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33748202197/job/100626318612) | [1m11s](https://github.com/iree-org/iree/actions/runs/33736967104/job/100590429444) | 0% (0/7) | 34 |
| `windows-2022` | github-hosted | 33 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33748202197/job/100626318631) | [36s](https://github.com/iree-org/iree/actions/runs/33736967104/job/100590429058) | 0% (0/6) | 33 |
| `ubuntu-24.04` | github-hosted | 227 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252278) | [10s](https://github.com/iree-org/iree/actions/runs/33766944727/job/100691703652) | 5% (2/43) | 227 |
| `azure-windows-scale` | ossci | 11 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/33766944749/job/100687209247) | [8s](https://github.com/iree-org/iree/actions/runs/33736967104/job/100590430185) | 0% (0/2) | 11 |
| `ubuntu-latest` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33748281225/job/100625792353) | [4s](https://github.com/iree-org/iree/actions/runs/33766943379/job/100687137583) | 0% (0/6) | 21 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 10 | 0 | — | — | [16m51s](https://github.com/iree-org/iree/actions/runs/33723404289/job/100548968195) | [1h21m](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661130993) | [1h21m](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661130993) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 10 | 0 | — | — | [12m55s](https://github.com/iree-org/iree/actions/runs/33766944727/job/100691703644) | [1h05m](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252233) | [1h05m](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252233) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [21m40s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747884) | [1h01m](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252522) | [1h01m](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252522) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 10 | 0 | — | — | [10m46s](https://github.com/iree-org/iree/actions/runs/33766944727/job/100691704064) | [39m17s](https://github.com/iree-org/iree/actions/runs/33736882103/job/100599397350) | [39m17s](https://github.com/iree-org/iree/actions/runs/33736882103/job/100599397350) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 10 | 0 | — | — | [7m12s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747759) | [36m26s](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661130918) | [36m26s](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661130918) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 10 | 0 | — | — | [19m05s](https://github.com/iree-org/iree/actions/runs/33751321379/job/100638003503) | [34m10s](https://github.com/iree-org/iree/actions/runs/33736882103/job/100599397398) | [34m10s](https://github.com/iree-org/iree/actions/runs/33736882103/job/100599397398) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [11m49s](https://github.com/iree-org/iree/actions/runs/33736967065/job/100592635413) | [27m10s](https://github.com/iree-org/iree/actions/runs/33751321379/job/100638003586) | [27m10s](https://github.com/iree-org/iree/actions/runs/33751321379/job/100638003586) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 0 | — | — | [5m14s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747741) | [25m39s](https://github.com/iree-org/iree/actions/runs/33736882103/job/100599397285) | [25m39s](https://github.com/iree-org/iree/actions/runs/33736882103/job/100599397285) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [9m14s](https://github.com/iree-org/iree/actions/runs/33744419882/job/100615877953) | [24m28s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476370) | [24m28s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476370) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33751321379/job/100638003401) | [22m14s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476462) | [22m14s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476462) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [7m40s](https://github.com/iree-org/iree/actions/runs/33736967065/job/100592635690) | [21m20s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252501) | [21m20s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252501) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 0 | — | — | [5m12s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252466) | [20m43s](https://github.com/iree-org/iree/actions/runs/33736967065/job/100592635846) | [20m43s](https://github.com/iree-org/iree/actions/runs/33736967065/job/100592635846) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [9m38s](https://github.com/iree-org/iree/actions/runs/33736967065/job/100592635511) | [15m39s](https://github.com/iree-org/iree/actions/runs/33736882103/job/100599397445) | [15m39s](https://github.com/iree-org/iree/actions/runs/33736882103/job/100599397445) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [1m49s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252248) | [13m45s](https://github.com/iree-org/iree/actions/runs/33744419882/job/100615878027) | [13m45s](https://github.com/iree-org/iree/actions/runs/33744419882/job/100615878027) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 0 | — | — | [6m21s](https://github.com/iree-org/iree/actions/runs/33736967065/job/100592635656) | [11m48s](https://github.com/iree-org/iree/actions/runs/33723404289/job/100548968375) | [11m48s](https://github.com/iree-org/iree/actions/runs/33723404289/job/100548968375) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 11 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/33744419932/job/100613584664) | [7m04s](https://github.com/iree-org/iree/actions/runs/33760490301/job/100665364235) | [7m04s](https://github.com/iree-org/iree/actions/runs/33760490301/job/100665364235) | 11 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 11 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/33766944749/job/100687209088) | [2m57s](https://github.com/iree-org/iree/actions/runs/33758667370/job/100659305231) | [2m57s](https://github.com/iree-org/iree/actions/runs/33758667370/job/100659305231) | 11 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33736882103/job/100589880209) | [2m52s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100659341560) | [2m52s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100659341560) | 11 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 11 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/33751321219/job/100635361471) | [2m08s](https://github.com/iree-org/iree/actions/runs/33736967104/job/100590429493) | [2m08s](https://github.com/iree-org/iree/actions/runs/33736967104/job/100590429493) | 11 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33751321219/job/100635361754) | [2m07s](https://github.com/iree-org/iree/actions/runs/33736967104/job/100590429497) | [2m07s](https://github.com/iree-org/iree/actions/runs/33736967104/job/100590429497) | 11 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 172 | 1% (1/172) |  | 1h31m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 244 | 1% (2/244) |  | 1h33m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 165 | 0% (0/165) |  | 1h34m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 210 | 4% (9/210) |  | 1h36m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h05m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h21m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
