# iree-ci-monitor

_Updated: 2026-08-13 00:55 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [47m42s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928462) | [47m42s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928462) | 0% (0/1) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [47m29s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928331) | [47m29s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928331) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [46m09s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928264) | [46m09s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928264) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [27m00s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928508) | [34m14s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928577) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [28m21s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928440) | [28m21s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928440) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [12m57s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928542) | [20m05s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928540) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [20m05s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928557) | [20m05s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928557) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [13m02s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928500) | [17m53s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928455) | 50% (1/2) | `shark10-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [5m58s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928511) | [13m58s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928422) | 0% (0/2) | `shark01-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [11m44s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928260) | [11m44s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928260) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [6m42s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928520) | [6m42s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928520) | 0% (0/1) | `shark10-ci` |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [53s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487098) | [1m24s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487154) | 0% (0/3) | 5 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487064) | [1m21s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487169) | 0% (0/3) | 5 |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487282) | [9s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487285) | 0% (0/6) | 6 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31673332454/job/94362448565) | [8s](https://github.com/iree-org/iree/actions/runs/31673332454/job/94362448524) | 0% (0/3) | 3 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487075) | [5s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487133) | 0% (0/3) | 6 |
| `ubuntu-24.04` | github-hosted | 27 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94362448515) | [4s](https://github.com/iree-org/iree/actions/runs/31670798189/job/94354853436) | 5% (1/22) | 27 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487257) | [1s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487257) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [47m42s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928462) | [47m42s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928462) | [47m42s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928462) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [47m29s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928331) | [47m29s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928331) | [47m29s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928331) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [46m09s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928264) | [46m09s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928264) | [46m09s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928264) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [34m14s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928577) | [34m14s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928577) | [34m14s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928577) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [28m21s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928440) | [28m21s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928440) | [28m21s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928440) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [27m00s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928508) | [27m00s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928508) | [27m00s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928508) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [20m05s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928557) | [20m05s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928557) | [20m05s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928557) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [20m05s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928540) | [20m05s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928540) | [20m05s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928540) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [17m53s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928455) | [17m53s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928455) | [17m53s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928455) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [13m58s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928422) | [13m58s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928422) | [13m58s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928422) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [13m02s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928500) | [13m02s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928500) | [13m02s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928500) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [12m57s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928542) | [12m57s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928542) | [12m57s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928542) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [11m44s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928260) | [11m44s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928260) | [11m44s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928260) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [6m42s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928520) | [6m42s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928520) | [6m42s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928520) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [5m58s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928511) | [5m58s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928511) | [5m58s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928511) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 1 | 0 | — | — | [1m24s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487154) | [1m24s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487154) | [1m24s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487154) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 1 | 0 | — | — | [1m21s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487169) | [1m21s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487169) | [1m21s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487169) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [1m11s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487268) | [1m11s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487268) | [1m11s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487268) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 1 | 0 | — | — | [1m04s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487150) | [1m04s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487150) | [1m04s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487150) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [53s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487098) | [53s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487098) | [53s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487098) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 161 | 6% (9/161) |  | 34m50s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 193 | 0% (0/193) |  | 35m26s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 156 | 8% (12/156) |  | 36m52s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 134 | 13% (17/134) |  | 59m30s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
