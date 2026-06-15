# iree-ci-monitor

_Updated: 2026-06-15 12:34 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [10m57s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442799) | [2h01m](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631054) | 0% (0/4) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 0 | — | — | 0 | [24m21s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631006) | [1h10m](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413947984) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 0 | — | — | 0 | [6m02s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630985) | [56m12s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703172) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [15m38s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630980) | [54m10s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631087) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [2m54s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442770) | [52m10s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630988) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [19m37s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419574) | [43m40s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413947972) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [7m18s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442833) | [40m57s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703210) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [5m41s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442703) | [25m53s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703195) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | [8m46s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703059) | [17m12s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630941) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [5m21s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442705) | [10m22s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630921) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [2m02s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703220) | [8m47s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948088) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419693) | [6m30s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630970) | 0% (0/2) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 24 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948071) | [2m32s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631058) | 25% (2/8) | 24 |
| `ubuntu-24.04` | github-hosted | 132 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81411751648) | [2m19s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631142) | 8% (3/39) | 132 |
| `azure-linux-scale` | ossci | 41 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/27566276308/job/81491454075) | [2m12s](https://github.com/iree-org/iree/actions/runs/27553863265/job/81447366937) | 0% (0/14) | 41 |
| `macos-14` | github-hosted | 22 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/27543742959/job/81411781946) | [1m42s](https://github.com/iree-org/iree/actions/runs/27535408025/job/81413294400) | 0% (0/7) | 22 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m23s](https://github.com/iree-org/iree/actions/runs/27542683630/job/81408149656) | [1m23s](https://github.com/iree-org/iree/actions/runs/27542683630/job/81408149656) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27568261118/job/81497853033) | [48s](https://github.com/iree-org/iree/actions/runs/27543742959/job/81411781998) | 0% (0/6) | 21 |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27559165360/job/81466269488) | [9s](https://github.com/iree-org/iree/actions/runs/27559165360/job/81466208243) | 0% (0/6) | 24 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27566276308/job/81491453867) | [5s](https://github.com/iree-org/iree/actions/runs/27543742959/job/81411781945) | 0% (0/6) | 21 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413947947) | [2s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419550) | 0% (0/2) | 6 |
| `azure-windows-scale` | ossci | 7 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27553863265/job/81447367215) | [2s](https://github.com/iree-org/iree/actions/runs/27568261118/job/81497853256) | 0% (0/2) | 7 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27542658154/job/81408059236) | [2s](https://github.com/iree-org/iree/actions/runs/27542658154/job/81408059236) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [50m33s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703271) | [2h01m](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631054) | [2h01m](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631054) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [5m00s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419687) | [1h45m](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631150) | [1h45m](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631150) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 6 | 0 | — | — | [24m21s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631006) | [1h10m](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413947984) | [1h10m](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413947984) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 6 | 0 | — | — | [6m02s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630985) | [56m12s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703172) | [56m12s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703172) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [16m43s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703272) | [54m10s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631087) | [54m10s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631087) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [2m54s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442770) | [52m10s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630988) | [52m10s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630988) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [19m37s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419574) | [43m40s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413947972) | [43m40s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413947972) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [15m38s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630980) | [41m46s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703235) | [41m46s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703235) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [7m00s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630993) | [40m57s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703210) | [40m57s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703210) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [8m11s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419710) | [35m26s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703267) | [35m26s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703267) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [13m45s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630975) | [25m53s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703195) | [25m53s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703195) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [4m13s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419783) | [25m44s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948055) | [25m44s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948055) | 4 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 0 | — | — | [8m46s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703059) | [17m12s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630941) | [17m12s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630941) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 6 | 0 | — | — | [5m21s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442705) | [10m22s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630921) | [10m22s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630921) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [2m02s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703220) | [8m47s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948088) | [8m47s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948088) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 6 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419693) | [6m30s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630970) | [6m30s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630970) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 6 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419708) | [4m41s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631127) | [4m41s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631127) | 6 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 6 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442772) | [4m25s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631033) | [4m25s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631033) | 6 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 6 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422704192) | [4m15s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630984) | [4m15s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630984) | 6 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 7 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81491143669) | [4m02s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81411799307) | [4m02s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81411799307) | 7 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 314 | 2% (7/314) |  | 19m02s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 224 | 2% (5/224) |  | 24m40s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 233 | 2% (5/233) |  | 24m44s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 263 | 8% (20/263) |  | 25m07s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 74 | 1% (1/74) |  | 34m17s ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h01m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h10m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
