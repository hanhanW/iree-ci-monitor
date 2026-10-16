# iree-ci-monitor

_Updated: 2026-10-15 21:37 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071593) | [31m04s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071623) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [16m07s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071426) | [24m03s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071649) | 0% (0/2) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [8m32s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071355) | [23m16s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071401) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [16m42s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071289) | [16m42s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071289) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [12m43s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071551) | [12m43s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071551) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [12m15s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071413) | [12m15s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071413) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071500) | [7m55s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071594) | 0% (0/2) | `shark55-ci` |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353053) | [13s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353264) | 0% (0/7) | 7 |
| `macos-15` | github-hosted | 3 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352897) | [7s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352706) | 0% (0/3) | 3 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352717) | [4s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353041) | 0% (0/3) | 3 |
| `ubuntu-24.04` | github-hosted | 23 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071503) | [3s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071624) | 9% (2/23) | 23 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38819488149/job/116712364504) | [2s](https://github.com/iree-org/iree/actions/runs/38819488453/job/116712293878) | 0% (0/3) | 9 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352722) | [2s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352764) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353114) | [1s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353114) | 0% (0/1) | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [31m04s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071623) | [31m04s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071623) | [31m04s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071623) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [24m03s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071649) | [24m03s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071649) | [24m03s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071649) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [23m16s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071401) | [23m16s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071401) | [23m16s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071401) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [16m42s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071289) | [16m42s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071289) | [16m42s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071289) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [16m07s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071426) | [16m07s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071426) | [16m07s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071426) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [12m43s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071551) | [12m43s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071551) | [12m43s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071551) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [12m15s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071413) | [12m15s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071413) | [12m15s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071413) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [8m32s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071355) | [8m32s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071355) | [8m32s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071355) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [7m55s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071594) | [7m55s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071594) | [7m55s](https://github.com/iree-org/iree/actions/runs/38818878069/job/116713071594) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [13s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353264) | [13s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353264) | [13s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353264) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353246) | [9s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353246) | [9s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353246) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353059) | [9s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353059) | [9s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353059) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353053) | [8s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353053) | [8s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353053) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352778) | [8s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352778) | [8s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352778) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352972) | [8s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352972) | [8s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352972) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352706) | [7s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352706) | [7s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352706) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352897) | [6s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352897) | [6s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352897) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352820) | [6s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352820) | [6s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352820) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352667) | [4s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352667) | [4s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710352667) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353041) | [4s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353041) | [4s](https://github.com/iree-org/iree/actions/runs/38818878026/job/116710353041) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 243 | 1% (2/243) |  | 5h11m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 303 | 6% (18/303) |  | 5h19m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
