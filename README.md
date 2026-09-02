# iree-ci-monitor

_Updated: 2026-09-02 09:38 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [10m27s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483532) | [1h02m](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267307) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [19m13s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441171) | [56m10s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267322) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [15m16s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483610) | [51m24s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267222) | 0% (0/6) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [14m17s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441025) | [44m37s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267054) | 0% (0/3) | `shark01-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [20m26s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483451) | [35m36s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267302) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [7m46s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441018) | [31m18s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267203) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [5m49s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255440953) | [30m44s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267029) | 0% (0/3) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [5m29s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267131) | [20m03s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483664) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [12m52s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441198) | [19m14s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483675) | 0% (0/3) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [6m08s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267174) | [18m18s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441211) | 17% (1/6) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483543) | [12m39s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267166) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `macos-14` | github-hosted | 13 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603192) | [3m16s](https://github.com/iree-org/iree/actions/runs/33604453096/job/100165251981) | 0% (0/10) | 13 |
| `ubuntu-24.04` | github-hosted | 71 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100186025487) | [3m02s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267396) | 3% (2/59) | 71 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603117) | [2m10s](https://github.com/iree-org/iree/actions/runs/33604453096/job/100165252066) | 11% (1/9) | 12 |
| `windows-2022` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33622431137/job/100222346360) | [1m54s](https://github.com/iree-org/iree/actions/runs/33604453096/job/100165251987) | 0% (0/9) | 12 |
| `azure-linux-scale` | ossci | 24 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603445) | [1m32s](https://github.com/iree-org/iree/actions/runs/33604453096/job/100165251933) | 0% (0/20) | 24 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m28s](https://github.com/iree-org/iree/actions/runs/33614235923/job/100196268494) | [1m28s](https://github.com/iree-org/iree/actions/runs/33614235923/job/100196268494) | 0% (0/1) | 1 |
| `ubuntu-latest` | github-hosted | 30 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33604446167/job/100165143227) | [4s](https://github.com/iree-org/iree/actions/runs/33618697480/job/100210442912) | 0% (0/9) | 30 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/33631726048/job/100252603507) | [2s](https://github.com/iree-org/iree/actions/runs/33622431137/job/100222346693) | 0% (0/3) | 4 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [10m27s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483532) | [1h02m](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267307) | [1h02m](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267307) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [26m00s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483583) | [56m10s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267322) | [56m10s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267322) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [18m40s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441212) | [51m24s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267222) | [51m24s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267222) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [14m17s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441025) | [44m37s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267054) | [44m37s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267054) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [19m13s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441171) | [44m28s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267252) | [44m28s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267252) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [20m26s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483451) | [35m36s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267302) | [35m36s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267302) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [8m31s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483551) | [31m18s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267203) | [31m18s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267203) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [5m49s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255440953) | [30m44s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267029) | [30m44s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267029) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [7m46s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441018) | [20m04s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267325) | [20m04s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267325) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [5m29s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267131) | [20m03s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483664) | [20m03s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483664) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [12m52s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441198) | [19m14s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483675) | [19m14s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483675) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [6m25s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267263) | [18m18s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441211) | [18m18s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441211) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [14m45s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441027) | [15m16s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483610) | [15m16s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483610) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483543) | [12m39s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267166) | [12m39s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267166) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [6m08s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267174) | [8m35s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441135) | [8m35s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255441135) | 2 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483645) | [3m33s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267456) | [3m33s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267456) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 4 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/33622431137/job/100222346285) | [3m16s](https://github.com/iree-org/iree/actions/runs/33604453096/job/100165251981) | [3m16s](https://github.com/iree-org/iree/actions/runs/33604453096/job/100165251981) | 4 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33631726084/job/100255440831) | [3m10s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267114) | [3m10s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267114) | 3 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483693) | [3m04s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267321) | [3m04s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267321) | 3 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33622431039/job/100224483534) | [3m02s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267396) | [3m02s](https://github.com/iree-org/iree/actions/runs/33604453016/job/100167267396) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 220 | 0% (0/220) |  | 3h12m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 192 | 5% (9/192) |  | 3h14m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 147 | 0% (0/147) |  | 3h18m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 158 | 1% (1/158) |  | 3h22m ago |

## Alerts

- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h02m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
