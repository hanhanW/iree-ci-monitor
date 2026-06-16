# iree-ci-monitor

_Updated: 2026-06-16 01:21 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [38m41s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639618) | [38m41s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639618) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [15m53s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639570) | [27m59s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639599) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [21m17s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639344) | [21m17s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639344) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [15m39s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639543) | [15m39s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639543) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [5m24s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639596) | [14m02s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639594) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [12m07s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639425) | [12m07s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639425) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639565) | [8m54s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639569) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [7m01s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639585) | [7m01s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639585) | 0% (0/1) | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639452) | [6m01s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639590) | 0% (0/2) | `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 27 | 0 | — | — | 2 | [8s](https://github.com/iree-org/iree/actions/runs/27597575942/job/81590995297) | [1m50s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459949) | 9% (2/22) | 27 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459915) | [1m43s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599460148) | 0% (0/3) | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459886) | [37s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459947) | 0% (0/3) | 6 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [18s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639620) | [26s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639608) | 0% (0/4) | 4 |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459963) | [9s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599460062) | 0% (0/7) | 7 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27600295748/job/81599418855) | [8s](https://github.com/iree-org/iree/actions/runs/27600295748/job/81599418857) | 0% (0/3) | 3 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599460059) | [6s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459944) | 0% (0/3) | 5 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459997) | [1s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459997) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639449) | [1s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639449) | 0% (0/1) | 1 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639450) | [1s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639450) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639586) | [1s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639586) | 0% (0/1) | `shark01-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639606) | [1s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639606) | 0% (0/1) | `iree-mi308-1` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [38m41s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639618) | [38m41s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639618) | [38m41s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639618) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [27m59s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639599) | [27m59s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639599) | [27m59s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639599) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [21m17s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639344) | [21m17s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639344) | [21m17s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639344) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [15m53s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639570) | [15m53s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639570) | [15m53s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639570) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [15m39s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639543) | [15m39s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639543) | [15m39s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639543) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [14m02s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639594) | [14m02s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639594) | [14m02s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639594) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [12m07s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639425) | [12m07s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639425) | [12m07s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639425) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [8m54s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639569) | [8m54s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639569) | [8m54s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639569) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [7m01s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639585) | [7m01s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639585) | [7m01s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639585) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [6m01s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639590) | [6m01s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639590) | [6m01s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639590) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [5m24s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639596) | [5m24s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639596) | [5m24s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639596) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 1 | 0 | — | — | [1m51s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599460421) | [1m51s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599460421) | [1m51s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599460421) | 1 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 1 | 0 | — | — | [1m50s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459949) | [1m50s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459949) | [1m50s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459949) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [1m43s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599460148) | [1m43s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599460148) | [1m43s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599460148) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 1 | 0 | — | — | [1m27s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459967) | [1m27s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459967) | [1m27s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459967) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 1 | 0 | — | — | [1m10s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459895) | [1m10s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459895) | [1m10s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459895) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [37s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459947) | [37s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459947) | [37s](https://github.com/iree-org/iree/actions/runs/27600297494/job/81599459947) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [26s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639608) | [26s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639608) | [26s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639608) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [18s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639620) | [18s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639620) | [18s](https://github.com/iree-org/iree/actions/runs/27600297684/job/81603639620) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/27599714352/job/81597655302) | [10s](https://github.com/iree-org/iree/actions/runs/27599714352/job/81597655302) | [10s](https://github.com/iree-org/iree/actions/runs/27599714352/job/81597655302) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 257 | 2% (5/257) |  | 6m28s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 219 | 8% (18/219) |  | 30m44s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 173 | 2% (4/173) |  | 31m05s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 187 | 3% (5/187) |  | 32m03s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 59 | 2% (1/59) |  | 40m46s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
