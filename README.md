# iree-ci-monitor

_Updated: 2026-08-06 02:08 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [59m44s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500480) | [1h10m](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158769) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158695) | [29m58s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500306) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [15m17s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500285) | [22m06s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158689) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158648) | [19m41s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500330) | 0% (0/1) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [8m53s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500276) | [18m58s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158738) | 0% (0/2) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [1m51s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500380) | [17m10s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158835) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [1m50s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500238) | [16m54s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158638) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [3m32s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500275) | [15m43s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158678) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [6m58s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500435) | [14m30s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500352) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [11m40s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500396) | [12m33s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158740) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158871) | [10m51s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500341) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `windows-2022` | github-hosted | 11 | 0 | — | — | 4 | [2s](https://github.com/iree-org/iree/actions/runs/31087665143/job/92570912753) | [1m31s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030297) | 0% (0/3) | 11 |
| `macos-14` | github-hosted | 11 | 0 | — | — | 3 | [46s](https://github.com/iree-org/iree/actions/runs/31087665143/job/92570912761) | [1m26s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030389) | 0% (0/3) | 11 |
| `ubuntu-24.04` | github-hosted | 57 | 0 | — | — | 7 | [3s](https://github.com/iree-org/iree/actions/runs/31079151663/job/92543741977) | [1m07s](https://github.com/iree-org/iree/actions/runs/31087665143/job/92570912765) | 0% (0/23) | 57 |
| `azure-linux-scale` | ossci | 18 | 1 | [1m34s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92570914930) | 2026-08-06 02:07 PDT | 5 | [8s](https://github.com/iree-org/iree/actions/runs/31087665143/job/92570912991) | [13s](https://github.com/iree-org/iree/actions/runs/31079151663/job/92543793552) | 0% (0/6) | 17 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/31079148451/job/92543732974) | [10s](https://github.com/iree-org/iree/actions/runs/31076636708/job/92535994025) | 0% (0/3) | 9 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030234) | [5s](https://github.com/iree-org/iree/actions/runs/31079151663/job/92543793439) | 0% (0/3) | 12 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030466) | [2s](https://github.com/iree-org/iree/actions/runs/31079151663/job/92543793592) | 0% (0/1) | 3 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [1m34s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92570914930) | 2026-08-06 02:07 PDT | `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | `integrates/llvm-20260731-cleanup` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [59m44s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500480) | [1h10m](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158769) | [1h10m](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158769) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [5m48s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158756) | [48m09s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500333) | [48m09s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500333) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158695) | [29m58s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500306) | [29m58s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500306) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [15m17s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500285) | [22m06s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158689) | [22m06s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158689) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158648) | [19m41s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500330) | [19m41s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500330) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [8m53s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500276) | [18m58s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158738) | [18m58s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158738) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [1m51s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500380) | [17m10s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158835) | [17m10s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158835) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [1m50s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500238) | [16m54s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158638) | [16m54s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158638) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [3m32s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500275) | [15m43s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158678) | [15m43s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158678) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [6m53s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158754) | [14m30s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500352) | [14m30s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500352) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [9m31s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500447) | [12m33s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158740) | [12m33s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158740) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [5m55s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158766) | [11m40s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500396) | [11m40s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500396) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158871) | [10m51s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500341) | [10m51s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500341) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [6m24s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158893) | [6m58s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500435) | [6m58s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500435) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158701) | [4m14s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500322) | [4m14s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500322) | 2 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31087665143/job/92570912623) | [1m48s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030454) | [1m48s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030454) | 3 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 3 | 1 | [1m34s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92570914930) | 2026-08-06 02:07 PDT | [2s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92543776235) | [8s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92536035590) | [8s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92536035590) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 3 | 0 | — | — | [1m18s](https://github.com/iree-org/iree/actions/runs/31079151663/job/92543793460) | [1m31s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030297) | [1m31s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030297) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 3 | 0 | — | — | [1m07s](https://github.com/iree-org/iree/actions/runs/31087665143/job/92570912765) | [1m27s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030291) | [1m27s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030291) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 3 | 0 | — | — | [51s](https://github.com/iree-org/iree/actions/runs/31079151663/job/92543793443) | [1m26s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030389) | [1m26s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030389) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 128 | 0% (0/128) |  | 55m39s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 99 | 1% (1/99) |  | 1h35m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 112 | 2% (2/112) |  | 1h35m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 96 | 0% (0/96) |  | 1h37m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 17 | 0% (0/17) |  | 2d19h ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h10m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
