# iree-ci-monitor

_Updated: 2026-10-01 22:45 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [46m54s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658817) | [48m07s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700687) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [20m00s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700589) | [30m09s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658663) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700466) | [14m19s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658620) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [3m25s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658734) | [5m49s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700281) | 0% (0/1) | `shark75-ci` |
| `azure-linux-scale` | ossci | 18 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/36918790447/job/110559424618) | [1m34s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110552746881) | 0% (0/7) | 18 |
| `macos-14` | github-hosted | 11 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/36921850796/job/110569930314) | [11s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552738735) | 0% (0/3) | 11 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/36968248175/job/110716624021) | [5s](https://github.com/iree-org/iree/actions/runs/36921850796/job/110569930230) | 0% (0/3) | 12 |
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/36917743145/job/110555816209) | [5s](https://github.com/iree-org/iree/actions/runs/36916796937/job/110552646847) | 0% (0/3) | 18 |
| `ubuntu-24.04` | github-hosted | 64 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/36964484083/job/110705128894) | [4s](https://github.com/iree-org/iree/actions/runs/36916798416/job/110552645028) | 0% (0/23) | 63 |
| `windows-2022` | github-hosted | 11 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552738266) | [4s](https://github.com/iree-org/iree/actions/runs/36918790447/job/110559423254) | 0% (0/3) | 11 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36918790447/job/110559424602) | [2s](https://github.com/iree-org/iree/actions/runs/36921850796/job/110569930669) | 0% (0/1) | 3 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 10 | [21h25m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382976) | 2026-10-01 22:45 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 20 | 20 | [21h25m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383120) | 2026-10-01 22:45 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 10 | 10 | [21h25m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382936) | 2026-10-01 22:45 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 20 | 20 | [21h25m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382988) | 2026-10-01 22:45 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [21h25m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382936) | 2026-10-01 22:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [21h25m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382976) | 2026-10-01 22:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [21h25m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382988) | 2026-10-01 22:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [21h25m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383120) | 2026-10-01 22:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [21h25m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383211) | 2026-10-01 22:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [21h25m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383216) | 2026-10-01 22:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [20h47m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492369) | 2026-10-01 22:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [20h47m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492455) | 2026-10-01 22:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [20h47m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492528) | 2026-10-01 22:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [20h47m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492574) | 2026-10-01 22:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [20h47m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492602) | 2026-10-01 22:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [20h47m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492701) | 2026-10-01 22:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [20h46m](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295665844) | 2026-10-01 22:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [20h46m](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295665863) | 2026-10-01 22:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [20h46m](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295665868) | 2026-10-01 22:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 10 | [21h25m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382976) | 2026-10-01 22:45 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 10 | 10 | [21h25m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382936) | 2026-10-01 22:45 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 10 | [21h25m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382988) | 2026-10-01 22:45 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 10 | [21h25m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383211) | 2026-10-01 22:45 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 10 | [21h25m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383216) | 2026-10-01 22:45 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 10 | [21h25m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383120) | 2026-10-01 22:45 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [38m29s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658801) | [48m07s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700687) | [48m07s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700687) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [9m40s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700481) | [46m54s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658817) | [46m54s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658817) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [20m00s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700589) | [30m09s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658663) | [30m09s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658663) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [8m42s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575659154) | [14m55s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700529) | [14m55s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700529) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700466) | [14m19s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658620) | [14m19s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658620) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [3m25s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658734) | [5m49s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700281) | [5m49s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700281) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36921850796/job/110569930910) | [1m35s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552739939) | [1m35s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552739939) | 3 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36921626941/job/110569389304) | [1m34s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110552746881) | [1m34s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110552746881) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [1m32s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552740025) | [1m32s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552740025) | [1m32s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552740025) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36921850796/job/110569930814) | [56s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552740035) | [56s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552740035) | 3 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 3 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/36918790447/job/110559424196) | [48s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552740164) | [48s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552740164) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 3 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36921850796/job/110569930880) | [20s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552740123) | [20s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552740123) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 3 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/36918790447/job/110559423439) | [11s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552738735) | [11s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552738735) | 3 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36921850796/job/110569930010) | [10s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552738321) | [10s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552738321) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 237 | 2% (4/237) |  | 8h10m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 228 | 1% (2/228) |  | 1d09h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 21h25m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 21h25m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 21h25m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 21h25m (> 2h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
