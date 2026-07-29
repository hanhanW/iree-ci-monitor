# iree-ci-monitor

_Updated: 2026-07-29 00:14 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [43m05s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487162) | [53m49s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427821) | — | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [44m37s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487241) | [45m27s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427817) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [32m17s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487042) | [37m39s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427825) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427776) | [37m12s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487045) | — | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427806) | [28m00s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487169) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [25m12s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427851) | [27m13s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487323) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [6m24s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487190) | [18m11s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487230) | — | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [7m45s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487174) | [14m48s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487221) | — | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [9m07s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427848) | [13m13s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487096) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427842) | [10m09s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487135) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [4m13s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487171) | [5m28s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427940) | — | `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 49 | 0 | — | — | 2 | [7s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496486979) | [5m01s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427903) | 0% (0/4) | 49 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427878) | [4m57s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487249) | — | `iree-mi308-1` |
| `azure-linux-scale` | ossci | 10 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/30417162110/job/90494351826) | [1m39s](https://github.com/iree-org/iree/actions/runs/30426271551/job/90494896180) | — | 10 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30417162110/job/90494351968) | [1m22s](https://github.com/iree-org/iree/actions/runs/30426271551/job/90494896104) | — | 2 |
| `macos-14` | github-hosted | 8 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/30426271551/job/90494895974) | [10s](https://github.com/iree-org/iree/actions/runs/30426904340/job/90495259937) | — | 8 |
| `windows-2022` | github-hosted | 8 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/30426271551/job/90494895952) | [7s](https://github.com/iree-org/iree/actions/runs/30426271551/job/90494895838) | — | 8 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30426904340/job/90495259916) | [5s](https://github.com/iree-org/iree/actions/runs/30426271551/job/90494895945) | — | 9 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427888) | [2s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487289) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [43m05s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487162) | [53m49s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427821) | [53m49s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427821) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [23m14s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487250) | [45m27s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427817) | [45m27s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427817) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [34m25s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427922) | [44m37s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487241) | [44m37s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487241) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [32m17s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487042) | [37m39s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427825) | [37m39s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427825) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427776) | [37m12s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487045) | [37m12s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487045) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427806) | [28m00s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487169) | [28m00s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487169) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [25m12s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427851) | [27m13s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487323) | [27m13s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487323) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [20m18s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427867) | [22m11s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487150) | [22m11s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487150) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427802) | [18m11s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487230) | [18m11s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487230) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [5m52s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427854) | [14m48s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487221) | [14m48s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487221) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [9m07s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427848) | [13m13s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487096) | [13m13s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487096) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427842) | [10m09s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487135) | [10m09s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487135) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [5m05s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427874) | [7m45s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487174) | [7m45s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487174) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [5m09s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427928) | [6m24s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487190) | [6m24s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487190) | 2 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 2 | 0 | — | — | [1m19s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487199) | [5m39s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427998) | [5m39s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427998) | 2 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 2 | 0 | — | — | [2m32s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487224) | [5m32s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427968) | [5m32s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427968) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [4m13s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487171) | [5m28s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427940) | [5m28s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427940) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 2 | 0 | — | — | [2m36s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487139) | [5m01s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427903) | [5m01s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427903) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427878) | [4m57s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487249) | [4m57s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487249) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 2 | 0 | — | — | [2m19s](https://github.com/iree-org/iree/actions/runs/30426271550/job/90496487259) | [4m28s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427807) | [4m28s](https://github.com/iree-org/iree/actions/runs/30417162138/job/90495427807) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 235 | 2% (4/235) |  | 9m47s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 188 | 6% (11/188) |  | 12m15s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 181 | 1% (2/181) |  | 26m48s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 176 | 2% (4/176) |  | 27m49s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 53 | 4% (2/53) |  | 48m20s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
