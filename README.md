# iree-ci-monitor

_Updated: 2026-06-29 18:19 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [12m11s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531068) | [12m11s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531068) | — | `shark01-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [11m16s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531086) | [11m16s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531086) | — | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [7m34s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531088) | [8m54s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531118) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [8m53s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531106) | [8m53s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531106) | — | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [3m40s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531087) | [7m28s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531136) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [1m43s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531045) | [7m05s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531101) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [4m56s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531099) | [4m56s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531099) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [3m45s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531069) | [3m45s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531069) | — | `shark10-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [1m06s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531154) | [2m01s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531052) | — | 4 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m20s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265100) | [1m20s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265100) | — | 1 |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265241) | [11s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265353) | — | 7 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265107) | [5s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265136) | — | 3 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [5s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265343) | [5s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265343) | — | 1 |
| `ubuntu-24.04` | github-hosted | 21 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531055) | [3s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165226545) | — | 21 |
| `macos-14` | github-hosted | 4 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265284) | [3s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265187) | — | 4 |
| `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28404603415/job/84164070978) | [3s](https://github.com/iree-org/iree/actions/runs/28404602848/job/84164069541) | 0% (0/2) | 2 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265150) | [2s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265198) | — | 3 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166530955) | [2s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166530955) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166530971) | [2s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166530971) | — | `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531061) | [2s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531061) | — | `iree-mi308-1` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531078) | [2s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531093) | — | `shark01-ci`, `shark55-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265434) | [1s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265434) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 1 | [17h25m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334980) | 2026-06-29 18:19 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [17h25m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334980) | 2026-06-29 18:19 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `implement-fpowi-in-vm` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 1 | 1 | [17h25m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334980) | 2026-06-29 18:19 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [12m11s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531068) | [12m11s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531068) | [12m11s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531068) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [11m16s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531086) | [11m16s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531086) | [11m16s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531086) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [8m54s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531118) | [8m54s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531118) | [8m54s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531118) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [8m53s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531106) | [8m53s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531106) | [8m53s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531106) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [7m34s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531088) | [7m34s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531088) | [7m34s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531088) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [7m28s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531136) | [7m28s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531136) | [7m28s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531136) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [7m05s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531101) | [7m05s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531101) | [7m05s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531101) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [4m56s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531099) | [4m56s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531099) | [4m56s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531099) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [3m45s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531069) | [3m45s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531069) | [3m45s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531069) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [3m40s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531087) | [3m40s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531087) | [3m40s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531087) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [2m01s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531052) | [2m01s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531052) | [2m01s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531052) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [1m43s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531045) | [1m43s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531045) | [1m43s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531045) | 1 |
| `.github/workflows/ci.yml` | linux_arm64_clang / linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m20s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265100) | [1m20s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265100) | [1m20s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265100) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [1m06s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531154) | [1m06s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531154) | [1m06s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531154) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [48s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531040) | [48s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531040) | [48s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531040) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265353) | [11s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265353) | [11s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265353) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265242) | [11s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265242) | [11s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265242) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_tsan / linux_x64_clang_tsan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265394) | [9s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265394) | [9s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265394) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265241) | [8s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265241) | [8s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265241) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 141 | 0% (0/141) |  | 3h06m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 182 | 0% (0/182) |  | 3h07m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 144 | 8% (11/144) |  | 3h08m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 140 | 0% (0/140) |  | 3h08m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 41 | 0% (0/41) |  | 3h11m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 17h25m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
