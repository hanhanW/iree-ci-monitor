# iree-ci-monitor

_Updated: 2026-09-24 04:53 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [48m43s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567366031) | [48m43s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567366031) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [42m45s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365644) | [42m45s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365644) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365474) | [36m59s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365472) | — | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [24m13s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365508) | [32m23s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365430) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365515) | [24m30s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365742) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [18m34s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365557) | [18m34s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365557) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [8m58s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365699) | [15m13s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365563) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [11m16s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365399) | [11m16s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365399) | — | `shark75-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m33s](https://github.com/iree-org/iree/actions/runs/35981379841/job/107573832148) | [1m33s](https://github.com/iree-org/iree/actions/runs/35981379841/job/107573832148) | 100% (1/1) | 1 |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761571) | [9s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761540) | 50% (1/2) | 7 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 1 | [7s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761420) | [9s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761278) | — | 6 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/35959215944/job/107504009963) | [8s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761243) | — | 6 |
| `ubuntu-24.04` | github-hosted | 36 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365580) | [4s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761391) | 0% (0/4) | 36 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/35987786808/job/107594417406) | [3s](https://github.com/iree-org/iree/actions/runs/35987786808/job/107594417617) | — | 3 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761299) | [3s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761459) | — | 5 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761528) | [1s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761528) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 1 | 0 | — | — | [48m43s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567366031) | [48m43s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567366031) | [48m43s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567366031) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [42m45s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365644) | [42m45s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365644) | [42m45s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365644) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [36m59s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365472) | [36m59s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365472) | [36m59s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365472) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [32m23s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365430) | [32m23s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365430) | [32m23s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365430) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [24m30s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365742) | [24m30s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365742) | [24m30s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365742) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [24m13s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365508) | [24m13s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365508) | [24m13s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365508) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [18m34s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365557) | [18m34s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365557) | [18m34s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365557) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [15m13s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365563) | [15m13s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365563) | [15m13s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365563) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [11m16s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365399) | [11m16s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365399) | [11m16s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365399) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [8m58s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365699) | [8m58s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365699) | [8m58s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107567365699) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m33s](https://github.com/iree-org/iree/actions/runs/35981379841/job/107573832148) | [1m33s](https://github.com/iree-org/iree/actions/runs/35981379841/job/107573832148) | [1m33s](https://github.com/iree-org/iree/actions/runs/35981379841/job/107573832148) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [37s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107576560516) | [37s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107576560516) | [37s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107576560516) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761540) | [9s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761540) | [9s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761540) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761278) | [9s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761278) | [9s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761278) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107560763325) | [9s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107560763325) | [9s](https://github.com/iree-org/iree/actions/runs/35977303036/job/107560763325) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761571) | [8s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761571) | [8s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761571) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761592) | [8s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761592) | [8s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761592) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761243) | [8s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761243) | [8s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761243) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761397) | [8s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761397) | [8s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761397) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/35959215944/job/107504009846) | [7s](https://github.com/iree-org/iree/actions/runs/35959215944/job/107504009846) | [7s](https://github.com/iree-org/iree/actions/runs/35959215944/job/107504009846) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 350 | 1% (5/350) |  | 1h50m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 315 | 2% (7/315) |  | 2h14m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 75 | 0% (0/75) |  | 6d14h ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-w7900` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
