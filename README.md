# iree-ci-monitor

_Updated: 2026-06-15 07:28 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [50m33s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703271) | [2h01m](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631054) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [50m53s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703179) | [1h10m](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413947984) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [21m34s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948090) | [56m12s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703172) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [29m04s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948112) | [54m10s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631087) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [23m27s](https://github.com/iree-org/iree/actions/runs/27535339784/job/81388109053) | [52m10s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630988) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [21m04s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703125) | [43m40s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413947972) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [9m16s](https://github.com/iree-org/iree/actions/runs/27535339784/job/81388109084) | [40m57s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703210) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [13m48s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948075) | [25m53s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703195) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [8m46s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703059) | [17m12s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630941) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [8m47s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948088) | [15m24s](https://github.com/iree-org/iree/actions/runs/27535339784/job/81388109118) | 0% (0/1) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [6m05s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703116) | [10m22s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630921) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948042) | [6m30s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630970) | 0% (0/1) | `iree-mi308-1` |
| `ubuntu-24.04` | github-hosted | 91 | 0 | — | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/27543742959/job/81411781917) | [3m25s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630955) | 18% (4/22) | 91 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27535339784/job/81388109066) | [2m32s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631058) | 25% (1/4) | 16 |
| `azure-linux-scale` | ossci | 25 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/27535339516/job/81383225055) | [2m03s](https://github.com/iree-org/iree/actions/runs/27546582458/job/81421501452) | 0% (0/8) | 25 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362887001) | [1m42s](https://github.com/iree-org/iree/actions/runs/27535408025/job/81413294400) | 0% (0/3) | 15 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m23s](https://github.com/iree-org/iree/actions/runs/27542683630/job/81408149656) | [1m23s](https://github.com/iree-org/iree/actions/runs/27542683630/job/81408149656) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 14 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/27535339516/job/81383224878) | [48s](https://github.com/iree-org/iree/actions/runs/27543742959/job/81411781998) | 0% (0/3) | 14 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27543742959/job/81411781992) | [44s](https://github.com/iree-org/iree/actions/runs/27535339516/job/81383224932) | 0% (0/3) | 15 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27546580448/job/81421438160) | [8s](https://github.com/iree-org/iree/actions/runs/27546240643/job/81420247339) | 0% (0/3) | 15 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413947947) | [2s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703054) | 0% (0/1) | 4 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27542658154/job/81408059236) | [2s](https://github.com/iree-org/iree/actions/runs/27542658154/job/81408059236) | — | 1 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27543742959/job/81411782038) | [1s](https://github.com/iree-org/iree/actions/runs/27546582458/job/81421501438) | 0% (0/1) | 4 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [1h16m](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948080) | [2h01m](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631054) | [2h01m](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631054) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [45m51s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703255) | [1h45m](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631150) | [1h45m](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631150) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [50m53s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703179) | [1h10m](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413947984) | [1h10m](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413947984) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [21m34s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948090) | [56m12s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703172) | [56m12s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703172) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [43m34s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948021) | [54m10s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631087) | [54m10s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631087) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [23m27s](https://github.com/iree-org/iree/actions/runs/27535339784/job/81388109053) | [52m10s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630988) | [52m10s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630988) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [21m04s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703125) | [43m40s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413947972) | [43m40s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413947972) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [29m04s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948112) | [41m46s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703235) | [41m46s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703235) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [7m00s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630993) | [40m57s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703210) | [40m57s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703210) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [14m24s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631124) | [35m26s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703267) | [35m26s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703267) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [13m48s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948075) | [25m53s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703195) | [25m53s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703195) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [19m42s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630994) | [25m44s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948055) | [25m44s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948055) | 4 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [8m46s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703059) | [17m12s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630941) | [17m12s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630941) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [8m47s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948088) | [15m24s](https://github.com/iree-org/iree/actions/runs/27535339784/job/81388109118) | [15m24s](https://github.com/iree-org/iree/actions/runs/27535339784/job/81388109118) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [6m05s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703116) | [10m22s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630921) | [10m22s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630921) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948042) | [6m30s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630970) | [6m30s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630970) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81413948011) | [4m41s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631127) | [4m41s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631127) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 4 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422703190) | [4m25s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631033) | [4m25s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414631033) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 4 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27546582446/job/81422704192) | [4m15s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630984) | [4m15s](https://github.com/iree-org/iree/actions/runs/27535408048/job/81414630984) | 4 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 4 | 0 | — | — | [13s](https://github.com/iree-org/iree/actions/runs/27535339784/job/81383225959) | [4m02s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81411799307) | [4m02s](https://github.com/iree-org/iree/actions/runs/27543742974/job/81411799307) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 300 | 2% (7/300) |  | 18m42s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 254 | 8% (20/254) |  | 45m46s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 213 | 2% (5/213) |  | 51m42s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 222 | 2% (5/222) |  | 57m04s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 71 | 1% (1/71) |  | 1h36m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h01m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h10m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
