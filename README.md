# iree-ci-monitor

_Updated: 2026-10-28 15:39 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [2h43m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675571) | [3h26m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675536) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [2h24m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675552) | [3h18m](https://github.com/iree-org/iree/actions/runs/40673981327/job/122822499586) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [2h47m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675436) | [3h13m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675457) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [1h45m](https://github.com/iree-org/iree/actions/runs/40673981327/job/122822499609) | [2h56m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675304) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [13m29s](https://github.com/iree-org/iree/actions/runs/40673981327/job/122822499688) | [53m14s](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675258) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [28m33s](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836676072) | [28m33s](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836676072) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [22m27s](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675511) | [22m27s](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675511) | 0% (0/1) | `shark55-ci` |
| `azure-linux-scale` | ossci | 16 | 0 | — | — | 1 | [9s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829887254) | [2m14s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822129158) | 0% (0/8) | 15 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822128759) | [5s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829886452) | 0% (0/3) | 6 |
| `macos-15` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829886696) | [5s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829886471) | 0% (0/3) | 6 |
| `ubuntu-24.04` | github-hosted | 62 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40691960477/job/122828757839) | [3s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829886476) | 0% (0/23) | 61 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822128651) | [3s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829886528) | 0% (0/3) | 6 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/40689986009/job/122822033897) | [3s](https://github.com/iree-org/iree/actions/runs/40691955077/job/122828744965) | 0% (0/3) | 6 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822129216) | [2s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829887331) | 0% (0/1) | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [1h17m](https://github.com/iree-org/iree/actions/runs/40673981327/job/122822499496) | [3h26m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675536) | [3h26m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675536) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [1h55m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675615) | [3h18m](https://github.com/iree-org/iree/actions/runs/40673981327/job/122822499586) | [3h18m](https://github.com/iree-org/iree/actions/runs/40673981327/job/122822499586) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [2h03m](https://github.com/iree-org/iree/actions/runs/40673981327/job/122822499535) | [3h13m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675457) | [3h13m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675457) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [1h30m](https://github.com/iree-org/iree/actions/runs/40673981327/job/122822499334) | [2h56m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675304) | [2h56m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675304) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [2h47m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675436) | [2h47m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675436) | [2h47m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675436) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [2h43m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675571) | [2h43m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675571) | [2h43m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675571) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [31m51s](https://github.com/iree-org/iree/actions/runs/40673981327/job/122822499545) | [2h24m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675552) | [2h24m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675552) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [1h28m](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675816) | [1h45m](https://github.com/iree-org/iree/actions/runs/40673981327/job/122822499609) | [1h45m](https://github.com/iree-org/iree/actions/runs/40673981327/job/122822499609) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [13m29s](https://github.com/iree-org/iree/actions/runs/40673981327/job/122822499688) | [53m14s](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675258) | [53m14s](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675258) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [28m33s](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836676072) | [28m33s](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836676072) | [28m33s](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836676072) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [22m27s](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675511) | [22m27s](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675511) | [22m27s](https://github.com/iree-org/iree/actions/runs/40689988479/job/122836675511) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829886698) | [2m22s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822128908) | [2m22s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822128908) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [2m14s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822129158) | [2m14s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822129158) | [2m14s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822129158) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829887254) | [2m04s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822128950) | [2m04s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822128950) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829886751) | [2m03s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822129309) | [2m03s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822129309) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829887168) | [2m02s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822129139) | [2m02s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822129139) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 4 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/40691960884/job/122829121227) | [1m31s](https://github.com/iree-org/iree/actions/runs/40689988479/job/122822129750) | [1m31s](https://github.com/iree-org/iree/actions/runs/40689988479/job/122822129750) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829886564) | [55s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822128939) | [55s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822128939) | 2 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 2 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822128656) | [5s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829886471) | [5s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829886471) | 2 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 2 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822128583) | [5s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829886313) | [5s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829886313) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 311 | 1% (4/311) |  | 5h57m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 262 | 3% (7/262) |  | 6h12m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 3h18m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h13m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 3h26m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h56m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
