# iree-ci-monitor

_Updated: 2026-09-19 13:45 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [6m28s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640136) | [40m53s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640262) | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [37m25s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640107) | [37m25s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640107) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [23m02s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640160) | [35m18s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640234) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [16m59s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640308) | [22m37s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640120) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [16m41s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640146) | [16m41s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640146) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [9m19s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640116) | [9m19s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640116) | — | `shark75-ci` |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [1m16s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993290) | [2m43s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105911993892) | — | 5 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993203) | [7s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993291) | — | 3 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993131) | [5s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993259) | — | 3 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35447871693/job/105909865905) | [3s](https://github.com/iree-org/iree/actions/runs/35447872325/job/105909846861) | — | 9 |
| `ubuntu-24.04` | github-hosted | 32 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640088) | [3s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640094) | 0% (0/1) | 32 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993247) | [3s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993281) | — | 3 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640053) | [2s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640062) | — | `shark55-ci`, `shark75-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993251) | [1s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993251) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 2 | [17h27m](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672695) | 2026-09-19 13:45 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 2 | [17h27m](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672722) | 2026-09-19 13:45 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [17h27m](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672695) | 2026-09-19 13:45 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `main` | push |
| [17h27m](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672722) | 2026-09-19 13:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [6h07m](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640040) | 2026-09-19 13:45 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `stream-flush-invalidate-lowering` | pull_request |
| [6h07m](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640153) | 2026-09-19 13:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `stream-flush-invalidate-lowering` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 2 | [17h27m](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672695) | 2026-09-19 13:45 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 2 | [17h27m](https://github.com/iree-org/iree/actions/runs/35416725134/job/105830672722) | 2026-09-19 13:45 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [40m53s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640262) | [40m53s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640262) | [40m53s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640262) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [37m25s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640107) | [37m25s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640107) | [37m25s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640107) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [35m18s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640234) | [35m18s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640234) | [35m18s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640234) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [23m02s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640160) | [23m02s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640160) | [23m02s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640160) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [22m37s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640120) | [22m37s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640120) | [22m37s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640120) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [16m59s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640308) | [16m59s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640308) | [16m59s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640308) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [16m41s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640146) | [16m41s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640146) | [16m41s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640146) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [9m19s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640116) | [9m19s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640116) | [9m19s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640116) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [6m28s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640136) | [6m28s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640136) | [6m28s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640136) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [2m43s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105911993892) | [2m43s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105911993892) | [2m43s](https://github.com/iree-org/iree/actions/runs/35444212759/job/105911993892) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [1m18s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993285) | [1m18s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993285) | [1m18s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993285) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [1m16s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993290) | [1m16s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993290) | [1m16s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993290) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [1m15s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993313) | [1m15s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993313) | [1m15s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993313) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993291) | [7s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993291) | [7s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993291) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993203) | [7s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993203) | [7s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993203) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993145) | [6s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993145) | [6s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993145) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993108) | [5s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993108) | [5s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993108) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993053) | [5s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993053) | [5s](https://github.com/iree-org/iree/actions/runs/35444212710/job/105911993053) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 322 | 0% (1/322) |  | 5h19m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 359 | 1% (3/359) |  | 5h24m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 230 | 2% (4/230) |  | 1d23h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 17 | 12% (2/17) |  | 5d05h ago |

## Alerts

- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job observed waiting 17h27m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 17h27m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
