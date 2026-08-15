# iree-ci-monitor

_Updated: 2026-08-14 18:51 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559958) | [26m29s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215375) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [14m59s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560239) | [25m23s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215483) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [13m10s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560097) | [19m18s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215370) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [10m59s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560135) | [18m35s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215373) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [12m43s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215371) | [16m32s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215286) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215169) | [11m58s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559933) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [8m31s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215388) | [10m21s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560075) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215299) | [8m32s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560069) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559963) | [7m15s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215291) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215266) | [5m26s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559877) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215330) | [4m07s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559969) | 0% (0/1) | `shark55-ci` |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864153044) | [18s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864153020) | 0% (0/6) | 6 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152726) | [5s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152735) | 0% (0/3) | 3 |
| `ubuntu-24.04` | github-hosted | 29 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215290) | [4s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864094528) | 0% (0/18) | 29 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31830290551/job/94864098258) | [4s](https://github.com/iree-org/iree/actions/runs/31830290551/job/94864098106) | 0% (0/3) | 3 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152754) | [3s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152747) | 0% (0/3) | 3 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152774) | [2s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152852) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152986) | [2s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152986) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559958) | [26m29s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215375) | [26m29s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215375) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [14m59s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560239) | [25m23s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215483) | [25m23s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215483) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [13m10s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560097) | [19m18s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215370) | [19m18s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215370) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [10m59s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560135) | [18m35s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215373) | [18m35s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215373) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [5m44s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559992) | [16m32s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215286) | [16m32s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215286) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [4m58s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560096) | [13m13s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215309) | [13m13s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215309) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560105) | [12m43s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215371) | [12m43s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215371) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215169) | [11m58s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559933) | [11m58s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559933) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [8m31s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215388) | [10m21s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560075) | [10m21s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560075) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215299) | [8m32s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560069) | [8m32s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560069) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559963) | [7m15s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215291) | [7m15s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215291) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559983) | [6m31s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215423) | [6m31s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215423) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [5m05s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215396) | [6m00s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560053) | [6m00s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560053) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215266) | [5m26s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559877) | [5m26s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559877) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215330) | [4m07s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559969) | [4m07s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559969) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [18s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152885) | [18s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152885) | [18s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152885) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [18s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152999) | [18s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152999) | [18s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152999) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [18s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864153020) | [18s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864153020) | [18s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864153020) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152861) | [9s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152861) | [9s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152861) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864153044) | [9s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864153044) | [9s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864153044) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 203 | 0% (0/203) |  | 6h24m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 167 | 7% (12/167) |  | 6h24m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 167 | 4% (6/167) |  | 6h30m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 138 | 9% (12/138) |  | 6h30m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
