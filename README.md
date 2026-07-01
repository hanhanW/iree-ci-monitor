# iree-ci-monitor

_Updated: 2026-06-30 18:25 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [33m55s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341708174) | [1h08m](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954731) | — | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [50m31s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618684) | [1h05m](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618541) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [46m53s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707830) | [56m46s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954717) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [40m57s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618419) | [43m43s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981355) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [24m47s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707716) | [42m57s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954783) | — | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [26m51s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981234) | [38m17s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707742) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [34m25s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954736) | [37m54s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618278) | — | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [16m38s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618295) | [31m17s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981323) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [13m35s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618582) | [30m05s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707866) | — | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | — | 0 | [16m04s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707648) | [29m38s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954939) | — | 16 |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [9m15s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981310) | [28m11s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707892) | — | `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [9m03s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618488) | [27m01s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954861) | — | `iree-mi308-1` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [10m04s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954767) | [15m32s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707992) | — | `shark55-ci` |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [1m33s](https://github.com/iree-org/iree/actions/runs/28457588344/job/84336648691) | [6m44s](https://github.com/iree-org/iree/actions/runs/28457588344/job/84336648741) | — | 15 |
| `ubuntu-24.04` | github-hosted | 96 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707790) | [6m35s](https://github.com/iree-org/iree/actions/runs/28457562355/job/84337141437) | — | 96 |
| `windows-2022` | github-hosted | 15 | 0 | — | — | 0 | [31s](https://github.com/iree-org/iree/actions/runs/28457505639/job/84336385878) | [6m06s](https://github.com/iree-org/iree/actions/runs/28457562355/job/84337141421) | — | 15 |
| `azure-linux-scale` | ossci | 26 | 0 | — | — | 0 | [1m21s](https://github.com/iree-org/iree/actions/runs/28457562355/job/84337141436) | [3m35s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84337613218) | — | 26 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 0 | [13s](https://github.com/iree-org/iree/actions/runs/28457588344/job/84336648668) | [2m05s](https://github.com/iree-org/iree/actions/runs/28457588344/job/84336648745) | — | 15 |
| `azure-windows-scale` | ossci | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28457562355/job/84337141593) | [12s](https://github.com/iree-org/iree/actions/runs/28457505639/job/84336386069) | — | 5 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28457448570/job/84336029714) | [2s](https://github.com/iree-org/iree/actions/runs/28457448570/job/84336029725) | — | 3 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 3 | 3 | [9h17m](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981214) | 2026-06-30 18:25 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [9h17m](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981214) | 2026-06-30 18:25 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/overload_iree_tiling_interface_ops` | pull_request |
| [9h13m](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954579) | 2026-06-30 18:25 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/scalable_vector_level_tiling` | pull_request |
| [9h10m](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707596) | 2026-06-30 18:25 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/scalable_distribution_tiling` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 3 | 3 | [9h17m](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981214) | 2026-06-30 18:25 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [33m55s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341708174) | [1h08m](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954731) | [1h08m](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954731) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [42m58s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981522) | [1h05m](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618541) | [1h05m](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618541) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [55m33s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981276) | [1h01m](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707759) | [1h01m](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707759) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [50m36s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618704) | [56m46s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954717) | [56m46s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954717) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [44m03s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954784) | [47m11s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981511) | [47m11s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981511) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [40m57s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618419) | [43m43s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981355) | [43m43s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981355) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [24m47s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707716) | [42m57s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954783) | [42m57s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954783) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [26m51s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981234) | [38m17s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707742) | [38m17s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707742) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [34m25s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954736) | [37m54s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618278) | [37m54s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618278) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 0 | — | — | [27m05s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618467) | [34m19s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981332) | [34m19s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981332) | 4 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [16m38s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618295) | [31m17s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981323) | [31m17s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981323) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [17m25s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618485) | [30m05s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707866) | [30m05s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707866) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 0 | — | — | [24m33s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618417) | [29m38s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954939) | [29m38s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954939) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [12m28s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954774) | [28m11s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707892) | [28m11s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707892) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 4 | 0 | — | — | [9m03s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618488) | [27m01s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954861) | [27m01s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954861) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [8m17s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707914) | [24m39s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954776) | [24m39s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954776) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [13m35s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618582) | [22m59s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954745) | [22m59s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954745) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 0 | — | — | [13m53s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618556) | [18m41s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954998) | [18m41s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954998) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 0 | — | — | [12m31s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618523) | [16m04s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707648) | [16m04s](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707648) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 143 | 0% (0/143) |  | 3h11m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 205 | 0% (0/205) |  | 7h59m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 178 | 8% (14/178) |  | 8h00m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 169 | 0% (0/169) |  | 8h11m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 47 | 0% (0/47) |  | 8h36m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 9h17m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h05m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h08m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
