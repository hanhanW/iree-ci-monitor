# iree-ci-monitor

_Updated: 2026-06-10 18:26 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [48m59s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737059) | [52m35s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943646) | — | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [23m57s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736720) | [50m23s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943619) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [24m15s](https://github.com/iree-org/iree/actions/runs/27287978538/job/80602310878) | [47m04s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943499) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [19m22s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737278) | [44m50s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943702) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [24m08s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764813) | [44m18s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737035) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [17m12s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737142) | [39m35s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764770) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [13m53s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736856) | [25m01s](https://github.com/iree-org/iree/actions/runs/27287978538/job/80602311272) | — | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [20m30s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764676) | [23m50s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736725) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [5m50s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764918) | [23m05s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737030) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [14m35s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943592) | [19m19s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736944) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [8m34s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764909) | [14m40s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737000) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764703) | [8m20s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736833) | — | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764612) | [3m09s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737021) | — | 16 |
| `azure-linux-scale` | ossci | 16 | 0 | — | — | 0 | [34s](https://github.com/iree-org/iree/actions/runs/27287978502/job/80600434659) | [1m35s](https://github.com/iree-org/iree/actions/runs/27287271492/job/80597867736) | — | 16 |
| `ubuntu-24.04` | github-hosted | 71 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27289866882/job/80607579071) | [1m33s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943631) | — | 71 |
| `macos-14` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27287978502/job/80600434608) | [1m28s](https://github.com/iree-org/iree/actions/runs/27287271492/job/80597867351) | — | 9 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27289866882/job/80607579040) | [3s](https://github.com/iree-org/iree/actions/runs/27287978502/job/80600434604) | — | 9 |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27287271492/job/80597867189) | [3s](https://github.com/iree-org/iree/actions/runs/27289866882/job/80607579389) | — | 9 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27287271492/job/80597867348) | [2s](https://github.com/iree-org/iree/actions/runs/27289866882/job/80607579568) | — | 3 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736816) | [2s](https://github.com/iree-org/iree/actions/runs/27287978538/job/80602310840) | — | 4 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27287267195/job/80597824730) | [2s](https://github.com/iree-org/iree/actions/runs/27287267195/job/80597824875) | — | 3 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [48m59s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737059) | [52m35s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943646) | [52m35s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943646) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [23m57s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736720) | [50m23s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943619) | [50m23s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943619) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [24m15s](https://github.com/iree-org/iree/actions/runs/27287978538/job/80602310878) | [47m04s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943499) | [47m04s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943499) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [19m22s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737278) | [44m50s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943702) | [44m50s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943702) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [24m08s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764813) | [44m18s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737035) | [44m18s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737035) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [17m12s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737142) | [39m35s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764770) | [39m35s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764770) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [27m33s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736960) | [34m13s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764776) | [34m13s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764776) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [18m56s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737088) | [25m01s](https://github.com/iree-org/iree/actions/runs/27287978538/job/80602311272) | [25m01s](https://github.com/iree-org/iree/actions/runs/27287978538/job/80602311272) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [20m30s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764676) | [23m50s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736725) | [23m50s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736725) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764784) | [23m05s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737030) | [23m05s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737030) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [14m35s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943592) | [19m19s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736944) | [19m19s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736944) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [9m12s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764812) | [14m40s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737000) | [14m40s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737000) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [9m38s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943564) | [14m14s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737045) | [14m14s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737045) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [9m51s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943610) | [13m53s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736856) | [13m53s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736856) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [8m34s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764909) | [10m14s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736933) | [10m14s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736933) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764703) | [8m20s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736833) | [8m20s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736833) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943832) | [5m34s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737299) | [5m34s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737299) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 0 | — | — | [19s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764838) | [3m09s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737021) | [3m09s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737021) | 4 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 3 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27287978502/job/80600434589) | [2m02s](https://github.com/iree-org/iree/actions/runs/27287271492/job/80597867284) | [2m02s](https://github.com/iree-org/iree/actions/runs/27287271492/job/80597867284) | 3 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27289866882/job/80607578970) | [1m51s](https://github.com/iree-org/iree/actions/runs/27287271492/job/80597867162) | [1m51s](https://github.com/iree-org/iree/actions/runs/27287271492/job/80597867162) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 302 | 3% (9/302) |  | 8h13m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 263 | 7% (19/263) |  | 8h30m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 222 | 2% (4/222) |  | 8h32m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 229 | 2% (5/229) |  | 8h45m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 72 | 1% (1/72) |  | 8h47m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
