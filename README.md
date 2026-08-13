# iree-ci-monitor

_Updated: 2026-08-13 06:50 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [11m45s](https://github.com/iree-org/iree/actions/runs/31698871520/job/94444635136) | [47m42s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928462) | 0% (0/3) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [28m21s](https://github.com/iree-org/iree/actions/runs/31681655126/job/94390187292) | [47m29s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928331) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [28m21s](https://github.com/iree-org/iree/actions/runs/31698871520/job/94444634988) | [46m09s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928264) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [20m05s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928557) | [36m01s](https://github.com/iree-org/iree/actions/runs/31698871520/job/94444635300) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [13m20s](https://github.com/iree-org/iree/actions/runs/31681655126/job/94390187221) | [34m14s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928577) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [15m26s](https://github.com/iree-org/iree/actions/runs/31695271611/job/94433926864) | [28m21s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928440) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [15m50s](https://github.com/iree-org/iree/actions/runs/31695271611/job/94433926907) | [22m00s](https://github.com/iree-org/iree/actions/runs/31681655126/job/94390187424) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [11m44s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928260) | [21m49s](https://github.com/iree-org/iree/actions/runs/31681655126/job/94390187159) | 0% (0/3) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [13m02s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928500) | [20m42s](https://github.com/iree-org/iree/actions/runs/31695271611/job/94433927028) | 17% (1/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [7m16s](https://github.com/iree-org/iree/actions/runs/31681655126/job/94390187296) | [18m33s](https://github.com/iree-org/iree/actions/runs/31681655126/job/94390187404) | 0% (0/6) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [6m42s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928520) | [7m06s](https://github.com/iree-org/iree/actions/runs/31698871520/job/94444635141) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 25 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/31698871526/job/94465714603) | [1m30s](https://github.com/iree-org/iree/actions/runs/31695271682/job/94431575422) | 0% (0/20) | 25 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m22s](https://github.com/iree-org/iree/actions/runs/31687546251/job/94407046689) | [1m22s](https://github.com/iree-org/iree/actions/runs/31687546251/job/94407046689) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 14 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31681655036/job/94388271864) | [1m21s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487169) | 0% (0/9) | 14 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31695271682/job/94431575237) | [1m11s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487268) | 0% (0/10) | 15 |
| `ubuntu-24.04` | github-hosted | 86 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/31695271682/job/94431575010) | [9s](https://github.com/iree-org/iree/actions/runs/31695271611/job/94433926857) | 2% (1/59) | 85 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31695271090/job/94431525869) | [8s](https://github.com/iree-org/iree/actions/runs/31673332454/job/94362448524) | 0% (0/9) | 15 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487133) | [5s](https://github.com/iree-org/iree/actions/runs/31695271682/job/94431575124) | 0% (0/9) | 15 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/31698871526/job/94465714882) | [2s](https://github.com/iree-org/iree/actions/runs/31681655036/job/94388272064) | 0% (0/3) | 4 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [11m45s](https://github.com/iree-org/iree/actions/runs/31698871520/job/94444635136) | [47m42s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928462) | [47m42s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928462) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [28m21s](https://github.com/iree-org/iree/actions/runs/31681655126/job/94390187292) | [47m29s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928331) | [47m29s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928331) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [28m21s](https://github.com/iree-org/iree/actions/runs/31698871520/job/94444634988) | [46m09s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928264) | [46m09s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928264) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [20m05s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928557) | [36m01s](https://github.com/iree-org/iree/actions/runs/31698871520/job/94444635300) | [36m01s](https://github.com/iree-org/iree/actions/runs/31698871520/job/94444635300) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [13m20s](https://github.com/iree-org/iree/actions/runs/31681655126/job/94390187221) | [34m14s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928577) | [34m14s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928577) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [15m26s](https://github.com/iree-org/iree/actions/runs/31695271611/job/94433926864) | [28m21s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928440) | [28m21s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928440) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [22m21s](https://github.com/iree-org/iree/actions/runs/31698871520/job/94444635051) | [27m00s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928508) | [27m00s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928508) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [16m13s](https://github.com/iree-org/iree/actions/runs/31698871520/job/94444635050) | [22m00s](https://github.com/iree-org/iree/actions/runs/31681655126/job/94390187424) | [22m00s](https://github.com/iree-org/iree/actions/runs/31681655126/job/94390187424) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [11m44s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928260) | [21m49s](https://github.com/iree-org/iree/actions/runs/31681655126/job/94390187159) | [21m49s](https://github.com/iree-org/iree/actions/runs/31681655126/job/94390187159) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [18m20s](https://github.com/iree-org/iree/actions/runs/31698871520/job/94444635132) | [20m42s](https://github.com/iree-org/iree/actions/runs/31695271611/job/94433927028) | [20m42s](https://github.com/iree-org/iree/actions/runs/31695271611/job/94433927028) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [15m50s](https://github.com/iree-org/iree/actions/runs/31695271611/job/94433926907) | [20m05s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928540) | [20m05s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928540) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [10m37s](https://github.com/iree-org/iree/actions/runs/31695271611/job/94433926931) | [18m33s](https://github.com/iree-org/iree/actions/runs/31681655126/job/94390187404) | [18m33s](https://github.com/iree-org/iree/actions/runs/31681655126/job/94390187404) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [11m30s](https://github.com/iree-org/iree/actions/runs/31695271611/job/94433926830) | [17m53s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928455) | [17m53s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928455) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [7m16s](https://github.com/iree-org/iree/actions/runs/31681655126/job/94390187296) | [13m58s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928422) | [13m58s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928422) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [6m42s](https://github.com/iree-org/iree/actions/runs/31673333337/job/94363928520) | [7m06s](https://github.com/iree-org/iree/actions/runs/31698871520/job/94444635141) | [7m06s](https://github.com/iree-org/iree/actions/runs/31698871520/job/94444635141) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 4 | 0 | — | — | [1m15s](https://github.com/iree-org/iree/actions/runs/31681655126/job/94388273437) | [1m48s](https://github.com/iree-org/iree/actions/runs/31695271611/job/94431599772) | [1m48s](https://github.com/iree-org/iree/actions/runs/31695271611/job/94431599772) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 3 | 0 | — | — | [1m15s](https://github.com/iree-org/iree/actions/runs/31681655036/job/94388272031) | [1m30s](https://github.com/iree-org/iree/actions/runs/31695271682/job/94431575422) | [1m30s](https://github.com/iree-org/iree/actions/runs/31695271682/job/94431575422) | 3 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 4 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31698871526/job/94465714603) | [1m25s](https://github.com/iree-org/iree/actions/runs/31695271682/job/94431575351) | [1m25s](https://github.com/iree-org/iree/actions/runs/31695271682/job/94431575351) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31681655036/job/94388272032) | [1m25s](https://github.com/iree-org/iree/actions/runs/31695271682/job/94431575349) | [1m25s](https://github.com/iree-org/iree/actions/runs/31695271682/job/94431575349) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31695271682/job/94431575237) | [1m24s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487154) | [1m24s](https://github.com/iree-org/iree/actions/runs/31673333196/job/94362487154) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 206 | 0% (0/206) |  | 50m11s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 171 | 5% (9/171) |  | 1h05m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 170 | 8% (13/170) |  | 1h11m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 142 | 12% (17/142) |  | 1h11m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
