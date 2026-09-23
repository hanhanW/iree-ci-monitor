# iree-ci-monitor

_Updated: 2026-09-23 14:33 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 12 | 1 | [59m44s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932915) | 2026-09-23 14:32 PDT | 0 | [31m04s](https://github.com/iree-org/iree/actions/runs/35897931913/job/107309709651) | [2h20m](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315493) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 24 | 0 | — | — | 0 | [28m54s](https://github.com/iree-org/iree/actions/runs/35897930861/job/107314101946) | [2h15m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888626) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 24 | 0 | — | — | 1 | [49m52s](https://github.com/iree-org/iree/actions/runs/35897932470/job/107312629419) | [2h14m](https://github.com/iree-org/iree/actions/runs/35860367806/job/107184134999) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 24 | 0 | — | — | 0 | [44m18s](https://github.com/iree-org/iree/actions/runs/35860367806/job/107184135088) | [2h12m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888670) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 24 | 0 | — | — | 0 | [21m39s](https://github.com/iree-org/iree/actions/runs/35897931913/job/107309709627) | [1h59m](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315170) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 12 | 0 | — | — | 1 | [35m48s](https://github.com/iree-org/iree/actions/runs/35900607075/job/107322248439) | [1h48m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888732) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 12 | 0 | — | — | 0 | [27m11s](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315460) | [1h19m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888553) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [37m09s](https://github.com/iree-org/iree/actions/runs/35910508653/job/107352869008) | [53m43s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802674) | — | `shark75-ci` |
| `azure-linux-scale` | ossci | 60 | 0 | — | — | 0 | [2m31s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751490) | [27m41s](https://github.com/iree-org/iree/actions/runs/35860367805/job/107180504989) | — | 60 |
| `azure-windows-scale` | ossci | 12 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/35897930850/job/107307683472) | [8m36s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180221080) | — | 12 |
| `ubuntu-24.04-arm` | github-hosted | 36 | 0 | — | — | 0 | [1m54s](https://github.com/iree-org/iree/actions/runs/35897932435/job/107306898898) | [6m37s](https://github.com/iree-org/iree/actions/runs/35897931940/job/107306972239) | — | 36 |
| `macos-14` | github-hosted | 36 | 0 | — | — | 0 | [2m26s](https://github.com/iree-org/iree/actions/runs/35897931505/job/107306775971) | [6m24s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180220927) | — | 36 |
| `ubuntu-24.04` | github-hosted | 315 | 0 | — | — | 0 | [23s](https://github.com/iree-org/iree/actions/runs/35897931940/job/107306759466) | [5m40s](https://github.com/iree-org/iree/actions/runs/35897931913/job/107309709680) | 0% (0/1) | 277 |
| `windows-2022` | github-hosted | 36 | 0 | — | — | 0 | [2m00s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751430) | [5m40s](https://github.com/iree-org/iree/actions/runs/35897931940/job/107306971924) | — | 36 |
| `ubuntu-latest` | github-hosted | 60 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35910502239/job/107348828740) | [1m05s](https://github.com/iree-org/iree/actions/runs/35860362399/job/107178794627) | — | 60 |
| `Linux,X64,iree-w7900` | self-hosted | 12 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [59m44s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932915) | 2026-09-23 14:32 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/jschuhmacher/stablehlo_dynamic_gather_broadcast` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 12 | 0 | — | — | [40m26s](https://github.com/iree-org/iree/actions/runs/35900607075/job/107322248456) | [2h29m](https://github.com/iree-org/iree/actions/runs/35860367806/job/107184134766) | [2h29m](https://github.com/iree-org/iree/actions/runs/35860367806/job/107184134766) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 12 | 1 | [59m44s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932915) | 2026-09-23 14:32 PDT | [31m04s](https://github.com/iree-org/iree/actions/runs/35897931913/job/107309709651) | [2h20m](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315493) | [2h20m](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315493) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 12 | 0 | — | — | [37m41s](https://github.com/iree-org/iree/actions/runs/35897930861/job/107314101957) | [2h16m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888880) | [2h16m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888880) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 12 | 0 | — | — | [44m18s](https://github.com/iree-org/iree/actions/runs/35860367806/job/107184135088) | [2h16m](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315269) | [2h16m](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315269) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 12 | 0 | — | — | [28m54s](https://github.com/iree-org/iree/actions/runs/35897930861/job/107314101946) | [2h15m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888626) | [2h15m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888626) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 12 | 0 | — | — | [59m05s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802839) | [2h12m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888637) | [2h14m](https://github.com/iree-org/iree/actions/runs/35860367806/job/107184134999) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 12 | 0 | — | — | [47m04s](https://github.com/iree-org/iree/actions/runs/35897930861/job/107314101892) | [2h06m](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315280) | [2h06m](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315280) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 12 | 0 | — | — | [24m40s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802689) | [2h00m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888461) | [2h00m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888461) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 12 | 0 | — | — | [11m02s](https://github.com/iree-org/iree/actions/runs/35860367806/job/107184134803) | [1h59m](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315170) | [1h59m](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315170) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 12 | 0 | — | — | [35m48s](https://github.com/iree-org/iree/actions/runs/35900607075/job/107322248439) | [1h48m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888732) | [1h48m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888732) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 12 | 0 | — | — | [27m11s](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315460) | [1h19m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888553) | [1h19m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888553) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 12 | 0 | — | — | [37m09s](https://github.com/iree-org/iree/actions/runs/35910508653/job/107352869008) | [53m43s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802674) | [58m20s](https://github.com/iree-org/iree/actions/runs/35897930861/job/107314102223) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 12 | 0 | — | — | [4m54s](https://github.com/iree-org/iree/actions/runs/35860367733/job/107179886844) | [28m22s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180221070) | [28m22s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180221070) | 12 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 12 | 0 | — | — | [2m14s](https://github.com/iree-org/iree/actions/runs/35897931940/job/107306972050) | [28m15s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180220833) | [28m15s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180220833) | 12 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 12 | 0 | — | — | [6m35s](https://github.com/iree-org/iree/actions/runs/35897930861/job/107308478792) | [27m41s](https://github.com/iree-org/iree/actions/runs/35860367805/job/107180504989) | [45m57s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107349860083) | 12 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 12 | 0 | — | — | [2m32s](https://github.com/iree-org/iree/actions/runs/35897931940/job/107306972147) | [26m54s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180221047) | [26m54s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180221047) | 12 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 12 | 0 | — | — | [1m43s](https://github.com/iree-org/iree/actions/runs/35860366367/job/107179220498) | [26m41s](https://github.com/iree-org/iree/actions/runs/35860366207/job/107180014491) | [26m41s](https://github.com/iree-org/iree/actions/runs/35860366207/job/107180014491) | 12 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 12 | 0 | — | — | [3m30s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751541) | [10m04s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180221061) | [10m04s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180221061) | 12 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 12 | 0 | — | — | [4m15s](https://github.com/iree-org/iree/actions/runs/35897932435/job/107306898903) | [10m01s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180220915) | [10m01s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180220915) | 12 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 12 | 0 | — | — | [1m36s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751267) | [8m56s](https://github.com/iree-org/iree/actions/runs/35860366207/job/107180014296) | [8m56s](https://github.com/iree-org/iree/actions/runs/35860366207/job/107180014296) | 12 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 396 | 2% (8/395) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 413 | 1% (5/412) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 134 | 1% (2/134) |  | 6d00h ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h15m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h14m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache` p95 queue 1h48m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h12m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h59m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-w7900` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
