# iree-ci-monitor

_Updated: 2026-07-02 18:02 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257663) | [40m00s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039932) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [27m11s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039943) | [34m00s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838258119) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039933) | [32m32s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257651) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [20m48s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257910) | [28m23s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039898) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [19m00s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039770) | [23m53s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257266) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039811) | [21m46s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257748) | 0% (0/1) | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [10m28s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039832) | [19m53s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845040061) | 50% (1/2) | `shark01-ci`, `shark10-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [13m52s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845040019) | [18m12s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257983) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [7m17s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845040011) | [9m58s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257880) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257646) | [5m47s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039936) | 0% (0/1) | `shark55-ci` |
| `azure-linux-scale` | ossci | 11 | 0 | — | — | 0 | [53s](https://github.com/iree-org/iree/actions/runs/28611002605/job/84843199286) | [2m34s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836781020) | 17% (1/6) | 11 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | — | 0 | [14s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257876) | [38s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039923) | 0% (0/4) | 8 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836781091) | [6s](https://github.com/iree-org/iree/actions/runs/28611002605/job/84843199213) | 0% (0/3) | 6 |
| `ubuntu-24.04` | github-hosted | 40 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28611002605/job/84843161311) | [4s](https://github.com/iree-org/iree/actions/runs/28609097391/job/84836749656) | 11% (2/18) | 40 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836780993) | [3s](https://github.com/iree-org/iree/actions/runs/28611002605/job/84843199429) | 0% (0/3) | 6 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28611002605/job/84843199297) | [3s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836781159) | 0% (0/3) | 6 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257364) | [2s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039788) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257891) | [2s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039836) | 0% (0/1) | `iree-mi308-1` |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28611000949/job/84843160193) | [2s](https://github.com/iree-org/iree/actions/runs/28611000949/job/84843160205) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836781320) | [1s](https://github.com/iree-org/iree/actions/runs/28611002605/job/84843199358) | 0% (0/1) | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257663) | [40m00s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039932) | [40m00s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039932) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [27m11s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039943) | [34m00s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838258119) | [34m00s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838258119) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039933) | [32m32s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257651) | [32m32s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257651) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [20m48s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257910) | [28m23s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039898) | [28m23s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039898) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [19m00s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039770) | [23m53s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257266) | [23m53s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257266) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039811) | [21m46s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257748) | [21m46s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257748) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257691) | [19m53s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845040061) | [19m53s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845040061) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [6m15s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845040074) | [18m12s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257983) | [18m12s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257983) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [7m07s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257859) | [13m52s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845040019) | [13m52s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845040019) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [9m53s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257896) | [10m28s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039832) | [10m28s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039832) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [7m17s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845040011) | [9m58s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257880) | [9m58s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257880) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [7m17s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845040015) | [7m37s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257865) | [7m37s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257865) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257646) | [5m47s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039936) | [5m47s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039936) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039979) | [5m32s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838258100) | [5m32s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838258100) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [53s](https://github.com/iree-org/iree/actions/runs/28611002605/job/84843199286) | [2m34s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836781020) | [2m34s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836781020) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [48s](https://github.com/iree-org/iree/actions/runs/28611002605/job/84843199370) | [2m22s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836781114) | [2m22s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836781114) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [51s](https://github.com/iree-org/iree/actions/runs/28611002605/job/84843199440) | [2m07s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836781115) | [2m07s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836781115) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [21s](https://github.com/iree-org/iree/actions/runs/28609097431/job/84836781116) | [1m58s](https://github.com/iree-org/iree/actions/runs/28611002605/job/84843199298) | [1m58s](https://github.com/iree-org/iree/actions/runs/28611002605/job/84843199298) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [55s](https://github.com/iree-org/iree/actions/runs/28611002605/job/84843199391) | [55s](https://github.com/iree-org/iree/actions/runs/28611002605/job/84843199391) | [55s](https://github.com/iree-org/iree/actions/runs/28611002605/job/84843199391) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/28609097577/job/84838257834) | [38s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039923) | [38s](https://github.com/iree-org/iree/actions/runs/28611002189/job/84845039923) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 227 | 8% (19/227) |  | 6h09m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 183 | 2% (3/183) |  | 6h18m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 258 | 3% (7/258) |  | 6h20m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 205 | 1% (3/205) |  | 6h29m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 59 | 2% (1/59) |  | 6h42m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
