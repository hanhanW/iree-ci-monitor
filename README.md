# iree-ci-monitor

_Updated: 2026-07-31 00:17 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 1 | [21m19s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454938) | [26m58s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086455001) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 1 | [21m52s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526264) | [26m08s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454920) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526266) | [21m18s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454994) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 1 | [17m08s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526388) | [18m20s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526335) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454720) | [15m45s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526193) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [10m56s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454946) | [15m12s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086455027) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [6m37s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526290) | [13m56s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454997) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [4m37s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454924) | [11m08s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526345) | 0% (0/1) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526200) | [10m29s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454794) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 1 | [24m27s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526395) | 2026-07-31 00:17 PDT | 0 | [8m06s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454931) | [8m06s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454931) | — | `shark75-ci` |
| `macos-14` | github-hosted | 8 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/30608579302/job/91086136352) | [1m18s](https://github.com/iree-org/iree/actions/runs/30610564282/job/91092203898) | 0% (0/3) | 8 |
| `windows-2022` | github-hosted | 8 | 0 | — | — | 1 | [5s](https://github.com/iree-org/iree/actions/runs/30610564282/job/91092203930) | [1m13s](https://github.com/iree-org/iree/actions/runs/30610564282/job/91092203892) | 0% (0/3) | 8 |
| `ubuntu-24.04` | github-hosted | 49 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526155) | [21s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454967) | 0% (0/22) | 47 |
| `azure-linux-scale` | ossci | 11 | 0 | — | — | 1 | [9s](https://github.com/iree-org/iree/actions/runs/30607758207/job/91085256132) | [13s](https://github.com/iree-org/iree/actions/runs/30610564282/job/91092203953) | 0% (0/5) | 11 |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526058) | [2s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454767) | 0% (0/1) | `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526226) | [2s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454863) | 0% (0/1) | `iree-mi308-1` |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/30608579302/job/91086136336) | [2s](https://github.com/iree-org/iree/actions/runs/30610564282/job/91092203912) | 0% (0/3) | 9 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30610563668/job/91092181300) | [2s](https://github.com/iree-org/iree/actions/runs/30610563668/job/91092181324) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30607758207/job/91085256087) | [1s](https://github.com/iree-org/iree/actions/runs/30610564282/job/91092203986) | 0% (0/1) | 2 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 2 | 2 | [1h10m](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454811) | 2026-07-31 00:17 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [1h10m](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454811) | 2026-07-31 00:17 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `fix/24751-tensor-slice-parameter-fold` | pull_request |
| [24m27s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526156) | 2026-07-31 00:17 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [24m27s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526395) | 2026-07-31 00:17 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 2 | [1h10m](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454811) | 2026-07-31 00:17 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [8m09s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526289) | [26m58s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086455001) | [26m58s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086455001) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [21m52s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526264) | [26m08s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454920) | [26m08s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454920) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 1 | [24m27s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526395) | 2026-07-31 00:17 PDT | [8m06s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454931) | [8m06s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454931) | [8m06s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454931) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [20m03s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526344) | [21m19s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454938) | [21m19s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454938) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526266) | [21m18s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454994) | [21m18s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454994) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [9m24s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454909) | [18m20s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526335) | [18m20s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526335) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454930) | [17m08s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526388) | [17m08s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526388) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454720) | [15m45s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526193) | [15m45s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526193) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526338) | [15m12s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086455027) | [15m12s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086455027) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [4m38s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526384) | [13m56s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454997) | [13m56s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454997) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [4m37s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454924) | [11m08s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526345) | [11m08s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526345) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [10m46s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526380) | [10m56s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454946) | [10m56s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454946) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526200) | [10m29s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454794) | [10m29s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454794) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454805) | [6m37s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526290) | [6m37s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526290) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526353) | [1m47s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454960) | [1m47s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454960) | 2 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526066) | [1m29s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454858) | [1m29s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454858) | 2 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30607758207/job/91085256002) | [1m18s](https://github.com/iree-org/iree/actions/runs/30610564282/job/91092203898) | [1m18s](https://github.com/iree-org/iree/actions/runs/30610564282/job/91092203898) | 2 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 2 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/30607758207/job/91085256005) | [1m13s](https://github.com/iree-org/iree/actions/runs/30610564282/job/91092203892) | [1m13s](https://github.com/iree-org/iree/actions/runs/30610564282/job/91092203892) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30607758207/job/91085256050) | [50s](https://github.com/iree-org/iree/actions/runs/30610564282/job/91092203904) | [50s](https://github.com/iree-org/iree/actions/runs/30610564282/job/91092203904) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 153 | 3% (4/152) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 160 | 0% (0/159) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 111 | 1% (1/110) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 115 | 1% (1/115) |  | 54s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 36 | 3% (1/36) |  | 13m13s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
