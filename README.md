# iree-ci-monitor

_Updated: 2026-10-27 05:19 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [28m21s](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518202) | [1h12m](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262489) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262745) | 2026-10-27 05:19 PDT | 0 | [37m08s](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518348) | [1h10m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518377) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 1 | [1h35m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518358) | 2026-10-27 05:19 PDT | 0 | [20m16s](https://github.com/iree-org/iree/actions/runs/40480675429/job/122118756193) | [1h05m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518335) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [15m49s](https://github.com/iree-org/iree/actions/runs/40480675429/job/122118755919) | [1h00m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143517889) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [8m29s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262736) | [40m47s](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518123) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 3 | [1h52m](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136263076) | 2026-10-27 05:19 PDT | 0 | [10m43s](https://github.com/iree-org/iree/actions/runs/40480675429/job/122118755897) | [21m34s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262618) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 1 | [1h35m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518166) | 2026-10-27 05:19 PDT | 0 | [9m32s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262452) | [21m12s](https://github.com/iree-org/iree/actions/runs/40480675429/job/122118755838) | 0% (0/1) | `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 67 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/40487429163/job/122132709626) | [5m30s](https://github.com/iree-org/iree/actions/runs/40489063838/job/122138107570) | 5% (1/22) | 66 |
| `macos-15` | github-hosted | 10 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/40487429163/job/122132709788) | [4m37s](https://github.com/iree-org/iree/actions/runs/40489063880/job/122138637353) | 0% (0/3) | 10 |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 0 | [1m19s](https://github.com/iree-org/iree/actions/runs/40487429163/job/122132709738) | [4m04s](https://github.com/iree-org/iree/actions/runs/40489063880/job/122138637272) | 0% (0/3) | 9 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/40487429163/job/122132709576) | [3m24s](https://github.com/iree-org/iree/actions/runs/40489063880/job/122138637198) | 0% (0/3) | 9 |
| `azure-linux-scale` | ossci | 23 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/40487429163/job/122132709876) | [2m17s](https://github.com/iree-org/iree/actions/runs/40480675301/job/122109982209) | 11% (1/9) | 23 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [2m14s](https://github.com/iree-org/iree/actions/runs/40481200514/job/122111671454) | [2m14s](https://github.com/iree-org/iree/actions/runs/40481200514/job/122111671454) | 100% (1/1) | 1 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/40487190900/job/122131828148) | [49s](https://github.com/iree-org/iree/actions/runs/40489056501/job/122138089849) | 0% (0/3) | 9 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/40487429163/job/122132709828) | [5s](https://github.com/iree-org/iree/actions/runs/40489063880/job/122138637420) | 0% (0/1) | 3 |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [1h52m](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262745) | 2026-10-27 05:19 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [1h52m](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136263076) | 2026-10-27 05:19 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [1h35m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518166) | 2026-10-27 05:19 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `integrates/llvm-20261026` | pull_request |
| [1h35m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518253) | 2026-10-27 05:19 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `integrates/llvm-20261026` | pull_request |
| [1h35m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518272) | 2026-10-27 05:19 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `integrates/llvm-20261026` | pull_request |
| [1h35m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518358) | 2026-10-27 05:19 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `integrates/llvm-20261026` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 2 | [1h52m](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136263076) | 2026-10-27 05:19 PDT | [10m43s](https://github.com/iree-org/iree/actions/runs/40480675429/job/122118755897) | [10m43s](https://github.com/iree-org/iree/actions/runs/40480675429/job/122118755897) | [10m43s](https://github.com/iree-org/iree/actions/runs/40480675429/job/122118755897) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262745) | 2026-10-27 05:19 PDT | [28m02s](https://github.com/iree-org/iree/actions/runs/40480675429/job/122118755892) | [37m08s](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518348) | [37m08s](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518348) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 1 | [1h35m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518166) | 2026-10-27 05:19 PDT | [9m32s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262452) | [21m12s](https://github.com/iree-org/iree/actions/runs/40480675429/job/122118755838) | [21m12s](https://github.com/iree-org/iree/actions/runs/40480675429/job/122118755838) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 1 | [1h35m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518272) | 2026-10-27 05:19 PDT | [1s](https://github.com/iree-org/iree/actions/runs/40480675429/job/122118755851) | [21m34s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262618) | [21m34s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262618) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 1 | [1h35m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518358) | 2026-10-27 05:19 PDT | [54s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262785) | [20m16s](https://github.com/iree-org/iree/actions/runs/40480675429/job/122118756193) | [20m16s](https://github.com/iree-org/iree/actions/runs/40480675429/job/122118756193) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [28m21s](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518202) | [1h12m](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262489) | [1h12m](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262489) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [49m45s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262911) | [1h10m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518377) | [1h10m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518377) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [21m44s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262830) | [1h05m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518335) | [1h05m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518335) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [15m49s](https://github.com/iree-org/iree/actions/runs/40480675429/job/122118755919) | [1h00m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143517889) | [1h00m](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143517889) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [8m29s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262736) | [40m47s](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518123) | [40m47s](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518123) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [11m39s](https://github.com/iree-org/iree/actions/runs/40480675429/job/122118755810) | [13m47s](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518031) | [13m47s](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518031) | 2 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40480675429/job/122118755634) | [6m21s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262637) | [6m21s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262637) | 3 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122132620315) | [5m37s](https://github.com/iree-org/iree/actions/runs/40489063865/job/122138108533) | [5m37s](https://github.com/iree-org/iree/actions/runs/40489063865/job/122138108533) | 3 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 3 | 0 | — | — | [16s](https://github.com/iree-org/iree/actions/runs/40487429163/job/122132709589) | [5m31s](https://github.com/iree-org/iree/actions/runs/40489063880/job/122138636988) | [5m31s](https://github.com/iree-org/iree/actions/runs/40489063880/job/122138636988) | 3 |
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40480674886/job/122109884164) | [5m30s](https://github.com/iree-org/iree/actions/runs/40489063838/job/122138107570) | [5m30s](https://github.com/iree-org/iree/actions/runs/40489063838/job/122138107570) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518306) | [5m25s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262708) | [5m25s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262708) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40487429163/job/122132709838) | [5m20s](https://github.com/iree-org/iree/actions/runs/40489063880/job/122138637312) | [5m20s](https://github.com/iree-org/iree/actions/runs/40489063880/job/122138637312) | 3 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 3 | 0 | — | — | [27s](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143518249) | [5m16s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262718) | [5m16s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262718) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40487429163/job/122132709626) | [5m05s](https://github.com/iree-org/iree/actions/runs/40489063880/job/122138637217) | [5m05s](https://github.com/iree-org/iree/actions/runs/40489063880/job/122138637217) | 3 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40489063865/job/122143517799) | [5m01s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262436) | [5m01s](https://github.com/iree-org/iree/actions/runs/40487428968/job/122136262436) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 319 | 0% (0/319) |  | 21m24s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 253 | 3% (8/253) |  | 30m21s ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h12m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h10m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h05m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
