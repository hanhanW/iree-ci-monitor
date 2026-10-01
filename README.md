# iree-ci-monitor

_Updated: 2026-10-01 15:45 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [34m29s](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464420) | [48m07s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700687) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [14m19s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658620) | [36m20s](https://github.com/iree-org/iree/actions/runs/36908228839/job/110534197163) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [5m49s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700281) | [32m35s](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464240) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [21m15s](https://github.com/iree-org/iree/actions/runs/36908228839/job/110534196842) | [31m24s](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464431) | 0% (0/4) | `shark75-ci` |
| `azure-linux-scale` | ossci | 30 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/36921850796/job/110569930910) | [1m35s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552739939) | 0% (0/13) | 30 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/36918790447/job/110559422958) | [10s](https://github.com/iree-org/iree/actions/runs/36918790447/job/110559423439) | 0% (0/6) | 15 |
| `ubuntu-latest` | github-hosted | 30 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/36917741098/job/110555807727) | [8s](https://github.com/iree-org/iree/actions/runs/36921840123/job/110569536939) | 0% (0/6) | 30 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/36908228882/job/110524160049) | [5s](https://github.com/iree-org/iree/actions/runs/36921850796/job/110569930397) | 0% (0/6) | 15 |
| `ubuntu-24.04` | github-hosted | 95 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36921850796/job/110569929710) | [4s](https://github.com/iree-org/iree/actions/runs/36908228882/job/110524160009) | 0% (0/38) | 94 |
| `windows-2022` | github-hosted | 15 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552738266) | [4s](https://github.com/iree-org/iree/actions/runs/36908228882/job/110524160050) | 0% (0/6) | 15 |
| `azure-windows-scale` | ossci | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552740594) | [2s](https://github.com/iree-org/iree/actions/runs/36921850796/job/110569930669) | 0% (0/2) | 5 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 10 | [14h23m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382976) | 2026-10-01 15:44 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 20 | 20 | [14h23m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383120) | 2026-10-01 15:44 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 10 | 10 | [14h23m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382936) | 2026-10-01 15:44 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 20 | 20 | [14h23m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382988) | 2026-10-01 15:44 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [14h23m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382936) | 2026-10-01 15:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [14h23m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382976) | 2026-10-01 15:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [14h23m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382988) | 2026-10-01 15:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [14h23m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383120) | 2026-10-01 15:44 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [14h23m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383211) | 2026-10-01 15:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [14h23m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383216) | 2026-10-01 15:44 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [13h46m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492369) | 2026-10-01 15:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [13h46m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492455) | 2026-10-01 15:44 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [13h46m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492528) | 2026-10-01 15:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [13h46m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492574) | 2026-10-01 15:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [13h46m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492602) | 2026-10-01 15:44 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [13h46m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492701) | 2026-10-01 15:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [13h45m](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295665844) | 2026-10-01 15:44 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [13h45m](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295665863) | 2026-10-01 15:44 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [13h45m](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295665868) | 2026-10-01 15:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 10 | [14h23m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382976) | 2026-10-01 15:44 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 10 | 10 | [14h23m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382936) | 2026-10-01 15:44 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 10 | [14h23m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382988) | 2026-10-01 15:44 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 10 | [14h23m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383211) | 2026-10-01 15:44 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 10 | [14h23m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383216) | 2026-10-01 15:44 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 10 | [14h23m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383120) | 2026-10-01 15:44 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [38m29s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658801) | [48m07s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700687) | [48m07s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700687) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [34m29s](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464420) | [46m54s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658817) | [46m54s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658817) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [14m19s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658620) | [36m20s](https://github.com/iree-org/iree/actions/runs/36908228839/job/110534197163) | [36m20s](https://github.com/iree-org/iree/actions/runs/36908228839/job/110534197163) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [5m49s](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700281) | [32m35s](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464240) | [32m35s](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464240) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [21m15s](https://github.com/iree-org/iree/actions/runs/36908228839/job/110534196842) | [31m24s](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464431) | [31m24s](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464431) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [25m47s](https://github.com/iree-org/iree/actions/runs/36908228839/job/110534196957) | [30m09s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658663) | [30m09s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110575658663) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36917741098/job/110555881688) | [2m13s](https://github.com/iree-org/iree/actions/runs/36894993429/job/110479717613) | [2m13s](https://github.com/iree-org/iree/actions/runs/36894993429/job/110479717613) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 6 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/36921850056/job/110570007446) | [2m08s](https://github.com/iree-org/iree/actions/runs/36908228839/job/110524196652) | [2m08s](https://github.com/iree-org/iree/actions/runs/36908228839/job/110524196652) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 5 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36921850796/job/110569930910) | [1m35s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552739939) | [1m35s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552739939) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 3 | 0 | — | — | [37s](https://github.com/iree-org/iree/actions/runs/36908228882/job/110524160718) | [1m32s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552740025) | [1m32s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552740025) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 5 | 0 | — | — | [56s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552740035) | [1m19s](https://github.com/iree-org/iree/actions/runs/36908228882/job/110524160705) | [1m19s](https://github.com/iree-org/iree/actions/runs/36908228882/job/110524160705) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 5 | 0 | — | — | [20s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552740123) | [1m19s](https://github.com/iree-org/iree/actions/runs/36894148576/job/110476861351) | [1m19s](https://github.com/iree-org/iree/actions/runs/36894148576/job/110476861351) | 5 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 5 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36894148576/job/110476861701) | [48s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552740164) | [48s](https://github.com/iree-org/iree/actions/runs/36916799604/job/110552740164) | 5 |
| `.github/workflows/clang_tidy.yml` | clang-tidy | `ubuntu-24.04` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36918790008/job/110559329774) | [38s](https://github.com/iree-org/iree/actions/runs/36908228208/job/110524064934) | [38s](https://github.com/iree-org/iree/actions/runs/36908228208/job/110524064934) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 304 | 2% (7/304) |  | 1h09m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 329 | 1% (2/329) |  | 1d02h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 14h23m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 14h23m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 14h23m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 14h23m (> 2h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
