# iree-ci-monitor

_Updated: 2026-07-05 05:45 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138082) | [26m25s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138113) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138084) | [21m26s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138054) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [19m38s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138067) | [19m38s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138067) | — | `shark01-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [18m35s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138035) | [18m35s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138035) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [16m03s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138053) | [16m17s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138129) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [12m01s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138061) | [12m01s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138061) | — | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [11m50s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138052) | [11m50s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138052) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [10m54s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138047) | [10m54s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138047) | — | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138089) | [9m50s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138120) | — | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [5m16s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138131) | [5m16s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138131) | — | `shark10-ci` |
| `ubuntu-24.04` | github-hosted | 32 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628430) | [1m57s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628526) | 0% (0/1) | 32 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m50s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628537) | [1m50s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628537) | — | 1 |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 0 | [49s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628540) | [1m38s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628509) | — | 7 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628437) | [1m37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628469) | — | 6 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28731838272/job/85198852709) | [1m19s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628538) | — | 6 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [53s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628556) | [53s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628556) | — | 1 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628450) | [51s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628483) | — | 5 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138123) | [27s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138124) | — | 4 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28733211163/job/85202612632) | [3s](https://github.com/iree-org/iree/actions/runs/28740504738/job/85222278487) | — | 9 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138085) | [2s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138085) | — | `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138090) | [2s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138090) | — | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628552) | [1s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628552) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [26m25s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138113) | [26m25s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138113) | [26m25s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138113) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [21m26s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138054) | [21m26s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138054) | [21m26s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138054) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [19m38s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138067) | [19m38s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138067) | [19m38s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138067) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [18m35s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138035) | [18m35s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138035) | [18m35s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138035) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [16m17s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138129) | [16m17s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138129) | [16m17s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138129) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [16m03s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138053) | [16m03s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138053) | [16m03s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138053) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [12m01s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138061) | [12m01s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138061) | [12m01s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138061) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [11m50s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138052) | [11m50s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138052) | [11m50s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138052) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [10m54s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138047) | [10m54s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138047) | [10m54s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138047) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [9m50s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138120) | [9m50s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138120) | [9m50s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138120) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [5m16s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138131) | [5m16s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138131) | [5m16s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138131) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 1 | 0 | — | — | [2m49s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138135) | [2m49s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138135) | [2m49s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138135) | 1 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 1 | 0 | — | — | [2m30s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138080) | [2m30s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138080) | [2m30s](https://github.com/iree-org/iree/actions/runs/28733212510/job/85203138080) | 1 |
| `.github/workflows/ci.yml` | linux_x64_gcc / linux_x64_gcc | `ubuntu-24.04` | 1 | 0 | — | — | [1m57s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628526) | [1m57s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628526) | [1m57s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628526) | 1 |
| `.github/workflows/ci.yml` | linux_arm64_clang / linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m50s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628537) | [1m50s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628537) | [1m50s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628537) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_byollvm / linux_x64_clang_byollvm | `ubuntu-24.04` | 1 | 0 | — | — | [1m49s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628546) | [1m49s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628546) | [1m49s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628546) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [1m38s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628509) | [1m38s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628509) | [1m38s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628509) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628516) | [1m37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628516) | [1m37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628516) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1m37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628469) | [1m37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628469) | [1m37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628469) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 1 | 0 | — | — | [1m30s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628488) | [1m30s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628488) | [1m30s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628488) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 275 | 3% (7/275) |  | 4h42m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 194 | 2% (3/194) |  | 4h46m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 249 | 8% (19/249) |  | 4h46m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 216 | 1% (3/216) |  | 4h47m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 65 | 2% (1/65) |  | 5h04m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
