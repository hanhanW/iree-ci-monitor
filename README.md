# iree-ci-monitor

_Updated: 2026-08-18 00:06 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [8m39s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978830) | [54m47s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750453) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [35m28s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093402) | [49m28s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750378) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [10m08s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978805) | [42m50s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750317) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [27m19s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750318) | [29m21s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978623) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [24m21s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978576) | [26m58s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750321) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [11m35s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093443) | [25m48s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978689) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [17m09s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978526) | [24m10s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093467) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [24s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093194) | [22m38s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750324) | 0% (0/2) | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [5m31s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750377) | [16m11s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978684) | 0% (0/4) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [1m52s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750611) | [13m34s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978723) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [4m50s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978615) | [6m56s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093372) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/32073402544/job/95521374446) | [5m04s](https://github.com/iree-org/iree/actions/runs/32070415965/job/95512187315) | 0% (0/2) | 3 |
| `windows-2022` | github-hosted | 11 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/32103297941/job/95607869050) | [50s](https://github.com/iree-org/iree/actions/runs/32070415965/job/95512187010) | 0% (0/6) | 11 |
| `azure-linux-scale` | ossci | 17 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/32070415965/job/95512187055) | [44s](https://github.com/iree-org/iree/actions/runs/32073402544/job/95521374560) | 0% (0/12) | 17 |
| `macos-14` | github-hosted | 11 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/32073402544/job/95521374449) | [41s](https://github.com/iree-org/iree/actions/runs/32070415965/job/95512187124) | 0% (0/6) | 11 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/32103297941/job/95607869089) | [16s](https://github.com/iree-org/iree/actions/runs/32070415965/job/95512187097) | 0% (0/6) | 12 |
| `ubuntu-24.04` | github-hosted | 66 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093502) | [4s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093488) | 2% (1/40) | 65 |
| `ubuntu-latest` | github-hosted | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32070413953/job/95512134725) | [3s](https://github.com/iree-org/iree/actions/runs/32070413953/job/95512134699) | 0% (0/7) | 7 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [45m36s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093472) | [54m47s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750453) | [54m47s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750453) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [35m28s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093402) | [49m28s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750378) | [49m28s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750378) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [10m08s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978805) | [42m50s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750317) | [42m50s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750317) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [8m39s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978830) | [40m19s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093349) | [40m19s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093349) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [27m19s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750318) | [29m21s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978623) | [29m21s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978623) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [24m21s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978576) | [26m58s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750321) | [26m58s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750321) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [22m48s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750375) | [25m48s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978689) | [25m48s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978689) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [17m09s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978526) | [24m10s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093467) | [24m10s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093467) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [24s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093194) | [22m38s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750324) | [22m38s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750324) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [14m15s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750224) | [16m11s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978684) | [16m11s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978684) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [10m27s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750522) | [13m34s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978723) | [13m34s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978723) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [11m35s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093443) | [13m17s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750436) | [13m17s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750436) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [1m52s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750611) | [12m45s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093476) | [12m45s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093476) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [4m50s](https://github.com/iree-org/iree/actions/runs/32070302982/job/95513978615) | [6m56s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093372) | [6m56s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093372) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [5m14s](https://github.com/iree-org/iree/actions/runs/32073402552/job/95523093436) | [5m31s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750377) | [5m31s](https://github.com/iree-org/iree/actions/runs/32070416159/job/95515750377) | 1 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/32073402544/job/95521374446) | [5m04s](https://github.com/iree-org/iree/actions/runs/32070415965/job/95512187315) | [5m04s](https://github.com/iree-org/iree/actions/runs/32070415965/job/95512187315) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 3 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/32070415965/job/95512187110) | [2m13s](https://github.com/iree-org/iree/actions/runs/32073402544/job/95521374430) | [2m13s](https://github.com/iree-org/iree/actions/runs/32073402544/job/95521374430) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 3 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/32073402544/job/95521374464) | [57s](https://github.com/iree-org/iree/actions/runs/32070415965/job/95512187166) | [57s](https://github.com/iree-org/iree/actions/runs/32070415965/job/95512187166) | 3 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32073402544/job/95521374254) | [52s](https://github.com/iree-org/iree/actions/runs/32070415965/job/95512186962) | [52s](https://github.com/iree-org/iree/actions/runs/32070415965/job/95512186962) | 3 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32070302205/job/95511817696) | [50s](https://github.com/iree-org/iree/actions/runs/32070415965/job/95512187010) | [50s](https://github.com/iree-org/iree/actions/runs/32070415965/job/95512187010) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 243 | 0% (1/243) |  | 8h09m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 204 | 5% (11/204) |  | 8h38m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 192 | 3% (6/192) |  | 8h42m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 168 | 6% (10/168) |  | 8h45m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
