# iree-ci-monitor

_Updated: 2026-09-06 21:48 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [45m43s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350828) | [1h03m](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350943) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [56m34s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350837) | [56m34s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350837) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [37m46s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350801) | [37m46s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350801) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [5m56s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350890) | [22m48s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350853) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [21m57s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350962) | [21m57s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350962) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [17m31s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350766) | [17m31s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350766) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [4m01s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350902) | [13m43s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350898) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [11m28s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350814) | [11m28s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350814) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [9m43s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350817) | [9m43s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350817) | 0% (0/1) | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [1m21s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350808) | [7m56s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350899) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [24s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350822) | [24s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350822) | 0% (0/1) | `shark10-ci` |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126721) | [8s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101545129578) | 0% (0/6) | 6 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126666) | [7s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126662) | 0% (0/3) | 3 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126611) | [5s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126689) | 0% (0/3) | 3 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126606) | [4s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126632) | 0% (0/3) | 3 |
| `ubuntu-24.04` | github-hosted | 22 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350769) | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101623366660) | 9% (2/22) | 22 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34054950863/job/101545107657) | [2s](https://github.com/iree-org/iree/actions/runs/34054950863/job/101545107699) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126841) | [1s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126841) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [1h03m](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350943) | [1h03m](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350943) | [1h03m](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350943) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [56m34s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350837) | [56m34s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350837) | [56m34s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350837) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [45m43s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350828) | [45m43s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350828) | [45m43s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350828) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [37m46s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350801) | [37m46s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350801) | [37m46s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350801) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [22m48s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350853) | [22m48s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350853) | [22m48s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350853) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [21m57s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350962) | [21m57s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350962) | [21m57s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350962) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [17m31s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350766) | [17m31s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350766) | [17m31s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350766) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [13m43s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350898) | [13m43s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350898) | [13m43s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350898) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [11m28s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350814) | [11m28s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350814) | [11m28s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350814) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [9m43s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350817) | [9m43s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350817) | [9m43s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350817) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [7m56s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350899) | [7m56s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350899) | [7m56s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350899) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [5m56s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350890) | [5m56s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350890) | [5m56s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350890) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [4m01s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350902) | [4m01s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350902) | [4m01s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350902) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [1m21s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350808) | [1m21s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350808) | [1m21s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350808) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [24s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350822) | [24s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350822) | [24s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101546350822) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126656) | [8s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126656) | [8s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126656) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126746) | [8s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126746) | [8s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126746) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126766) | [8s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126766) | [8s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126766) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126721) | [8s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126721) | [8s](https://github.com/iree-org/iree/actions/runs/34054951144/job/101545126721) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101545129578) | [8s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101545129578) | [8s](https://github.com/iree-org/iree/actions/runs/34054951336/job/101545129578) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 129 | 2% (2/129) |  | 8h01m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 86 | 0% (0/86) |  | 8h38m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 107 | 5% (5/107) |  | 8h44m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 97 | 0% (0/97) |  | 8h46m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h03m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
