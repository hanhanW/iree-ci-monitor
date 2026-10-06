# iree-ci-monitor

_Updated: 2026-10-05 23:27 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37415122736/job/112114029013) | [20m13s](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120861) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [12m00s](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120819) | [19m15s](https://github.com/iree-org/iree/actions/runs/37415122736/job/112114029198) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [13m55s](https://github.com/iree-org/iree/actions/runs/37415122736/job/112114029110) | [18m22s](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120842) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120635) | [1m56s](https://github.com/iree-org/iree/actions/runs/37415122736/job/112114028966) | 0% (0/1) | `shark75-ci` |
| `azure-linux-scale` | ossci | 13 | 0 | — | — | 0 | [11s](https://github.com/iree-org/iree/actions/runs/37415122592/job/112111985940) | [1m44s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342840) | 0% (0/7) | 13 |
| `macos-14` | github-hosted | 8 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/37415122592/job/112111985708) | [9s](https://github.com/iree-org/iree/actions/runs/37417780079/job/112120200672) | 0% (0/3) | 8 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/37417780079/job/112120200614) | [6s](https://github.com/iree-org/iree/actions/runs/37415122592/job/112111985664) | 0% (0/3) | 9 |
| `windows-2022` | github-hosted | 8 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342279) | [4s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342380) | 0% (0/3) | 8 |
| `ubuntu-24.04` | github-hosted | 48 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/37415122736/job/112114029067) | [3s](https://github.com/iree-org/iree/actions/runs/37417780079/job/112120140789) | 0% (0/22) | 47 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37415122592/job/112111985871) | [3s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342826) | 0% (0/1) | 2 |
| `ubuntu-latest` | github-hosted | 4 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/37415122174/job/112111942629) | [3s](https://github.com/iree-org/iree/actions/runs/37415122174/job/112111942651) | 0% (0/4) | 4 |
| `Linux,X64,gfx1100` | self-hosted | 30 | 30 | [20h25m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518868) | 2026-10-05 23:27 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 15 | 15 | [20h25m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518866) | 2026-10-05 23:27 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 30 | 30 | [20h25m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518900) | 2026-10-05 23:27 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 15 | 15 | [20h25m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518852) | 2026-10-05 23:27 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [20h25m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518852) | 2026-10-05 23:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/jschuhmacher/strict-properties` | pull_request |
| [20h25m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518866) | 2026-10-05 23:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/jschuhmacher/strict-properties` | pull_request |
| [20h25m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518868) | 2026-10-05 23:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/jschuhmacher/strict-properties` | pull_request |
| [20h25m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518900) | 2026-10-05 23:27 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/jschuhmacher/strict-properties` | pull_request |
| [20h25m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518960) | 2026-10-05 23:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/jschuhmacher/strict-properties` | pull_request |
| [20h25m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710519011) | 2026-10-05 23:27 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/jschuhmacher/strict-properties` | pull_request |
| [20h03m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070934) | 2026-10-05 23:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `bump-version-3.13` | pull_request |
| [20h03m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070942) | 2026-10-05 23:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `bump-version-3.13` | pull_request |
| [20h03m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070964) | 2026-10-05 23:27 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `bump-version-3.13` | pull_request |
| [20h03m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070975) | 2026-10-05 23:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `bump-version-3.13` | pull_request |
| [20h03m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718071039) | 2026-10-05 23:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `bump-version-3.13` | pull_request |
| [20h03m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718071090) | 2026-10-05 23:27 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `bump-version-3.13` | pull_request |
| [18h53m](https://github.com/iree-org/iree/actions/runs/37302785332/job/111742224798) | 2026-10-05 23:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [18h53m](https://github.com/iree-org/iree/actions/runs/37302785332/job/111742224938) | 2026-10-05 23:27 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [18h53m](https://github.com/iree-org/iree/actions/runs/37302785332/job/111742224953) | 2026-10-05 23:27 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 15 | 15 | [20h25m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518866) | 2026-10-05 23:27 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 15 | 15 | [20h25m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518852) | 2026-10-05 23:27 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 15 | 15 | [20h25m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518868) | 2026-10-05 23:27 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 15 | 15 | [20h25m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518960) | 2026-10-05 23:27 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 15 | 15 | [20h25m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710519011) | 2026-10-05 23:27 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 15 | 15 | [20h25m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518900) | 2026-10-05 23:27 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37415122736/job/112114029013) | [20m13s](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120861) | [20m13s](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120861) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [12m00s](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120819) | [19m15s](https://github.com/iree-org/iree/actions/runs/37415122736/job/112114029198) | [19m15s](https://github.com/iree-org/iree/actions/runs/37415122736/job/112114029198) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [4m56s](https://github.com/iree-org/iree/actions/runs/37415122736/job/112114029029) | [18m22s](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120842) | [18m22s](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120842) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [13m06s](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120666) | [13m55s](https://github.com/iree-org/iree/actions/runs/37415122736/job/112114029110) | [13m55s](https://github.com/iree-org/iree/actions/runs/37415122736/job/112114029110) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [5m15s](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999121017) | [6m59s](https://github.com/iree-org/iree/actions/runs/37415122736/job/112114029094) | [6m59s](https://github.com/iree-org/iree/actions/runs/37415122736/job/112114029094) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120635) | [1m56s](https://github.com/iree-org/iree/actions/runs/37415122736/job/112114028966) | [1m56s](https://github.com/iree-org/iree/actions/runs/37415122736/job/112114028966) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [26s](https://github.com/iree-org/iree/actions/runs/37415122736/job/112111986585) | [1m53s](https://github.com/iree-org/iree/actions/runs/37378873742/job/111995364927) | [1m53s](https://github.com/iree-org/iree/actions/runs/37378873742/job/111995364927) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/37415122592/job/112111985714) | [1m44s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342840) | [1m44s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342840) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37415122592/job/112111985783) | [1m42s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342681) | [1m42s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342681) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/37415122592/job/112111985940) | [1m32s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342841) | [1m32s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342841) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37415122592/job/112111985688) | [1m31s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342469) | [1m31s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342469) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/37415122592/job/112111985818) | [10s](https://github.com/iree-org/iree/actions/runs/37415122592/job/112111985818) | [10s](https://github.com/iree-org/iree/actions/runs/37415122592/job/112111985818) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37415122592/job/112111985708) | [9s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342513) | [9s](https://github.com/iree-org/iree/actions/runs/37378873804/job/111995342513) | 2 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37417780079/job/112120200672) | [9s](https://github.com/iree-org/iree/actions/runs/37417780079/job/112120200672) | [9s](https://github.com/iree-org/iree/actions/runs/37417780079/job/112120200672) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 351 | 1% (4/351) |  | 1h14m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 163 | 1% (2/163) |  | 5d09h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 20h25m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 20h25m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 20h25m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 20h25m (> 2h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
