# iree-ci-monitor

_Updated: 2026-07-01 18:19 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [17m43s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292663) | [57m42s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748368) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [33m03s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292853) | [48m14s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748510) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292614) | [42m21s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748277) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [15m01s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292843) | [40m09s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748353) | 100% (1/1) | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [9m26s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292914) | [36m56s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748511) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [29m24s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748631) | [32m50s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748462) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [19m23s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748424) | [20m45s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748528) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [2m43s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748512) | [18m17s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292808) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [13m20s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292796) | [15m18s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748529) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [5m48s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292793) | [11m10s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748467) | 0% (0/1) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [9m24s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748483) | [9m45s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292775) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 12 | 0 | — | — | 0 | [1m10s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292696) | [7m46s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748396) | 25% (1/4) | 12 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292873) | [4m42s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748382) | 0% (0/1) | `iree-mi308-1` |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/28530040692/job/84592216857) | [10s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84592217790) | 0% (0/1) | 6 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/28530040692/job/84592216775) | [6s](https://github.com/iree-org/iree/actions/runs/28530040692/job/84592216698) | — | 3 |
| `ubuntu-24.04` | github-hosted | 45 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292780) | [3s](https://github.com/iree-org/iree/actions/runs/28530040692/job/84599491461) | 15% (2/13) | 45 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28530040692/job/84592216618) | [3s](https://github.com/iree-org/iree/actions/runs/28530040692/job/84592216751) | — | 3 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28530040692/job/84592216653) | [3s](https://github.com/iree-org/iree/actions/runs/28530040692/job/84592216728) | — | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28530040692/job/84592216887) | [1s](https://github.com/iree-org/iree/actions/runs/28530040692/job/84592216887) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [17m43s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292663) | [57m42s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748368) | [57m42s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748368) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [33m03s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292853) | [48m14s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748510) | [48m14s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748510) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292614) | [42m21s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748277) | [42m21s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748277) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [15m01s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292843) | [40m09s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748353) | [40m09s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748353) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292899) | [36m56s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748511) | [36m56s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748511) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [9m45s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292862) | [32m50s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748462) | [32m50s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748462) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292824) | [29m24s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748631) | [29m24s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748631) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292836) | [20m45s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748528) | [20m45s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748528) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [12m18s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292916) | [19m23s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748424) | [19m23s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748424) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [2m43s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748512) | [18m17s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292808) | [18m17s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292808) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [13m20s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292796) | [15m18s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748529) | [15m18s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748529) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [5m48s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292793) | [11m10s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748467) | [11m10s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748467) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [9m45s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292775) | [9m45s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292775) | [9m45s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292775) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [2m43s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748430) | [9m26s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292914) | [9m26s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292914) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [4m47s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292895) | [9m24s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748483) | [9m24s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748483) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 3 | 0 | — | — | [54s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292881) | [7m46s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748396) | [7m46s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748396) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 3 | 0 | — | — | [1m32s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292768) | [6m17s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748339) | [6m17s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748339) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292873) | [4m42s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748382) | [4m42s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748382) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292866) | [3m36s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748426) | [3m36s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748426) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28527902230/job/84572748182) | [1m10s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292696) | [1m10s](https://github.com/iree-org/iree/actions/runs/28530040682/job/84594292696) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 198 | 8% (16/198) |  | 7h25m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 226 | 1% (2/226) |  | 7h39m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 159 | 1% (1/159) |  | 7h39m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 185 | 1% (1/185) |  | 7h46m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 52 | 0% (0/52) |  | 7h47m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
