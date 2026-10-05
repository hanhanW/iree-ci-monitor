# iree-ci-monitor

_Updated: 2026-10-05 07:50 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 10 | 2 | [1h58m](https://github.com/iree-org/iree/actions/runs/37311001145/job/111770421721) | 2026-10-05 07:48 PDT | 0 | [19m21s](https://github.com/iree-org/iree/actions/runs/37308691480/job/111762843327) | [1h58m](https://github.com/iree-org/iree/actions/runs/37310364140/job/111767433594) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 20 | 8 | [2h18m](https://github.com/iree-org/iree/actions/runs/37308784118/job/111762799033) | 2026-10-05 07:48 PDT | 0 | [37m01s](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070864) | [1h29m](https://github.com/iree-org/iree/actions/runs/37310364140/job/111767433914) | 0% (0/4) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 20 | 8 | [2h18m](https://github.com/iree-org/iree/actions/runs/37308784118/job/111762799098) | 2026-10-05 07:48 PDT | 0 | [1h00m](https://github.com/iree-org/iree/actions/runs/37308784118/job/111762798834) | [1h28m](https://github.com/iree-org/iree/actions/runs/37311013979/job/111775386855) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 10 | 0 | — | — | 1 | [10m10s](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070617) | [1h19m](https://github.com/iree-org/iree/actions/runs/37308791765/job/111763021554) | 0% (0/4) | `shark75-ci` |
| `azure-windows-scale` | ossci | 11 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/37292378268/job/111705642319) | [8m48s](https://github.com/iree-org/iree/actions/runs/37308784085/job/111759410530) | 0% (0/4) | 10 |
| `ubuntu-24.04` | github-hosted | 298 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/37324856991/job/111817608550) | [7m19s](https://github.com/iree-org/iree/actions/runs/37311001135/job/111770089862) | 3% (2/78) | 262 |
| `ubuntu-latest` | github-hosted | 60 | 0 | — | — | 0 | [33s](https://github.com/iree-org/iree/actions/runs/37308785535/job/111758817273) | [6m25s](https://github.com/iree-org/iree/actions/runs/37311398232/job/111767432883) | 0% (0/12) | 60 |
| `macos-14` | github-hosted | 36 | 0 | — | — | 1 | [30s](https://github.com/iree-org/iree/actions/runs/37308784085/job/111759409942) | [3m34s](https://github.com/iree-org/iree/actions/runs/37308791717/job/111759288853) | 0% (0/12) | 36 |
| `windows-2022` | github-hosted | 35 | 0 | — | — | 3 | [42s](https://github.com/iree-org/iree/actions/runs/37310364489/job/111766039654) | [3m10s](https://github.com/iree-org/iree/actions/runs/37308784085/job/111759409943) | 0% (0/12) | 35 |
| `ubuntu-24.04-arm` | github-hosted | 36 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/37326868145/job/111819843570) | [3m00s](https://github.com/iree-org/iree/actions/runs/37308784085/job/111759409920) | 0% (0/12) | 36 |
| `azure-linux-scale` | ossci | 72 | 0 | — | — | 11 | [9s](https://github.com/iree-org/iree/actions/runs/37292378268/job/111705642251) | [2m21s](https://github.com/iree-org/iree/actions/runs/37308784085/job/111759410293) | 0% (0/30) | 72 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [2m02s](https://github.com/iree-org/iree/actions/runs/37291724400/job/111703446169) | [2m02s](https://github.com/iree-org/iree/actions/runs/37291724400/job/111703446169) | 100% (1/1) | 1 |
| `Linux,X64,gfx1100` | self-hosted | 20 | 20 | [4h46m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518868) | 2026-10-05 07:48 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 20 | 20 | [4h46m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518900) | 2026-10-05 07:48 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 10 | [4h46m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518866) | 2026-10-05 07:48 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 10 | 10 | [4h46m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518852) | 2026-10-05 07:48 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 10 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [4h46m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518852) | 2026-10-05 07:48 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/jschuhmacher/strict-properties` | pull_request |
| [4h46m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518866) | 2026-10-05 07:48 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/jschuhmacher/strict-properties` | pull_request |
| [4h46m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518868) | 2026-10-05 07:48 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/jschuhmacher/strict-properties` | pull_request |
| [4h46m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518900) | 2026-10-05 07:48 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/jschuhmacher/strict-properties` | pull_request |
| [4h46m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518960) | 2026-10-05 07:48 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/jschuhmacher/strict-properties` | pull_request |
| [4h46m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710519011) | 2026-10-05 07:48 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/jschuhmacher/strict-properties` | pull_request |
| [4h25m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070934) | 2026-10-05 07:48 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `bump-version-3.13` | pull_request |
| [4h25m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070942) | 2026-10-05 07:48 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `bump-version-3.13` | pull_request |
| [4h25m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070964) | 2026-10-05 07:48 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `bump-version-3.13` | pull_request |
| [4h25m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070975) | 2026-10-05 07:48 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `bump-version-3.13` | pull_request |
| [4h25m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718071039) | 2026-10-05 07:48 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `bump-version-3.13` | pull_request |
| [4h25m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718071090) | 2026-10-05 07:48 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `bump-version-3.13` | pull_request |
| [3h15m](https://github.com/iree-org/iree/actions/runs/37302785332/job/111742224798) | 2026-10-05 07:48 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [3h15m](https://github.com/iree-org/iree/actions/runs/37302785332/job/111742224938) | 2026-10-05 07:48 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [3h15m](https://github.com/iree-org/iree/actions/runs/37302785332/job/111742224953) | 2026-10-05 07:48 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 10 | [4h46m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518866) | 2026-10-05 07:48 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 10 | 10 | [4h46m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518852) | 2026-10-05 07:48 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 10 | [4h46m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518868) | 2026-10-05 07:48 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 10 | [4h46m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518960) | 2026-10-05 07:48 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 10 | [4h46m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710519011) | 2026-10-05 07:48 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 10 | [4h46m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518900) | 2026-10-05 07:48 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 5 | [2h18m](https://github.com/iree-org/iree/actions/runs/37308784118/job/111762799098) | 2026-10-05 07:48 PDT | [1h15m](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518774) | [1h34m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718071023) | [1h34m](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718071023) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 10 | 5 | [2h18m](https://github.com/iree-org/iree/actions/runs/37308784118/job/111762799033) | 2026-10-05 07:48 PDT | [32m54s](https://github.com/iree-org/iree/actions/runs/37302785332/job/111742224889) | [1h14m](https://github.com/iree-org/iree/actions/runs/37311013979/job/111775387130) | [1h14m](https://github.com/iree-org/iree/actions/runs/37311013979/job/111775387130) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 10 | 3 | [2h17m](https://github.com/iree-org/iree/actions/runs/37308791765/job/111763021801) | 2026-10-05 07:48 PDT | [39m49s](https://github.com/iree-org/iree/actions/runs/37292378186/job/111710518953) | [1h46m](https://github.com/iree-org/iree/actions/runs/37311001145/job/111770421797) | [1h46m](https://github.com/iree-org/iree/actions/runs/37311001145/job/111770421797) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 3 | [2h06m](https://github.com/iree-org/iree/actions/runs/37310364140/job/111767433636) | 2026-10-05 07:48 PDT | [44m48s](https://github.com/iree-org/iree/actions/runs/37308791765/job/111763021805) | [1h26m](https://github.com/iree-org/iree/actions/runs/37308691480/job/111762843235) | [1h26m](https://github.com/iree-org/iree/actions/runs/37308691480/job/111762843235) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 10 | 2 | [1h58m](https://github.com/iree-org/iree/actions/runs/37311001145/job/111770421721) | 2026-10-05 07:48 PDT | [19m21s](https://github.com/iree-org/iree/actions/runs/37308691480/job/111762843327) | [1h58m](https://github.com/iree-org/iree/actions/runs/37310364140/job/111767433594) | [1h58m](https://github.com/iree-org/iree/actions/runs/37310364140/job/111767433594) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 10 | 0 | — | — | [10m10s](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070617) | [1h19m](https://github.com/iree-org/iree/actions/runs/37308791765/job/111763021554) | [1h19m](https://github.com/iree-org/iree/actions/runs/37308791765/job/111763021554) | 1 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 21 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37324857078/job/111812977041) | [12m09s](https://github.com/iree-org/iree/actions/runs/37311014076/job/111768045463) | [12m09s](https://github.com/iree-org/iree/actions/runs/37311014076/job/111768045463) | 11 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 10 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070840) | [11m55s](https://github.com/iree-org/iree/actions/runs/37310364140/job/111767433756) | [11m55s](https://github.com/iree-org/iree/actions/runs/37310364140/job/111767433756) | 10 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | 21 | 0 | — | — | [54s](https://github.com/iree-org/iree/actions/runs/37308793341/job/111758837943) | [10m25s](https://github.com/iree-org/iree/actions/runs/37311014848/job/111766156203) | [13m29s](https://github.com/iree-org/iree/actions/runs/37311013979/job/111766153253) | 19 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | 21 | 0 | — | — | [27s](https://github.com/iree-org/iree/actions/runs/37302785710/job/111739344739) | [10m11s](https://github.com/iree-org/iree/actions/runs/37311001135/job/111766111246) | [13m40s](https://github.com/iree-org/iree/actions/runs/37311015013/job/111766158640) | 19 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 11 | 0 | — | — | [45s](https://github.com/iree-org/iree/actions/runs/37292378268/job/111705642075) | [9m14s](https://github.com/iree-org/iree/actions/runs/37310364489/job/111766039825) | [9m14s](https://github.com/iree-org/iree/actions/runs/37310364489/job/111766039825) | 11 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 17 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/37309618371/job/111761545454) | [9m09s](https://github.com/iree-org/iree/actions/runs/37311006538/job/111766134593) | [9m17s](https://github.com/iree-org/iree/actions/runs/37311006389/job/111766131724) | 17 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37292378268/job/111705642319) | [8m48s](https://github.com/iree-org/iree/actions/runs/37308784085/job/111759410530) | [8m48s](https://github.com/iree-org/iree/actions/runs/37308784085/job/111759410530) | 10 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 10 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/37295380211/job/111718070849) | [7m34s](https://github.com/iree-org/iree/actions/runs/37308691480/job/111762842968) | [7m34s](https://github.com/iree-org/iree/actions/runs/37308691480/job/111762842968) | 10 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 338 | 1% (4/337) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 206 | 1% (2/206) |  | 4d18h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 4h46m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 4h46m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 2h18m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 4h46m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 4h46m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job observed waiting 2h18m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h58m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h29m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h19m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h28m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
