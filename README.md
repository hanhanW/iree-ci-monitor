# iree-ci-monitor

_Updated: 2026-05-16 11:38 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [24m53s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310640) | [36m51s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310656) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [16m54s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310545) | [16m54s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310545) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [6m45s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310652) | [15m05s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310626) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [12m35s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310619) | [14m33s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310648) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [8m56s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310553) | [8m56s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310553) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [7m57s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310614) | [7m57s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310614) | — | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310606) | [6m41s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310604) | — | `shark01-ci`, `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [4m17s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310616) | [4m17s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310616) | — | `shark10-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310636) | [14s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310655) | — | 4 |
| `azure-linux-scale` | ossci | 6 | 1 | [19m47s](https://github.com/iree-org/iree/actions/runs/25783793136/job/75732425036) | 2026-05-13 00:23 PDT | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907594) | [10s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907639) | — | 5 |
| `ubuntu-24.04` | github-hosted | 27 | 2 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310571) | [2s](https://github.com/iree-org/iree/actions/runs/25964362160/job/76325095743) | 0% (0/1) | 25 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907589) | [2s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907592) | — | 3 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907570) | [2s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907579) | — | 3 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25960962642/job/76316087809) | [2s](https://github.com/iree-org/iree/actions/runs/25964485647/job/76325429661) | — | 15 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907585) | [1s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907593) | — | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907636) | [1s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907636) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310593) | [1s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310593) | — | 1 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310599) | [1s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310599) | — | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310603) | [1s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310603) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310605) | [1s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310605) | — | `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310608) | [1s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310608) | — | `iree-mi308-1` |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | `users/keshavvinayak01/gpuvectoralloc-swizzle` | pull_request |
| [4h53m](https://github.com/iree-org/iree/actions/runs/25907295886/job/76143196900) | 2026-05-15 05:58 PDT | `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | `users/keshavvinayak01/gpuvectoralloc-swizzle` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | 2 | 1 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | [2s](https://github.com/iree-org/iree/actions/runs/25962023772/job/76318896979) | [2s](https://github.com/iree-org/iree/actions/runs/25962023772/job/76318896979) | [2s](https://github.com/iree-org/iree/actions/runs/25962023772/job/76318896979) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 2 | 1 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295886/job/76143196900) | 2026-05-15 05:58 PDT | [1s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907556) | [1s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907556) | [1s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907556) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [36m51s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310656) | [36m51s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310656) | [36m51s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310656) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [24m53s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310640) | [24m53s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310640) | [24m53s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310640) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 1 | [19m47s](https://github.com/iree-org/iree/actions/runs/25783793136/job/75732425036) | 2026-05-13 00:23 PDT | [10s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907639) | [10s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907639) | [10s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907639) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [16m54s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310545) | [16m54s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310545) | [16m54s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310545) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [15m05s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310626) | [15m05s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310626) | [15m05s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310626) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [14m33s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310648) | [14m33s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310648) | [14m33s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310648) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [12m35s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310619) | [12m35s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310619) | [12m35s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310619) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [8m56s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310553) | [8m56s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310553) | [8m56s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310553) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [7m57s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310614) | [7m57s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310614) | [7m57s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310614) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [6m45s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310652) | [6m45s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310652) | [6m45s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310652) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [6m41s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310604) | [6m41s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310604) | [6m41s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310604) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [4m17s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310616) | [4m17s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310616) | [4m17s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310616) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [14s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310655) | [14s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310655) | [14s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310655) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907594) | [9s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907594) | [9s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907594) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907601) | [9s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907601) | [9s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907601) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907578) | [7s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907578) | [7s](https://github.com/iree-org/iree/actions/runs/25962023792/job/76318907578) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310630) | [7s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310630) | [7s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310630) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310636) | [7s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310636) | [7s](https://github.com/iree-org/iree/actions/runs/25962023785/job/76319310636) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1147 | 3% (30/1145) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 1022 | 6% (66/1022) |  | 5h32m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark55-ci`, `self-hosted,persistent-cache,Linux,X64` | 887 | 1% (12/887) |  | 5h34m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark01-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 937 | 1% (14/937) |  | 5h35m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 311 | 2% (5/311) |  | 5h47m ago |

## Alerts

- **[stale-queued]** `ubuntu-24.04` oldest queued job observed waiting 4h53m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
