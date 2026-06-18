# iree-ci-monitor

_Updated: 2026-06-17 18:28 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [17m37s](https://github.com/iree-org/iree/actions/runs/27718828323/job/82004619281) | [30m30s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406890) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [13m43s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944229969) | [27m15s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406797) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [10m34s](https://github.com/iree-org/iree/actions/runs/27715276884/job/81991719412) | [24m10s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230237) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [13m30s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230081) | [23m15s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406976) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [4m32s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406861) | [21m16s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230192) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [7m28s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944229849) | [18m22s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406666) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [4m30s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406836) | [14m46s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944229929) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [9m39s](https://github.com/iree-org/iree/actions/runs/27715276884/job/81991719081) | [13m16s](https://github.com/iree-org/iree/actions/runs/27718828323/job/82004619395) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [1m37s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406653) | [11m25s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230015) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [6m55s](https://github.com/iree-org/iree/actions/runs/27718828323/job/82004619280) | [11m10s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944229923) | 0% (0/1) | `shark01-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230047) | [9m38s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406776) | 0% (0/1) | `iree-mi308-1` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [4m52s](https://github.com/iree-org/iree/actions/runs/27715276884/job/81991719073) | [9m08s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230115) | 0% (0/2) | `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27718828323/job/82004619346) | [3m43s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406795) | 0% (0/4) | 16 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/27702567647/job/81942681984) | [2m48s](https://github.com/iree-org/iree/actions/runs/27702569098/job/81942690948) | 0% (0/3) | 12 |
| `ubuntu-24.04` | github-hosted | 89 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27715276884/job/81991719209) | [2m28s](https://github.com/iree-org/iree/actions/runs/27702569098/job/81942690735) | 0% (0/19) | 87 |
| `macos-14` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27715276994/job/81986525445) | [2m08s](https://github.com/iree-org/iree/actions/runs/27702569098/job/81942691018) | 0% (0/3) | 12 |
| `windows-2022` | github-hosted | 12 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/27718828288/job/81998679790) | [2m01s](https://github.com/iree-org/iree/actions/runs/27702569098/job/81942690790) | 0% (0/3) | 12 |
| `azure-linux-scale` | ossci | 23 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/27715276994/job/81986525574) | [28s](https://github.com/iree-org/iree/actions/runs/27702569098/job/81942691015) | 0% (0/7) | 23 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27702567647/job/81942682309) | [12s](https://github.com/iree-org/iree/actions/runs/27702569098/job/81942691047) | 0% (0/1) | 4 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27718828323/job/82004619074) | [11s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406645) | 100% (1/1) | 4 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27718824296/job/81998627600) | [9s](https://github.com/iree-org/iree/actions/runs/27718824296/job/81998627752) | 0% (0/3) | 9 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [17m37s](https://github.com/iree-org/iree/actions/runs/27718828323/job/82004619281) | [30m30s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406890) | [30m30s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406890) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [13m43s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944229969) | [27m15s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406797) | [27m15s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406797) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [15m57s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406872) | [24m10s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230237) | [24m10s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230237) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [13m30s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230081) | [23m15s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406976) | [23m15s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406976) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [4m32s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406861) | [21m16s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230192) | [21m16s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230192) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [7m28s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944229849) | [18m22s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406666) | [18m22s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406666) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [17m02s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230097) | [18m13s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406908) | [18m13s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406908) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [4m24s](https://github.com/iree-org/iree/actions/runs/27718828323/job/82004619294) | [17m23s](https://github.com/iree-org/iree/actions/runs/27715276884/job/81991719503) | [17m23s](https://github.com/iree-org/iree/actions/runs/27715276884/job/81991719503) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [4m30s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406836) | [14m46s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944229929) | [14m46s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944229929) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [9m39s](https://github.com/iree-org/iree/actions/runs/27715276884/job/81991719081) | [13m16s](https://github.com/iree-org/iree/actions/runs/27718828323/job/82004619395) | [13m16s](https://github.com/iree-org/iree/actions/runs/27718828323/job/82004619395) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [1m37s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406653) | [11m25s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230015) | [11m25s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230015) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [6m55s](https://github.com/iree-org/iree/actions/runs/27718828323/job/82004619280) | [11m10s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944229923) | [11m10s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944229923) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [8m49s](https://github.com/iree-org/iree/actions/runs/27718828323/job/82004619340) | [10m21s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406896) | [10m21s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406896) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230047) | [9m38s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406776) | [9m38s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406776) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [6m17s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406811) | [9m08s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230115) | [9m08s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230115) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 0 | — | — | [18s](https://github.com/iree-org/iree/actions/runs/27715276884/job/81991719452) | [7m22s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406965) | [7m22s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406965) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [1m25s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406784) | [4m52s](https://github.com/iree-org/iree/actions/runs/27715276884/job/81991719073) | [4m52s](https://github.com/iree-org/iree/actions/runs/27715276884/job/81991719073) | 3 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 4 | 0 | — | — | [1m34s](https://github.com/iree-org/iree/actions/runs/27702567647/job/81942681841) | [3m44s](https://github.com/iree-org/iree/actions/runs/27702569098/job/81942690971) | [3m44s](https://github.com/iree-org/iree/actions/runs/27702569098/job/81942690971) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230051) | [3m43s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406795) | [3m43s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406795) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 4 | 0 | — | — | [1m30s](https://github.com/iree-org/iree/actions/runs/27702567647/job/81942682035) | [3m34s](https://github.com/iree-org/iree/actions/runs/27702569098/job/81942690891) | [3m34s](https://github.com/iree-org/iree/actions/runs/27702569098/job/81942690891) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 171 | 5% (9/171) |  | 3h45m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 229 | 0% (0/229) |  | 3h50m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 175 | 1% (1/175) |  | 3h52m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 164 | 0% (0/164) |  | 3h54m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 52 | 0% (0/52) |  | 3h56m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
