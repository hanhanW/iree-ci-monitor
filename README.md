# iree-ci-monitor

_Updated: 2026-08-11 12:28 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 16 | 0 | — | — | 0 | [29m14s](https://github.com/iree-org/iree/actions/runs/31495120113/job/93841001471) | [1h32m](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831692177) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 8 | 0 | — | — | 0 | [24m01s](https://github.com/iree-org/iree/actions/runs/31512099326/job/93851254733) | [1h23m](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831691988) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 16 | 0 | — | — | 0 | [5m51s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354356) | [57m45s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569469) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 8 | 0 | — | — | 0 | [16m35s](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831692010) | [54m06s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569129) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [25m40s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569133) | [50m45s](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831692170) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 8 | 0 | — | — | 0 | [25m41s](https://github.com/iree-org/iree/actions/runs/31495120113/job/93841001353) | [35m58s](https://github.com/iree-org/iree/actions/runs/31491657959/job/93818599279) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [13m49s](https://github.com/iree-org/iree/actions/runs/31495120113/job/93841001450) | [25m47s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569079) | 100% (3/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 16 | 0 | — | — | 0 | [8m28s](https://github.com/iree-org/iree/actions/runs/31491657959/job/93818599028) | [24m26s](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831692109) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 8 | 0 | — | — | 0 | [11m52s](https://github.com/iree-org/iree/actions/runs/31491657959/job/93818599115) | [21m04s](https://github.com/iree-org/iree/actions/runs/31495120113/job/93841001383) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 16 | 0 | — | — | 0 | [7m03s](https://github.com/iree-org/iree/actions/runs/31495120113/job/93841001300) | [13m07s](https://github.com/iree-org/iree/actions/runs/31495120113/job/93841001544) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [9m08s](https://github.com/iree-org/iree/actions/runs/31512099326/job/93851254849) | [12m00s](https://github.com/iree-org/iree/actions/runs/31497238925/job/93818090647) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `azure-windows-scale` | ossci | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31491657946/job/93814884749) | [7m56s](https://github.com/iree-org/iree/actions/runs/31497238879/job/93814900508) | 0% (0/3) | 8 |
| `ubuntu-24.04-arm` | github-hosted | 24 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/31503998192/job/93827999237) | [4m41s](https://github.com/iree-org/iree/actions/runs/31497238879/job/93814900473) | 0% (0/9) | 24 |
| `windows-2022` | github-hosted | 24 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31506388792/job/93828982601) | [2m58s](https://github.com/iree-org/iree/actions/runs/31497238879/job/93814900413) | 0% (0/9) | 24 |
| `azure-linux-scale` | ossci | 45 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/31506388792/job/93828983292) | [1m48s](https://github.com/iree-org/iree/actions/runs/31497238925/job/93814920910) | 0% (0/20) | 45 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m28s](https://github.com/iree-org/iree/actions/runs/31478323730/job/93737202823) | [1m28s](https://github.com/iree-org/iree/actions/runs/31478323730/job/93737202823) | 0% (0/1) | 1 |
| `macos-14` | github-hosted | 25 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/31480340510/job/93743642734) | [1m21s](https://github.com/iree-org/iree/actions/runs/31497238879/job/93814900505) | 0% (0/10) | 25 |
| `ubuntu-24.04` | github-hosted | 171 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31495120113/job/93841001356) | [50s](https://github.com/iree-org/iree/actions/runs/31480340510/job/93743642716) | 5% (3/57) | 169 |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31501898794/job/93813767796) | [9s](https://github.com/iree-org/iree/actions/runs/31501897454/job/93813828390) | 0% (0/9) | 24 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [30m52s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569214) | [1h34m](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831692171) | [1h34m](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831692171) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [25m05s](https://github.com/iree-org/iree/actions/runs/31491657959/job/93818599146) | [1h32m](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831692177) | [1h32m](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831692177) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 8 | 0 | — | — | [24m01s](https://github.com/iree-org/iree/actions/runs/31512099326/job/93851254733) | [1h23m](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831691988) | [1h23m](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831691988) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 8 | 0 | — | — | [15m06s](https://github.com/iree-org/iree/actions/runs/31497238925/job/93818090968) | [1h00m](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831692107) | [1h00m](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831692107) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 8 | 0 | — | — | [3m15s](https://github.com/iree-org/iree/actions/runs/31512099326/job/93851254866) | [57m45s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569469) | [57m45s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569469) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 8 | 0 | — | — | [16m35s](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831692010) | [54m06s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569129) | [54m06s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569129) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 8 | 0 | — | — | [25m40s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569133) | [50m45s](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831692170) | [50m45s](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831692170) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 8 | 0 | — | — | [25m41s](https://github.com/iree-org/iree/actions/runs/31495120113/job/93841001353) | [35m58s](https://github.com/iree-org/iree/actions/runs/31491657959/job/93818599279) | [35m58s](https://github.com/iree-org/iree/actions/runs/31491657959/job/93818599279) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [8m48s](https://github.com/iree-org/iree/actions/runs/31512099326/job/93851254925) | [34m03s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569191) | [34m03s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569191) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 8 | 0 | — | — | [13m49s](https://github.com/iree-org/iree/actions/runs/31495120113/job/93841001450) | [25m47s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569079) | [25m47s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569079) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [8m03s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354586) | [24m19s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569247) | [24m19s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569247) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 8 | 0 | — | — | [11m52s](https://github.com/iree-org/iree/actions/runs/31491657959/job/93818599115) | [21m04s](https://github.com/iree-org/iree/actions/runs/31495120113/job/93841001383) | [21m04s](https://github.com/iree-org/iree/actions/runs/31495120113/job/93841001383) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [10m16s](https://github.com/iree-org/iree/actions/runs/31503998300/job/93831692040) | [19m16s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569045) | [19m16s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93832569045) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [7m03s](https://github.com/iree-org/iree/actions/runs/31495120113/job/93841001300) | [12m33s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354574) | [12m33s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354574) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 8 | 0 | — | — | [9m08s](https://github.com/iree-org/iree/actions/runs/31512099326/job/93851254849) | [12m00s](https://github.com/iree-org/iree/actions/runs/31497238925/job/93818090647) | [12m00s](https://github.com/iree-org/iree/actions/runs/31497238925/job/93818090647) | 2 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31491657946/job/93814884749) | [7m56s](https://github.com/iree-org/iree/actions/runs/31497238879/job/93814900508) | [7m56s](https://github.com/iree-org/iree/actions/runs/31497238879/job/93814900508) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 8 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/31506388792/job/93828982682) | [5m26s](https://github.com/iree-org/iree/actions/runs/31497238879/job/93814900577) | [5m26s](https://github.com/iree-org/iree/actions/runs/31497238879/job/93814900577) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 8 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/31503998192/job/93827999166) | [5m22s](https://github.com/iree-org/iree/actions/runs/31497238879/job/93814900570) | [5m22s](https://github.com/iree-org/iree/actions/runs/31497238879/job/93814900570) | 8 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 8 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710732) | [5m13s](https://github.com/iree-org/iree/actions/runs/31497238879/job/93814900316) | [5m13s](https://github.com/iree-org/iree/actions/runs/31497238879/job/93814900316) | 8 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 8 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31503998192/job/93827999154) | [4m58s](https://github.com/iree-org/iree/actions/runs/31497238879/job/93814900361) | [4m58s](https://github.com/iree-org/iree/actions/runs/31497238879/job/93814900361) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 161 | 6% (9/161) |  | 13m14s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 186 | 0% (0/186) |  | 33m06s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 150 | 3% (5/150) |  | 35m33s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 132 | 11% (15/132) |  | 39m19s ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h23m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
