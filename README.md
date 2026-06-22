# iree-ci-monitor

_Updated: 2026-06-22 07:13 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [40m49s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202389) | [40m49s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202389) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [30m56s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202356) | [30m56s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202356) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [13m37s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202431) | [25m44s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202464) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [20m16s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202292) | [20m16s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202292) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [13m51s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202257) | [13m51s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202257) | 0% (0/1) | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [7m38s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202321) | [11m33s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202319) | 50% (1/2) | `shark10-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [7m08s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202515) | [10m35s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202509) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202411) | [6m16s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202410) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m33s](https://github.com/iree-org/iree/actions/runs/27948417324/job/82698931820) | [1m33s](https://github.com/iree-org/iree/actions/runs/27948417324/job/82698931820) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 11 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418405) | [1m03s](https://github.com/iree-org/iree/actions/runs/27942341465/job/82678542242) | 0% (0/3) | 11 |
| `azure-linux-scale` | ossci | 18 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/27956365787/job/82726121462) | [1m03s](https://github.com/iree-org/iree/actions/runs/27942341465/job/82678542248) | 12% (1/8) | 18 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202478) | [11s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202198) | 0% (0/4) | 4 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/27955992113/job/82724440505) | [6s](https://github.com/iree-org/iree/actions/runs/27956365787/job/82726121313) | 0% (0/3) | 12 |
| `macos-14` | github-hosted | 12 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/27955992113/job/82724440511) | [4s](https://github.com/iree-org/iree/actions/runs/27948388130/job/82698832213) | 0% (0/3) | 12 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/27948381213/job/82698810283) | [4s](https://github.com/iree-org/iree/actions/runs/27948381213/job/82698810283) | — | 1 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202323) | [4s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202323) | 0% (0/1) | `iree-mi308-1` |
| `ubuntu-24.04` | github-hosted | 54 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27955992113/job/82724398010) | [3s](https://github.com/iree-org/iree/actions/runs/27956366138/job/82726915249) | 14% (3/22) | 54 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202108) | [2s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202108) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202158) | [2s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202158) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202359) | [2s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202359) | 0% (0/1) | `shark01-ci` |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27942338052/job/82678505735) | [2s](https://github.com/iree-org/iree/actions/runs/27942338052/job/82678505783) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27955992113/job/82724440693) | [1s](https://github.com/iree-org/iree/actions/runs/27956365787/job/82726121701) | 0% (0/1) | 3 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 1 | [4h47m](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202183) | 2026-06-22 07:13 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [4h47m](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202183) | 2026-06-22 07:13 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 1 | 1 | [4h47m](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202183) | 2026-06-22 07:13 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [40m49s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202389) | [40m49s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202389) | [40m49s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202389) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [30m56s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202356) | [30m56s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202356) | [30m56s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202356) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [25m44s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202464) | [25m44s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202464) | [25m44s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202464) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [20m16s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202292) | [20m16s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202292) | [20m16s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202292) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [13m51s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202257) | [13m51s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202257) | [13m51s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202257) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [13m37s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202431) | [13m37s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202431) | [13m37s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202431) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [11m33s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202319) | [11m33s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202319) | [11m33s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202319) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [10m35s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202509) | [10m35s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202509) | [10m35s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202509) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [7m38s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202321) | [7m38s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202321) | [7m38s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202321) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [7m08s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202515) | [7m08s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202515) | [7m08s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202515) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [6m16s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202410) | [6m16s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202410) | [6m16s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202410) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m33s](https://github.com/iree-org/iree/actions/runs/27948417324/job/82698931820) | [1m33s](https://github.com/iree-org/iree/actions/runs/27948417324/job/82698931820) | [1m33s](https://github.com/iree-org/iree/actions/runs/27948417324/job/82698931820) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 3 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27956365787/job/82726122516) | [1m11s](https://github.com/iree-org/iree/actions/runs/27942341465/job/82678542215) | [1m11s](https://github.com/iree-org/iree/actions/runs/27942341465/job/82678542215) | 3 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 3 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27955992296/job/82724456077) | [1m11s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82678552417) | [1m11s](https://github.com/iree-org/iree/actions/runs/27942341280/job/82678552417) | 3 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 3 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/27955992113/job/82724440482) | [1m03s](https://github.com/iree-org/iree/actions/runs/27942341465/job/82678542242) | [1m03s](https://github.com/iree-org/iree/actions/runs/27942341465/job/82678542242) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [1m03s](https://github.com/iree-org/iree/actions/runs/27942341465/job/82678542248) | [1m03s](https://github.com/iree-org/iree/actions/runs/27942341465/job/82678542248) | [1m03s](https://github.com/iree-org/iree/actions/runs/27942341465/job/82678542248) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27956365787/job/82726121744) | [47s](https://github.com/iree-org/iree/actions/runs/27942341465/job/82678542234) | [47s](https://github.com/iree-org/iree/actions/runs/27942341465/job/82678542234) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27956365787/job/82726121370) | [47s](https://github.com/iree-org/iree/actions/runs/27942341465/job/82678542199) | [47s](https://github.com/iree-org/iree/actions/runs/27942341465/job/82678542199) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 3 | 0 | — | — | [26s](https://github.com/iree-org/iree/actions/runs/27956365787/job/82726121434) | [37s](https://github.com/iree-org/iree/actions/runs/27942341465/job/82678542275) | [37s](https://github.com/iree-org/iree/actions/runs/27942341465/job/82678542275) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 122 | 6% (7/122) |  | 4h04m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 161 | 0% (0/161) |  | 4h09m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 115 | 0% (0/115) |  | 4h21m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 131 | 0% (0/131) |  | 4h27m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 36 | 0% (0/36) |  | 4h37m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 4h47m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
