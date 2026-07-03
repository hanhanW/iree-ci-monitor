# iree-ci-monitor

_Updated: 2026-07-03 00:27 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 2 | [19m01s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026383) | 2026-07-03 00:27 PDT | 0 | [22m16s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055009) | [33m44s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055059) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [4m49s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026451) | [19m15s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054966) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [8m43s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026462) | [16m12s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054999) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054994) | [15m28s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026246) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 1 | [10m26s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026342) | [15m05s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026670) | 0% (0/1) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 2 | [14m44s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026651) | [14m48s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055077) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026285) | [13m47s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055032) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054984) | [9m10s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026449) | 0% (0/1) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026320) | [8m11s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054896) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054820) | [6m40s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026277) | 0% (0/1) | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [2m02s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026440) | [6m34s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054911) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `macos-14` | github-hosted | 16 | 0 | — | — | 2 | [35s](https://github.com/iree-org/iree/actions/runs/28643900428/job/84945971141) | [2m46s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741205) | 0% (0/3) | 16 |
| `macos-15-intel` | github-hosted | 2 | 0 | — | — | 1 | [1m22s](https://github.com/iree-org/iree/actions/runs/28645102454/job/84950063973) | [2m22s](https://github.com/iree-org/iree/actions/runs/28643900428/job/84945971261) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 2 | [6s](https://github.com/iree-org/iree/actions/runs/28645102454/job/84950063768) | [2m20s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741256) | 0% (0/3) | 15 |
| `windows-2022` | github-hosted | 14 | 0 | — | — | 4 | [3s](https://github.com/iree-org/iree/actions/runs/28643900428/job/84945971102) | [1m56s](https://github.com/iree-org/iree/actions/runs/28643900428/job/84945971165) | 0% (0/3) | 14 |
| `ubuntu-24.04` | github-hosted | 70 | 0 | — | — | 4 | [2s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84946717699) | [1m45s](https://github.com/iree-org/iree/actions/runs/28645102454/job/84950063830) | 10% (2/20) | 70 |
| `azure-linux-scale` | ossci | 25 | 0 | — | — | 6 | [13s](https://github.com/iree-org/iree/actions/runs/28643900428/job/84945971289) | [1m43s](https://github.com/iree-org/iree/actions/runs/28638016059/job/84942116789) | 0% (0/5) | 25 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 2 | 0 | — | — | 1 | [1m25s](https://github.com/iree-org/iree/actions/runs/28643900428/job/84945971229) | [1m25s](https://github.com/iree-org/iree/actions/runs/28645102454/job/84950063843) | — | 2 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055020) | [1m07s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026379) | 0% (0/4) | 8 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026450) | [5s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054918) | 0% (0/1) | `iree-mi308-1` |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28644147243/job/84946717854) | [4s](https://github.com/iree-org/iree/actions/runs/28645100357/job/84949762045) | 0% (0/3) | 9 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741438) | [1s](https://github.com/iree-org/iree/actions/runs/28645102454/job/84950063988) | 0% (0/1) | 4 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [19m01s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026383) | 2026-07-03 00:27 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [19m01s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026578) | 2026-07-03 00:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 1 | [19m01s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026383) | 2026-07-03 00:27 PDT | [33m44s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055059) | [33m44s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055059) | [33m44s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055059) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 1 | [19m01s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026578) | 2026-07-03 00:27 PDT | [22m16s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055009) | [22m16s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055009) | [22m16s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055009) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [4m49s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026451) | [19m15s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054966) | [19m15s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054966) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [8m43s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026462) | [16m12s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054999) | [16m12s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054999) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054994) | [15m28s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026246) | [15m28s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026246) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [5m48s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055024) | [15m05s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026670) | [15m05s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026670) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [14m34s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026376) | [14m48s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055077) | [14m48s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055077) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [11m19s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055039) | [14m44s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026651) | [14m44s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026651) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026285) | [13m47s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055032) | [13m47s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055032) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [6m13s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055087) | [10m26s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026342) | [10m26s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026342) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054984) | [9m10s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026449) | [9m10s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026449) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026320) | [8m11s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054896) | [8m11s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054896) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054820) | [6m40s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026277) | [6m40s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026277) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026367) | [6m34s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054911) | [6m34s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054911) | 2 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28645102454/job/84950063644) | [4m35s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741238) | [4m35s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741238) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 4 | 0 | — | — | [1m46s](https://github.com/iree-org/iree/actions/runs/28643900428/job/84945971172) | [4m34s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741305) | [4m34s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741305) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 4 | 0 | — | — | [2m18s](https://github.com/iree-org/iree/actions/runs/28643900428/job/84945971164) | [3m05s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741290) | [3m05s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741290) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 4 | 0 | — | — | [1m33s](https://github.com/iree-org/iree/actions/runs/28638016059/job/84942116744) | [2m59s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741319) | [2m59s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741319) | 4 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 4 | 0 | — | — | [1m02s](https://github.com/iree-org/iree/actions/runs/28638016059/job/84942116676) | [2m46s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741205) | [2m46s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741205) | 4 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28645102460/job/84950567098) | [2m29s](https://github.com/iree-org/iree/actions/runs/28643900376/job/84946801175) | [2m29s](https://github.com/iree-org/iree/actions/runs/28643900376/job/84946801175) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 266 | 3% (7/265) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 211 | 1% (3/210) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 235 | 8% (19/234) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 189 | 2% (3/188) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 61 | 2% (1/61) |  | 8m50s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
