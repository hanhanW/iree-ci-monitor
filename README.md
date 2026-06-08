# iree-ci-monitor

_Updated: 2026-06-08 12:10 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 40 | 0 | — | — | 0 | [57m59s](https://github.com/iree-org/iree/actions/runs/27148693300/job/80145192466) | [2h42m](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749356) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 20 | 0 | — | — | 0 | [1h47m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132492555) | [2h19m](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749324) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 20 | 0 | — | — | 0 | [22m27s](https://github.com/iree-org/iree/actions/runs/27145054427/job/80122727552) | [1h58m](https://github.com/iree-org/iree/actions/runs/27147332262/job/80130583909) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 20 | 0 | — | — | 0 | [51m58s](https://github.com/iree-org/iree/actions/runs/27148693300/job/80145192408) | [1h40m](https://github.com/iree-org/iree/actions/runs/27147332262/job/80130584032) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 40 | 0 | — | — | 0 | [14m31s](https://github.com/iree-org/iree/actions/runs/27148739726/job/80145376397) | [1h29m](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132467) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 40 | 0 | — | — | 0 | [27m36s](https://github.com/iree-org/iree/actions/runs/27147331764/job/80131078738) | [57m14s](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132634) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 40 | 0 | — | — | 0 | [16m03s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749314) | [52m16s](https://github.com/iree-org/iree/actions/runs/27147334646/job/80131349496) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 20 | 0 | — | — | 0 | [9m15s](https://github.com/iree-org/iree/actions/runs/27144972690/job/80122459747) | [49m51s](https://github.com/iree-org/iree/actions/runs/27147331764/job/80131078733) | 0% (0/1) | `iree-mi308-1` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 20 | 0 | — | — | 0 | [17m45s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749181) | [49m40s](https://github.com/iree-org/iree/actions/runs/27148739726/job/80145376325) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 20 | 0 | — | — | 0 | [18m24s](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132492956) | [28m44s](https://github.com/iree-org/iree/actions/runs/27147331909/job/80130943977) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 20 | 0 | — | — | 0 | [14m14s](https://github.com/iree-org/iree/actions/runs/27144974545/job/80122577417) | [28m27s](https://github.com/iree-org/iree/actions/runs/27147334646/job/80131349018) | 0% (0/1) | `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 536 | 0 | — | — | 0 | [2m13s](https://github.com/iree-org/iree/actions/runs/27144973630/job/80120085621) | [26m50s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749312) | 0% (0/14) | 448 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 20 | 0 | — | — | 0 | [12m38s](https://github.com/iree-org/iree/actions/runs/27144974545/job/80122577749) | [24m44s](https://github.com/iree-org/iree/actions/runs/27147334646/job/80131349176) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 80 | 0 | — | — | 0 | [5m18s](https://github.com/iree-org/iree/actions/runs/27144972690/job/80122459696) | [22m31s](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493077) | 0% (0/4) | 73 |
| `ubuntu-24.04-arm` | github-hosted | 75 | 0 | — | — | 0 | [1m56s](https://github.com/iree-org/iree/actions/runs/27148692771/job/80138937237) | [17m18s](https://github.com/iree-org/iree/actions/runs/27144974553/job/80121038584) | — | 64 |
| `windows-2022` | github-hosted | 75 | 0 | — | — | 0 | [3m51s](https://github.com/iree-org/iree/actions/runs/27147331954/job/80129564504) | [15m41s](https://github.com/iree-org/iree/actions/runs/27147330955/job/80129616227) | — | 65 |
| `macos-14` | github-hosted | 76 | 0 | — | — | 0 | [2m08s](https://github.com/iree-org/iree/actions/runs/27148692771/job/80138937366) | [15m13s](https://github.com/iree-org/iree/actions/runs/27144974553/job/80121039009) | 0% (0/1) | 67 |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | — | 0 | [20s](https://github.com/iree-org/iree/actions/runs/27147326143/job/80128600066) | [13m35s](https://github.com/iree-org/iree/actions/runs/27148732438/job/80133669608) | — | 24 |
| `azure-windows-scale` | ossci | 25 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/27144972704/job/80120821125) | [4m03s](https://github.com/iree-org/iree/actions/runs/27147335331/job/80129639409) | — | 23 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 20 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27149692727/job/80157183899) | [3m04s](https://github.com/iree-org/iree/actions/runs/27145054427/job/80122727595) | 0% (0/1) | 20 |
| `azure-linux-scale` | ossci | 127 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/27147331706/job/80129627409) | [2m57s](https://github.com/iree-org/iree/actions/runs/27149692727/job/80151546215) | 0% (0/3) | 127 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m23s](https://github.com/iree-org/iree/actions/runs/27132797840/job/80077707290) | [1m23s](https://github.com/iree-org/iree/actions/runs/27132797840/job/80077707290) | 0% (0/1) | 1 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/27132751798/job/80077554342) | [4s](https://github.com/iree-org/iree/actions/runs/27132751798/job/80077554342) | 100% (1/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 20 | 0 | — | — | [1h02m](https://github.com/iree-org/iree/actions/runs/27147331764/job/80131078734) | [2h25m](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749366) | [2h49m](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132660) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 20 | 0 | — | — | [1h47m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132492555) | [2h19m](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749324) | [2h24m](https://github.com/iree-org/iree/actions/runs/27147334646/job/80131349118) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 20 | 0 | — | — | [22m27s](https://github.com/iree-org/iree/actions/runs/27145054427/job/80122727552) | [1h58m](https://github.com/iree-org/iree/actions/runs/27147332262/job/80130583909) | [2h02m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132492044) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 20 | 0 | — | — | [45m52s](https://github.com/iree-org/iree/actions/runs/27147331909/job/80130944026) | [1h51m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493543) | [2h42m](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749356) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 20 | 0 | — | — | [51m58s](https://github.com/iree-org/iree/actions/runs/27148693300/job/80145192408) | [1h40m](https://github.com/iree-org/iree/actions/runs/27147332262/job/80130584032) | [1h44m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493458) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 20 | 0 | — | — | [17m19s](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132492999) | [1h04m](https://github.com/iree-org/iree/actions/runs/27147334646/job/80131349207) | [1h48m](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132521) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 20 | 0 | — | — | [13m38s](https://github.com/iree-org/iree/actions/runs/27148693300/job/80145192602) | [1h00m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493372) | [1h29m](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132467) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 20 | 0 | — | — | [27m12s](https://github.com/iree-org/iree/actions/runs/27148739726/job/80145376612) | [53m06s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749353) | [57m14s](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132634) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 20 | 0 | — | — | [16m03s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749314) | [51m15s](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132492569) | [52m16s](https://github.com/iree-org/iree/actions/runs/27147334646/job/80131349496) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 20 | 0 | — | — | [9m15s](https://github.com/iree-org/iree/actions/runs/27144972690/job/80122459747) | [49m51s](https://github.com/iree-org/iree/actions/runs/27147331764/job/80131078733) | [53m45s](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493434) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 20 | 0 | — | — | [37m19s](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132553) | [49m48s](https://github.com/iree-org/iree/actions/runs/27147331764/job/80131078559) | [59m37s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749339) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 20 | 0 | — | — | [17m45s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749181) | [49m40s](https://github.com/iree-org/iree/actions/runs/27148739726/job/80145376325) | [1h04m](https://github.com/iree-org/iree/actions/runs/27147331764/job/80131078810) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 20 | 0 | — | — | [16m19s](https://github.com/iree-org/iree/actions/runs/27148739726/job/80145376400) | [43m17s](https://github.com/iree-org/iree/actions/runs/27147331764/job/80131078723) | [1h25m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493446) | 3 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 25 | 0 | — | — | [8m21s](https://github.com/iree-org/iree/actions/runs/27147330955/job/80129616107) | [31m35s](https://github.com/iree-org/iree/actions/runs/27144972800/job/80120965183) | [33m18s](https://github.com/iree-org/iree/actions/runs/27147331706/job/80129627373) | 19 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 25 | 0 | — | — | [5m18s](https://github.com/iree-org/iree/actions/runs/27144452812/job/80118730054) | [31m17s](https://github.com/iree-org/iree/actions/runs/27144973263/job/80120799853) | [34m30s](https://github.com/iree-org/iree/actions/runs/27147330955/job/80129616345) | 20 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 33 | 0 | — | — | [3m44s](https://github.com/iree-org/iree/actions/runs/27144452905/job/80118755914) | [29m57s](https://github.com/iree-org/iree/actions/runs/27147331706/job/80129627321) | [31m38s](https://github.com/iree-org/iree/actions/runs/27144972800/job/80120965137) | 18 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 33 | 0 | — | — | [3m18s](https://github.com/iree-org/iree/actions/runs/27144452905/job/80118756026) | [29m09s](https://github.com/iree-org/iree/actions/runs/27147331706/job/80129627149) | [33m37s](https://github.com/iree-org/iree/actions/runs/27144972800/job/80120965331) | 22 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 20 | 0 | — | — | [18m24s](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132492956) | [28m44s](https://github.com/iree-org/iree/actions/runs/27147331909/job/80130943977) | [35m48s](https://github.com/iree-org/iree/actions/runs/27148739726/job/80145376417) | 1 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 20 | 0 | — | — | [16m19s](https://github.com/iree-org/iree/actions/runs/27145054427/job/80122727593) | [28m41s](https://github.com/iree-org/iree/actions/runs/27147332262/job/80130583807) | [32m05s](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132201) | 18 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 20 | 0 | — | — | [14m14s](https://github.com/iree-org/iree/actions/runs/27144974545/job/80122577417) | [28m27s](https://github.com/iree-org/iree/actions/runs/27147334646/job/80131349018) | [39m02s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749119) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 355 | 1% (4/355) |  | 18m57s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 294 | 3% (10/294) |  | 29m42s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 258 | 0% (0/258) |  | 31m13s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 278 | 1% (2/278) |  | 33m03s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 83 | 0% (0/83) |  | 34m17s ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h29m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h42m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h58m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h19m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h40m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
