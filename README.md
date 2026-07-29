# iree-ci-monitor

_Updated: 2026-07-29 11:38 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 20 | 0 | — | — | 1 | [17m30s](https://github.com/iree-org/iree/actions/runs/30465381855/job/90623814836) | [41m08s](https://github.com/iree-org/iree/actions/runs/30440782355/job/90541339594) | 0% (0/5) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 10 | 0 | — | — | 0 | [20m13s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819460) | [37m25s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599905892) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [12m21s](https://github.com/iree-org/iree/actions/runs/30452408293/job/90579528076) | [35m10s](https://github.com/iree-org/iree/actions/runs/30451617302/job/90616390311) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [9m18s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819505) | [30m26s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599905705) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 10 | 0 | — | — | 0 | [3m32s](https://github.com/iree-org/iree/actions/runs/30474877493/job/90665834203) | [27m23s](https://github.com/iree-org/iree/actions/runs/30440403038/job/90544093562) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 20 | 0 | — | — | 0 | [6m56s](https://github.com/iree-org/iree/actions/runs/30447115707/job/90566266707) | [24m40s](https://github.com/iree-org/iree/actions/runs/30440403038/job/90544093706) | 0% (0/6) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 10 | 0 | — | — | 0 | [9m57s](https://github.com/iree-org/iree/actions/runs/30451617302/job/90616390244) | [24m30s](https://github.com/iree-org/iree/actions/runs/30447115707/job/90566266592) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 20 | 0 | — | — | 0 | [5m10s](https://github.com/iree-org/iree/actions/runs/30465381855/job/90623814715) | [19m19s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599906146) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30474877493/job/90665834290) | [16m00s](https://github.com/iree-org/iree/actions/runs/30440403038/job/90544093652) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 20 | 0 | — | — | 0 | [6m01s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599906144) | [14m48s](https://github.com/iree-org/iree/actions/runs/30452408293/job/90579528083) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 10 | 0 | — | — | 0 | [7m37s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599905789) | [14m09s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819406) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30452408293/job/90579528050) | [7m24s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819550) | 0% (0/3) | `iree-mi308-1` |
| `azure-linux-scale` | ossci | 59 | 0 | — | — | 2 | [9s](https://github.com/iree-org/iree/actions/runs/30452408544/job/90577498266) | [3m41s](https://github.com/iree-org/iree/actions/runs/30458637745/job/90598709900) | 0% (0/20) | 59 |
| `macos-15-intel` | github-hosted | 2 | 0 | — | — | 1 | [5s](https://github.com/iree-org/iree/actions/runs/30442398898/job/90544541673) | [2m06s](https://github.com/iree-org/iree/actions/runs/30458637745/job/90598709729) | 0% (0/1) | 2 |
| `windows-2022` | github-hosted | 30 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/30474877288/job/90663629594) | [1m55s](https://github.com/iree-org/iree/actions/runs/30477920655/job/90664245649) | 0% (0/9) | 30 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 2 | 0 | — | — | 0 | [1m27s](https://github.com/iree-org/iree/actions/runs/30442444644/job/90544695322) | [1m32s](https://github.com/iree-org/iree/actions/runs/30458637745/job/90598709699) | 0% (0/1) | 2 |
| `macos-14` | github-hosted | 32 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/30452408544/job/90577498273) | [1m27s](https://github.com/iree-org/iree/actions/runs/30440780665/job/90539358751) | 0% (0/10) | 32 |
| `ubuntu-24.04` | github-hosted | 205 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/30465381855/job/90623814551) | [1m18s](https://github.com/iree-org/iree/actions/runs/30451614276/job/90613381060) | 2% (1/56) | 201 |
| `ubuntu-24.04-arm` | github-hosted | 30 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30458410008/job/90597918235) | [41s](https://github.com/iree-org/iree/actions/runs/30458637745/job/90598709614) | 0% (0/9) | 30 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30465381855/job/90623814390) | [32s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819222) | 0% (0/3) | 10 |
| `ubuntu-latest` | github-hosted | 27 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30458633663/job/90598629846) | [9s](https://github.com/iree-org/iree/actions/runs/30462813387/job/90613022271) | 0% (0/9) | 27 |
| `azure-windows-scale` | ossci | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30452408544/job/90577498374) | [2s](https://github.com/iree-org/iree/actions/runs/30477920655/job/90664245867) | 0% (0/3) | 10 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [26m15s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819526) | [44m36s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599906075) | [44m36s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599906075) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 10 | 0 | — | — | [20m13s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819460) | [37m25s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599905892) | [37m25s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599905892) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [15m33s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819426) | [37m15s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599906019) | [37m15s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599906019) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [3m10s](https://github.com/iree-org/iree/actions/runs/30474877493/job/90665834527) | [35m52s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599906109) | [35m52s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599906109) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 10 | 0 | — | — | [12m21s](https://github.com/iree-org/iree/actions/runs/30452408293/job/90579528076) | [35m10s](https://github.com/iree-org/iree/actions/runs/30451617302/job/90616390311) | [35m10s](https://github.com/iree-org/iree/actions/runs/30451617302/job/90616390311) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [8m19s](https://github.com/iree-org/iree/actions/runs/30447115707/job/90566266541) | [32m06s](https://github.com/iree-org/iree/actions/runs/30440782355/job/90541339201) | [32m06s](https://github.com/iree-org/iree/actions/runs/30440782355/job/90541339201) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 10 | 0 | — | — | [9m18s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819505) | [30m26s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599905705) | [30m26s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599905705) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 10 | 0 | — | — | [3m32s](https://github.com/iree-org/iree/actions/runs/30474877493/job/90665834203) | [27m23s](https://github.com/iree-org/iree/actions/runs/30440403038/job/90544093562) | [27m23s](https://github.com/iree-org/iree/actions/runs/30440403038/job/90544093562) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 0 | — | — | [6m28s](https://github.com/iree-org/iree/actions/runs/30465381855/job/90623814759) | [25m53s](https://github.com/iree-org/iree/actions/runs/30440782355/job/90541339624) | [25m53s](https://github.com/iree-org/iree/actions/runs/30440782355/job/90541339624) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [6m56s](https://github.com/iree-org/iree/actions/runs/30447115707/job/90566266707) | [24m40s](https://github.com/iree-org/iree/actions/runs/30440403038/job/90544093706) | [24m40s](https://github.com/iree-org/iree/actions/runs/30440403038/job/90544093706) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 10 | 0 | — | — | [9m57s](https://github.com/iree-org/iree/actions/runs/30451617302/job/90616390244) | [24m30s](https://github.com/iree-org/iree/actions/runs/30447115707/job/90566266592) | [24m30s](https://github.com/iree-org/iree/actions/runs/30447115707/job/90566266592) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [6m43s](https://github.com/iree-org/iree/actions/runs/30447115707/job/90566266673) | [19m19s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599906146) | [19m19s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599906146) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30474877493/job/90665834290) | [16m00s](https://github.com/iree-org/iree/actions/runs/30440403038/job/90544093652) | [16m00s](https://github.com/iree-org/iree/actions/runs/30440403038/job/90544093652) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 10 | 0 | — | — | [7m37s](https://github.com/iree-org/iree/actions/runs/30458410198/job/90599905789) | [14m09s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819406) | [14m09s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819406) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 0 | — | — | [5m22s](https://github.com/iree-org/iree/actions/runs/30440403038/job/90544093740) | [12m22s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819576) | [12m22s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819576) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30452408293/job/90579528050) | [7m24s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819550) | [7m24s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819550) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_tsan / linux_x64_clang_tsan | `azure-linux-scale` | 1 | 0 | — | — | [3m48s](https://github.com/iree-org/iree/actions/runs/30458637745/job/90598709968) | [3m48s](https://github.com/iree-org/iree/actions/runs/30458637745/job/90598709968) | [3m48s](https://github.com/iree-org/iree/actions/runs/30458637745/job/90598709968) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 10 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30452408544/job/90577498447) | [3m44s](https://github.com/iree-org/iree/actions/runs/30458637745/job/90598710127) | [3m44s](https://github.com/iree-org/iree/actions/runs/30458637745/job/90598710127) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 5 | 0 | — | — | [1m19s](https://github.com/iree-org/iree/actions/runs/30477920655/job/90664245952) | [3m42s](https://github.com/iree-org/iree/actions/runs/30458637745/job/90598710072) | [3m42s](https://github.com/iree-org/iree/actions/runs/30458637745/job/90598710072) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 10 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/30458410008/job/90597918529) | [3m41s](https://github.com/iree-org/iree/actions/runs/30458637745/job/90598709900) | [3m41s](https://github.com/iree-org/iree/actions/runs/30458637745/job/90598709900) | 10 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 282 | 1% (4/281) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 232 | 5% (11/232) |  | 4m33s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 213 | 1% (2/213) |  | 8m31s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 203 | 2% (4/203) |  | 9m08s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 63 | 3% (2/63) |  | 9m09s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
