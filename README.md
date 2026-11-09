# iree-ci-monitor

_Updated: 2026-11-09 14:27 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 18 | 8 | [6h12m](https://github.com/iree-org/iree/actions/runs/42651349881/job/129282660338) | 2026-11-09 14:26 PST | 0 | [4h12m](https://github.com/iree-org/iree/actions/runs/42653695425/job/129291944246) | [5h53m](https://github.com/iree-org/iree/actions/runs/42647529684/job/129270256947) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 18 | 4 | [5h48m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888683) | 2026-11-09 14:26 PST | 1 | [2h27m](https://github.com/iree-org/iree/actions/runs/42685742546/job/129396556852) | [5h16m](https://github.com/iree-org/iree/actions/runs/42658371014/job/129308407794) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 18 | 0 | — | — | 0 | [1h59m](https://github.com/iree-org/iree/actions/runs/42653695425/job/129291944294) | [5h08m](https://github.com/iree-org/iree/actions/runs/42645011480/job/129260620895) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [1h51m](https://github.com/iree-org/iree/actions/runs/42647529684/job/129270256803) | [4h48m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888586) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 9 | 0 | — | — | 0 | [2h34m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888214) | [4h06m](https://github.com/iree-org/iree/actions/runs/42653695425/job/129291943729) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 18 | 0 | — | — | 1 | [1h59m](https://github.com/iree-org/iree/actions/runs/42647529684/job/129270256773) | [2h22m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888582) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 9 | 1 | [27m57s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058803) | 2026-11-09 14:26 PST | 0 | [1h06m](https://github.com/iree-org/iree/actions/runs/42645011480/job/129260620907) | [1h44m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888496) | 0% (0/1) | `shark55-ci` |
| `azure-windows-scale` | ossci | 9 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363396) | [9m56s](https://github.com/iree-org/iree/actions/runs/42647529902/job/129264890001) | 0% (0/1) | 9 |
| `macos-15` | github-hosted | 28 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/42651349726/job/129278375454) | [3m30s](https://github.com/iree-org/iree/actions/runs/42647529902/job/129264889228) | 0% (0/3) | 28 |
| `azure-linux-scale` | ossci | 57 | 0 | — | — | 2 | [14s](https://github.com/iree-org/iree/actions/runs/42685742392/job/129392083505) | [2m24s](https://github.com/iree-org/iree/actions/runs/42647529684/job/129264891058) | 0% (0/7) | 57 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [2m23s](https://github.com/iree-org/iree/actions/runs/42645011442/job/129256619499) | [2m23s](https://github.com/iree-org/iree/actions/runs/42645011442/job/129256619499) | — | 1 |
| `ubuntu-24.04-arm` | github-hosted | 27 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/42653695471/job/129287566181) | [2m01s](https://github.com/iree-org/iree/actions/runs/42647529902/job/129264889005) | 0% (0/3) | 27 |
| `ubuntu-24.04` | github-hosted | 183 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/42658371014/job/129303162742) | [1m54s](https://github.com/iree-org/iree/actions/runs/42654621055/job/129289677123) | 6% (1/18) | 180 |
| `windows-2022` | github-hosted | 27 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/42685742392/job/129392083311) | [1m28s](https://github.com/iree-org/iree/actions/runs/42647529902/job/129264889222) | 0% (0/3) | 27 |
| `ubuntu-latest` | github-hosted | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/42705092425/job/129459690548) | [1m11s](https://github.com/iree-org/iree/actions/runs/42654620207/job/129289682479) | 0% (0/4) | 7 |
| `Linux,X64,iree-w7900` | self-hosted | 9 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [6h12m](https://github.com/iree-org/iree/actions/runs/42651349881/job/129282660338) | 2026-11-09 14:26 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `runtime-dlpack-access` | pull_request |
| [5h48m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888683) | 2026-11-09 14:26 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [5h48m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888816) | 2026-11-09 14:26 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [5h48m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888857) | 2026-11-09 14:26 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [5h48m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888883) | 2026-11-09 14:26 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [5h28m](https://github.com/iree-org/iree/actions/runs/42658371014/job/129308407364) | 2026-11-09 14:26 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `inner_tiled_thread` | pull_request |
| [5h28m](https://github.com/iree-org/iree/actions/runs/42658371014/job/129308407666) | 2026-11-09 14:26 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `inner_tiled_thread` | pull_request |
| [5h28m](https://github.com/iree-org/iree/actions/runs/42658371014/job/129308407938) | 2026-11-09 14:26 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `inner_tiled_thread` | pull_request |
| [2h36m](https://github.com/iree-org/iree/actions/runs/42685742546/job/129396557031) | 2026-11-09 14:26 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/jschuhmacher/stablehlo_target_registry` | pull_request |
| [27m57s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058803) | 2026-11-09 14:26 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `dependabot/github_actions/github-actions-a4114cef40` | pull_request |
| [27m57s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058957) | 2026-11-09 14:26 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `dependabot/github_actions/github-actions-a4114cef40` | pull_request |
| [27m57s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059115) | 2026-11-09 14:26 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `dependabot/github_actions/github-actions-a4114cef40` | pull_request |
| [27m57s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468059310) | 2026-11-09 14:26 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `dependabot/github_actions/github-actions-a4114cef40` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 9 | 5 | [6h12m](https://github.com/iree-org/iree/actions/runs/42651349881/job/129282660338) | 2026-11-09 14:26 PST | [5h51m](https://github.com/iree-org/iree/actions/runs/42645011480/job/129260621154) | [5h53m](https://github.com/iree-org/iree/actions/runs/42647529684/job/129270256947) | [5h53m](https://github.com/iree-org/iree/actions/runs/42647529684/job/129270256947) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 9 | 2 | [5h48m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888683) | 2026-11-09 14:26 PST | [2h27m](https://github.com/iree-org/iree/actions/runs/42685742546/job/129396556852) | [5h50m](https://github.com/iree-org/iree/actions/runs/42651349881/job/129282660476) | [5h50m](https://github.com/iree-org/iree/actions/runs/42651349881/job/129282660476) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 9 | 3 | [5h48m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888883) | 2026-11-09 14:26 PST | [3h24m](https://github.com/iree-org/iree/actions/runs/42647529684/job/129270257251) | [5h41m](https://github.com/iree-org/iree/actions/runs/42653695425/job/129291943999) | [5h41m](https://github.com/iree-org/iree/actions/runs/42653695425/job/129291943999) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 9 | 2 | [5h48m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888857) | 2026-11-09 14:26 PST | [2h17m](https://github.com/iree-org/iree/actions/runs/42651349881/job/129282660245) | [5h16m](https://github.com/iree-org/iree/actions/runs/42658371014/job/129308407794) | [5h16m](https://github.com/iree-org/iree/actions/runs/42658371014/job/129308407794) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [2h00m](https://github.com/iree-org/iree/actions/runs/42658371014/job/129308407790) | [5h14m](https://github.com/iree-org/iree/actions/runs/42645011480/job/129260620882) | [5h14m](https://github.com/iree-org/iree/actions/runs/42645011480/job/129260620882) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [1h59m](https://github.com/iree-org/iree/actions/runs/42653695425/job/129291944294) | [5h08m](https://github.com/iree-org/iree/actions/runs/42645011480/job/129260620895) | [5h08m](https://github.com/iree-org/iree/actions/runs/42645011480/job/129260620895) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 9 | 0 | — | — | [1h51m](https://github.com/iree-org/iree/actions/runs/42647529684/job/129270256803) | [4h48m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888586) | [4h48m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888586) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 9 | 0 | — | — | [2h34m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888214) | [4h06m](https://github.com/iree-org/iree/actions/runs/42653695425/job/129291943729) | [4h06m](https://github.com/iree-org/iree/actions/runs/42653695425/job/129291943729) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [2h08m](https://github.com/iree-org/iree/actions/runs/42658371014/job/129308407370) | [3h12m](https://github.com/iree-org/iree/actions/runs/42645011480/job/129260620641) | [3h12m](https://github.com/iree-org/iree/actions/runs/42645011480/job/129260620641) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [1h45m](https://github.com/iree-org/iree/actions/runs/42651349881/job/129282660408) | [2h22m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888582) | [2h22m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888582) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 9 | 1 | [27m57s](https://github.com/iree-org/iree/actions/runs/42706404699/job/129468058803) | 2026-11-09 14:26 PST | [1h06m](https://github.com/iree-org/iree/actions/runs/42645011480/job/129260620907) | [1h44m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888496) | [1h44m](https://github.com/iree-org/iree/actions/runs/42654621055/job/129296888496) | 1 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 9 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/42706404633/job/129464363396) | [9m56s](https://github.com/iree-org/iree/actions/runs/42647529902/job/129264890001) | [9m56s](https://github.com/iree-org/iree/actions/runs/42647529902/job/129264890001) | 9 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 9 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/42651349726/job/129278375253) | [7m34s](https://github.com/iree-org/iree/actions/runs/42654620752/job/129290829672) | [7m34s](https://github.com/iree-org/iree/actions/runs/42654620752/job/129290829672) | 9 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42658371014/job/129308407142) | [5m15s](https://github.com/iree-org/iree/actions/runs/42653695425/job/129291943945) | [5m15s](https://github.com/iree-org/iree/actions/runs/42653695425/job/129291943945) | 9 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42658371014/job/129308407489) | [4m58s](https://github.com/iree-org/iree/actions/runs/42653695425/job/129291943799) | [4m58s](https://github.com/iree-org/iree/actions/runs/42653695425/job/129291943799) | 9 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42658370992/job/129303242028) | [4m37s](https://github.com/iree-org/iree/actions/runs/42654620752/job/129290829755) | [4m37s](https://github.com/iree-org/iree/actions/runs/42654620752/job/129290829755) | 9 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 9 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/42654620752/job/129290829264) | [4m01s](https://github.com/iree-org/iree/actions/runs/42647529902/job/129264889363) | [4m01s](https://github.com/iree-org/iree/actions/runs/42647529902/job/129264889363) | 9 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42653695471/job/129287566042) | [3m44s](https://github.com/iree-org/iree/actions/runs/42647529902/job/129264889051) | [3m44s](https://github.com/iree-org/iree/actions/runs/42647529902/job/129264889051) | 9 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42658370992/job/129303241576) | [3m12s](https://github.com/iree-org/iree/actions/runs/42647529902/job/129264889106) | [3m12s](https://github.com/iree-org/iree/actions/runs/42647529902/job/129264889106) | 9 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 9 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/42653695471/job/129287566735) | [3m04s](https://github.com/iree-org/iree/actions/runs/42647529902/job/129264889258) | [3m04s](https://github.com/iree-org/iree/actions/runs/42647529902/job/129264889258) | 9 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 517 | 1% (4/516) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 418 | 1% (3/417) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 5h48m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 6h12m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h44m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 5h16m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 4h48m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 5h08m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 4h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 5h53m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h22m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
