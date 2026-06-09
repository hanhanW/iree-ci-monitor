# iree-ci-monitor

_Updated: 2026-06-08 18:17 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 22 | 0 | — | — | 0 | [57m59s](https://github.com/iree-org/iree/actions/runs/27148693300/job/80145192466) | [2h42m](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749356) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 11 | 0 | — | — | 0 | [1h47m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132492555) | [2h24m](https://github.com/iree-org/iree/actions/runs/27147334646/job/80131349118) | — | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 11 | 0 | — | — | 0 | [54m05s](https://github.com/iree-org/iree/actions/runs/27148693300/job/80145192225) | [2h02m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132492044) | — | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 11 | 0 | — | — | 0 | [51m58s](https://github.com/iree-org/iree/actions/runs/27148693300/job/80145192408) | [1h44m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493458) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 22 | 0 | — | — | 0 | [14m31s](https://github.com/iree-org/iree/actions/runs/27148739726/job/80145376397) | [1h29m](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132467) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [17m45s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749181) | [1h04m](https://github.com/iree-org/iree/actions/runs/27147331764/job/80131078810) | — | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 22 | 0 | — | — | 0 | [35m03s](https://github.com/iree-org/iree/actions/runs/27148739726/job/80145376358) | [57m14s](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132634) | — | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 11 | 0 | — | — | 0 | [13m03s](https://github.com/iree-org/iree/actions/runs/27148693300/job/80145192280) | [53m45s](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493434) | — | `iree-mi308-1` |
| `Linux,X64,rdna3` | self-hosted | 22 | 0 | — | — | 0 | [12m59s](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132638) | [52m16s](https://github.com/iree-org/iree/actions/runs/27147334646/job/80131349496) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 11 | 0 | — | — | 0 | [12m52s](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132179) | [39m02s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749119) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [19m22s](https://github.com/iree-org/iree/actions/runs/27148693300/job/80145192782) | [35m48s](https://github.com/iree-org/iree/actions/runs/27148739726/job/80145376417) | — | `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 166 | 0 | — | — | 0 | [5m28s](https://github.com/iree-org/iree/actions/runs/27147332324/job/80130136578) | [28m14s](https://github.com/iree-org/iree/actions/runs/27148739726/job/80133679301) | — | 166 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [15m48s](https://github.com/iree-org/iree/actions/runs/27148739726/job/80145376538) | [25m02s](https://github.com/iree-org/iree/actions/runs/27147331909/job/80130943829) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 44 | 0 | — | — | 0 | [2m34s](https://github.com/iree-org/iree/actions/runs/27148739726/job/80145376373) | [22m31s](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493077) | — | 44 |
| `ubuntu-latest` | github-hosted | 4 | 0 | — | — | 0 | [13m35s](https://github.com/iree-org/iree/actions/runs/27148732438/job/80133669608) | [13m52s](https://github.com/iree-org/iree/actions/runs/27148732438/job/80133669664) | 0% (0/1) | 4 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [1m56s](https://github.com/iree-org/iree/actions/runs/27148692771/job/80138937237) | [12m05s](https://github.com/iree-org/iree/actions/runs/27148739165/job/80138193865) | — | 18 |
| `windows-2022` | github-hosted | 18 | 0 | — | — | 0 | [1m08s](https://github.com/iree-org/iree/actions/runs/27147332324/job/80130136586) | [11m34s](https://github.com/iree-org/iree/actions/runs/27147332324/job/80130136601) | — | 18 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27149694916/job/80151537090) | [7m54s](https://github.com/iree-org/iree/actions/runs/27147332324/job/80130136830) | — | 6 |
| `macos-14` | github-hosted | 18 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27148739165/job/80138193641) | [5m54s](https://github.com/iree-org/iree/actions/runs/27148739165/job/80138193771) | — | 18 |
| `azure-linux-scale` | ossci | 29 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/27147331301/job/80147284423) | [3m59s](https://github.com/iree-org/iree/actions/runs/27147332324/job/80130136756) | — | 29 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27150305022/job/80166925460) | [2m32s](https://github.com/iree-org/iree/actions/runs/27147334646/job/80131348967) | — | 11 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 11 | 0 | — | — | [1h02m](https://github.com/iree-org/iree/actions/runs/27147331764/job/80131078734) | [2h49m](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132660) | [2h49m](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132660) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 11 | 0 | — | — | [45m52s](https://github.com/iree-org/iree/actions/runs/27147331909/job/80130944026) | [2h42m](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749356) | [2h42m](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749356) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 11 | 0 | — | — | [1h47m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132492555) | [2h24m](https://github.com/iree-org/iree/actions/runs/27147334646/job/80131349118) | [2h24m](https://github.com/iree-org/iree/actions/runs/27147334646/job/80131349118) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 11 | 0 | — | — | [54m05s](https://github.com/iree-org/iree/actions/runs/27148693300/job/80145192225) | [2h02m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132492044) | [2h02m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132492044) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 11 | 0 | — | — | [17m19s](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132492999) | [1h48m](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132521) | [1h48m](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132521) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 11 | 0 | — | — | [51m58s](https://github.com/iree-org/iree/actions/runs/27148693300/job/80145192408) | [1h44m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493458) | [1h44m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493458) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 11 | 0 | — | — | [14m15s](https://github.com/iree-org/iree/actions/runs/27147331909/job/80130943987) | [1h29m](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132467) | [1h29m](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132467) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 11 | 0 | — | — | [11m30s](https://github.com/iree-org/iree/actions/runs/27147334646/job/80131349297) | [1h25m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493446) | [1h25m](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493446) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 11 | 0 | — | — | [17m45s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749181) | [1h04m](https://github.com/iree-org/iree/actions/runs/27147331764/job/80131078810) | [1h04m](https://github.com/iree-org/iree/actions/runs/27147331764/job/80131078810) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 11 | 0 | — | — | [37m30s](https://github.com/iree-org/iree/actions/runs/27148693300/job/80145192463) | [59m37s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749339) | [59m37s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749339) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 11 | 0 | — | — | [27m36s](https://github.com/iree-org/iree/actions/runs/27147331764/job/80131078738) | [57m14s](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132634) | [57m14s](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132634) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 11 | 0 | — | — | [13m03s](https://github.com/iree-org/iree/actions/runs/27148693300/job/80145192280) | [53m45s](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493434) | [53m45s](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493434) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 11 | 0 | — | — | [16m03s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749314) | [52m16s](https://github.com/iree-org/iree/actions/runs/27147334646/job/80131349496) | [52m16s](https://github.com/iree-org/iree/actions/runs/27147334646/job/80131349496) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 11 | 0 | — | — | [12m52s](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132179) | [39m02s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749119) | [39m02s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749119) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 11 | 0 | — | — | [17m15s](https://github.com/iree-org/iree/actions/runs/27147331820/job/80131749338) | [36m15s](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132393) | [36m15s](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132393) | 11 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 11 | 0 | — | — | [19m22s](https://github.com/iree-org/iree/actions/runs/27148693300/job/80145192782) | [35m48s](https://github.com/iree-org/iree/actions/runs/27148739726/job/80145376417) | [35m48s](https://github.com/iree-org/iree/actions/runs/27148739726/job/80145376417) | 1 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 11 | 0 | — | — | [9m36s](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132310) | [34m21s](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493050) | [34m21s](https://github.com/iree-org/iree/actions/runs/27147331984/job/80132493050) | 11 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 11 | 0 | — | — | [17m49s](https://github.com/iree-org/iree/actions/runs/27147331764/job/80131078602) | [32m05s](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132201) | [32m05s](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131132201) | 11 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 11 | 0 | — | — | [16m20s](https://github.com/iree-org/iree/actions/runs/27147331479/job/80131133169) | [30m36s](https://github.com/iree-org/iree/actions/runs/27147331764/job/80131078498) | [30m36s](https://github.com/iree-org/iree/actions/runs/27147331764/job/80131078498) | 11 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | 4 | 0 | — | — | [28m14s](https://github.com/iree-org/iree/actions/runs/27148739726/job/80133679301) | [29m44s](https://github.com/iree-org/iree/actions/runs/27148693300/job/80133516547) | [29m44s](https://github.com/iree-org/iree/actions/runs/27148693300/job/80133516547) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 335 | 1% (4/335) |  | 6h26m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 278 | 4% (10/278) |  | 6h36m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 246 | 0% (0/246) |  | 6h38m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 266 | 1% (2/266) |  | 6h40m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 79 | 0% (0/79) |  | 6h41m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h29m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h42m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h04m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h24m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h44m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
