# iree-ci-monitor

_Updated: 2026-08-24 06:16 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 14 | 1 | [57m22s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408503) | 2026-08-24 06:15 PDT | 2 | [39m06s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245655) | [1h20m](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422004057) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 7 | 0 | — | — | 0 | [20m33s](https://github.com/iree-org/iree/actions/runs/32719848942/job/97410951125) | [1h05m](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422003830) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 7 | 0 | — | — | 1 | [28m20s](https://github.com/iree-org/iree/actions/runs/32719848942/job/97410951283) | [1h00m](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245725) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 14 | 0 | — | — | 0 | [16m54s](https://github.com/iree-org/iree/actions/runs/32719848942/job/97410951064) | [36m28s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245689) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [4m27s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245650) | [33m40s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382623918) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 14 | 0 | — | — | 0 | [11m55s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382624103) | [30m38s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408280) | 0% (0/2) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [18m03s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382624089) | [27m25s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245644) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 7 | 0 | — | — | 0 | [6m14s](https://github.com/iree-org/iree/actions/runs/32719848942/job/97410951035) | [21m49s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408140) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 14 | 0 | — | — | 0 | [12m15s](https://github.com/iree-org/iree/actions/runs/32719848942/job/97410951235) | [20m42s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492411) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [9m22s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245638) | [18m24s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492308) | 0% (0/1) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 7 | 2 | [1h08m](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245788) | 2026-08-24 06:15 PDT | 0 | [6m30s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492258) | [12m11s](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422003988) | 0% (0/1) | `shark75-ci` |
| `ubuntu-24.04-arm` | github-hosted | 27 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/32710345403/job/97380266966) | [1m39s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982176) | 0% (0/3) | 27 |
| `azure-linux-scale` | ossci | 43 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/32711849180/job/97384804334) | [1m26s](https://github.com/iree-org/iree/actions/runs/32723519155/job/97419809589) | 0% (0/8) | 43 |
| `macos-14` | github-hosted | 27 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329989020) | [1m23s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982033) | 0% (0/4) | 27 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m22s](https://github.com/iree-org/iree/actions/runs/32711839453/job/97384704694) | [1m22s](https://github.com/iree-org/iree/actions/runs/32711839453/job/97384704694) | 0% (0/1) | 1 |
| `ubuntu-24.04` | github-hosted | 170 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245871) | [1m09s](https://github.com/iree-org/iree/actions/runs/32711849180/job/97384803280) | 0% (0/21) | 166 |
| `windows-2022` | github-hosted | 26 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32724632491/job/97423126386) | [6s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988894) | 0% (0/3) | 26 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32723518495/job/97419757578) | [3s](https://github.com/iree-org/iree/actions/runs/32718375077/job/97404356042) | 0% (0/3) | 12 |
| `azure-windows-scale` | ossci | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32710345403/job/97380267280) | [2s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982715) | 0% (0/1) | 8 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [1h08m](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245788) | 2026-08-24 06:15 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `vk-local-fallback` | pull_request |
| [57m22s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408149) | 2026-08-24 06:15 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `fix-arc` | pull_request |
| [57m22s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408503) | 2026-08-24 06:15 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `fix-arc` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [44m59s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245720) | [1h20m](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422004057) | [1h20m](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422004057) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 7 | 2 | [1h08m](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245788) | 2026-08-24 06:15 PDT | [6m30s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492258) | [12m11s](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422003988) | [12m11s](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422003988) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 7 | 0 | — | — | [20m33s](https://github.com/iree-org/iree/actions/runs/32719848942/job/97410951125) | [1h05m](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422003830) | [1h05m](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422003830) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 7 | 0 | — | — | [28m20s](https://github.com/iree-org/iree/actions/runs/32719848942/job/97410951283) | [1h00m](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245725) | [1h00m](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245725) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 7 | 1 | [57m22s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408503) | 2026-08-24 06:15 PDT | [37m48s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382624216) | [49m04s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492536) | [49m04s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492536) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 7 | 0 | — | — | [13m12s](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422003969) | [40m39s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245647) | [40m39s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245647) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 7 | 0 | — | — | [8m13s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492380) | [36m28s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245689) | [36m28s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245689) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 7 | 0 | — | — | [4m27s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245650) | [33m40s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382623918) | [33m40s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382623918) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [7m42s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382623929) | [30m56s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408341) | [30m56s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408341) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [5m19s](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422003986) | [30m38s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408280) | [30m38s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408280) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 7 | 0 | — | — | [18m03s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382624089) | [27m25s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245644) | [27m25s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245644) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 7 | 0 | — | — | [6m14s](https://github.com/iree-org/iree/actions/runs/32719848942/job/97410951035) | [21m49s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408140) | [21m49s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97428408140) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 7 | 0 | — | — | [8m22s](https://github.com/iree-org/iree/actions/runs/32719848942/job/97410951207) | [21m20s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245754) | [21m20s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245754) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 7 | 0 | — | — | [9m22s](https://github.com/iree-org/iree/actions/runs/32724632496/job/97425245638) | [18m24s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492308) | [18m24s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492308) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 7 | 0 | — | — | [9m34s](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422003981) | [14m10s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382624539) | [14m10s](https://github.com/iree-org/iree/actions/runs/32710345372/job/97382624539) | 3 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 7 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32711849182/job/97387492353) | [5m32s](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422004146) | [5m32s](https://github.com/iree-org/iree/actions/runs/32723519149/job/97422004146) | 7 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32725554408/job/97425907789) | [2m12s](https://github.com/iree-org/iree/actions/runs/32725606654/job/97426076776) | [2m12s](https://github.com/iree-org/iree/actions/runs/32725606654/job/97426076776) | 9 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32723519155/job/97419809358) | [2m05s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982088) | [2m05s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982088) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 8 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/32719848859/job/97408786992) | [1m58s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982311) | [1m58s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982311) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 8 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32704317443/job/97362150423) | [1m43s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982273) | [1m43s](https://github.com/iree-org/iree/actions/runs/32725554547/job/97425982273) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 246 | 1% (3/243) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 235 | 2% (5/233) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 172 | 0% (0/171) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 177 | 0% (0/176) | yes | running |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h00m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h05m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
