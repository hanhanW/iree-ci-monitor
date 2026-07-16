# iree-ci-monitor

_Updated: 2026-07-16 07:25 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 1 | [22m05s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531129) | [22m05s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531129) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 1 | [18m28s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531354) | [19m42s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531244) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [6m35s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531389) | [16m41s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531186) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531330) | [16m09s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531161) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [13m07s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531247) | [13m07s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531247) | — | `shark01-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [10m08s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531384) | [10m08s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531384) | — | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [6m40s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531164) | [9m55s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531394) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [4m58s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531148) | [4m58s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531148) | — | `shark10-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m26s](https://github.com/iree-org/iree/actions/runs/29488923147/job/87590019866) | [1m26s](https://github.com/iree-org/iree/actions/runs/29488923147/job/87590019866) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 1 | [56s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87639347694) | [59s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331328) | 0% (0/2) | 7 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331383) | [6s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331221) | — | 6 |
| `ubuntu-24.04` | github-hosted | 36 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29503815011/job/87639274775) | [3s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331088) | 50% (3/6) | 35 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523477) | [3s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331091) | — | 6 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331242) | [3s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331175) | — | 5 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29495515504/job/87611420607) | [3s](https://github.com/iree-org/iree/actions/runs/29495515504/job/87611420599) | — | 6 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/29488888041/job/87589912024) | [3s](https://github.com/iree-org/iree/actions/runs/29488888041/job/87589912024) | — | 1 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531007) | [2s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531007) | — | `shark01-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531040) | [2s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531040) | — | `shark75-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531118) | [2s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531118) | — | 1 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531122) | [2s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531122) | — | `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531437) | [2s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531437) | — | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331412) | [1s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331412) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [22m05s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531129) | [22m05s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531129) | [22m05s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531129) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [19m42s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531244) | [19m42s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531244) | [19m42s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531244) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [18m28s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531354) | [18m28s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531354) | [18m28s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531354) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [16m41s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531186) | [16m41s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531186) | [16m41s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531186) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [16m09s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531161) | [16m09s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531161) | [16m09s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531161) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [13m07s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531247) | [13m07s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531247) | [13m07s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531247) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [10m08s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531384) | [10m08s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531384) | [10m08s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531384) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [9m55s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531394) | [9m55s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531394) | [9m55s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531394) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [6m40s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531164) | [6m40s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531164) | [6m40s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531164) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [6m35s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531389) | [6m35s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531389) | [6m35s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531389) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [4m58s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531148) | [4m58s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531148) | [4m58s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531148) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m26s](https://github.com/iree-org/iree/actions/runs/29488923147/job/87590019866) | [1m26s](https://github.com/iree-org/iree/actions/runs/29488923147/job/87590019866) | [1m26s](https://github.com/iree-org/iree/actions/runs/29488923147/job/87590019866) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [59s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331328) | [59s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331328) | [59s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331328) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [57s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331394) | [57s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331394) | [57s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331394) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [57s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331299) | [57s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331299) | [57s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331299) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [56s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87639347694) | [56s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87639347694) | [56s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87639347694) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523482) | [6s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523482) | [6s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523482) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331145) | [6s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331145) | [6s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331145) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331221) | [6s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331221) | [6s](https://github.com/iree-org/iree/actions/runs/29503815476/job/87639331221) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523468) | [5s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523468) | [5s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523468) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 163 | 1% (2/162) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 119 | 1% (1/118) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 138 | 1% (1/138) |  | 1m50s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 136 | 10% (13/136) |  | 5m08s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 38 | 0% (0/38) |  | 9m55s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
