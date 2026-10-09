# iree-ci-monitor

_Updated: 2026-10-09 06:27 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [1h01m](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728142) | [2h11m](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353130) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [1h06m](https://github.com/iree-org/iree/actions/runs/37927622834/job/113813255970) | [1h46m](https://github.com/iree-org/iree/actions/runs/37922347529/job/113795470602) | 0% (0/8) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [48m36s](https://github.com/iree-org/iree/actions/runs/37905671390/job/113740879416) | [1h32m](https://github.com/iree-org/iree/actions/runs/37922347529/job/113795470498) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [28m20s](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728001) | [1h31m](https://github.com/iree-org/iree/actions/runs/37905671390/job/113740879270) | 100% (4/4) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 1 | [1h14m](https://github.com/iree-org/iree/actions/runs/37927622834/job/113813255697) | 2026-10-09 06:26 PDT | 1 | [33m39s](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353442) | [1h15m](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728446) | 0% (0/6) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [36m02s](https://github.com/iree-org/iree/actions/runs/37922347529/job/113795470058) | [44m44s](https://github.com/iree-org/iree/actions/runs/37922347529/job/113795470556) | 0% (0/8) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [19m52s](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728220) | [42m21s](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353070) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [25m56s](https://github.com/iree-org/iree/actions/runs/37899888193/job/113721874867) | [42m01s](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728207) | 0% (0/4) | `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 135 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728152) | [1m53s](https://github.com/iree-org/iree/actions/runs/37899888193/job/113721874969) | 6% (5/82) | 133 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m48s](https://github.com/iree-org/iree/actions/runs/37911987998/job/113759071424) | [1m48s](https://github.com/iree-org/iree/actions/runs/37911987998/job/113759071424) | 100% (1/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/37905671349/job/113738496031) | [1m44s](https://github.com/iree-org/iree/actions/runs/37922347405/job/113793148920) | 0% (0/12) | 21 |
| `macos-15` | github-hosted | 21 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/37927622741/job/113810329528) | [1m13s](https://github.com/iree-org/iree/actions/runs/37922347405/job/113793148978) | 0% (0/13) | 21 |
| `windows-2022` | github-hosted | 20 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/37905671349/job/113738495968) | [1m09s](https://github.com/iree-org/iree/actions/runs/37906749963/job/113742014774) | 17% (2/12) | 20 |
| `ubuntu-latest` | github-hosted | 28 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37922342073/job/113793021739) | [49s](https://github.com/iree-org/iree/actions/runs/37900793145/job/113722627968) | 0% (0/12) | 27 |
| `azure-linux-scale` | ossci | 42 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/37899888179/job/113719774371) | [29s](https://github.com/iree-org/iree/actions/runs/37922347405/job/113793149101) | 3% (1/30) | 42 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/37905671349/job/113738496188) | [2s](https://github.com/iree-org/iree/actions/runs/37927622741/job/113810329670) | 0% (0/4) | 6 |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [1h14m](https://github.com/iree-org/iree/actions/runs/37927622834/job/113813255697) | 2026-10-09 06:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [1h01m](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728142) | [2h11m](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353130) | [2h11m](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353130) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [1h33m](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728250) | [1h52m](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353467) | [1h52m](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353467) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [33m23s](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728233) | [1h46m](https://github.com/iree-org/iree/actions/runs/37922347529/job/113795470602) | [1h46m](https://github.com/iree-org/iree/actions/runs/37922347529/job/113795470602) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [48m36s](https://github.com/iree-org/iree/actions/runs/37905671390/job/113740879416) | [1h36m](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353377) | [1h36m](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353377) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 6 | 0 | — | — | [28m20s](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728001) | [1h31m](https://github.com/iree-org/iree/actions/runs/37905671390/job/113740879270) | [1h31m](https://github.com/iree-org/iree/actions/runs/37905671390/job/113740879270) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [20m07s](https://github.com/iree-org/iree/actions/runs/37905671390/job/113740879430) | [1h15m](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728446) | [1h15m](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728446) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 1 | [1h14m](https://github.com/iree-org/iree/actions/runs/37927622834/job/113813255697) | 2026-10-09 06:26 PDT | [37m44s](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728216) | [1h04m](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353317) | [1h04m](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353317) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [10m53s](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353501) | [55m34s](https://github.com/iree-org/iree/actions/runs/37922347529/job/113795470669) | [55m34s](https://github.com/iree-org/iree/actions/runs/37922347529/job/113795470669) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [36m40s](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353238) | [46m06s](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728005) | [46m06s](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728005) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [19m52s](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728220) | [42m21s](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353070) | [42m21s](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353070) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [25m56s](https://github.com/iree-org/iree/actions/runs/37899888193/job/113721874867) | [42m01s](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728207) | [42m01s](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728207) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [7m41s](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728278) | [38m49s](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353654) | [38m49s](https://github.com/iree-org/iree/actions/runs/37900160178/job/113723353654) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 6 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/37905671349/job/113738496031) | [2m45s](https://github.com/iree-org/iree/actions/runs/37900160268/job/113720626336) | [2m45s](https://github.com/iree-org/iree/actions/runs/37900160268/job/113720626336) | 6 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728191) | [2m32s](https://github.com/iree-org/iree/actions/runs/37922347529/job/113795470675) | [2m32s](https://github.com/iree-org/iree/actions/runs/37922347529/job/113795470675) | 6 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37906750063/job/113744728364) | [2m32s](https://github.com/iree-org/iree/actions/runs/37922347529/job/113795470295) | [2m32s](https://github.com/iree-org/iree/actions/runs/37922347529/job/113795470295) | 6 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37899888193/job/113721874885) | [2m32s](https://github.com/iree-org/iree/actions/runs/37922347529/job/113795470277) | [2m32s](https://github.com/iree-org/iree/actions/runs/37922347529/job/113795470277) | 6 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37927622834/job/113813255523) | [2m32s](https://github.com/iree-org/iree/actions/runs/37922347529/job/113795470202) | [2m32s](https://github.com/iree-org/iree/actions/runs/37922347529/job/113795470202) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 6 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37927622741/job/113810329463) | [2m13s](https://github.com/iree-org/iree/actions/runs/37900160268/job/113720626272) | [2m13s](https://github.com/iree-org/iree/actions/runs/37900160268/job/113720626272) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 6 | 0 | — | — | [39s](https://github.com/iree-org/iree/actions/runs/37905671349/job/113738496077) | [2m04s](https://github.com/iree-org/iree/actions/runs/37922347405/job/113793149070) | [2m04s](https://github.com/iree-org/iree/actions/runs/37922347405/job/113793149070) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 6 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37927622741/job/113810329534) | [2m02s](https://github.com/iree-org/iree/actions/runs/37900160268/job/113720626280) | [2m02s](https://github.com/iree-org/iree/actions/runs/37900160268/job/113720626280) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 211 | 15% (32/210) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 365 | 0% (1/365) |  | 29m34s ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h11m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h15m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache` p95 queue 1h31m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h46m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
