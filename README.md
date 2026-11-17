# iree-ci-monitor

_Updated: 2026-11-17 13:00 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [2h05m](https://github.com/iree-org/iree/actions/runs/44126919012/job/134197759484) | [3h21m](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139403013) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 1 | [50m58s](https://github.com/iree-org/iree/actions/runs/44130381409/job/134219703951) | [2h44m](https://github.com/iree-org/iree/actions/runs/44109545194/job/134141845303) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [27m14s](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139402289) | [1h37m](https://github.com/iree-org/iree/actions/runs/44126919012/job/134197758888) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [51m04s](https://github.com/iree-org/iree/actions/runs/44116210874/job/134159758756) | [1h00m](https://github.com/iree-org/iree/actions/runs/44126919012/job/134197759142) | 0% (0/1) | `shark75-ci` |
| `azure-windows-scale` | ossci | 8 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/44130045665/job/134204415395) | [6m56s](https://github.com/iree-org/iree/actions/runs/44110279721/job/134134877483) | 0% (0/1) | 8 |
| `macos-15` | github-hosted | 24 | 0 | — | — | 0 | [14s](https://github.com/iree-org/iree/actions/runs/44116211348/job/134156124307) | [1m51s](https://github.com/iree-org/iree/actions/runs/44109756066/job/134132087590) | 0% (0/3) | 24 |
| `azure-linux-scale` | ossci | 51 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/44126918840/job/134193308226) | [1m51s](https://github.com/iree-org/iree/actions/runs/44109756066/job/134132087003) | 0% (0/7) | 47 |
| `ubuntu-24.04-arm` | github-hosted | 24 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/44130045665/job/134204414567) | [1m39s](https://github.com/iree-org/iree/actions/runs/44109756066/job/134132088329) | 0% (0/3) | 24 |
| `ubuntu-24.04` | github-hosted | 144 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/44110279721/job/134134876150) | [1m24s](https://github.com/iree-org/iree/actions/runs/44109545194/job/134141845419) | 0% (0/19) | 142 |
| `windows-2022` | github-hosted | 24 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/44116211348/job/134156125420) | [1m20s](https://github.com/iree-org/iree/actions/runs/44110279721/job/134134876800) | 0% (0/3) | 24 |
| `Linux,X64,rdna3` | self-hosted | 12 | 10 | [5h45m](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139403026) | 2026-11-17 12:59 PST | 0 | [3s](https://github.com/iree-org/iree/actions/runs/44110279916/job/134140239583) | [3s](https://github.com/iree-org/iree/actions/runs/44110279916/job/134140239583) | — | `shark55-ci` |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/44130032736/job/134204261596) | [3s](https://github.com/iree-org/iree/actions/runs/44099916129/job/134096960197) | 0% (0/3) | 15 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 5 | [5h45m](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139405606) | 2026-11-17 12:59 PST | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 12 | 10 | [5h45m](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139402954) | 2026-11-17 12:59 PST | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [5h45m](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139402954) | 2026-11-17 12:59 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/yalong/honor-skip-intermediate-roundings-rvv-zvfhmin` | pull_request |
| [5h45m](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139403026) | 2026-11-17 12:59 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/yalong/honor-skip-intermediate-roundings-rvv-zvfhmin` | pull_request |
| [5h45m](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139405087) | 2026-11-17 12:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/yalong/honor-skip-intermediate-roundings-rvv-zvfhmin` | pull_request |
| [5h45m](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139405149) | 2026-11-17 12:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/yalong/honor-skip-intermediate-roundings-rvv-zvfhmin` | pull_request |
| [5h45m](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139405606) | 2026-11-17 12:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/yalong/honor-skip-intermediate-roundings-rvv-zvfhmin` | pull_request |
| [5h42m](https://github.com/iree-org/iree/actions/runs/44109545194/job/134141845293) | 2026-11-17 12:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `nxp/qdq-choose-pt2e-torch` | pull_request |
| [5h42m](https://github.com/iree-org/iree/actions/runs/44109545194/job/134141845310) | 2026-11-17 12:59 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `nxp/qdq-choose-pt2e-torch` | pull_request |
| [5h42m](https://github.com/iree-org/iree/actions/runs/44109545194/job/134141845323) | 2026-11-17 12:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `nxp/qdq-choose-pt2e-torch` | pull_request |
| [5h42m](https://github.com/iree-org/iree/actions/runs/44109545194/job/134141845364) | 2026-11-17 12:59 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `nxp/qdq-choose-pt2e-torch` | pull_request |
| [5h42m](https://github.com/iree-org/iree/actions/runs/44109545194/job/134141845472) | 2026-11-17 12:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `nxp/qdq-choose-pt2e-torch` | pull_request |
| [5h16m](https://github.com/iree-org/iree/actions/runs/44116210874/job/134159758744) | 2026-11-17 12:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `schuermans/max-dispatch-binding-bytes` | pull_request |
| [5h16m](https://github.com/iree-org/iree/actions/runs/44116210874/job/134159758875) | 2026-11-17 12:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `schuermans/max-dispatch-binding-bytes` | pull_request |
| [5h16m](https://github.com/iree-org/iree/actions/runs/44116210874/job/134159758919) | 2026-11-17 12:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `schuermans/max-dispatch-binding-bytes` | pull_request |
| [5h16m](https://github.com/iree-org/iree/actions/runs/44116210874/job/134159759158) | 2026-11-17 12:59 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `schuermans/max-dispatch-binding-bytes` | pull_request |
| [5h16m](https://github.com/iree-org/iree/actions/runs/44116210874/job/134159759183) | 2026-11-17 12:59 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `schuermans/max-dispatch-binding-bytes` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 5 | [5h45m](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139405606) | 2026-11-17 12:59 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 5 | [5h45m](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139405087) | 2026-11-17 12:59 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 5 | [5h45m](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139405149) | 2026-11-17 12:59 PST | [3s](https://github.com/iree-org/iree/actions/runs/44110279916/job/134140239583) | [3s](https://github.com/iree-org/iree/actions/runs/44110279916/job/134140239583) | [3s](https://github.com/iree-org/iree/actions/runs/44110279916/job/134140239583) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 5 | [5h45m](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139402954) | 2026-11-17 12:59 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 5 | [5h45m](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139403026) | 2026-11-17 12:59 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [2h31m](https://github.com/iree-org/iree/actions/runs/44109545194/job/134141845699) | [3h21m](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139403013) | [3h21m](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139403013) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [1h47m](https://github.com/iree-org/iree/actions/runs/44126919012/job/134197759490) | [3h19m](https://github.com/iree-org/iree/actions/runs/44109545194/job/134141845484) | [3h19m](https://github.com/iree-org/iree/actions/runs/44109545194/job/134141845484) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [1h35m](https://github.com/iree-org/iree/actions/runs/44126919012/job/134197759186) | [2h44m](https://github.com/iree-org/iree/actions/runs/44109545194/job/134141845303) | [2h44m](https://github.com/iree-org/iree/actions/runs/44109545194/job/134141845303) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [27m14s](https://github.com/iree-org/iree/actions/runs/44101886801/job/134139402289) | [1h37m](https://github.com/iree-org/iree/actions/runs/44126919012/job/134197758888) | [1h37m](https://github.com/iree-org/iree/actions/runs/44126919012/job/134197758888) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [25m44s](https://github.com/iree-org/iree/actions/runs/44109545194/job/134141845341) | [1h09m](https://github.com/iree-org/iree/actions/runs/44126919012/job/134197759055) | [1h09m](https://github.com/iree-org/iree/actions/runs/44126919012/job/134197759055) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [51m04s](https://github.com/iree-org/iree/actions/runs/44116210874/job/134159758756) | [1h00m](https://github.com/iree-org/iree/actions/runs/44126919012/job/134197759142) | [1h00m](https://github.com/iree-org/iree/actions/runs/44126919012/job/134197759142) | 1 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 8 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/44130045665/job/134204415395) | [6m56s](https://github.com/iree-org/iree/actions/runs/44110279721/job/134134877483) | [6m56s](https://github.com/iree-org/iree/actions/runs/44110279721/job/134134877483) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 8 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/44116211348/job/134156125183) | [2m19s](https://github.com/iree-org/iree/actions/runs/44109756066/job/134132086874) | [2m19s](https://github.com/iree-org/iree/actions/runs/44109756066/job/134132086874) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 8 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/44116211348/job/134156125420) | [2m15s](https://github.com/iree-org/iree/actions/runs/44110279721/job/134134877671) | [2m15s](https://github.com/iree-org/iree/actions/runs/44110279721/job/134134877671) | 8 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 8 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/44130045665/job/134204414193) | [2m13s](https://github.com/iree-org/iree/actions/runs/44110279721/job/134134876428) | [2m13s](https://github.com/iree-org/iree/actions/runs/44110279721/job/134134876428) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 8 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/44130381530/job/134205897820) | [1m59s](https://github.com/iree-org/iree/actions/runs/44110279721/job/134134876676) | [1m59s](https://github.com/iree-org/iree/actions/runs/44110279721/job/134134876676) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 8 | 0 | — | — | [14s](https://github.com/iree-org/iree/actions/runs/44116211348/job/134156126032) | [1m52s](https://github.com/iree-org/iree/actions/runs/44110279721/job/134134876780) | [1m52s](https://github.com/iree-org/iree/actions/runs/44110279721/job/134134876780) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 8 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/44130045665/job/134204415299) | [1m51s](https://github.com/iree-org/iree/actions/runs/44109756066/job/134132087003) | [1m51s](https://github.com/iree-org/iree/actions/runs/44109756066/job/134132087003) | 8 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 8 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44116211348/job/134156129261) | [1m51s](https://github.com/iree-org/iree/actions/runs/44109756066/job/134132086918) | [1m51s](https://github.com/iree-org/iree/actions/runs/44109756066/job/134132086918) | 8 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44126919012/job/134197759538) | [1m47s](https://github.com/iree-org/iree/actions/runs/44109545194/job/134141845413) | [1m47s](https://github.com/iree-org/iree/actions/runs/44109545194/job/134141845413) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 410 | 0% (2/409) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 371 | 1% (4/371) |  | 2h15m ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 5h45m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 5h45m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 5h45m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h21m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h37m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h44m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
