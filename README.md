# iree-ci-monitor

_Updated: 2026-08-24 18:54 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405189) | [23m45s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607515196) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [9m36s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405322) | [16m27s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607515238) | — | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [9m20s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514796) | [15m09s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405276) | — | `shark01-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [6m53s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365547) | [13m37s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405312) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [9m03s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514822) | [13m04s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405282) | — | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [5m22s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405307) | [12m57s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514954) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [4m05s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514775) | [11m13s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405262) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [3m14s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365359) | [9m04s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405205) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [5m41s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405265) | [8m32s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514828) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405225) | [8m06s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514833) | — | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514906) | [7m32s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365608) | — | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 25 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/32750234454/job/97505618023) | [20s](https://github.com/iree-org/iree/actions/runs/32781647408/job/97604871433) | — | 24 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/32749822444/job/97504604167) | [5s](https://github.com/iree-org/iree/actions/runs/32750234454/job/97505617684) | — | 15 |
| `ubuntu-24.04` | github-hosted | 86 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/32749221461/job/97501922786) | [3s](https://github.com/iree-org/iree/actions/runs/32781647408/job/97604871324) | — | 84 |
| `windows-2022` | github-hosted | 15 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/32749822444/job/97504604172) | [3s](https://github.com/iree-org/iree/actions/runs/32781647408/job/97604871170) | — | 15 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32781647408/job/97604871319) | [3s](https://github.com/iree-org/iree/actions/runs/32749822444/job/97504604328) | — | 15 |
| `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/32781005101/job/97602849649) | [3s](https://github.com/iree-org/iree/actions/runs/32781005101/job/97602849649) | 0% (0/1) | 1 |
| `azure-windows-scale` | ossci | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32750234454/job/97505618079) | [2s](https://github.com/iree-org/iree/actions/runs/32781647408/job/97604871358) | — | 5 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405189) | [23m45s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607515196) | [23m45s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607515196) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [12m05s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405317) | [16m27s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607515238) | [16m27s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607515238) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [9m20s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514796) | [15m09s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405276) | [15m09s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405276) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [6m53s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365547) | [13m37s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405312) | [13m37s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405312) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [9m36s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405322) | [13m32s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607515074) | [13m32s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607515074) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [7m25s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405381) | [13m07s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607515101) | [13m07s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607515101) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [9m03s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514822) | [13m04s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405282) | [13m04s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405282) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [7m09s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365536) | [12m57s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514954) | [12m57s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514954) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [4m05s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514775) | [11m13s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405262) | [11m13s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405262) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [3m14s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365359) | [9m04s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405205) | [9m04s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405205) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [5m41s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405265) | [8m32s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514828) | [8m32s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514828) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [4m04s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365500) | [8m06s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514833) | [8m06s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514833) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514906) | [7m32s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365608) | [7m32s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365608) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [5m22s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405307) | [6m13s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365633) | [6m13s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97509365633) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 5 | 0 | — | — | [20s](https://github.com/iree-org/iree/actions/runs/32781647408/job/97604871433) | [1m27s](https://github.com/iree-org/iree/actions/runs/32749822444/job/97504604292) | [1m27s](https://github.com/iree-org/iree/actions/runs/32749822444/job/97504604292) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 5 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/32750234454/job/97505618023) | [17s](https://github.com/iree-org/iree/actions/runs/32781647408/job/97604871447) | [17s](https://github.com/iree-org/iree/actions/runs/32781647408/job/97604871447) | 5 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 5 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/32750234454/job/97505618033) | [13s](https://github.com/iree-org/iree/actions/runs/32781647408/job/97604871284) | [13s](https://github.com/iree-org/iree/actions/runs/32781647408/job/97604871284) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 5 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/32750234454/job/97505617989) | [13s](https://github.com/iree-org/iree/actions/runs/32781647408/job/97604871336) | [13s](https://github.com/iree-org/iree/actions/runs/32781647408/job/97604871336) | 5 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 5 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/32750234352/job/97505561972) | [8s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97520043612) | [8s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97520043612) | 5 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32754875614/job/97523405251) | [7s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514898) | [7s](https://github.com/iree-org/iree/actions/runs/32781647371/job/97607514898) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 220 | 1% (3/219) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 211 | 2% (5/210) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 158 | 0% (0/157) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 151 | 0% (0/150) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
