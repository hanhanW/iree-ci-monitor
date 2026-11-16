# iree-ci-monitor

_Updated: 2026-11-16 14:12 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 14 | 0 | — | — | 0 | [14m17s](https://github.com/iree-org/iree/actions/runs/43904387611/job/133472097725) | [48m58s](https://github.com/iree-org/iree/actions/runs/43904834863/job/133437627077) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 14 | 0 | — | — | 0 | [17m06s](https://github.com/iree-org/iree/actions/runs/43939775875/job/133561715627) | [48m06s](https://github.com/iree-org/iree/actions/runs/43899495293/job/133434825478) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 7 | 0 | — | — | 0 | [9m12s](https://github.com/iree-org/iree/actions/runs/43958023630/job/133622631039) | [42m38s](https://github.com/iree-org/iree/actions/runs/43894835012/job/133413946464) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [10m27s](https://github.com/iree-org/iree/actions/runs/43904834863/job/133437638066) | [35m25s](https://github.com/iree-org/iree/actions/runs/43894835012/job/133413946520) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 14 | 0 | — | — | 0 | [12m00s](https://github.com/iree-org/iree/actions/runs/43904387611/job/133472097648) | [30m38s](https://github.com/iree-org/iree/actions/runs/43899495293/job/133434825146) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [14m12s](https://github.com/iree-org/iree/actions/runs/43894835012/job/133413946550) | [27m22s](https://github.com/iree-org/iree/actions/runs/43904834863/job/133437627189) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 14 | 0 | — | — | 0 | [3m49s](https://github.com/iree-org/iree/actions/runs/43931550747/job/133531156408) | [13m24s](https://github.com/iree-org/iree/actions/runs/43939775875/job/133561715223) | 0% (0/4) | `shark55-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 45 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/43958023428/job/133617874017) | [2m15s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430916585) | 0% (0/15) | 45 |
| `windows-2022` | github-hosted | 21 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/43931550664/job/133525300217) | [1m18s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430915355) | 0% (0/6) | 21 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/43931550664/job/133525299996) | [13s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430914870) | 0% (0/6) | 21 |
| `macos-15` | github-hosted | 21 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/43894835109/job/133395567833) | [8s](https://github.com/iree-org/iree/actions/runs/43939776062/job/133554042927) | 0% (0/6) | 21 |
| `ubuntu-latest` | github-hosted | 23 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/43939763399/job/133553858481) | [3s](https://github.com/iree-org/iree/actions/runs/43958013243/job/133617622137) | 0% (0/8) | 23 |
| `ubuntu-24.04` | github-hosted | 146 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/43931550747/job/133531156837) | [3s](https://github.com/iree-org/iree/actions/runs/43958023428/job/133617873732) | 0% (0/39) | 144 |
| `azure-windows-scale` | ossci | 7 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430916476) | [1s](https://github.com/iree-org/iree/actions/runs/43958023428/job/133617873946) | 0% (0/2) | 7 |
| `Linux,X64,iree-w7900` | self-hosted | 7 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 7 | 0 | — | — | [14m17s](https://github.com/iree-org/iree/actions/runs/43904387611/job/133472097725) | [1h14m](https://github.com/iree-org/iree/actions/runs/43894835012/job/133413946785) | [1h14m](https://github.com/iree-org/iree/actions/runs/43894835012/job/133413946785) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [25m25s](https://github.com/iree-org/iree/actions/runs/43904834863/job/133437627827) | [59m45s](https://github.com/iree-org/iree/actions/runs/43894835012/job/133413946615) | [59m45s](https://github.com/iree-org/iree/actions/runs/43894835012/job/133413946615) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 7 | 0 | — | — | [17m13s](https://github.com/iree-org/iree/actions/runs/43931550747/job/133531156626) | [54m11s](https://github.com/iree-org/iree/actions/runs/43894835012/job/133413946734) | [54m11s](https://github.com/iree-org/iree/actions/runs/43894835012/job/133413946734) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 7 | 0 | — | — | [15m10s](https://github.com/iree-org/iree/actions/runs/43904387611/job/133472098146) | [48m58s](https://github.com/iree-org/iree/actions/runs/43904834863/job/133437627077) | [48m58s](https://github.com/iree-org/iree/actions/runs/43904834863/job/133437627077) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 7 | 0 | — | — | [12m54s](https://github.com/iree-org/iree/actions/runs/43939775875/job/133561715550) | [48m06s](https://github.com/iree-org/iree/actions/runs/43899495293/job/133434825478) | [48m06s](https://github.com/iree-org/iree/actions/runs/43899495293/job/133434825478) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 7 | 0 | — | — | [9m12s](https://github.com/iree-org/iree/actions/runs/43958023630/job/133622631039) | [42m38s](https://github.com/iree-org/iree/actions/runs/43894835012/job/133413946464) | [42m38s](https://github.com/iree-org/iree/actions/runs/43894835012/job/133413946464) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 7 | 0 | — | — | [10m27s](https://github.com/iree-org/iree/actions/runs/43904834863/job/133437638066) | [35m25s](https://github.com/iree-org/iree/actions/runs/43894835012/job/133413946520) | [35m25s](https://github.com/iree-org/iree/actions/runs/43894835012/job/133413946520) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [5m29s](https://github.com/iree-org/iree/actions/runs/43931550747/job/133531156649) | [29m27s](https://github.com/iree-org/iree/actions/runs/43904834863/job/133437627186) | [29m27s](https://github.com/iree-org/iree/actions/runs/43904834863/job/133437627186) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 7 | 0 | — | — | [14m12s](https://github.com/iree-org/iree/actions/runs/43894835012/job/133413946550) | [27m22s](https://github.com/iree-org/iree/actions/runs/43904834863/job/133437627189) | [27m22s](https://github.com/iree-org/iree/actions/runs/43904834863/job/133437627189) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [7m10s](https://github.com/iree-org/iree/actions/runs/43904387611/job/133472097595) | [20m09s](https://github.com/iree-org/iree/actions/runs/43899495293/job/133434825256) | [20m09s](https://github.com/iree-org/iree/actions/runs/43899495293/job/133434825256) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [3m49s](https://github.com/iree-org/iree/actions/runs/43931550747/job/133531156408) | [11m13s](https://github.com/iree-org/iree/actions/runs/43939775875/job/133561714694) | [11m13s](https://github.com/iree-org/iree/actions/runs/43939775875/job/133561714694) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 7 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/43899495293/job/133429414675) | [2m27s](https://github.com/iree-org/iree/actions/runs/43904834863/job/133431052621) | [2m27s](https://github.com/iree-org/iree/actions/runs/43904834863/job/133431052621) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 7 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/43931550664/job/133525300491) | [2m15s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430916809) | [2m15s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430916809) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 7 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/43904387493/job/133466624511) | [2m15s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430916585) | [2m15s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430916585) | 7 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 7 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/43899495709/job/133429368269) | [2m11s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430916612) | [2m11s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430916612) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 7 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/43958023428/job/133617873713) | [1m29s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430916825) | [1m29s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430916825) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 7 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/43904387493/job/133466624126) | [1m24s](https://github.com/iree-org/iree/actions/runs/43931550664/job/133525300628) | [1m24s](https://github.com/iree-org/iree/actions/runs/43931550664/job/133525300628) | 7 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 7 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43931550664/job/133525300190) | [1m20s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430915472) | [1m20s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430915472) | 7 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 7 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43939776062/job/133554042794) | [1m18s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430915355) | [1m18s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430915355) | 7 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 7 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43931550664/job/133525300349) | [59s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430915182) | [59s](https://github.com/iree-org/iree/actions/runs/43904834910/job/133430915182) | 7 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 447 | 0% (2/447) |  | 32m41s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 380 | 1% (4/380) |  | 37m50s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
