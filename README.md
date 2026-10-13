# iree-ci-monitor

_Updated: 2026-10-13 07:19 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 16 | 1 | [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712546) | 2026-10-13 07:17 PDT | 1 | [26m07s](https://github.com/iree-org/iree/actions/runs/38388471848/job/115268646365) | [1h23m](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197819924) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 16 | 2 | [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712357) | 2026-10-13 07:17 PDT | 0 | [29m19s](https://github.com/iree-org/iree/actions/runs/38388815748/job/115270726685) | [1h22m](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197820125) | 0% (0/6) | `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [21m32s](https://github.com/iree-org/iree/actions/runs/38366670920/job/115196059518) | [1h16m](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197821692) | 100% (2/2) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [7m46s](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197820416) | [1h11m](https://github.com/iree-org/iree/actions/runs/38370514385/job/115208705228) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 16 | 2 | [31m44s](https://github.com/iree-org/iree/actions/runs/38406694165/job/115331356325) | 2026-10-13 07:17 PDT | 1 | [25m54s](https://github.com/iree-org/iree/actions/runs/38402100476/job/115315577172) | [1h09m](https://github.com/iree-org/iree/actions/runs/38370514385/job/115208705278) | 0% (0/6) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 8 | 1 | [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712340) | 2026-10-13 07:17 PDT | 0 | [15m38s](https://github.com/iree-org/iree/actions/runs/38388815748/job/115270726812) | [52m54s](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197820640) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 8 | 1 | [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712674) | 2026-10-13 07:17 PDT | 0 | [20m43s](https://github.com/iree-org/iree/actions/runs/38370514385/job/115208705255) | [30m01s](https://github.com/iree-org/iree/actions/runs/38388815748/job/115270726718) | 0% (0/3) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 16 | 2 | [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712337) | 2026-10-13 07:17 PDT | 0 | [4m07s](https://github.com/iree-org/iree/actions/runs/38402100476/job/115315577028) | [16m47s](https://github.com/iree-org/iree/actions/runs/38370514385/job/115208705407) | 0% (0/6) | `shark55-ci`, `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 243 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115337797071) | [2m47s](https://github.com/iree-org/iree/actions/runs/38366670920/job/115196059570) | 5% (4/76) | 221 |
| `macos-15` | github-hosted | 37 | 0 | — | — | 1 | [9s](https://github.com/iree-org/iree/actions/runs/38405811674/job/115325117293) | [2m18s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207675) | 0% (0/12) | 37 |
| `azure-linux-scale` | ossci | 78 | 0 | — | — | 7 | [9s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325208817) | [2m15s](https://github.com/iree-org/iree/actions/runs/38409797849/job/115339949877) | 4% (1/27) | 78 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [2m12s](https://github.com/iree-org/iree/actions/runs/38377156072/job/115228303511) | [2m12s](https://github.com/iree-org/iree/actions/runs/38377156072/job/115228303511) | 100% (1/1) | 1 |
| `windows-2022` | github-hosted | 36 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/38409797849/job/115339949213) | [2m02s](https://github.com/iree-org/iree/actions/runs/38406697790/job/115329152275) | 0% (0/12) | 36 |
| `ubuntu-24.04-arm` | github-hosted | 36 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/38406694431/job/115328867364) | [1m49s](https://github.com/iree-org/iree/actions/runs/38367113503/job/115195300018) | 0% (0/12) | 36 |
| `azure-windows-scale` | ossci | 12 | 0 | — | — | 2 | [1s](https://github.com/iree-org/iree/actions/runs/38409506387/job/115337914836) | [47s](https://github.com/iree-org/iree/actions/runs/38409797849/job/115339949856) | 0% (0/3) | 11 |
| `ubuntu-latest` | github-hosted | 51 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38409508514/job/115337815093) | [30s](https://github.com/iree-org/iree/actions/runs/38367109799/job/115194769505) | 0% (0/12) | 51 |
| `ubuntu-cca-77785908-7ef3-498a-9ae0-bbebb95125d3` | github-hosted | 1 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/38370283664/job/115205283223) | [4s](https://github.com/iree-org/iree/actions/runs/38370283664/job/115205283223) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 8 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [31m44s](https://github.com/iree-org/iree/actions/runs/38406694165/job/115331356325) | 2026-10-13 07:17 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/roberto-laudani/qdq-per-channel-group` | pull_request |
| [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712337) | 2026-10-13 07:17 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | `main` | push |
| [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712340) | 2026-10-13 07:17 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `main` | push |
| [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712357) | 2026-10-13 07:17 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712413) | 2026-10-13 07:17 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | `main` | push |
| [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712546) | 2026-10-13 07:17 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712614) | 2026-10-13 07:17 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712674) | 2026-10-13 07:17 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `main` | push |
| [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712710) | 2026-10-13 07:17 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 8 | 1 | [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712546) | 2026-10-13 07:17 PDT | [18m27s](https://github.com/iree-org/iree/actions/runs/38406694165/job/115331356163) | [1h32m](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197820010) | [1h32m](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197820010) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 8 | 1 | [31m44s](https://github.com/iree-org/iree/actions/runs/38406694165/job/115331356325) | 2026-10-13 07:17 PDT | [23m22s](https://github.com/iree-org/iree/actions/runs/38370514385/job/115208705293) | [1h31m](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197819980) | [1h31m](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197819980) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 8 | 1 | [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712710) | 2026-10-13 07:17 PDT | [49m46s](https://github.com/iree-org/iree/actions/runs/38388471848/job/115268646631) | [1h29m](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197820287) | [1h29m](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197820287) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [34m21s](https://github.com/iree-org/iree/actions/runs/38388815748/job/115270726903) | [1h23m](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197819924) | [1h23m](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197819924) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 8 | 1 | [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712357) | 2026-10-13 07:17 PDT | [29m19s](https://github.com/iree-org/iree/actions/runs/38388815748/job/115270726685) | [1h22m](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197820125) | [1h22m](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197820125) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 3 | 0 | — | — | [21m32s](https://github.com/iree-org/iree/actions/runs/38366670920/job/115196059518) | [1h16m](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197821692) | [1h16m](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197821692) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 8 | 0 | — | — | [7m46s](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197820416) | [1h11m](https://github.com/iree-org/iree/actions/runs/38370514385/job/115208705228) | [1h11m](https://github.com/iree-org/iree/actions/runs/38370514385/job/115208705228) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 8 | 1 | [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712614) | 2026-10-13 07:17 PDT | [31m41s](https://github.com/iree-org/iree/actions/runs/38388471848/job/115268646409) | [1h09m](https://github.com/iree-org/iree/actions/runs/38370514385/job/115208705278) | [1h09m](https://github.com/iree-org/iree/actions/runs/38370514385/job/115208705278) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 1 | [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712337) | 2026-10-13 07:17 PDT | [6m44s](https://github.com/iree-org/iree/actions/runs/38406694165/job/115331355920) | [1h02m](https://github.com/iree-org/iree/actions/runs/38366670920/job/115196059954) | [1h02m](https://github.com/iree-org/iree/actions/runs/38366670920/job/115196059954) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 8 | 1 | [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712340) | 2026-10-13 07:17 PDT | [15m38s](https://github.com/iree-org/iree/actions/runs/38388815748/job/115270726812) | [52m54s](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197820640) | [52m54s](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197820640) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 8 | 1 | [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712674) | 2026-10-13 07:17 PDT | [20m43s](https://github.com/iree-org/iree/actions/runs/38370514385/job/115208705255) | [30m01s](https://github.com/iree-org/iree/actions/runs/38388815748/job/115270726718) | [30m01s](https://github.com/iree-org/iree/actions/runs/38388815748/job/115270726718) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 1 | [10m25s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712413) | 2026-10-13 07:17 PDT | [11s](https://github.com/iree-org/iree/actions/runs/38388815748/job/115270726704) | [16m47s](https://github.com/iree-org/iree/actions/runs/38370514385/job/115208705407) | [16m47s](https://github.com/iree-org/iree/actions/runs/38370514385/job/115208705407) | 2 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 16 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/38402100534/job/115312157047) | [6m37s](https://github.com/iree-org/iree/actions/runs/38367113503/job/115195299789) | [6m37s](https://github.com/iree-org/iree/actions/runs/38367113503/job/115195299789) | 12 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712400) | [6m12s](https://github.com/iree-org/iree/actions/runs/38366670920/job/115196059601) | [6m12s](https://github.com/iree-org/iree/actions/runs/38366670920/job/115196059601) | 8 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 16 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/38402100534/job/115312156873) | [6m09s](https://github.com/iree-org/iree/actions/runs/38367113503/job/115195299806) | [6m09s](https://github.com/iree-org/iree/actions/runs/38367113503/job/115195299806) | 12 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 12 | 0 | — | — | [45s](https://github.com/iree-org/iree/actions/runs/38405811674/job/115325117731) | [6m04s](https://github.com/iree-org/iree/actions/runs/38367113503/job/115195299861) | [6m04s](https://github.com/iree-org/iree/actions/runs/38367113503/job/115195299861) | 12 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712369) | [4m15s](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197819810) | [4m15s](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197819810) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 12 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38406697790/job/115329152688) | [4m02s](https://github.com/iree-org/iree/actions/runs/38388471580/job/115266084059) | [4m02s](https://github.com/iree-org/iree/actions/runs/38388471580/job/115266084059) | 12 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712603) | [3m47s](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197820138) | [3m47s](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197820138) | 8 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712746) | [3m38s](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197819945) | [3m38s](https://github.com/iree-org/iree/actions/runs/38367113422/job/115197819945) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 300 | 14% (41/299) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 274 | 0% (0/273) | yes | running |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h11m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h22m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h23m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache` p95 queue 1h16m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h09m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d
- **[spof]** `ubuntu-cca-77785908-7ef3-498a-9ae0-bbebb95125d3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
