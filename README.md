# iree-ci-monitor

_Updated: 2026-10-21 14:46 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [15m14s](https://github.com/iree-org/iree/actions/runs/39607316670/job/119260594944) | [1h20m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615579) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 14 | 0 | — | — | 0 | [14m30s](https://github.com/iree-org/iree/actions/runs/39652221066/job/119407787886) | [1h13m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615692) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [29m53s](https://github.com/iree-org/iree/actions/runs/39652221066/job/119407787700) | [1h07m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615750) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 15 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | 0 | [17m54s](https://github.com/iree-org/iree/actions/runs/39646002016/job/119386001961) | [1h07m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615660) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 16 | 2 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | 0 | [12m13s](https://github.com/iree-org/iree/actions/runs/39646002016/job/119386001906) | [1h02m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214616347) | 0% (0/2) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 14 | 0 | — | — | 0 | [2m54s](https://github.com/iree-org/iree/actions/runs/39646002016/job/119386001512) | [44m27s](https://github.com/iree-org/iree/actions/runs/39595459103/job/119210108857) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 7 | 0 | — | — | 0 | [9m51s](https://github.com/iree-org/iree/actions/runs/39607316670/job/119260594774) | [21m42s](https://github.com/iree-org/iree/actions/runs/39595459103/job/119210108767) | 0% (0/1) | `shark75-ci` |
| `azure-linux-scale` | ossci | 52 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/39607316851/job/119246860594) | [4m21s](https://github.com/iree-org/iree/actions/runs/39652221089/job/119404601921) | 0% (0/7) | 52 |
| `macos-15` | github-hosted | 24 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/39607316851/job/119246860059) | [1m24s](https://github.com/iree-org/iree/actions/runs/39595459157/job/119206961793) | 0% (0/3) | 24 |
| `windows-2022` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39646001938/job/119381737040) | [1m04s](https://github.com/iree-org/iree/actions/runs/39652221089/job/119404601873) | 0% (0/3) | 24 |
| `ubuntu-24.04-arm` | github-hosted | 24 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/39646001938/job/119381737071) | [53s](https://github.com/iree-org/iree/actions/runs/39595459157/job/119206961885) | 0% (0/3) | 24 |
| `ubuntu-24.04` | github-hosted | 163 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39626273203/job/119327393538) | [3s](https://github.com/iree-org/iree/actions/runs/39652221066/job/119426141956) | 0% (0/20) | 160 |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39645998329/job/119381615936) | [3s](https://github.com/iree-org/iree/actions/runs/39652212982/job/119403195920) | 0% (0/3) | 24 |
| `azure-windows-scale` | ossci | 8 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/39646001938/job/119381738360) | [2s](https://github.com/iree-org/iree/actions/runs/39622742847/job/119403857349) | 0% (0/1) | 8 |
| `Linux,X64,iree-w7900` | self-hosted | 7 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `fix-spirv-wide-elementwise` | pull_request |
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `fix-spirv-wide-elementwise` | pull_request |
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827580) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `fix-spirv-wide-elementwise` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 7 | 0 | — | — | [15m14s](https://github.com/iree-org/iree/actions/runs/39607316670/job/119260594944) | [1h20m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615579) | [1h20m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615579) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [22m22s](https://github.com/iree-org/iree/actions/runs/39607316670/job/119260595092) | [1h18m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615675) | [1h18m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615675) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 7 | 0 | — | — | [24m53s](https://github.com/iree-org/iree/actions/runs/39607316670/job/119260594765) | [1h15m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615880) | [1h15m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615880) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [6m29s](https://github.com/iree-org/iree/actions/runs/39646002016/job/119386001732) | [1h13m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615692) | [1h13m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615692) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 7 | 0 | — | — | [29m53s](https://github.com/iree-org/iree/actions/runs/39652221066/job/119407787700) | [1h07m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615750) | [1h07m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615750) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 8 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | [17m54s](https://github.com/iree-org/iree/actions/runs/39646002016/job/119386001961) | [1h07m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615660) | [1h07m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615660) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 8 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827580) | 2026-10-19 06:26 PDT | [11m15s](https://github.com/iree-org/iree/actions/runs/39593998836/job/119205283284) | [1h04m](https://github.com/iree-org/iree/actions/runs/39595459103/job/119210108843) | [1h04m](https://github.com/iree-org/iree/actions/runs/39595459103/job/119210108843) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 8 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | [15m32s](https://github.com/iree-org/iree/actions/runs/39652221066/job/119407787866) | [1h02m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214616347) | [1h02m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214616347) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [5m55s](https://github.com/iree-org/iree/actions/runs/39626273203/job/119316843425) | [58m01s](https://github.com/iree-org/iree/actions/runs/39593998836/job/119205283281) | [58m01s](https://github.com/iree-org/iree/actions/runs/39593998836/job/119205283281) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 7 | 0 | — | — | [9m51s](https://github.com/iree-org/iree/actions/runs/39607316670/job/119260594774) | [21m42s](https://github.com/iree-org/iree/actions/runs/39595459103/job/119210108767) | [21m42s](https://github.com/iree-org/iree/actions/runs/39595459103/job/119210108767) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [2m54s](https://github.com/iree-org/iree/actions/runs/39646002016/job/119386001512) | [19m12s](https://github.com/iree-org/iree/actions/runs/39607316670/job/119260595174) | [19m12s](https://github.com/iree-org/iree/actions/runs/39607316670/job/119260595174) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 8 | 0 | — | — | [13s](https://github.com/iree-org/iree/actions/runs/39622742847/job/119403856489) | [4m30s](https://github.com/iree-org/iree/actions/runs/39652221089/job/119404601660) | [4m30s](https://github.com/iree-org/iree/actions/runs/39652221089/job/119404601660) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 8 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/39607316851/job/119246860594) | [4m29s](https://github.com/iree-org/iree/actions/runs/39652221089/job/119404601874) | [4m29s](https://github.com/iree-org/iree/actions/runs/39652221089/job/119404601874) | 8 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 8 | 0 | — | — | [23s](https://github.com/iree-org/iree/actions/runs/39631204737/job/119329681136) | [4m21s](https://github.com/iree-org/iree/actions/runs/39652221089/job/119404601921) | [4m21s](https://github.com/iree-org/iree/actions/runs/39652221089/job/119404601921) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 8 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/39607316851/job/119246860406) | [4m19s](https://github.com/iree-org/iree/actions/runs/39652221089/job/119404602206) | [4m19s](https://github.com/iree-org/iree/actions/runs/39652221089/job/119404602206) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 8 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/39607316851/job/119246860561) | [3m15s](https://github.com/iree-org/iree/actions/runs/39652221089/job/119404601790) | [3m15s](https://github.com/iree-org/iree/actions/runs/39652221089/job/119404601790) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 4 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/39607316851/job/119246860454) | [2m59s](https://github.com/iree-org/iree/actions/runs/39652221089/job/119404601687) | [2m59s](https://github.com/iree-org/iree/actions/runs/39652221089/job/119404601687) | 4 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 8 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/39646002016/job/119381727893) | [1m56s](https://github.com/iree-org/iree/actions/runs/39622742926/job/119403865094) | [1m56s](https://github.com/iree-org/iree/actions/runs/39622742926/job/119403865094) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39646001938/job/119381737136) | [1m44s](https://github.com/iree-org/iree/actions/runs/39596898107/job/119211419199) | [1m44s](https://github.com/iree-org/iree/actions/runs/39596898107/job/119211419199) | 8 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39631204737/job/119329680830) | [1m32s](https://github.com/iree-org/iree/actions/runs/39596898107/job/119211419060) | [1m32s](https://github.com/iree-org/iree/actions/runs/39596898107/job/119211419060) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 411 | 2% (9/411) |  | 2h39m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 485 | 1% (3/485) |  | 2h43m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h07m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h13m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h07m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
