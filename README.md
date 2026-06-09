# iree-ci-monitor

_Updated: 2026-06-09 00:33 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [22m33s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467551) | [22m33s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467551) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 1 | [20m16s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467466) | [21m48s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467563) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [14m36s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467499) | [14m36s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467499) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [6m08s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467579) | [11m32s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467472) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467501) | [11m15s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467489) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467553) | [10m48s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467480) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [8m12s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467405) | [8m12s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467405) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [5m41s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467496) | [5m41s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467496) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [5m29s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467473) | [5m29s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467473) | 0% (0/1) | `shark10-ci` |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772402) | [1m37s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772429) | 0% (0/3) | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/27188110910/job/80261615214) | [1m11s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772350) | 0% (0/3) | 6 |
| `ubuntu-24.04` | github-hosted | 26 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467463) | [1m10s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772462) | 14% (3/21) | 26 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772319) | [40s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772434) | 0% (0/3) | 5 |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772444) | [20s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772435) | 0% (0/6) | 6 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467410) | [8s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467474) | 0% (0/4) | 4 |
| `ubuntu-latest` | github-hosted | 4 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27188475111/job/80262744046) | [3s](https://github.com/iree-org/iree/actions/runs/27188475111/job/80262744047) | 0% (0/4) | 4 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467337) | [2s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467337) | 100% (1/1) | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467367) | [2s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467367) | 0% (0/1) | `shark01-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772437) | [1s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772437) | 0% (0/1) | 1 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467448) | [1s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467448) | 0% (0/1) | `iree-mi308-1` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467465) | [1s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467465) | 0% (0/1) | `shark10-ci` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [22m33s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467551) | [22m33s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467551) | [22m33s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467551) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [21m48s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467563) | [21m48s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467563) | [21m48s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467563) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [20m16s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467466) | [20m16s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467466) | [20m16s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467466) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [14m36s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467499) | [14m36s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467499) | [14m36s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467499) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [11m32s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467472) | [11m32s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467472) | [11m32s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467472) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [11m15s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467489) | [11m15s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467489) | [11m15s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467489) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [10m48s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467480) | [10m48s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467480) | [10m48s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467480) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [8m12s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467405) | [8m12s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467405) | [8m12s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467405) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [6m08s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467579) | [6m08s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467579) | [6m08s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467579) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [5m41s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467496) | [5m41s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467496) | [5m41s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467496) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [5m29s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467473) | [5m29s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467473) | [5m29s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467473) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 1 | 0 | — | — | [1m51s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772271) | [1m51s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772271) | [1m51s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772271) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [1m37s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772429) | [1m37s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772429) | [1m37s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772429) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [1m29s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772388) | [1m29s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772388) | [1m29s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772388) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1m11s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772350) | [1m11s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772350) | [1m11s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772350) | 1 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 1 | 0 | — | — | [1m10s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772462) | [1m10s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772462) | [1m10s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772462) | 1 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 1 | 0 | — | — | [40s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772434) | [40s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772434) | [40s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772434) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [20s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772435) | [20s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772435) | [20s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772435) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [18s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772447) | [18s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772447) | [18s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772447) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772399) | [9s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772399) | [9s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772399) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 282 | 4% (10/281) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 339 | 1% (4/339) |  | 59s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 270 | 1% (2/270) |  | 1m19s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 249 | 0% (0/249) |  | 9m08s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 80 | 0% (0/80) |  | 20m26s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
