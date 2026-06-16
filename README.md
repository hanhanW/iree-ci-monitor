# iree-ci-monitor

_Updated: 2026-06-16 12:33 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [12m33s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928322) | [30m19s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392780) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [23m17s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928255) | [28m14s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629757838) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [12m28s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569594) | [24m49s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392754) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [17m37s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928336) | [24m25s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392473) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [6m48s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928331) | [20m09s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569669) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [8m21s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629757946) | [18m46s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392707) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [9m41s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629757927) | [18m10s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928190) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [8m42s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629757818) | [18m04s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392619) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [5m36s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569623) | [15m10s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392888) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [5m57s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392786) | [14m59s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569642) | 50% (1/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [12m08s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392714) | [13m26s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928392) | 0% (0/1) | `shark01-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 23 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81651180904) | [2m13s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853757) | 0% (0/8) | 23 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m26s](https://github.com/iree-org/iree/actions/runs/27612557681/job/81640353861) | [1m26s](https://github.com/iree-org/iree/actions/runs/27612557681/job/81640353861) | 0% (0/1) | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928321) | [19s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392482) | 25% (1/4) | 16 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27629651187/job/81700851210) | [13s](https://github.com/iree-org/iree/actions/runs/27629651046/job/81700890024) | 0% (0/3) | 9 |
| `ubuntu-24.04` | github-hosted | 84 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27610895035/job/81651115050) | [10s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81662945647) | 10% (2/21) | 83 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27610895274/job/81651158471) | [10s](https://github.com/iree-org/iree/actions/runs/27617050521/job/81663001135) | 0% (0/3) | 12 |
| `macos-14` | github-hosted | 13 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853660) | [8s](https://github.com/iree-org/iree/actions/runs/27610895274/job/81651158559) | 0% (0/4) | 13 |
| `windows-2022` | github-hosted | 12 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/27608729551/job/81628261954) | [7s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853538) | 0% (0/3) | 12 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569539) | [3s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392832) | 0% (0/1) | `iree-mi308-1` |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27612513862/job/81640204852) | [3s](https://github.com/iree-org/iree/actions/runs/27612513862/job/81640204852) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392595) | [2s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569563) | 0% (0/1) | 4 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853865) | [2s](https://github.com/iree-org/iree/actions/runs/27610895274/job/81651158701) | 0% (0/1) | 4 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [23m29s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928233) | [30m19s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392780) | [30m19s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392780) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [23m17s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928255) | [28m14s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629757838) | [28m14s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629757838) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [12m28s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569594) | [24m49s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392754) | [24m49s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392754) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [17m37s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928336) | [24m25s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392473) | [24m25s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392473) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [12m32s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392711) | [20m09s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569669) | [20m09s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569669) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [8m21s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629757946) | [18m46s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392707) | [18m46s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392707) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [12m33s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928322) | [18m12s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569611) | [18m12s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569611) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [9m41s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629757927) | [18m10s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928190) | [18m10s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928190) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [8m42s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629757818) | [18m04s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392619) | [18m04s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392619) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [7m37s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928397) | [15m10s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392888) | [15m10s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392888) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [12m02s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392903) | [14m59s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569642) | [14m59s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569642) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392773) | [14m32s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569773) | [14m32s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569773) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [12m08s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392714) | [13m26s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928392) | [13m26s](https://github.com/iree-org/iree/actions/runs/27610895343/job/81652928392) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [5m57s](https://github.com/iree-org/iree/actions/runs/27617050558/job/81664392786) | [12m03s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569534) | [12m03s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569534) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [3m40s](https://github.com/iree-org/iree/actions/runs/27608729536/job/81629758044) | [8m04s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569784) | [8m04s](https://github.com/iree-org/iree/actions/runs/27617422516/job/81658569784) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27610895274/job/81651158695) | [2m17s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853805) | [2m17s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853805) | 4 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27608729551/job/81628262203) | [2m13s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853619) | [2m13s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853619) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [2m13s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853757) | [2m13s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853757) | [2m13s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656853757) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m26s](https://github.com/iree-org/iree/actions/runs/27612557681/job/81640353861) | [1m26s](https://github.com/iree-org/iree/actions/runs/27612557681/job/81640353861) | [1m26s](https://github.com/iree-org/iree/actions/runs/27612557681/job/81640353861) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 4 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/27617050521/job/81663001135) | [42s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656854211) | [42s](https://github.com/iree-org/iree/actions/runs/27617422598/job/81656854211) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 279 | 2% (5/279) |  | 5h52m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 192 | 2% (4/192) |  | 5h56m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 236 | 8% (20/236) |  | 6h01m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 204 | 2% (5/204) |  | 6h04m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 64 | 2% (1/64) |  | 6h18m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
