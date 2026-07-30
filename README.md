# iree-ci-monitor

_Updated: 2026-07-29 17:51 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 9 | 0 | — | — | 0 | [9m57s](https://github.com/iree-org/iree/actions/runs/30451617302/job/90616390244) | [43m43s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394743) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [24m08s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819398) | [41m58s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394738) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 9 | 0 | — | — | 0 | [20m13s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819460) | [34m54s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394960) | 0% (0/4) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 18 | 0 | — | — | 0 | [12m07s](https://github.com/iree-org/iree/actions/runs/30474877493/job/90665834556) | [33m52s](https://github.com/iree-org/iree/actions/runs/30451617302/job/90616390599) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 9 | 0 | — | — | 0 | [7m29s](https://github.com/iree-org/iree/actions/runs/30482553128/job/90706926968) | [31m08s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394615) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [9m18s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819505) | [29m05s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394702) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 18 | 0 | — | — | 0 | [8m25s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251964) | [27m41s](https://github.com/iree-org/iree/actions/runs/30484936090/job/90690358793) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 18 | 0 | — | — | 0 | [6m11s](https://github.com/iree-org/iree/actions/runs/30482553128/job/90706927210) | [27m37s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394827) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 9 | 0 | — | — | 0 | [6m03s](https://github.com/iree-org/iree/actions/runs/30451617302/job/90616390397) | [14m09s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819406) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 18 | 0 | — | — | 0 | [6m59s](https://github.com/iree-org/iree/actions/runs/30451617302/job/90616390420) | [12m22s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819576) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30474877493/job/90665834505) | [11m09s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394772) | 0% (0/4) | `iree-mi308-1` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [2m53s](https://github.com/iree-org/iree/actions/runs/30465381855/job/90623814600) | [10m17s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394742) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 46 | 0 | — | — | 1 | [19s](https://github.com/iree-org/iree/actions/runs/30499875150/job/90737010137) | [1m26s](https://github.com/iree-org/iree/actions/runs/30484936365/job/90688177963) | 0% (0/23) | 46 |
| `windows-2022` | github-hosted | 24 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/30499875150/job/90737010475) | [1m24s](https://github.com/iree-org/iree/actions/runs/30477920655/job/90664245864) | 0% (0/12) | 24 |
| `ubuntu-24.04` | github-hosted | 165 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30465381855/job/90623814606) | [1m13s](https://github.com/iree-org/iree/actions/runs/30477920655/job/90664245706) | 0% (0/74) | 165 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394625) | [32s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819222) | 0% (0/4) | 9 |
| `macos-14` | github-hosted | 25 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/30465389311/job/90621787164) | [32s](https://github.com/iree-org/iree/actions/runs/30485027407/job/90688515814) | 0% (0/12) | 25 |
| `ubuntu-24.04-arm` | github-hosted | 24 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30474877288/job/90663629188) | [29s](https://github.com/iree-org/iree/actions/runs/30477920655/job/90664245656) | 0% (0/12) | 24 |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30499874874/job/90736976399) | [15s](https://github.com/iree-org/iree/actions/runs/30485026338/job/90688434266) | 0% (0/12) | 24 |
| `azure-windows-scale` | ossci | 8 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30499875150/job/90737010118) | [2s](https://github.com/iree-org/iree/actions/runs/30477920655/job/90664245867) | 0% (0/4) | 8 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 1 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 9 | 0 | — | — | [9m57s](https://github.com/iree-org/iree/actions/runs/30451617302/job/90616390244) | [43m43s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394743) | [43m43s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394743) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 9 | 0 | — | — | [24m08s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819398) | [41m58s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394738) | [41m58s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394738) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 9 | 0 | — | — | [20m13s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819460) | [34m54s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394960) | [34m54s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394960) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [13m20s](https://github.com/iree-org/iree/actions/runs/30451617302/job/90616390431) | [34m46s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394795) | [34m46s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394795) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [12m07s](https://github.com/iree-org/iree/actions/runs/30474877493/job/90665834556) | [33m52s](https://github.com/iree-org/iree/actions/runs/30451617302/job/90616390599) | [33m52s](https://github.com/iree-org/iree/actions/runs/30451617302/job/90616390599) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 9 | 0 | — | — | [7m29s](https://github.com/iree-org/iree/actions/runs/30482553128/job/90706926968) | [31m08s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394615) | [31m08s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394615) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [8m52s](https://github.com/iree-org/iree/actions/runs/30482553128/job/90706927185) | [30m46s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394713) | [30m46s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394713) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 9 | 0 | — | — | [9m18s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819505) | [29m05s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394702) | [29m05s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394702) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 9 | 0 | — | — | [10m11s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738252051) | [28m54s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394861) | [28m54s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394861) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [5m40s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819391) | [28m43s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394717) | [28m43s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394717) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [8m25s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251964) | [27m41s](https://github.com/iree-org/iree/actions/runs/30484936090/job/90690358793) | [27m41s](https://github.com/iree-org/iree/actions/runs/30484936090/job/90690358793) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [10m37s](https://github.com/iree-org/iree/actions/runs/30482553128/job/90706927109) | [27m37s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394827) | [27m37s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394827) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 9 | 0 | — | — | [6m03s](https://github.com/iree-org/iree/actions/runs/30451617302/job/90616390397) | [14m09s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819406) | [14m09s](https://github.com/iree-org/iree/actions/runs/30477938704/job/90666819406) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30474877493/job/90665834505) | [11m09s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394772) | [11m09s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394772) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 9 | 0 | — | — | [6m28s](https://github.com/iree-org/iree/actions/runs/30465381855/job/90623814759) | [11m08s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394784) | [11m08s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394784) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 9 | 0 | — | — | [2m53s](https://github.com/iree-org/iree/actions/runs/30465381855/job/90623814600) | [10m17s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394742) | [10m17s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394742) | 3 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 9 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251995) | [2m44s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394807) | [2m44s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394807) | 9 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 9 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30484936090/job/90690358543) | [2m27s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394762) | [2m27s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394762) | 9 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251919) | [2m08s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394797) | [2m08s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394797) | 9 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 9 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30482553128/job/90706927098) | [2m00s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394751) | [2m00s](https://github.com/iree-org/iree/actions/runs/30485027380/job/90690394751) | 9 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 192 | 1% (2/192) |  | 45m11s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 173 | 5% (9/173) |  | 47m58s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 136 | 1% (2/136) |  | 49m43s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 143 | 0% (0/143) |  | 51m46s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 43 | 2% (1/43) |  | 59m13s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
