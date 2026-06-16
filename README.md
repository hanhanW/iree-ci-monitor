# iree-ci-monitor

_Updated: 2026-06-16 07:09 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [12m28s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569594) | [38m41s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639618) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 0 | — | — | 0 | [16m37s](https://github.com/iree-org/iree/actions/runs/27605082606/job/81621606844) | [28m14s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629757838) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [16m19s](https://github.com/iree-org/iree/actions/runs/27605082606/job/81621606688) | [27m59s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639599) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | [11m44s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629757817) | [24m25s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392473) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [5m41s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569758) | [21m17s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639344) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [4m24s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569489) | [18m46s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392707) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 0 | — | — | 0 | [8m11s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569841) | [18m10s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928190) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [6m48s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928331) | [15m57s](https://github.com/iree-org/iree/actions/runs/27605082606/job/81621606832) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [5m50s](https://github.com/iree-org/iree/actions/runs/27605082606/job/81621606821) | [14m32s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569773) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569588) | [13m26s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928392) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [6m01s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639590) | [12m03s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569534) | 25% (1/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 35 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27608729551/job/81628261979) | [2m13s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853619) | 0% (0/15) | 35 |
| `macos-14` | github-hosted | 21 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853479) | [1m27s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459967) | 0% (0/6) | 21 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m26s](https://github.com/iree-org/iree/actions/runs/27612557681/job/81640353861) | [1m26s](https://github.com/iree-org/iree/actions/runs/27612557681/job/81640353861) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27608729551/job/81628261858) | [42s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656854211) | 0% (0/6) | 21 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 24 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928306) | [19s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392698) | 12% (1/8) | 24 |
| `ubuntu-24.04` | github-hosted | 128 | 0 | — | — | 2 | [8s](https://github.com/iree-org/iree/actions/runs/27605082180/job/81620012603) | [18s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629757875) | 8% (3/40) | 127 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27617420578/job/81656798735) | [8s](https://github.com/iree-org/iree/actions/runs/27617420578/job/81656798729) | 0% (0/6) | 6 |
| `windows-2022` | github-hosted | 20 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853680) | [7s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853538) | 0% (0/6) | 20 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928302) | [3s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392832) | 0% (0/2) | `iree-mi308-1` |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/27612513862/job/81640204852) | [3s](https://github.com/iree-org/iree/actions/runs/27612513862/job/81640204852) | — | 1 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27608729551/job/81628261946) | [2s](https://github.com/iree-org/iree/actions/runs/27610895274/job/81651158701) | 0% (0/2) | 6 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27605082606/job/81621606638) | [2s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569563) | 0% (0/2) | 6 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [12m28s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569594) | [38m41s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639618) | [38m41s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639618) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [15m53s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639570) | [30m19s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392780) | [30m19s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392780) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 6 | 0 | — | — | [16m37s](https://github.com/iree-org/iree/actions/runs/27605082606/job/81621606844) | [28m14s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629757838) | [28m14s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629757838) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [12m33s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928322) | [27m59s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639599) | [27m59s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639599) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 0 | — | — | [11m44s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629757817) | [24m25s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392473) | [24m25s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392473) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [5m41s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569758) | [21m17s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639344) | [21m17s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639344) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [5m29s](https://github.com/iree-org/iree/actions/runs/27605082606/job/81621606919) | [20m09s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569669) | [20m09s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569669) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 6 | 0 | — | — | [4m24s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569489) | [18m46s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392707) | [18m46s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392707) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 6 | 0 | — | — | [8m11s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569841) | [18m10s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928190) | [18m10s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928190) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [3m40s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629758044) | [15m57s](https://github.com/iree-org/iree/actions/runs/27605082606/job/81621606832) | [15m57s](https://github.com/iree-org/iree/actions/runs/27605082606/job/81621606832) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [5m36s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569623) | [15m10s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392888) | [15m10s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392888) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928210) | [14m59s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569642) | [14m59s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569642) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392773) | [14m32s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569773) | [14m32s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569773) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569588) | [13m26s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928392) | [13m26s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928392) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [5m57s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392786) | [12m03s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569534) | [12m03s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569534) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 6 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27608729551/job/81628261979) | [2m17s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853805) | [2m17s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853805) | 6 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 6 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459978) | [2m13s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853619) | [2m13s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853619) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599460062) | [2m13s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853757) | [2m13s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853757) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 6 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27608729551/job/81628261855) | [1m51s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599460421) | [1m51s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599460421) | 6 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27617050521/job/81663000923) | [1m50s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459949) | [1m50s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459949) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 279 | 2% (5/279) |  | 29m15s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 192 | 2% (4/192) |  | 32m42s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 236 | 8% (20/236) |  | 38m12s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 204 | 2% (5/204) |  | 40m45s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 64 | 2% (1/64) |  | 54m21s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
