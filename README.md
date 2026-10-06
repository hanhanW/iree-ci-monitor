# iree-ci-monitor

_Updated: 2026-10-05 17:07 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [29m33s](https://github.com/iree-org/iree/actions/runs/37355026459/job/111919594619) | [2h01m](https://github.com/iree-org/iree/actions/runs/37326868500/job/111824697495) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 10 | 0 | — | — | 0 | [14m33s](https://github.com/iree-org/iree/actions/runs/37355026459/job/111919594946) | [1h41m](https://github.com/iree-org/iree/actions/runs/37326868500/job/111824697292) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 10 | 0 | — | — | 0 | [26m42s](https://github.com/iree-org/iree/actions/runs/37355020777/job/111918218209) | [1h29m](https://github.com/iree-org/iree/actions/runs/37326868500/job/111824697301) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 5 | 0 | — | — | 0 | [7m55s](https://github.com/iree-org/iree/actions/runs/37324856991/job/111817608729) | [41m57s](https://github.com/iree-org/iree/actions/runs/37355026459/job/111919594878) | 0% (0/1) | `shark75-ci` |
| `azure-linux-scale` | ossci | 31 | 0 | — | — | 0 | [16s](https://github.com/iree-org/iree/actions/runs/37355020778/job/111915338341) | [22m13s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915480190) | 0% (0/7) | 31 |
| `windows-2022` | github-hosted | 15 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342380) | [1m58s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915479350) | 0% (0/3) | 15 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/37324857078/job/111812977388) | [1m41s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915479398) | 0% (0/3) | 15 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/37355020778/job/111915337788) | [1m28s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915479272) | 0% (0/3) | 15 |
| `ubuntu-24.04` | github-hosted | 101 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/37324857078/job/111812869190) | [38s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915150398) | 0% (0/19) | 99 |
| `ubuntu-latest` | github-hosted | 22 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37355923175/job/111918181140) | [4s](https://github.com/iree-org/iree/actions/runs/37355921959/job/111918261364) | 0% (0/4) | 22 |
| `azure-windows-scale` | ossci | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37326868145/job/111819844938) | [3s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342826) | 0% (0/1) | 5 |
| `Linux,X64,gfx1100` | self-hosted | 28 | 28 | [14h04m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518868) | 2026-10-05 17:06 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 28 | 28 | [14h04m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518900) | 2026-10-05 17:06 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 14 | 14 | [14h04m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518866) | 2026-10-05 17:06 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 14 | 14 | [14h04m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518852) | 2026-10-05 17:06 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 5 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [14h04m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518852) | 2026-10-05 17:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/jschuhmacher/strict-properties` | pull_request |
| [14h04m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518866) | 2026-10-05 17:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/jschuhmacher/strict-properties` | pull_request |
| [14h04m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518868) | 2026-10-05 17:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/jschuhmacher/strict-properties` | pull_request |
| [14h04m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518900) | 2026-10-05 17:06 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/jschuhmacher/strict-properties` | pull_request |
| [14h04m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518960) | 2026-10-05 17:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/jschuhmacher/strict-properties` | pull_request |
| [14h04m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710519011) | 2026-10-05 17:06 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/jschuhmacher/strict-properties` | pull_request |
| [13h42m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070934) | 2026-10-05 17:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `bump-version-3.13` | pull_request |
| [13h42m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070942) | 2026-10-05 17:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `bump-version-3.13` | pull_request |
| [13h42m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070964) | 2026-10-05 17:06 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `bump-version-3.13` | pull_request |
| [13h42m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070975) | 2026-10-05 17:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `bump-version-3.13` | pull_request |
| [13h42m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718071039) | 2026-10-05 17:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `bump-version-3.13` | pull_request |
| [13h42m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718071090) | 2026-10-05 17:06 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `bump-version-3.13` | pull_request |
| [12h32m](https://github.com/iree-org/iree/actions/runs/37302785332/job/111742224798) | 2026-10-05 17:06 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [12h32m](https://github.com/iree-org/iree/actions/runs/37302785332/job/111742224938) | 2026-10-05 17:06 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [12h32m](https://github.com/iree-org/iree/actions/runs/37302785332/job/111742224953) | 2026-10-05 17:06 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 14 | 14 | [14h04m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518866) | 2026-10-05 17:06 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 14 | 14 | [14h04m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518852) | 2026-10-05 17:06 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 14 | 14 | [14h04m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518868) | 2026-10-05 17:06 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 14 | 14 | [14h04m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518960) | 2026-10-05 17:06 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 14 | 14 | [14h04m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710519011) | 2026-10-05 17:06 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 14 | 14 | [14h04m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518900) | 2026-10-05 17:06 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 5 | 0 | — | — | [29m33s](https://github.com/iree-org/iree/actions/runs/37355026459/job/111919594619) | [2h01m](https://github.com/iree-org/iree/actions/runs/37326868500/job/111824697495) | [2h01m](https://github.com/iree-org/iree/actions/runs/37326868500/job/111824697495) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [14m33s](https://github.com/iree-org/iree/actions/runs/37355026459/job/111919594946) | [1h41m](https://github.com/iree-org/iree/actions/runs/37326868500/job/111824697292) | [1h41m](https://github.com/iree-org/iree/actions/runs/37326868500/job/111824697292) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [34m22s](https://github.com/iree-org/iree/actions/runs/37355026459/job/111919595013) | [1h29m](https://github.com/iree-org/iree/actions/runs/37326868500/job/111824697301) | [1h29m](https://github.com/iree-org/iree/actions/runs/37326868500/job/111824697301) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [26m42s](https://github.com/iree-org/iree/actions/runs/37355020777/job/111918218209) | [1h23m](https://github.com/iree-org/iree/actions/runs/37326868500/job/111824697364) | [1h23m](https://github.com/iree-org/iree/actions/runs/37326868500/job/111824697364) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [16m05s](https://github.com/iree-org/iree/actions/runs/37355026459/job/111919594703) | [1h07m](https://github.com/iree-org/iree/actions/runs/37326868500/job/111824697438) | [1h07m](https://github.com/iree-org/iree/actions/runs/37326868500/job/111824697438) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 5 | 0 | — | — | [7m55s](https://github.com/iree-org/iree/actions/runs/37324856991/job/111817608729) | [41m57s](https://github.com/iree-org/iree/actions/runs/37355026459/job/111919594878) | [41m57s](https://github.com/iree-org/iree/actions/runs/37355026459/job/111919594878) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 5 | 0 | — | — | [1m32s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342841) | [25m45s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915480122) | [25m45s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915480122) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 5 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37355020778/job/111915337994) | [22m17s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915479989) | [22m17s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915479989) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 5 | 0 | — | — | [16s](https://github.com/iree-org/iree/actions/runs/37355020778/job/111915338341) | [22m13s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915480190) | [22m13s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915480190) | 5 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 5 | 0 | — | — | [25s](https://github.com/iree-org/iree/actions/runs/37355020778/job/111915338208) | [21m47s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915480020) | [21m47s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915480020) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 5 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37355020778/job/111915338481) | [21m39s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915479965) | [21m39s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915479965) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [15m49s](https://github.com/iree-org/iree/actions/runs/37355020778/job/111915338380) | [15m49s](https://github.com/iree-org/iree/actions/runs/37355020778/job/111915338380) | [15m49s](https://github.com/iree-org/iree/actions/runs/37355020778/job/111915338380) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 5 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342380) | [2m12s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915479593) | [2m12s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915479593) | 5 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 5 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/37326868145/job/111819843860) | [1m58s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915479350) | [1m58s](https://github.com/iree-org/iree/actions/runs/37355026527/job/111915479350) | 5 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 345 | 1% (4/345) |  | 1h41m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 163 | 1% (2/163) |  | 5d03h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 14h04m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 14h04m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 14h04m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 14h04m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h41m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h29m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
