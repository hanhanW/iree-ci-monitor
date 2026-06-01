# iree-ci-monitor

_Updated: 2026-05-31 18:29 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [16m24s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082916) | [22m15s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082907) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [5m08s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082934) | [20m09s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082929) | 0% (0/2) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [15m50s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082910) | [17m48s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082940) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [14m43s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082905) | [14m43s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082905) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [10m06s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082867) | [10m06s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082867) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [6m51s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082896) | [8m58s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082921) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [8m10s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082798) | [8m10s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082798) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2m12s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082912) | [2m12s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082912) | 0% (0/1) | `shark75-ci` |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687053) | [14s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687108) | 0% (0/6) | 6 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082926) | [8s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082939) | 75% (3/4) | 4 |
| `ubuntu-24.04` | github-hosted | 20 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082864) | [3s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737672209) | 11% (2/18) | 20 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687041) | [2s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737686967) | 33% (1/3) | 3 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687048) | [2s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687060) | 0% (0/3) | 3 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082814) | [2s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082814) | 100% (1/1) | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082826) | [2s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082826) | 0% (0/1) | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082857) | [2s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082857) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082891) | [2s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082891) | 0% (0/1) | `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082901) | [2s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082901) | 0% (0/1) | `iree-mi308-1` |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737686982) | [1s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687032) | 0% (0/3) | 3 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26717150580/job/78737671869) | [1s](https://github.com/iree-org/iree/actions/runs/26717150580/job/78737671875) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [0s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687092) | [0s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687092) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [22m15s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082907) | [22m15s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082907) | [22m15s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082907) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [20m09s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082929) | [20m09s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082929) | [20m09s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082929) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [17m48s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082940) | [17m48s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082940) | [17m48s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082940) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [16m24s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082916) | [16m24s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082916) | [16m24s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082916) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [15m50s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082910) | [15m50s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082910) | [15m50s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082910) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [14m43s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082905) | [14m43s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082905) | [14m43s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082905) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [10m06s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082867) | [10m06s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082867) | [10m06s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082867) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [8m58s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082921) | [8m58s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082921) | [8m58s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082921) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [8m10s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082798) | [8m10s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082798) | [8m10s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082798) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [6m51s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082896) | [6m51s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082896) | [6m51s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082896) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [5m08s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082934) | [5m08s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082934) | [5m08s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082934) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [2m12s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082912) | [2m12s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082912) | [2m12s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082912) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [14s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687108) | [14s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687108) | [14s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687108) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687107) | [8s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687107) | [8s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687107) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687097) | [8s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687097) | [8s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687097) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082926) | [8s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082926) | [8s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082926) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082939) | [8s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082939) | [8s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082939) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687053) | [7s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687053) | [7s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687053) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082861) | [7s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082861) | [7s](https://github.com/iree-org/iree/actions/runs/26717151042/job/78738082861) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687052) | [4s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687052) | [4s](https://github.com/iree-org/iree/actions/runs/26717151053/job/78737687052) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 264 | 5% (12/263) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 287 | 1% (3/287) |  | 8h59m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 204 | 0% (0/204) |  | 9h06m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 198 | 2% (3/198) |  | 9h10m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 67 | 1% (1/67) |  | 9h23m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
