# iree-ci-monitor

_Updated: 2026-10-14 21:47 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 14 | 0 | — | — | 0 | [16m58s](https://github.com/iree-org/iree/actions/runs/38654117478/job/116161987351) | [40m43s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768556) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 14 | 0 | — | — | 0 | [14m18s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015385) | [36m12s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768495) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [3m16s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015435) | [28m44s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768508) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 14 | 0 | — | — | 0 | [5m47s](https://github.com/iree-org/iree/actions/runs/38649163524/job/116145955397) | [25m59s](https://github.com/iree-org/iree/actions/runs/38663624196/job/116192819306) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [10m03s](https://github.com/iree-org/iree/actions/runs/38660957850/job/116184993524) | [20m09s](https://github.com/iree-org/iree/actions/runs/38663624196/job/116192819277) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 7 | 0 | — | — | 0 | [11m18s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768440) | [15m21s](https://github.com/iree-org/iree/actions/runs/38660957850/job/116184993602) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 14 | 0 | — | — | 0 | [6m13s](https://github.com/iree-org/iree/actions/runs/38649163524/job/116145955378) | [13m12s](https://github.com/iree-org/iree/actions/runs/38663624196/job/116192819295) | 0% (0/4) | `shark55-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 43 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/38654117520/job/116159755795) | [1m35s](https://github.com/iree-org/iree/actions/runs/38635008537/job/116095893098) | 0% (0/14) | 43 |
| `macos-15` | github-hosted | 21 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/38649163522/job/116143477795) | [10s](https://github.com/iree-org/iree/actions/runs/38649163522/job/116143477734) | 0% (0/6) | 21 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/38660957830/job/116181876258) | [5s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796695) | 0% (0/6) | 21 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38635853889/job/116098715897) | [3s](https://github.com/iree-org/iree/actions/runs/38635852311/job/116098803455) | 0% (0/6) | 12 |
| `ubuntu-24.04` | github-hosted | 147 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38660957829/job/116181805365) | [3s](https://github.com/iree-org/iree/actions/runs/38649163524/job/116145955524) | 2% (1/44) | 146 |
| `windows-2022` | github-hosted | 21 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38654117520/job/116159755258) | [2s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796705) | 0% (0/6) | 21 |
| `azure-windows-scale` | ossci | 7 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/38649163522/job/116143478146) | [1s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796853) | 0% (0/2) | 7 |
| `Linux,X64,iree-w7900` | self-hosted | 7 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 7 | 0 | — | — | [14m18s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015385) | [47m48s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768747) | [47m48s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768747) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 7 | 0 | — | — | [18m06s](https://github.com/iree-org/iree/actions/runs/38635008547/job/116099046413) | [46m33s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768635) | [46m33s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768635) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 7 | 0 | — | — | [12m17s](https://github.com/iree-org/iree/actions/runs/38635008547/job/116099046402) | [40m43s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768556) | [40m43s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768556) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 7 | 0 | — | — | [1m51s](https://github.com/iree-org/iree/actions/runs/38649163524/job/116145955437) | [36m12s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768495) | [36m12s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768495) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 7 | 0 | — | — | [3m16s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015435) | [28m44s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768508) | [28m44s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768508) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [4m38s](https://github.com/iree-org/iree/actions/runs/38649163524/job/116145955629) | [26m28s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768790) | [26m28s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768790) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [5m47s](https://github.com/iree-org/iree/actions/runs/38649163524/job/116145955397) | [25m59s](https://github.com/iree-org/iree/actions/runs/38663624196/job/116192819306) | [25m59s](https://github.com/iree-org/iree/actions/runs/38663624196/job/116192819306) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [5m32s](https://github.com/iree-org/iree/actions/runs/38635008547/job/116099045835) | [20m35s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768458) | [20m35s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768458) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 7 | 0 | — | — | [10m03s](https://github.com/iree-org/iree/actions/runs/38660957850/job/116184993524) | [20m09s](https://github.com/iree-org/iree/actions/runs/38663624196/job/116192819277) | [20m09s](https://github.com/iree-org/iree/actions/runs/38663624196/job/116192819277) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 7 | 0 | — | — | [11m18s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768440) | [15m21s](https://github.com/iree-org/iree/actions/runs/38660957850/job/116184993602) | [15m21s](https://github.com/iree-org/iree/actions/runs/38660957850/job/116184993602) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [7m06s](https://github.com/iree-org/iree/actions/runs/38654117478/job/116161987242) | [13m12s](https://github.com/iree-org/iree/actions/runs/38663624196/job/116192819295) | [13m12s](https://github.com/iree-org/iree/actions/runs/38663624196/job/116192819295) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38635008537/job/116095893277) | [2m38s](https://github.com/iree-org/iree/actions/runs/38654117520/job/116159755711) | [2m38s](https://github.com/iree-org/iree/actions/runs/38654117520/job/116159755711) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 7 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38649163522/job/116143478137) | [1m36s](https://github.com/iree-org/iree/actions/runs/38635008537/job/116095893479) | [1m36s](https://github.com/iree-org/iree/actions/runs/38635008537/job/116095893479) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 7 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/38660957830/job/116181876605) | [1m35s](https://github.com/iree-org/iree/actions/runs/38635008537/job/116095893098) | [1m35s](https://github.com/iree-org/iree/actions/runs/38635008537/job/116095893098) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 7 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38663624265/job/116191199336) | [1m24s](https://github.com/iree-org/iree/actions/runs/38635008537/job/116095893295) | [1m24s](https://github.com/iree-org/iree/actions/runs/38635008537/job/116095893295) | 7 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 7 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/38654117520/job/116159755554) | [1m03s](https://github.com/iree-org/iree/actions/runs/38635008537/job/116095893042) | [1m03s](https://github.com/iree-org/iree/actions/runs/38635008537/job/116095893042) | 7 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 7 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38649163524/job/116145955213) | [37s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768597) | [37s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116038768597) | 7 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116245633862) | [26s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116061285306) | [26s](https://github.com/iree-org/iree/actions/runs/38617234283/job/116061285306) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 7 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38635008537/job/116095893079) | [14s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796810) | [14s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796810) | 7 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 7 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/38660957830/job/116181876428) | [12s](https://github.com/iree-org/iree/actions/runs/38635008537/job/116095893242) | [12s](https://github.com/iree-org/iree/actions/runs/38635008537/job/116095893242) | 7 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 281 | 1% (2/281) |  | 23m32s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 365 | 8% (30/365) |  | 25m22s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
