# iree-ci-monitor

_Updated: 2026-06-22 12:29 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [13m43s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756223023) | [16m38s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317572) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [7m12s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222566) | [13m47s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317123) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [8m51s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317372) | [11m25s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222946) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222937) | [10m13s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317371) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317517) | [10m10s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222903) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317200) | [9m39s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222604) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [1m08s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317450) | [9m03s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222561) | — | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [1m52s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222804) | [5m31s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317683) | — | `shark10-ci`, `shark75-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222979) | [4m27s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317580) | — | 8 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222850) | [4m23s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317513) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [2m02s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317519) | [3m29s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317530) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [1m37s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222932) | [2m25s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222969) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m33s](https://github.com/iree-org/iree/actions/runs/27948417324/job/82698931820) | [1m33s](https://github.com/iree-org/iree/actions/runs/27948417324/job/82698931820) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 22 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82754532137) | [11s](https://github.com/iree-org/iree/actions/runs/27955992113/job/82724440708) | 50% (1/2) | 22 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/27964465756/job/82754527727) | [7s](https://github.com/iree-org/iree/actions/runs/27962454602/job/82747408981) | — | 12 |
| `windows-2022` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27962454602/job/82747408950) | [6s](https://github.com/iree-org/iree/actions/runs/27955992113/job/82724440482) | — | 12 |
| `macos-14` | github-hosted | 13 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27962454602/job/82747408943) | [4s](https://github.com/iree-org/iree/actions/runs/27962454602/job/82747409291) | 0% (0/1) | 13 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/27948381213/job/82698810283) | [4s](https://github.com/iree-org/iree/actions/runs/27948381213/job/82698810283) | 0% (0/1) | 1 |
| `ubuntu-24.04` | github-hosted | 71 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27964465047/job/82754473174) | [3s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756223139) | 40% (2/5) | 71 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27965042102/job/82756566406) | [3s](https://github.com/iree-org/iree/actions/runs/27965206117/job/82757075237) | — | 6 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27964465756/job/82754527900) | [2s](https://github.com/iree-org/iree/actions/runs/27962454602/job/82747409216) | — | 4 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222787) | [2s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317516) | — | `iree-mi308-1` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 3 | 3 | [10h02m](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202183) | 2026-06-22 12:28 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [10h02m](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202183) | 2026-06-22 12:28 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [4h16m](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317105) | 2026-06-22 12:28 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `add-gpu-ada-known-target` | pull_request |
| [3h46m](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756223051) | 2026-06-22 12:28 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `devtbi/tduf` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 3 | 3 | [10h02m](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202183) | 2026-06-22 12:28 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [12m12s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222926) | [16m38s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317572) | [16m38s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317572) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [7m12s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222566) | [13m47s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317123) | [13m47s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317123) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [6m56s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317561) | [13m43s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756223023) | [13m43s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756223023) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [8m51s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317372) | [11m25s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222946) | [11m25s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222946) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222937) | [10m13s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317371) | [10m13s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317371) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317517) | [10m10s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222903) | [10m10s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222903) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317200) | [9m39s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222604) | [9m39s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222604) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [1m08s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317450) | [9m03s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222561) | [9m03s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222561) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222883) | [5m31s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317683) | [5m31s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317683) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222664) | [4m27s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317580) | [4m27s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317580) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222850) | [4m23s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317513) | [4m23s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317513) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222887) | [3m29s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317530) | [3m29s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317530) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317476) | [2m25s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222969) | [2m25s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222969) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222488) | [2m24s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317187) | [2m24s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317187) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [1m27s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222890) | [2m02s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317519) | [2m02s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317519) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [1m36s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317603) | [1m52s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222804) | [1m52s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222804) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317464) | [1m37s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222932) | [1m37s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222932) | 2 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m33s](https://github.com/iree-org/iree/actions/runs/27948417324/job/82698931820) | [1m33s](https://github.com/iree-org/iree/actions/runs/27948417324/job/82698931820) | [1m33s](https://github.com/iree-org/iree/actions/runs/27948417324/job/82698931820) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222979) | [37s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317467) | [37s](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317467) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 172 | 0% (0/172) |  | 3h25m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 130 | 5% (7/130) |  | 3h32m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 138 | 0% (0/138) |  | 3h33m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 38 | 0% (0/38) |  | 3h36m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 119 | 0% (0/119) |  | 3h44m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 10h02m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
