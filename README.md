# iree-ci-monitor

_Updated: 2026-05-25 18:18 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 26 | 0 | — | — | 0 | [1h38m](https://github.com/iree-org/iree/actions/runs/26413436341/job/77753995358) | [3h34m](https://github.com/iree-org/iree/actions/runs/26414858666/job/77758374933) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 13 | 0 | — | — | 0 | [50m24s](https://github.com/iree-org/iree/actions/runs/26414858666/job/77758374907) | [3h14m](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060834) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 13 | 0 | — | — | 0 | [35m57s](https://github.com/iree-org/iree/actions/runs/26413873244/job/77754812369) | [3h05m](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060805) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 13 | 0 | — | — | 0 | [1h18m](https://github.com/iree-org/iree/actions/runs/26414226358/job/77755901846) | [2h41m](https://github.com/iree-org/iree/actions/runs/26414828808/job/77757629366) | 0% (0/1) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 13 | 0 | — | — | 0 | [12m17s](https://github.com/iree-org/iree/actions/runs/26413873244/job/77754812342) | [2h35m](https://github.com/iree-org/iree/actions/runs/26414955715/job/77758689584) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 26 | 0 | — | — | 0 | [38m40s](https://github.com/iree-org/iree/actions/runs/26414848287/job/77757903461) | [2h34m](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060859) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 13 | 0 | — | — | 0 | [15m39s](https://github.com/iree-org/iree/actions/runs/26413436341/job/77753995279) | [2h27m](https://github.com/iree-org/iree/actions/runs/26414226358/job/77755901807) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 26 | 0 | — | — | 0 | [1h02m](https://github.com/iree-org/iree/actions/runs/26414828808/job/77757629388) | [2h21m](https://github.com/iree-org/iree/actions/runs/26414848287/job/77757903419) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 13 | 0 | — | — | 0 | [45m04s](https://github.com/iree-org/iree/actions/runs/26414226358/job/77755901749) | [2h19m](https://github.com/iree-org/iree/actions/runs/26414955715/job/77758689520) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 26 | 0 | — | — | 0 | [28m03s](https://github.com/iree-org/iree/actions/runs/26413873244/job/77754812407) | [1h38m](https://github.com/iree-org/iree/actions/runs/26414858666/job/77758374917) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 13 | 0 | — | — | 0 | [11m52s](https://github.com/iree-org/iree/actions/runs/26412726412/job/77751416417) | [41m27s](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060839) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 13 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26414828808/job/77757629402) | [28m36s](https://github.com/iree-org/iree/actions/runs/26414848287/job/77757903407) | 0% (0/1) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 52 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/26408988025/job/77739835380) | [10m56s](https://github.com/iree-org/iree/actions/runs/26414858666/job/77758374919) | 0% (0/4) | 52 |
| `ubuntu-24.04` | github-hosted | 257 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26413873244/job/77754812414) | [7m29s](https://github.com/iree-org/iree/actions/runs/26414858666/job/77758375007) | 0% (0/18) | 257 |
| `ubuntu-24.04-arm` | github-hosted | 39 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26413436320/job/77752906860) | [4m03s](https://github.com/iree-org/iree/actions/runs/26414858668/job/77757301293) | 0% (0/3) | 39 |
| `windows-2022` | github-hosted | 39 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26414226357/job/77755104475) | [3m17s](https://github.com/iree-org/iree/actions/runs/26414854396/job/77757251524) | 0% (0/3) | 39 |
| `macos-14` | github-hosted | 39 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26409374438/job/77740461522) | [3m00s](https://github.com/iree-org/iree/actions/runs/26414858668/job/77757301374) | 0% (0/3) | 39 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [56s](https://github.com/iree-org/iree/actions/runs/26414955027/job/77757317440) | [1m37s](https://github.com/iree-org/iree/actions/runs/26414955027/job/77757317448) | 0% (0/3) | 3 |
| `azure-linux-scale` | ossci | 66 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/26413436320/job/77752906995) | [1m33s](https://github.com/iree-org/iree/actions/runs/26414858666/job/77757278309) | 0% (0/6) | 66 |
| `azure-windows-scale` | ossci | 13 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26413873239/job/77754018300) | [27s](https://github.com/iree-org/iree/actions/runs/26414848284/job/77757004133) | 0% (0/1) | 13 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 13 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060788) | [9s](https://github.com/iree-org/iree/actions/runs/26408988025/job/77739835347) | 0% (0/1) | 13 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 13 | 0 | — | — | [1h38m](https://github.com/iree-org/iree/actions/runs/26413436341/job/77753995358) | [3h43m](https://github.com/iree-org/iree/actions/runs/26414955715/job/77758689606) | [3h43m](https://github.com/iree-org/iree/actions/runs/26414955715/job/77758689606) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 13 | 0 | — | — | [24m27s](https://github.com/iree-org/iree/actions/runs/26409374575/job/77741191044) | [3h29m](https://github.com/iree-org/iree/actions/runs/26414858666/job/77758374906) | [3h29m](https://github.com/iree-org/iree/actions/runs/26414858666/job/77758374906) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 13 | 0 | — | — | [50m24s](https://github.com/iree-org/iree/actions/runs/26414858666/job/77758374907) | [3h14m](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060834) | [3h14m](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060834) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 13 | 0 | — | — | [35m57s](https://github.com/iree-org/iree/actions/runs/26413873244/job/77754812369) | [3h05m](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060805) | [3h05m](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060805) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 13 | 0 | — | — | [1h02m](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060827) | [2h46m](https://github.com/iree-org/iree/actions/runs/26414226358/job/77755901897) | [2h46m](https://github.com/iree-org/iree/actions/runs/26414226358/job/77755901897) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 13 | 0 | — | — | [1h18m](https://github.com/iree-org/iree/actions/runs/26414226358/job/77755901846) | [2h41m](https://github.com/iree-org/iree/actions/runs/26414828808/job/77757629366) | [2h41m](https://github.com/iree-org/iree/actions/runs/26414828808/job/77757629366) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 13 | 0 | — | — | [12m17s](https://github.com/iree-org/iree/actions/runs/26413873244/job/77754812342) | [2h35m](https://github.com/iree-org/iree/actions/runs/26414955715/job/77758689584) | [2h35m](https://github.com/iree-org/iree/actions/runs/26414955715/job/77758689584) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 13 | 0 | — | — | [38m40s](https://github.com/iree-org/iree/actions/runs/26414848287/job/77757903461) | [2h34m](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060859) | [2h34m](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060859) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 13 | 0 | — | — | [15m39s](https://github.com/iree-org/iree/actions/runs/26413436341/job/77753995279) | [2h27m](https://github.com/iree-org/iree/actions/runs/26414226358/job/77755901807) | [2h27m](https://github.com/iree-org/iree/actions/runs/26414226358/job/77755901807) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 13 | 0 | — | — | [47m30s](https://github.com/iree-org/iree/actions/runs/26414955715/job/77758689634) | [2h24m](https://github.com/iree-org/iree/actions/runs/26414226358/job/77755901855) | [2h24m](https://github.com/iree-org/iree/actions/runs/26414226358/job/77755901855) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 13 | 0 | — | — | [1h26m](https://github.com/iree-org/iree/actions/runs/26414955715/job/77758689597) | [2h20m](https://github.com/iree-org/iree/actions/runs/26413873244/job/77754812434) | [2h20m](https://github.com/iree-org/iree/actions/runs/26413873244/job/77754812434) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 13 | 0 | — | — | [45m04s](https://github.com/iree-org/iree/actions/runs/26414226358/job/77755901749) | [2h19m](https://github.com/iree-org/iree/actions/runs/26414955715/job/77758689520) | [2h20m](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060774) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 13 | 0 | — | — | [37m19s](https://github.com/iree-org/iree/actions/runs/26414828808/job/77757629345) | [1h52m](https://github.com/iree-org/iree/actions/runs/26414955715/job/77758689615) | [1h52m](https://github.com/iree-org/iree/actions/runs/26414955715/job/77758689615) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 13 | 0 | — | — | [15m29s](https://github.com/iree-org/iree/actions/runs/26409374575/job/77741191062) | [1h07m](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060844) | [1h07m](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060844) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 13 | 0 | — | — | [11m52s](https://github.com/iree-org/iree/actions/runs/26412726412/job/77751416417) | [41m27s](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060839) | [41m27s](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060839) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 13 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26414828808/job/77757629402) | [28m36s](https://github.com/iree-org/iree/actions/runs/26414848287/job/77757903407) | [31m32s](https://github.com/iree-org/iree/actions/runs/26414955715/job/77758689626) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 13 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26414828806/job/77756941703) | [15m04s](https://github.com/iree-org/iree/actions/runs/26414854396/job/77757251506) | [17m34s](https://github.com/iree-org/iree/actions/runs/26414858668/job/77757301291) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 13 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26414828806/job/77756941712) | [11m23s](https://github.com/iree-org/iree/actions/runs/26414848284/job/77757004095) | [13m00s](https://github.com/iree-org/iree/actions/runs/26414854396/job/77757251515) | 13 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 13 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/26408988025/job/77739835479) | [10m56s](https://github.com/iree-org/iree/actions/runs/26414858666/job/77758374919) | [17m15s](https://github.com/iree-org/iree/actions/runs/26414854375/job/77758060874) | 13 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 13 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26409374575/job/77741190995) | [10m40s](https://github.com/iree-org/iree/actions/runs/26414848287/job/77757903510) | [14m58s](https://github.com/iree-org/iree/actions/runs/26414828808/job/77757629376) | 13 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 302 | 2% (7/301) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 232 | 4% (9/231) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 280 | 7% (20/279) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 223 | 1% (2/222) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 74 | 3% (2/74) |  | 5h40m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h34m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 3h14m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h34m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h05m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 2h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h41m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h21m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h35m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h38m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
