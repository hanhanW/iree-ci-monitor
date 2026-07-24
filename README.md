# iree-ci-monitor

_Updated: 2026-07-24 11:49 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 0 | — | — | 0 | [9m43s](https://github.com/iree-org/iree/actions/runs/30096642614/job/89494034466) | [40m25s](https://github.com/iree-org/iree/actions/runs/30093017605/job/89482091194) | — | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [12m17s](https://github.com/iree-org/iree/actions/runs/30086302425/job/89460647389) | [30m28s](https://github.com/iree-org/iree/actions/runs/30096642614/job/89494034467) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [14m05s](https://github.com/iree-org/iree/actions/runs/30096642614/job/89494034521) | [24m19s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934610) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934168) | [23m27s](https://github.com/iree-org/iree/actions/runs/30097109448/job/89503379956) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [11m40s](https://github.com/iree-org/iree/actions/runs/30083299966/job/89453355393) | [20m37s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934620) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [5m49s](https://github.com/iree-org/iree/actions/runs/30083299966/job/89453355382) | [17m14s](https://github.com/iree-org/iree/actions/runs/30086302425/job/89460647378) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30096642614/job/89494034390) | [17m05s](https://github.com/iree-org/iree/actions/runs/30093017605/job/89482091250) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [10m08s](https://github.com/iree-org/iree/actions/runs/30097109448/job/89503380221) | [16m58s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934624) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [8m06s](https://github.com/iree-org/iree/actions/runs/30097109448/job/89503380065) | [16m05s](https://github.com/iree-org/iree/actions/runs/30086302425/job/89460647232) | — | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [10m53s](https://github.com/iree-org/iree/actions/runs/30086302425/job/89460647396) | [14m46s](https://github.com/iree-org/iree/actions/runs/30096642614/job/89494034383) | — | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30093017605/job/89482091047) | [6m21s](https://github.com/iree-org/iree/actions/runs/30083299966/job/89453355352) | — | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 32 | 0 | — | — | 0 | [14s](https://github.com/iree-org/iree/actions/runs/30097109499/job/89501580686) | [2m20s](https://github.com/iree-org/iree/actions/runs/30097109499/job/89501580693) | 0% (0/2) | 32 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m28s](https://github.com/iree-org/iree/actions/runs/30084578270/job/89453659444) | [1m28s](https://github.com/iree-org/iree/actions/runs/30084578270/job/89453659444) | 0% (0/1) | 1 |
| `macos-14` | github-hosted | 19 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30093017654/job/89480404666) | [25s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376846) | 0% (0/1) | 19 |
| `windows-2022` | github-hosted | 18 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30097109499/job/89501580676) | [5s](https://github.com/iree-org/iree/actions/runs/30096642569/job/89492270413) | — | 18 |
| `ubuntu-24.04` | github-hosted | 167 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30097109448/job/89503380079) | [3s](https://github.com/iree-org/iree/actions/runs/30106791136/job/89526053191) | 33% (1/3) | 151 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30096642569/job/89492270370) | [3s](https://github.com/iree-org/iree/actions/runs/30097109499/job/89501580621) | — | 18 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30091088506/job/89474319453) | [3s](https://github.com/iree-org/iree/actions/runs/30091088506/job/89474319375) | — | 15 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30084571541/job/89453637149) | [3s](https://github.com/iree-org/iree/actions/runs/30084571541/job/89453637149) | 0% (0/1) | 1 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30093017654/job/89480404794) | [2s](https://github.com/iree-org/iree/actions/runs/30097109499/job/89501580855) | — | 6 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30086302425/job/89460647261) | [2s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934342) | — | 6 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30086302425/job/89460647224) | [2s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934419) | — | `iree-mi308-1` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 6 | 0 | — | — | [9m43s](https://github.com/iree-org/iree/actions/runs/30096642614/job/89494034466) | [40m25s](https://github.com/iree-org/iree/actions/runs/30093017605/job/89482091194) | [40m25s](https://github.com/iree-org/iree/actions/runs/30093017605/job/89482091194) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [12m17s](https://github.com/iree-org/iree/actions/runs/30086302425/job/89460647389) | [30m28s](https://github.com/iree-org/iree/actions/runs/30096642614/job/89494034467) | [30m28s](https://github.com/iree-org/iree/actions/runs/30096642614/job/89494034467) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [14m05s](https://github.com/iree-org/iree/actions/runs/30096642614/job/89494034521) | [24m38s](https://github.com/iree-org/iree/actions/runs/30083299966/job/89453355228) | [24m38s](https://github.com/iree-org/iree/actions/runs/30083299966/job/89453355228) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934168) | [23m27s](https://github.com/iree-org/iree/actions/runs/30097109448/job/89503379956) | [23m27s](https://github.com/iree-org/iree/actions/runs/30097109448/job/89503379956) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [15m52s](https://github.com/iree-org/iree/actions/runs/30097109448/job/89503380137) | [22m05s](https://github.com/iree-org/iree/actions/runs/30086302425/job/89460647381) | [22m05s](https://github.com/iree-org/iree/actions/runs/30086302425/job/89460647381) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [5m31s](https://github.com/iree-org/iree/actions/runs/30086302425/job/89460647445) | [20m02s](https://github.com/iree-org/iree/actions/runs/30097109448/job/89503380136) | [20m02s](https://github.com/iree-org/iree/actions/runs/30097109448/job/89503380136) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [5m40s](https://github.com/iree-org/iree/actions/runs/30097109448/job/89503380143) | [19m03s](https://github.com/iree-org/iree/actions/runs/30096642614/job/89494034583) | [19m03s](https://github.com/iree-org/iree/actions/runs/30096642614/job/89494034583) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [5m49s](https://github.com/iree-org/iree/actions/runs/30083299966/job/89453355382) | [17m14s](https://github.com/iree-org/iree/actions/runs/30086302425/job/89460647378) | [17m14s](https://github.com/iree-org/iree/actions/runs/30086302425/job/89460647378) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [14m31s](https://github.com/iree-org/iree/actions/runs/30096642614/job/89494034516) | [17m14s](https://github.com/iree-org/iree/actions/runs/30093017605/job/89482091290) | [17m14s](https://github.com/iree-org/iree/actions/runs/30093017605/job/89482091290) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [10m53s](https://github.com/iree-org/iree/actions/runs/30086302425/job/89460647396) | [17m06s](https://github.com/iree-org/iree/actions/runs/30097109448/job/89503380148) | [17m06s](https://github.com/iree-org/iree/actions/runs/30097109448/job/89503380148) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30096642614/job/89494034390) | [17m05s](https://github.com/iree-org/iree/actions/runs/30093017605/job/89482091250) | [17m05s](https://github.com/iree-org/iree/actions/runs/30093017605/job/89482091250) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 6 | 0 | — | — | [8m06s](https://github.com/iree-org/iree/actions/runs/30097109448/job/89503380065) | [16m05s](https://github.com/iree-org/iree/actions/runs/30086302425/job/89460647232) | [16m05s](https://github.com/iree-org/iree/actions/runs/30086302425/job/89460647232) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [6m36s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934360) | [14m46s](https://github.com/iree-org/iree/actions/runs/30096642614/job/89494034383) | [14m46s](https://github.com/iree-org/iree/actions/runs/30096642614/job/89494034383) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30096642614/job/89494034511) | [13m40s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934618) | [13m40s](https://github.com/iree-org/iree/actions/runs/30106875997/job/89527934618) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30093017605/job/89482091047) | [6m21s](https://github.com/iree-org/iree/actions/runs/30083299966/job/89453355352) | [6m21s](https://github.com/iree-org/iree/actions/runs/30083299966/job/89453355352) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 6 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/30097109499/job/89501580466) | [4m01s](https://github.com/iree-org/iree/actions/runs/30083300036/job/89449904892) | [4m01s](https://github.com/iree-org/iree/actions/runs/30083300036/job/89449904892) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 6 | 0 | — | — | [14s](https://github.com/iree-org/iree/actions/runs/30097109499/job/89501580686) | [3m48s](https://github.com/iree-org/iree/actions/runs/30083300036/job/89449904931) | [3m48s](https://github.com/iree-org/iree/actions/runs/30083300036/job/89449904931) | 6 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 6 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/30086302427/job/89459212111) | [2m20s](https://github.com/iree-org/iree/actions/runs/30097109499/job/89501580693) | [2m20s](https://github.com/iree-org/iree/actions/runs/30097109499/job/89501580693) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30106876000/job/89526376826) | [1m44s](https://github.com/iree-org/iree/actions/runs/30086302427/job/89459211993) | [1m44s](https://github.com/iree-org/iree/actions/runs/30086302427/job/89459211993) | 6 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | 1 | 0 | — | — | [1m41s](https://github.com/iree-org/iree/actions/runs/30084576846/job/89453655012) | [1m41s](https://github.com/iree-org/iree/actions/runs/30084576846/job/89453655012) | [1m41s](https://github.com/iree-org/iree/actions/runs/30084576846/job/89453655012) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 300 | 1% (3/300) |  | 2h25m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 409 | 1% (5/409) |  | 2h27m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 335 | 5% (16/335) |  | 2h28m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 313 | 1% (3/313) |  | 2h29m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 94 | 1% (1/94) |  | 2h42m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
