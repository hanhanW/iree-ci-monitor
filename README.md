# iree-ci-monitor

_Updated: 2026-08-11 19:46 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [17m19s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354456) | [17m19s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354456) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [9m04s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354447) | [16m08s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354327) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [5m23s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354444) | [12m33s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354574) | — | `shark10-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [9m59s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354387) | [9m59s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354387) | — | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [7m42s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354509) | [8m03s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354586) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [7m18s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354373) | [7m18s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354373) | — | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354465) | [5m51s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354356) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [3m47s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354388) | [3m47s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354388) | — | `shark10-ci` |
| `ubuntu-24.04` | github-hosted | 25 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882637632) | [10s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710838) | 67% (2/3) | 24 |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882711017) | [10s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93882726057) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710805) | [5s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710766) | — | 3 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710694) | [3s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710864) | — | 3 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710886) | [3s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710848) | — | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882711157) | [1s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882711157) | — | 1 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354329) | [1s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354329) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354334) | [1s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354334) | — | `shark01-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354503) | [1s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354503) | — | `shark10-ci` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [17m19s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354456) | [17m19s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354456) | [17m19s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354456) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [16m08s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354327) | [16m08s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354327) | [16m08s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354327) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [12m33s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354574) | [12m33s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354574) | [12m33s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354574) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [9m59s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354387) | [9m59s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354387) | [9m59s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354387) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [9m04s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354447) | [9m04s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354447) | [9m04s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354447) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [8m03s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354586) | [8m03s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354586) | [8m03s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354586) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [7m42s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354509) | [7m42s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354509) | [7m42s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354509) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [7m18s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354373) | [7m18s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354373) | [7m18s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354373) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [5m51s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354356) | [5m51s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354356) | [5m51s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354356) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [5m23s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354444) | [5m23s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354444) | [5m23s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354444) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [3m47s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354388) | [3m47s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354388) | [3m47s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354388) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31503998300/job/93861726532) | [13s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93856583982) | [13s](https://github.com/iree-org/iree/actions/runs/31506388787/job/93856583982) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710838) | [10s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710838) | [10s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710838) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93882726057) | [10s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93882726057) | [10s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93882726057) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354724) | [10s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354724) | [10s](https://github.com/iree-org/iree/actions/runs/31513382779/job/93886354724) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882711022) | [9s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882711022) | [9s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882711022) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710825) | [8s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710825) | [8s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710825) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882711017) | [8s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882711017) | [8s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882711017) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710740) | [6s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710740) | [6s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710740) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710766) | [5s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710766) | [5s](https://github.com/iree-org/iree/actions/runs/31513382842/job/93882710766) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 148 | 6% (9/148) |  | 7h31m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 173 | 0% (0/173) |  | 7h51m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 141 | 4% (5/141) |  | 7h54m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 122 | 12% (15/122) |  | 7h57m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
