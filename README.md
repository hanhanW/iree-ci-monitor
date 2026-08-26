# iree-ci-monitor

_Updated: 2026-08-26 06:18 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [11m55s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98095143672) | [18m16s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826377) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [4m56s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826251) | [16m34s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826331) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826193) | [16m14s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082464) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [9m47s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826206) | [15m47s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082402) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826202) | [14m17s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98095143520) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [2m44s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98095143590) | [14m10s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826419) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [10m08s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826141) | [13m40s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826518) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826214) | [12m46s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082522) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [11m30s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98095144586) | [11m50s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082450) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826039) | [7m40s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082551) | 0% (0/2) | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [3m38s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98095143713) | [4m50s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826420) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 21 | 0 | — | — | 0 | [1m05s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98100986847) | [1m46s](https://github.com/iree-org/iree/actions/runs/32944070235/job/98100988396) | 7% (1/15) | 21 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m30s](https://github.com/iree-org/iree/actions/runs/32952961678/job/98128324445) | [1m30s](https://github.com/iree-org/iree/actions/runs/32952961678/job/98128324445) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32944070235/job/98100988327) | [1m04s](https://github.com/iree-org/iree/actions/runs/32955758282/job/98136981450) | 0% (0/6) | 11 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/32944070235/job/98100988279) | [45s](https://github.com/iree-org/iree/actions/runs/32955758282/job/98136981420) | 0% (0/6) | 12 |
| `ubuntu-24.04` | github-hosted | 91 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/32955758282/job/98136938561) | [32s](https://github.com/iree-org/iree/actions/runs/32944070235/job/98100988333) | 0% (0/40) | 85 |
| `ubuntu-latest` | github-hosted | 39 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32955757853/job/98136942131) | [4s](https://github.com/iree-org/iree/actions/runs/32951886045/job/98124900566) | 0% (0/9) | 39 |
| `macos-14` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32944070235/job/98100988329) | [3s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368555) | 0% (0/7) | 12 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/32955758282/job/98136981543) | [2s](https://github.com/iree-org/iree/actions/runs/32944070235/job/98100988413) | 0% (0/2) | 3 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [11m55s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98095143672) | [18m16s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826377) | [18m16s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826377) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [7m05s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082554) | [16m34s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826331) | [16m34s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826331) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826193) | [16m14s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082464) | [16m14s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082464) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [9m47s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826206) | [15m47s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082402) | [15m47s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082402) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826202) | [14m17s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98095143520) | [14m17s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98095143520) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [3m15s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082536) | [14m10s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826419) | [14m10s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826419) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [11m35s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082515) | [13m40s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826518) | [13m40s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826518) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826214) | [12m46s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082522) | [12m46s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082522) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [2m09s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98095143727) | [12m31s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826170) | [12m31s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826170) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [11m30s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98095144586) | [11m50s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082450) | [11m50s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082450) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [10m08s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826141) | [10m17s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98095143746) | [10m17s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98095143746) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826039) | [7m40s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082551) | [7m40s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082551) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [3m57s](https://github.com/iree-org/iree/actions/runs/32944069861/job/98108082612) | [4m56s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826251) | [4m56s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826251) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [3m38s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98095143713) | [4m50s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826420) | [4m50s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826420) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [4m12s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98139826259) | [4m35s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98095143495) | [4m35s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98095143495) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 3 | 0 | — | — | [1m19s](https://github.com/iree-org/iree/actions/runs/32955758023/job/98136992674) | [3m58s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98087468667) | [3m58s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98087468667) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 3 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/32955758282/job/98136981511) | [1m46s](https://github.com/iree-org/iree/actions/runs/32944070235/job/98100988396) | [1m46s](https://github.com/iree-org/iree/actions/runs/32944070235/job/98100988396) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/32955758282/job/98136981657) | [1m42s](https://github.com/iree-org/iree/actions/runs/32944070235/job/98100988344) | [1m42s](https://github.com/iree-org/iree/actions/runs/32944070235/job/98100988344) | 3 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 3 | 0 | — | — | [1m22s](https://github.com/iree-org/iree/actions/runs/32944070235/job/98100988432) | [1m38s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465360) | [1m38s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465360) | 3 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | 1 | 0 | — | — | [1m34s](https://github.com/iree-org/iree/actions/runs/32952956075/job/98128307677) | [1m34s](https://github.com/iree-org/iree/actions/runs/32952956075/job/98128307677) | [1m34s](https://github.com/iree-org/iree/actions/runs/32952956075/job/98128307677) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 289 | 1% (4/288) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 256 | 3% (7/255) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 204 | 0% (0/203) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 212 | 0% (0/211) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
