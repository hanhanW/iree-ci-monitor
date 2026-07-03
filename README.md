# iree-ci-monitor

_Updated: 2026-07-03 05:58 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [24m15s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847256) | [35m26s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847394) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [13m47s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055032) | [19m40s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847246) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [4m49s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026451) | [19m15s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054966) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [16m12s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054999) | [17m40s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847162) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [10m22s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847031) | [15m28s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026246) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [5m57s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847380) | [15m05s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026670) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [12m20s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847175) | [14m48s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055077) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [6m40s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026277) | [13m22s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847119) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026367) | [12m18s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847105) | 0% (0/2) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054984) | [9m10s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026449) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [6m25s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847205) | [8m11s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054896) | 0% (0/1) | `shark01-ci` |
| `macos-14` | github-hosted | 25 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/28646265418/job/84953754491) | [2m46s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741205) | 0% (0/3) | 25 |
| `macos-15-intel` | github-hosted | 5 | 0 | — | — | 2 | [1m22s](https://github.com/iree-org/iree/actions/runs/28645102454/job/84950063973) | [2m22s](https://github.com/iree-org/iree/actions/runs/28643900428/job/84945971261) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/28645697082/job/84951991190) | [2m20s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741256) | 0% (0/3) | 21 |
| `windows-2022` | github-hosted | 20 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28645697082/job/84951991087) | [1m56s](https://github.com/iree-org/iree/actions/runs/28643900428/job/84945971165) | 0% (0/3) | 20 |
| `ubuntu-24.04` | github-hosted | 122 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/28645697082/job/84951991315) | [1m38s](https://github.com/iree-org/iree/actions/runs/28645697302/job/84952891086) | 13% (3/23) | 122 |
| `azure-linux-scale` | ossci | 41 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/28646265418/job/84953754767) | [1m38s](https://github.com/iree-org/iree/actions/runs/28643900428/job/84945971260) | 12% (1/8) | 41 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 5 | 0 | — | — | 0 | [1m25s](https://github.com/iree-org/iree/actions/runs/28645102454/job/84950063843) | [1m36s](https://github.com/iree-org/iree/actions/runs/28653824702/job/84978000960) | 0% (0/1) | 5 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/28645697302/job/84952891198) | [32s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026326) | 0% (0/4) | 16 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741438) | [26s](https://github.com/iree-org/iree/actions/runs/28645697082/job/84951991408) | 0% (0/1) | 6 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026450) | [5s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054918) | 0% (0/1) | `iree-mi308-1` |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28659163896/job/84995403250) | [4s](https://github.com/iree-org/iree/actions/runs/28645100357/job/84949762045) | 0% (0/3) | 24 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [34m22s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026383) | [35m26s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847394) | [35m26s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847394) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [23m27s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026578) | [24m15s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847256) | [24m15s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847256) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [13m47s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055032) | [19m40s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847246) | [19m40s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847246) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [4m49s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026451) | [19m15s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054966) | [19m15s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054966) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [16m12s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054999) | [17m40s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847162) | [17m40s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847162) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [10m22s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847031) | [15m28s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026246) | [15m28s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026246) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [5m48s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055024) | [15m05s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026670) | [15m05s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026670) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [14m34s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026376) | [14m48s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055077) | [14m48s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055077) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [12m20s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847175) | [14m44s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026651) | [14m44s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026651) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [6m40s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026277) | [13m22s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847119) | [13m22s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847119) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [2m02s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026440) | [12m18s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847105) | [12m18s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847105) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [6m13s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943055087) | [10m26s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026342) | [10m26s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026342) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054984) | [9m10s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026449) | [9m10s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026449) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [6m25s](https://github.com/iree-org/iree/actions/runs/28646265430/job/84954847205) | [8m11s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054896) | [8m11s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054896) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28644147768/job/84948026367) | [6m34s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054911) | [6m34s](https://github.com/iree-org/iree/actions/runs/28638016055/job/84943054911) | 2 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28645102454/job/84950063644) | [4m35s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741238) | [4m35s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741238) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 6 | 0 | — | — | [1m31s](https://github.com/iree-org/iree/actions/runs/28645697082/job/84951991231) | [4m34s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741305) | [4m34s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741305) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 6 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/28645102454/job/84950063768) | [3m05s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741290) | [3m05s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741290) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 6 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28645102454/job/84950063714) | [2m59s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741319) | [2m59s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741319) | 6 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 6 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28645102454/job/84950063673) | [2m46s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741205) | [2m46s](https://github.com/iree-org/iree/actions/runs/28644147771/job/84946741205) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 273 | 3% (7/273) |  | 4h22m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 240 | 8% (19/240) |  | 4h39m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 215 | 1% (3/215) |  | 4h42m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 193 | 2% (3/193) |  | 4h44m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 63 | 2% (1/63) |  | 4h54m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
