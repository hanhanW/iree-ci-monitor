# iree-ci-monitor

_Updated: 2026-06-27 18:24 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 14 | 0 | — | — | 0 | [2h04m](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077751) | [3h05m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041484) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [1h29m](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820588) | [2h36m](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077724) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 7 | 0 | — | — | 0 | [1h25m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041444) | [2h16m](https://github.com/iree-org/iree/actions/runs/28299106146/job/83844610742) | — | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 7 | 0 | — | — | 0 | [1h06m](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077633) | [2h10m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041355) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 7 | 0 | — | — | 0 | [1h18m](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820596) | [2h06m](https://github.com/iree-org/iree/actions/runs/28299106146/job/83844610756) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 14 | 0 | — | — | 0 | [1h35m](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978313) | [1h58m](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820619) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 7 | 0 | — | — | 0 | [38m12s](https://github.com/iree-org/iree/actions/runs/28299106146/job/83844610637) | [1h26m](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978268) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 14 | 0 | — | — | 0 | [49m55s](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978320) | [1h23m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041461) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [14m34s](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820556) | [1h19m](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077674) | — | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 14 | 0 | — | — | 0 | [14m55s](https://github.com/iree-org/iree/actions/runs/28298636190/job/83843455623) | [1h04m](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077740) | — | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [5m35s](https://github.com/iree-org/iree/actions/runs/28298243961/job/83842403412) | [38m51s](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820585) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 7 | 0 | — | — | 0 | [4m33s](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978328) | [34m43s](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041406) | — | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 28 | 0 | — | — | 0 | [2m17s](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820595) | [15m03s](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978318) | — | 28 |
| `ubuntu-24.04` | github-hosted | 134 | 0 | — | — | 0 | [32s](https://github.com/iree-org/iree/actions/runs/28299136769/job/83844378693) | [8m37s](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820544) | — | 134 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [50s](https://github.com/iree-org/iree/actions/runs/28299121821/job/83844226086) | [7m06s](https://github.com/iree-org/iree/actions/runs/28299152505/job/83844390349) | — | 21 |
| `windows-2022` | github-hosted | 21 | 0 | — | — | 0 | [1m04s](https://github.com/iree-org/iree/actions/runs/28299121821/job/83844226070) | [7m03s](https://github.com/iree-org/iree/actions/runs/28299152505/job/83844390344) | — | 21 |
| `macos-14` | github-hosted | 21 | 0 | — | — | 0 | [12s](https://github.com/iree-org/iree/actions/runs/28299152505/job/83844390354) | [5m02s](https://github.com/iree-org/iree/actions/runs/28299177799/job/83844390148) | — | 21 |
| `azure-linux-scale` | ossci | 35 | 0 | — | — | 0 | [2m02s](https://github.com/iree-org/iree/actions/runs/28299121821/job/83844226159) | [4m12s](https://github.com/iree-org/iree/actions/runs/28299152505/job/83844390408) | — | 35 |
| `azure-windows-scale` | ossci | 7 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28299121821/job/83844226142) | [8s](https://github.com/iree-org/iree/actions/runs/28299177799/job/83844390285) | — | 7 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 7 | 6 | [6h20m](https://github.com/iree-org/iree/actions/runs/28298636190/job/83843455562) | 2026-06-27 18:24 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [6h20m](https://github.com/iree-org/iree/actions/runs/28298636190/job/83843455562) | 2026-06-27 18:24 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/fill-buffer-1byte-edge` | pull_request |
| [6h02m](https://github.com/iree-org/iree/actions/runs/28299106146/job/83844610658) | 2026-06-27 18:24 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/copy-buffer-1byte-grid` | pull_request |
| [5h59m](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820560) | 2026-06-27 18:24 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/indirect-dispatch-stack-garbage` | pull_request |
| [5h56m](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978281) | 2026-06-27 18:24 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/staging-buffer-overflow` | pull_request |
| [5h55m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041346) | 2026-06-27 18:24 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/export-name-lookup` | pull_request |
| [5h54m](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077655) | 2026-06-27 18:24 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/indirect-dispatch-offset` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 7 | 6 | [6h20m](https://github.com/iree-org/iree/actions/runs/28298636190/job/83843455562) | 2026-06-27 18:24 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [2h43m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041447) | [3h11m](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077745) | [3h11m](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077745) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [32m06s](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978307) | [3h05m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041484) | [3h05m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041484) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 7 | 0 | — | — | [1h29m](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820588) | [2h36m](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077724) | [2h36m](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077724) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 7 | 0 | — | — | [1h25m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041444) | [2h16m](https://github.com/iree-org/iree/actions/runs/28299106146/job/83844610742) | [2h16m](https://github.com/iree-org/iree/actions/runs/28299106146/job/83844610742) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 7 | 0 | — | — | [1h06m](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077633) | [2h10m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041355) | [2h10m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041355) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 7 | 0 | — | — | [1h18m](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820596) | [2h06m](https://github.com/iree-org/iree/actions/runs/28299106146/job/83844610756) | [2h06m](https://github.com/iree-org/iree/actions/runs/28299106146/job/83844610756) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 7 | 0 | — | — | [1h38m](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820609) | [2h03m](https://github.com/iree-org/iree/actions/runs/28299106146/job/83844610751) | [2h03m](https://github.com/iree-org/iree/actions/runs/28299106146/job/83844610751) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 7 | 0 | — | — | [1h05m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041473) | [1h58m](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820619) | [1h58m](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820619) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 7 | 0 | — | — | [17m27s](https://github.com/iree-org/iree/actions/runs/28299106146/job/83844610785) | [1h30m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041445) | [1h30m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041445) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 7 | 0 | — | — | [38m12s](https://github.com/iree-org/iree/actions/runs/28299106146/job/83844610637) | [1h26m](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978268) | [1h26m](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978268) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 7 | 0 | — | — | [56m15s](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978308) | [1h23m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041461) | [1h23m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041461) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 7 | 0 | — | — | [14m34s](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820556) | [1h19m](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077674) | [1h19m](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077674) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [32m00s](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820589) | [1h17m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041435) | [1h17m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041435) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [13m28s](https://github.com/iree-org/iree/actions/runs/28298636190/job/83843455694) | [49m04s](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077726) | [49m04s](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077726) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 7 | 0 | — | — | [5m35s](https://github.com/iree-org/iree/actions/runs/28298243961/job/83842403412) | [38m51s](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820585) | [38m51s](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820585) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 7 | 0 | — | — | [4m33s](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978328) | [34m43s](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041406) | [34m43s](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041406) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 7 | 0 | — | — | [4m02s](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978314) | [15m18s](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077748) | [15m18s](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077748) | 7 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 7 | 0 | — | — | [2m17s](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820595) | [15m03s](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978318) | [15m03s](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978318) | 7 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 7 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820550) | [13m11s](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978367) | [13m11s](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978367) | 7 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 149 | 0% (0/149) |  | 2h32m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 122 | 7% (9/122) |  | 3h41m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 110 | 0% (0/110) |  | 3h47m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 106 | 0% (0/106) |  | 3h55m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 33 | 0% (0/33) |  | 5h10m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 6h20m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h23m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h36m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h05m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h10m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h26m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h16m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h58m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h06m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h04m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
