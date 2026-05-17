# iree-ci-monitor

_Updated: 2026-05-17 00:17 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [8m02s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815156) | [26m49s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815137) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [14m27s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815118) | [24m53s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815129) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [20m04s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815110) | [20m04s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815110) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [17m49s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815105) | [17m49s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815105) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [6m27s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815128) | [16m11s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815114) | — | `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [11m27s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815097) | [11m27s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815097) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815099) | [7m07s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815119) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [6m48s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815132) | [6m48s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815132) | — | `shark01-ci` |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [24s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345405) | [2m57s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357347155) | — | 5 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [18s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815127) | [21s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815126) | — | 4 |
| `ubuntu-24.04` | github-hosted | 28 | 2 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815131) | [3s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345330) | 0% (0/1) | 26 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498084) | [3s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345352) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345385) | [3s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498086) | — | 6 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815034) | [2s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815034) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815048) | [2s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815048) | — | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815086) | [2s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815086) | — | `shark01-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815103) | [2s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815103) | — | `iree-mi308-1` |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345383) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498100) | — | 5 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815074) | [1s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815074) | — | 1 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345420) | [1s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345420) | — | 1 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | `users/keshavvinayak01/gpuvectoralloc-swizzle` | pull_request |
| [4h53m](https://github.com/iree-org/iree/actions/runs/25907295886/job/76143196900) | 2026-05-15 05:58 PDT | `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | `users/keshavvinayak01/gpuvectoralloc-swizzle` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | 2 | 1 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | [2s](https://github.com/iree-org/iree/actions/runs/25976457430/job/76357336235) | [2s](https://github.com/iree-org/iree/actions/runs/25976457430/job/76357336235) | [2s](https://github.com/iree-org/iree/actions/runs/25976457430/job/76357336235) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 2 | 1 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295886/job/76143196900) | 2026-05-15 05:58 PDT | [2s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345361) | [2s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345361) | [2s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345361) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [26m49s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815137) | [26m49s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815137) | [26m49s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815137) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [24m53s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815129) | [24m53s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815129) | [24m53s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815129) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [20m04s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815110) | [20m04s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815110) | [20m04s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815110) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [17m49s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815105) | [17m49s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815105) | [17m49s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815105) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [16m11s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815114) | [16m11s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815114) | [16m11s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815114) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [14m27s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815118) | [14m27s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815118) | [14m27s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815118) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [11m27s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815097) | [11m27s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815097) | [11m27s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815097) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [8m02s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815156) | [8m02s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815156) | [8m02s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815156) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [7m07s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815119) | [7m07s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815119) | [7m07s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815119) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [6m48s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815132) | [6m48s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815132) | [6m48s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815132) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [6m27s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815128) | [6m27s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815128) | [6m27s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815128) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [2m57s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357347155) | [2m57s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357347155) | [2m57s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357347155) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [2m04s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345426) | [2m04s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345426) | [2m04s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345426) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [24s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345405) | [24s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345405) | [24s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345405) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [22s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345411) | [22s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345411) | [22s](https://github.com/iree-org/iree/actions/runs/25976457438/job/76357345411) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [21s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815126) | [21s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815126) | [21s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815126) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [18s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815127) | [18s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815127) | [18s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815127) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815124) | [9s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815124) | [9s](https://github.com/iree-org/iree/actions/runs/25976457437/job/76357815124) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1099 | 2% (22/1097) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark55-ci`, `self-hosted,persistent-cache,Linux,X64` | 859 | 1% (11/859) |  | 6h31m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 977 | 6% (56/977) |  | 6h34m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark01-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 895 | 1% (11/895) |  | 6h36m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 300 | 2% (5/300) |  | 6h51m ago |

## Alerts

- **[stale-queued]** `ubuntu-24.04` oldest queued job observed waiting 4h53m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
