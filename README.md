# iree-ci-monitor

_Updated: 2026-08-07 19:23 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [18m54s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196270) | [29m59s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511421) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [15m36s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196496) | [28m06s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511507) | 0% (0/4) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [11m26s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511440) | [26m23s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196312) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [18m48s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196341) | [22m18s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511431) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511267) | [22m11s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196072) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [9m55s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511317) | [13m23s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196128) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [8m13s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511456) | [12m22s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196370) | 0% (0/4) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [9m24s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196241) | [11m24s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196198) | 25% (1/4) | `shark01-ci`, `shark10-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [48s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196231) | [9m22s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511412) | 100% (2/2) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [6m19s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196392) | [8m08s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511496) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511326) | [3m31s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196116) | 0% (0/2) | `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 40 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511458) | [9s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511513) | 8% (3/37) | 40 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31200173451/job/92938111181) | [9s](https://github.com/iree-org/iree/actions/runs/31198986139/job/92934155423) | 0% (0/6) | 6 |
| `azure-linux-scale` | ossci | 12 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/31200173451/job/92938111404) | [9s](https://github.com/iree-org/iree/actions/runs/31200173451/job/92938111350) | 0% (0/12) | 12 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31200171742/job/92938023930) | [9s](https://github.com/iree-org/iree/actions/runs/31200171742/job/92938023758) | 0% (0/6) | 6 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31200173451/job/92938111190) | [5s](https://github.com/iree-org/iree/actions/runs/31198986139/job/92934155543) | 0% (0/6) | 6 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31198986139/job/92934155594) | [4s](https://github.com/iree-org/iree/actions/runs/31198986139/job/92934155393) | 0% (0/6) | 6 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31200173451/job/92938111486) | [2s](https://github.com/iree-org/iree/actions/runs/31198986139/job/92934155917) | 0% (0/2) | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [18m54s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196270) | [29m59s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511421) | [29m59s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511421) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [15m36s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196496) | [28m06s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511507) | [28m06s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511507) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [11m26s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511440) | [26m23s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196312) | [26m23s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196312) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [18m48s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196341) | [22m18s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511431) | [22m18s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511431) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511267) | [22m11s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196072) | [22m11s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196072) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [9m55s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511317) | [13m23s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196128) | [13m23s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196128) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [5m04s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196254) | [13m01s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511465) | [13m01s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511465) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [8m13s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511456) | [12m22s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196370) | [12m22s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196370) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [9m46s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511499) | [11m35s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196306) | [11m35s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196306) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511245) | [11m24s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196198) | [11m24s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196198) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [5m18s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511430) | [9m24s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196241) | [9m24s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196241) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [48s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196231) | [9m22s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511412) | [9m22s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511412) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [6m19s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196392) | [8m08s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511496) | [8m08s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511496) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511419) | [6m21s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196251) | [6m21s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196251) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511326) | [3m31s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196116) | [3m31s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196116) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31198986139/job/92934156377) | [2m07s](https://github.com/iree-org/iree/actions/runs/31200173451/job/92938111553) | [2m07s](https://github.com/iree-org/iree/actions/runs/31200173451/job/92938111553) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31200173451/job/92938111404) | [9s](https://github.com/iree-org/iree/actions/runs/31198986139/job/92934155683) | [9s](https://github.com/iree-org/iree/actions/runs/31198986139/job/92934155683) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31198986139/job/92934155855) | [9s](https://github.com/iree-org/iree/actions/runs/31200173451/job/92938111350) | [9s](https://github.com/iree-org/iree/actions/runs/31200173451/job/92938111350) | 2 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31200173451/job/92938111181) | [9s](https://github.com/iree-org/iree/actions/runs/31198986139/job/92934155423) | [9s](https://github.com/iree-org/iree/actions/runs/31198986139/job/92934155423) | 2 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31200173451/job/92938111169) | [9s](https://github.com/iree-org/iree/actions/runs/31198986139/job/92934155509) | [9s](https://github.com/iree-org/iree/actions/runs/31198986139/job/92934155509) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 3% (3/102) |  | 3h03m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 116 | 3% (4/116) |  | 8h44m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 131 | 0% (0/131) |  | 8h54m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 100 | 5% (5/100) |  | 8h58m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
