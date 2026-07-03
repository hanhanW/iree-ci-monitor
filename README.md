# iree-ci-monitor

_Updated: 2026-07-03 11:45 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [1h11m](https://github.com/iree-org/iree/actions/runs/28672765195/job/85040703090) | [2h47m](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352802) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 18 | 0 | — | — | 1 | [1h49m](https://github.com/iree-org/iree/actions/runs/28672765195/job/85040702994) | [2h25m](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352868) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [20m22s](https://github.com/iree-org/iree/actions/runs/28672765195/job/85040702866) | [1h32m](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576500) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 9 | 0 | — | — | 0 | [24m04s](https://github.com/iree-org/iree/actions/runs/28664895851/job/85015553025) | [1h28m](https://github.com/iree-org/iree/actions/runs/28670311469/job/85033071830) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 9 | 0 | — | — | 0 | [57m16s](https://github.com/iree-org/iree/actions/runs/28670311469/job/85033071988) | [1h22m](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352774) | 0% (0/2) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 9 | 0 | — | — | 0 | [42m37s](https://github.com/iree-org/iree/actions/runs/28668251960/job/85026554607) | [1h00m](https://github.com/iree-org/iree/actions/runs/28664270433/job/85013409808) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 18 | 0 | — | — | 0 | [27m22s](https://github.com/iree-org/iree/actions/runs/28664270433/job/85013409856) | [57m58s](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352822) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [10m34s](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352765) | [57m28s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576546) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 9 | 0 | — | — | 0 | [25m42s](https://github.com/iree-org/iree/actions/runs/28668251960/job/85026554563) | [54m23s](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352854) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 18 | 0 | — | — | 0 | [30m09s](https://github.com/iree-org/iree/actions/runs/28664895851/job/85015553233) | [41m22s](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352849) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 18 | 0 | — | — | 0 | [7m59s](https://github.com/iree-org/iree/actions/runs/28664895851/job/85015553208) | [38m57s](https://github.com/iree-org/iree/actions/runs/28670311469/job/85033072083) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28663308774/job/85012989569) | [22m17s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576517) | 0% (0/2) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 36 | 0 | — | — | 0 | [12s](https://github.com/iree-org/iree/actions/runs/28672248763/job/85039111733) | [4m27s](https://github.com/iree-org/iree/actions/runs/28664270433/job/85013409758) | 25% (2/8) | 36 |
| `ubuntu-24.04-arm` | github-hosted | 33 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/28677345279/job/85053423057) | [3m56s](https://github.com/iree-org/iree/actions/runs/28668718806/job/85026944962) | 0% (0/6) | 33 |
| `ubuntu-24.04` | github-hosted | 220 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28670311469/job/85033071891) | [3m36s](https://github.com/iree-org/iree/actions/runs/28668251446/job/85025230722) | 3% (1/39) | 212 |
| `windows-2022` | github-hosted | 33 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28663308807/job/85008898430) | [2m35s](https://github.com/iree-org/iree/actions/runs/28668718806/job/85026944976) | 0% (0/6) | 33 |
| `ubuntu-latest` | github-hosted | 42 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28659163561/job/84995431248) | [1m57s](https://github.com/iree-org/iree/actions/runs/28668406229/job/85025715987) | 0% (0/6) | 42 |
| `azure-linux-scale` | ossci | 63 | 0 | — | — | 3 | [8s](https://github.com/iree-org/iree/actions/runs/28668718806/job/85026945012) | [1m55s](https://github.com/iree-org/iree/actions/runs/28668251446/job/85025230812) | 7% (1/14) | 63 |
| `macos-14` | github-hosted | 35 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28677345279/job/85053423068) | [1m45s](https://github.com/iree-org/iree/actions/runs/28668251446/job/85025230839) | 0% (0/7) | 35 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 2 | 0 | — | — | 0 | [1m36s](https://github.com/iree-org/iree/actions/runs/28653824702/job/84978000960) | [1m36s](https://github.com/iree-org/iree/actions/runs/28653824702/job/84978000960) | 0% (0/1) | 2 |
| `azure-windows-scale` | ossci | 11 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/28668718806/job/85026945034) | [7s](https://github.com/iree-org/iree/actions/runs/28668251446/job/85025230894) | 0% (0/2) | 11 |
| `macos-15-intel` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28646265418/job/85013904621) | [3s](https://github.com/iree-org/iree/actions/runs/28653810479/job/84977952751) | 0% (0/1) | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 9 | 0 | — | — | [1h11m](https://github.com/iree-org/iree/actions/runs/28672765195/job/85040703090) | [2h47m](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352802) | [2h47m](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352802) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [1h55m](https://github.com/iree-org/iree/actions/runs/28672765195/job/85040703143) | [2h31m](https://github.com/iree-org/iree/actions/runs/28670311469/job/85033071995) | [2h31m](https://github.com/iree-org/iree/actions/runs/28670311469/job/85033071995) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [1h49m](https://github.com/iree-org/iree/actions/runs/28672765195/job/85040702994) | [2h18m](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352874) | [2h18m](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352874) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 9 | 0 | — | — | [20m22s](https://github.com/iree-org/iree/actions/runs/28672765195/job/85040702866) | [1h32m](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576500) | [1h32m](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576500) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 9 | 0 | — | — | [24m04s](https://github.com/iree-org/iree/actions/runs/28664895851/job/85015553025) | [1h28m](https://github.com/iree-org/iree/actions/runs/28670311469/job/85033071830) | [1h28m](https://github.com/iree-org/iree/actions/runs/28670311469/job/85033071830) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 9 | 0 | — | — | [57m16s](https://github.com/iree-org/iree/actions/runs/28670311469/job/85033071988) | [1h22m](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352774) | [1h22m](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352774) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 9 | 0 | — | — | [29m13s](https://github.com/iree-org/iree/actions/runs/28670311469/job/85033071941) | [1h15m](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576683) | [1h15m](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576683) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 9 | 0 | — | — | [42m37s](https://github.com/iree-org/iree/actions/runs/28668251960/job/85026554607) | [1h00m](https://github.com/iree-org/iree/actions/runs/28664270433/job/85013409808) | [1h00m](https://github.com/iree-org/iree/actions/runs/28664270433/job/85013409808) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 9 | 0 | — | — | [20m36s](https://github.com/iree-org/iree/actions/runs/28668251960/job/85026554700) | [57m58s](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352822) | [57m58s](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352822) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 9 | 0 | — | — | [10m34s](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352765) | [57m28s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576546) | [57m28s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576546) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 9 | 0 | — | — | [25m42s](https://github.com/iree-org/iree/actions/runs/28668251960/job/85026554563) | [54m23s](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352854) | [54m23s](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352854) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [6m57s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576526) | [44m00s](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352818) | [44m00s](https://github.com/iree-org/iree/actions/runs/28668718798/job/85028352818) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [40m28s](https://github.com/iree-org/iree/actions/runs/28670311469/job/85033072050) | [42m41s](https://github.com/iree-org/iree/actions/runs/28668251960/job/85026554686) | [42m41s](https://github.com/iree-org/iree/actions/runs/28668251960/job/85026554686) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [22m17s](https://github.com/iree-org/iree/actions/runs/28670311469/job/85033071918) | [36m42s](https://github.com/iree-org/iree/actions/runs/28664895851/job/85015553263) | [36m42s](https://github.com/iree-org/iree/actions/runs/28664895851/job/85015553263) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [19m21s](https://github.com/iree-org/iree/actions/runs/28668251960/job/85026554724) | [29m26s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576535) | [29m26s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576535) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28663308774/job/85012989569) | [22m17s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576517) | [22m17s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576517) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 9 | 0 | — | — | [21s](https://github.com/iree-org/iree/actions/runs/28664895851/job/85015553287) | [8m55s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576708) | [8m55s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576708) | 9 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 9 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/28663308774/job/85012989689) | [8m33s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576596) | [8m33s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576596) | 9 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28672248763/job/85039111757) | [6m07s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576614) | [6m07s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576614) | 9 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28668251960/job/85026554522) | [5m45s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576612) | [5m45s](https://github.com/iree-org/iree/actions/runs/28668251413/job/85026576612) | 9 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 308 | 2% (7/307) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 216 | 1% (3/216) |  | 1h34m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 238 | 1% (3/238) |  | 1h37m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 269 | 8% (21/269) |  | 1h41m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 72 | 1% (1/72) |  | 1h55m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h47m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h25m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h28m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h22m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h00m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
