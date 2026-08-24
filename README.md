# iree-ci-monitor

_Updated: 2026-08-24 12:03 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 22 | 0 | — | — | 0 | [22m31s](https://github.com/iree-org/iree/actions/runs/32740814446/job/97478145515) | [1h20m](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422004057) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 11 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/32740814446/job/97478145063) | [1h20m](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245788) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 11 | 0 | — | — | 0 | [13m45s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492289) | [1h05m](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422003830) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 11 | 0 | — | — | 0 | [25m16s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492433) | [1h00m](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245725) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 22 | 0 | — | — | 0 | [9m51s](https://github.com/iree-org/iree/actions/runs/32740814446/job/97478145525) | [36m28s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245689) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [6m31s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365422) | [33m40s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382623918) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 22 | 0 | — | — | 0 | [5m59s](https://github.com/iree-org/iree/actions/runs/32719848942/job/97410951164) | [30m38s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408280) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [18m03s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382624089) | [27m25s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245644) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 11 | 0 | — | — | 0 | [9m04s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405205) | [21m49s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408140) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 22 | 0 | — | — | 0 | [7m09s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365536) | [20m42s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492411) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [9m22s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245638) | [18m24s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492308) | 0% (0/1) | `shark10-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 64 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97520043612) | [1m27s](https://github.com/iree-org/iree/actions/runs/32749822444/job/97504604292) | 0% (0/8) | 63 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m22s](https://github.com/iree-org/iree/actions/runs/32711839453/job/97384704694) | [1m22s](https://github.com/iree-org/iree/actions/runs/32711839453/job/97384704694) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 36 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/32737057871/job/97462352995) | [1m16s](https://github.com/iree-org/iree/actions/runs/32724632491/job/97423126525) | 0% (0/3) | 36 |
| `macos-14` | github-hosted | 37 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/32719848859/job/97408786836) | [12s](https://github.com/iree-org/iree/actions/runs/32711849180/job/97384803326) | 0% (0/4) | 37 |
| `ubuntu-24.04` | github-hosted | 252 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365514) | [5s](https://github.com/iree-org/iree/actions/runs/32749221818/job/97502023660) | 0% (0/21) | 246 |
| `windows-2022` | github-hosted | 36 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32750234454/job/97505617688) | [4s](https://github.com/iree-org/iree/actions/runs/32740814524/job/97475076650) | 0% (0/3) | 36 |
| `azure-windows-scale` | ossci | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32710345403/job/97380267280) | [3s](https://github.com/iree-org/iree/actions/runs/32737057871/job/97462353214) | 0% (0/1) | 12 |
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32737857775/job/97464928256) | [3s](https://github.com/iree-org/iree/actions/runs/32737859284/job/97464936677) | 0% (0/3) | 18 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 11 | 0 | — | — | [9m36s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405322) | [1h25m](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408503) | [1h25m](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408503) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 11 | 0 | — | — | [22m31s](https://github.com/iree-org/iree/actions/runs/32740814446/job/97478145515) | [1h20m](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422004057) | [1h20m](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422004057) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 11 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32740814446/job/97478145063) | [1h20m](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245788) | [1h20m](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245788) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 11 | 0 | — | — | [13m45s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492289) | [1h05m](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422003830) | [1h05m](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422003830) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 11 | 0 | — | — | [25m16s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492433) | [1h00m](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245725) | [1h00m](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245725) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 11 | 0 | — | — | [9m51s](https://github.com/iree-org/iree/actions/runs/32740814446/job/97478145525) | [40m39s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245647) | [40m39s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245647) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 11 | 0 | — | — | [8m13s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492380) | [36m28s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245689) | [36m28s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245689) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 11 | 0 | — | — | [6m31s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365422) | [33m40s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382623918) | [33m40s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382623918) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 11 | 0 | — | — | [5m59s](https://github.com/iree-org/iree/actions/runs/32719848942/job/97410951164) | [30m56s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408341) | [30m56s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408341) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 11 | 0 | — | — | [4m04s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365500) | [30m38s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408280) | [30m38s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408280) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 11 | 0 | — | — | [18m03s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382624089) | [27m25s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245644) | [27m25s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245644) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 11 | 0 | — | — | [9m04s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405205) | [21m49s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408140) | [21m49s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408140) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 11 | 0 | — | — | [7m09s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365536) | [21m20s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245754) | [21m20s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245754) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 11 | 0 | — | — | [9m22s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245638) | [18m24s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492308) | [18m24s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492308) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 11 | 0 | — | — | [6m13s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365633) | [14m10s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382624539) | [14m10s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382624539) | 3 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 11 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382624308) | [5m32s](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422004146) | [5m32s](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422004146) | 11 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 12 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32749822444/job/97504604157) | [2m05s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982088) | [2m05s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982088) | 12 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 12 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/32740814524/job/97475076667) | [1m58s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982311) | [1m58s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982311) | 12 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 12 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32740814524/job/97475076755) | [1m43s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982273) | [1m43s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982273) | 12 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 12 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/32737057871/job/97462352995) | [1m39s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982176) | [1m39s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982176) | 12 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 190 | 0% (0/189) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 264 | 2% (4/263) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 182 | 0% (0/181) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 251 | 2% (5/250) | yes | running |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h00m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h05m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
