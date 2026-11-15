# iree-ci-monitor

_Updated: 2026-11-14 22:41 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [22m52s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593225) | [33m01s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022569) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [23m39s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022561) | [30m30s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593354) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [23m12s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022439) | [29m18s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593314) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [17m12s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593331) | [29m04s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022592) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [16m13s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022308) | [23m01s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593194) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593212) | [11m27s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022458) | — | `shark55-ci` |
| `azure-linux-scale` | ossci | 12 | 0 | — | — | 0 | [1m31s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132698536807) | [1m49s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683494086) | — | 12 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/43676755297/job/132698534673) | [5s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683493834) | — | 9 |
| `macos-15` | github-hosted | 8 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/43676755297/job/132698534570) | [3s](https://github.com/iree-org/iree/actions/runs/43679844334/job/132707917450) | — | 8 |
| `ubuntu-24.04` | github-hosted | 54 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683493839) | [2s](https://github.com/iree-org/iree/actions/runs/43679844334/job/132707917422) | 0% (0/4) | 52 |
| `windows-2022` | github-hosted | 8 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683493866) | [2s](https://github.com/iree-org/iree/actions/runs/43679844334/job/132707917437) | — | 8 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022339) | [1s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593218) | — | `shark75-ci` |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683494064) | [1s](https://github.com/iree-org/iree/actions/runs/43676755297/job/132698534862) | — | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [8m37s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593317) | [33m01s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022569) | [33m01s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022569) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [8m14s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022515) | [30m30s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593354) | [30m30s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593354) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022350) | [29m18s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593314) | [29m18s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593314) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [17m12s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593331) | [29m04s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022592) | [29m04s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022592) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [13m02s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593285) | [23m39s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022561) | [23m39s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022561) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [3m29s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593222) | [23m12s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022439) | [23m12s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022439) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [16m13s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022308) | [23m01s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593194) | [23m01s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593194) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [16m06s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022517) | [22m52s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593225) | [22m52s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593225) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593212) | [11m27s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022458) | [11m27s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022458) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [6m00s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132685022577) | [6m11s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593254) | [6m11s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132700593254) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/43676755297/job/132698534822) | [1m54s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683493968) | [1m54s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683493968) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/43676755297/job/132698534744) | [1m49s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683493891) | [1m49s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683493891) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 2 | 0 | — | — | [1m31s](https://github.com/iree-org/iree/actions/runs/43676755297/job/132698534831) | [1m49s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683494086) | [1m49s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683494086) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/43676755297/job/132698534733) | [1m32s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683493971) | [1m32s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683493971) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/43671860694/job/132683491656) | [1m31s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132698536807) | [1m31s](https://github.com/iree-org/iree/actions/runs/43676755286/job/132698536807) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/43676755297/job/132698534751) | [1m26s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683493906) | [1m26s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683493906) | 2 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 2 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/43676755297/job/132698534600) | [5s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683493834) | [5s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683493834) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 2 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683494035) | [4s](https://github.com/iree-org/iree/actions/runs/43676755297/job/132698534673) | [4s](https://github.com/iree-org/iree/actions/runs/43676755297/job/132698534673) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 2 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/43671860708/job/132683493842) | [4s](https://github.com/iree-org/iree/actions/runs/43676755297/job/132698534616) | [4s](https://github.com/iree-org/iree/actions/runs/43676755297/job/132698534616) | 2 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/43679844334/job/132707917446) | [4s](https://github.com/iree-org/iree/actions/runs/43679844334/job/132707917446) | [4s](https://github.com/iree-org/iree/actions/runs/43679844334/job/132707917446) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 346 | 1% (3/346) |  | 1h27m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 404 | 0% (2/404) |  | 1h30m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
