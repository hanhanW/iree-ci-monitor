# iree-ci-monitor

_Updated: 2026-09-23 21:57 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [1h02m](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932915) | [1h11m](https://github.com/iree-org/iree/actions/runs/35910508653/job/107352869016) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [53m20s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932779) | [1h06m](https://github.com/iree-org/iree/actions/runs/35910508653/job/107352868446) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [27m10s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802594) | [1h03m](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802788) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [36m38s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932912) | [59m15s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369933058) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [57m25s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932926) | [58m21s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802519) | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [47m27s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932928) | [53m43s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802674) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [12m51s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802769) | [48m36s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932955) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [10m22s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932796) | [31m07s](https://github.com/iree-org/iree/actions/runs/35910508653/job/107352869075) | — | `shark55-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 19 | 0 | — | — | 0 | [2m18s](https://github.com/iree-org/iree/actions/runs/35910508441/job/107349724716) | [20m10s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751704) | — | 19 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35910508441/job/107349724687) | [8m26s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751749) | — | 4 |
| `macos-14` | github-hosted | 12 | 0 | — | — | 0 | [48s](https://github.com/iree-org/iree/actions/runs/35910508805/job/107348916904) | [3m35s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751379) | — | 12 |
| `windows-2022` | github-hosted | 12 | 0 | — | — | 0 | [43s](https://github.com/iree-org/iree/actions/runs/35910508441/job/107349724217) | [2m25s](https://github.com/iree-org/iree/actions/runs/35910508441/job/107349724253) | — | 12 |
| `ubuntu-24.04` | github-hosted | 92 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802696) | [2m09s](https://github.com/iree-org/iree/actions/runs/35910508441/job/107349724068) | 0% (0/3) | 82 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [42s](https://github.com/iree-org/iree/actions/runs/35910508805/job/107348916688) | [1m36s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751267) | — | 12 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/35910501281/job/107348824590) | [4s](https://github.com/iree-org/iree/actions/runs/35910501281/job/107348824987) | — | 12 |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [1h02m](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932915) | [1h11m](https://github.com/iree-org/iree/actions/runs/35910508653/job/107352869016) | [1h11m](https://github.com/iree-org/iree/actions/runs/35910508653/job/107352869016) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [53m20s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932779) | [1h06m](https://github.com/iree-org/iree/actions/runs/35910508653/job/107352868446) | [1h06m](https://github.com/iree-org/iree/actions/runs/35910508653/job/107352868446) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [53m20s](https://github.com/iree-org/iree/actions/runs/35910508653/job/107352869375) | [1h03m](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802788) | [1h03m](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802788) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [59m05s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802839) | [59m15s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369933058) | [59m15s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369933058) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 3 | 0 | — | — | [57m25s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932926) | [58m21s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802519) | [58m21s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802519) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [47m27s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932928) | [53m43s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802674) | [53m43s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802674) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [18m35s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802577) | [48m36s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932955) | [48m36s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932955) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 3 | 0 | — | — | [20m06s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107349753169) | [45m57s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107349860083) | [45m57s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107349860083) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [27m10s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802594) | [41m28s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932943) | [41m28s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932943) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [36m38s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932912) | [39m21s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802563) | [39m21s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802563) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [9m10s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369932942) | [31m07s](https://github.com/iree-org/iree/actions/runs/35910508653/job/107352869075) | [31m07s](https://github.com/iree-org/iree/actions/runs/35910508653/job/107352869075) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [10m43s](https://github.com/iree-org/iree/actions/runs/35910508653/job/107352869054) | [24m40s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802689) | [24m40s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802689) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 4 | 0 | — | — | [2m18s](https://github.com/iree-org/iree/actions/runs/35910508441/job/107349724716) | [20m10s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751704) | [20m10s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751704) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [12m51s](https://github.com/iree-org/iree/actions/runs/35910508284/job/107359802769) | [17m27s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369933192) | [17m27s](https://github.com/iree-org/iree/actions/runs/35910508215/job/107369933192) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 4 | 0 | — | — | [2m01s](https://github.com/iree-org/iree/actions/runs/35910508441/job/107349724676) | [16m17s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751709) | [16m17s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751709) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 4 | 0 | — | — | [1m43s](https://github.com/iree-org/iree/actions/runs/35910508441/job/107349724494) | [15m53s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751552) | [15m53s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751552) | 4 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35910508441/job/107349724687) | [8m26s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751749) | [8m26s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751749) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 4 | 0 | — | — | [2m03s](https://github.com/iree-org/iree/actions/runs/35910508441/job/107349724361) | [3m35s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751379) | [3m35s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751379) | 4 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 4 | 0 | — | — | [2m04s](https://github.com/iree-org/iree/actions/runs/35910508441/job/107349724163) | [3m33s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751455) | [3m33s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751455) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 4 | 0 | — | — | [2m11s](https://github.com/iree-org/iree/actions/runs/35910508441/job/107349724238) | [3m30s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751541) | [3m30s](https://github.com/iree-org/iree/actions/runs/35910507890/job/107349751541) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 342 | 1% (5/342) |  | 7h15m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 311 | 2% (7/311) |  | 7h20m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 75 | 0% (0/75) |  | 6d07h ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h11m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h03m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-w7900` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
