# iree-ci-monitor

_Updated: 2026-07-17 11:39 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [23m00s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121317) | [38m34s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913209) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 10 | 0 | — | — | 0 | [9m34s](https://github.com/iree-org/iree/actions/runs/29590130059/job/87919369188) | [31m28s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913292) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 5 | 0 | — | — | 0 | [13m34s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121334) | [30m42s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913254) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 5 | 0 | — | — | 0 | [15m47s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416388) | [29m43s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913198) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `azure-windows-scale` | ossci | 10 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29596128373/job/87936885377) | [29m25s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026788) | 100% (1/1) | 10 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121153) | [27m25s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913406) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 10 | 0 | — | — | 0 | [13m47s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913283) | [20m10s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416573) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 10 | 0 | — | — | 0 | [9m47s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416524) | [19m02s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913326) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [5m26s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121277) | [17m49s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913252) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 10 | 0 | — | — | 0 | [5m26s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121355) | [17m33s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913325) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121267) | [8m07s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913349) | 0% (0/1) | `iree-mi308-1` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29590130059/job/87919369246) | [4m59s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416397) | 0% (0/1) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416325) | [1m49s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913141) | 0% (0/1) | `shark75-ci` |
| `azure-linux-scale` | ossci | 60 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/29587481593/job/87908484478) | [1m48s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87896085684) | 11% (1/9) | 60 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m26s](https://github.com/iree-org/iree/actions/runs/29571578881/job/87856366233) | [1m26s](https://github.com/iree-org/iree/actions/runs/29571578881/job/87856366233) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 30 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/29587481593/job/87908484187) | [40s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026767) | 0% (0/3) | 30 |
| `windows-2022` | github-hosted | 30 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29581337585/job/87887549407) | [5s](https://github.com/iree-org/iree/actions/runs/29590130007/job/87916891431) | 0% (0/3) | 30 |
| `ubuntu-24.04` | github-hosted | 162 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913171) | [4s](https://github.com/iree-org/iree/actions/runs/29588247210/job/87910509110) | 10% (2/21) | 159 |
| `macos-14` | github-hosted | 31 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29581337585/job/87887549336) | [4s](https://github.com/iree-org/iree/actions/runs/29576914390/job/87873389443) | 0% (0/4) | 31 |
| `ubuntu-latest` | github-hosted | 36 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29569274131/job/87848982825) | [4s](https://github.com/iree-org/iree/actions/runs/29588678289/job/87911975261) | 0% (0/3) | 36 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/29571537612/job/87856234453) | [4s](https://github.com/iree-org/iree/actions/runs/29571537612/job/87856234453) | 0% (0/1) | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121207) | [3s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416278) | 0% (0/1) | 5 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 5 | 0 | — | — | [23m00s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121317) | [38m34s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913209) | [38m34s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913209) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [12m03s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121344) | [31m28s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913292) | [31m28s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913292) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 5 | 0 | — | — | [13m34s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121334) | [30m42s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913254) | [30m42s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913254) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 5 | 0 | — | — | [15m47s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416388) | [29m43s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913198) | [29m43s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913198) | 2 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 10 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29596128373/job/87936885377) | [29m25s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026788) | [29m25s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026788) | 10 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121153) | [27m25s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913406) | [27m25s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913406) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 5 | 0 | — | — | [13m47s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913283) | [20m10s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416573) | [20m10s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416573) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [9m47s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416524) | [19m02s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913326) | [19m02s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913326) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 5 | 0 | — | — | [14m14s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913194) | [18m30s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121409) | [18m30s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121409) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [9m34s](https://github.com/iree-org/iree/actions/runs/29590130059/job/87919369188) | [18m05s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416528) | [18m05s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416528) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 5 | 0 | — | — | [5m26s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121277) | [17m49s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913252) | [17m49s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913252) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [7m54s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121282) | [17m33s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913325) | [17m33s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913325) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [10m09s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913329) | [15m23s](https://github.com/iree-org/iree/actions/runs/29590130059/job/87919369343) | [15m23s](https://github.com/iree-org/iree/actions/runs/29590130059/job/87919369343) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [5m26s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121355) | [11m22s](https://github.com/iree-org/iree/actions/runs/29590130059/job/87919369293) | [11m22s](https://github.com/iree-org/iree/actions/runs/29590130059/job/87919369293) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29583920211/job/87898121267) | [8m07s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913349) | [8m07s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913349) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29590130059/job/87919369246) | [4m59s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416397) | [4m59s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416397) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 10 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87913685496) | [4m39s](https://github.com/iree-org/iree/actions/runs/29581337596/job/87887563713) | [4m39s](https://github.com/iree-org/iree/actions/runs/29581337596/job/87887563713) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 7 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29581337585/job/87887549418) | [2m31s](https://github.com/iree-org/iree/actions/runs/29585485783/job/87901753103) | [2m31s](https://github.com/iree-org/iree/actions/runs/29585485783/job/87901753103) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 10 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/29596128373/job/87936885443) | [2m25s](https://github.com/iree-org/iree/actions/runs/29585485783/job/87901753061) | [2m25s](https://github.com/iree-org/iree/actions/runs/29585485783/job/87901753061) | 10 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416325) | [1m49s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913141) | [1m49s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913141) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 132 | 10% (13/132) |  | 1h29m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 144 | 1% (2/144) |  | 1h31m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 164 | 1% (1/164) |  | 1h31m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 129 | 0% (0/129) |  | 1h33m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 38 | 0% (0/38) |  | 1h33m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
