# iree-ci-monitor

_Updated: 2026-10-07 06:32 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 26 | 13 | [2h25m](https://github.com/iree-org/iree/actions/runs/37610937094/job/112760368202) | 2026-10-07 06:30 PDT | 0 | [13m31s](https://github.com/iree-org/iree/actions/runs/37587711914/job/112684010472) | [1h36m](https://github.com/iree-org/iree/actions/runs/37613401257/job/112768617584) | 0% (0/3) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 26 | 12 | [2h03m](https://github.com/iree-org/iree/actions/runs/37613401257/job/112768617530) | 2026-10-07 06:30 PDT | 0 | [16m39s](https://github.com/iree-org/iree/actions/runs/37618793557/job/112786540354) | [56m13s](https://github.com/iree-org/iree/actions/runs/37610937094/job/112760367824) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 13 | 7 | [2h03m](https://github.com/iree-org/iree/actions/runs/37613401257/job/112768617524) | 2026-10-07 06:30 PDT | 0 | [23m44s](https://github.com/iree-org/iree/actions/runs/37608221818/job/112802829633) | [40m03s](https://github.com/iree-org/iree/actions/runs/37587711914/job/112684010596) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 13 | 5 | [1h52m](https://github.com/iree-org/iree/actions/runs/37613511183/job/112772582329) | 2026-10-07 06:30 PDT | 1 | [20m21s](https://github.com/iree-org/iree/actions/runs/37617348754/job/112782333376) | [36m11s](https://github.com/iree-org/iree/actions/runs/37618793557/job/112786540254) | 0% (0/1) | `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 288 | 0 | — | — | 15 | [3s](https://github.com/iree-org/iree/actions/runs/37617348754/job/112782333216) | [6m50s](https://github.com/iree-org/iree/actions/runs/37623831789/job/112804082112) | 1% (1/77) | 280 |
| `ubuntu-24.04-arm` | github-hosted | 45 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/37618793676/job/112783629003) | [3m37s](https://github.com/iree-org/iree/actions/runs/37623978258/job/112802681126) | 0% (0/12) | 45 |
| `azure-linux-scale` | ossci | 91 | 0 | — | — | 10 | [15s](https://github.com/iree-org/iree/actions/runs/37617348754/job/112778879535) | [3m09s](https://github.com/iree-org/iree/actions/runs/37608221782/job/112798502167) | 11% (3/27) | 90 |
| `ubuntu-latest` | github-hosted | 48 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/37617342657/job/112778778409) | [3m05s](https://github.com/iree-org/iree/actions/runs/37626663455/job/112810074858) | 0% (0/12) | 48 |
| `macos-14` | github-hosted | 39 | 0 | — | — | 1 | [17s](https://github.com/iree-org/iree/actions/runs/37613511020/job/112766617883) | [2m40s](https://github.com/iree-org/iree/actions/runs/37623978258/job/112802681258) | 0% (0/12) | 39 |
| `windows-2022` | github-hosted | 44 | 0 | — | — | 0 | [32s](https://github.com/iree-org/iree/actions/runs/37608221782/job/112798501799) | [2m33s](https://github.com/iree-org/iree/actions/runs/37623978258/job/112802681264) | 0% (0/12) | 44 |
| `macos-15` | github-hosted | 8 | 0 | — | — | 1 | [1m19s](https://github.com/iree-org/iree/actions/runs/37624995196/job/112809218414) | [1m53s](https://github.com/iree-org/iree/actions/runs/37624995196/job/112809218509) | — | 8 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m50s](https://github.com/iree-org/iree/actions/runs/37601185545/job/112725667143) | [1m50s](https://github.com/iree-org/iree/actions/runs/37601185545/job/112725667143) | 100% (1/1) | 1 |
| `azure-windows-scale` | ossci | 14 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/37601737988/job/112727566775) | [2s](https://github.com/iree-org/iree/actions/runs/37624995196/job/112809218797) | 25% (1/4) | 14 |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 19 | 17 | [23h17m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313612) | 2026-10-07 06:30 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 38 | 34 | [23h17m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313832) | 2026-10-07 06:30 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 19 | 17 | [23h17m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313472) | 2026-10-07 06:30 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 38 | 34 | [23h17m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313855) | 2026-10-07 06:30 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 13 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [23h17m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313472) | 2026-10-07 06:30 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [23h17m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313612) | 2026-10-07 06:30 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [23h17m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313832) | 2026-10-07 06:30 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [23h17m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313855) | 2026-10-07 06:30 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [23h17m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313864) | 2026-10-07 06:30 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [23h17m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313928) | 2026-10-07 06:30 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [23h05m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051077) | 2026-10-07 06:30 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [23h05m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051248) | 2026-10-07 06:30 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [23h05m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051249) | 2026-10-07 06:30 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [23h05m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051272) | 2026-10-07 06:30 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [23h05m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051325) | 2026-10-07 06:30 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [23h05m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051395) | 2026-10-07 06:30 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [23h01m](https://github.com/iree-org/iree/actions/runs/37477997055/job/112323157558) | 2026-10-07 06:30 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [23h01m](https://github.com/iree-org/iree/actions/runs/37477997055/job/112323157752) | 2026-10-07 06:30 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [23h01m](https://github.com/iree-org/iree/actions/runs/37477997055/job/112323157820) | 2026-10-07 06:30 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 19 | 17 | [23h17m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313472) | 2026-10-07 06:30 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 19 | 17 | [23h17m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313612) | 2026-10-07 06:30 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 19 | 17 | [23h17m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313864) | 2026-10-07 06:30 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 19 | 17 | [23h17m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313832) | 2026-10-07 06:30 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 19 | 17 | [23h17m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313855) | 2026-10-07 06:30 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 19 | 17 | [23h17m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313928) | 2026-10-07 06:30 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 13 | 7 | [2h25m](https://github.com/iree-org/iree/actions/runs/37610937094/job/112760368202) | 2026-10-07 06:30 PDT | [24m34s](https://github.com/iree-org/iree/actions/runs/37587711914/job/112684010689) | [1h36m](https://github.com/iree-org/iree/actions/runs/37613401257/job/112768617584) | [1h36m](https://github.com/iree-org/iree/actions/runs/37613401257/job/112768617584) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 13 | 7 | [2h03m](https://github.com/iree-org/iree/actions/runs/37613401257/job/112768617524) | 2026-10-07 06:30 PDT | [23m44s](https://github.com/iree-org/iree/actions/runs/37608221818/job/112802829633) | [40m03s](https://github.com/iree-org/iree/actions/runs/37587711914/job/112684010596) | [40m03s](https://github.com/iree-org/iree/actions/runs/37587711914/job/112684010596) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 13 | 6 | [2h03m](https://github.com/iree-org/iree/actions/runs/37613401257/job/112768617632) | 2026-10-07 06:30 PDT | [13m31s](https://github.com/iree-org/iree/actions/runs/37587711914/job/112684010472) | [1h03m](https://github.com/iree-org/iree/actions/runs/37617348754/job/112782333826) | [1h03m](https://github.com/iree-org/iree/actions/runs/37617348754/job/112782333826) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 13 | 6 | [2h03m](https://github.com/iree-org/iree/actions/runs/37613401257/job/112768617530) | 2026-10-07 06:30 PDT | [30m19s](https://github.com/iree-org/iree/actions/runs/37587711914/job/112684010656) | [56m13s](https://github.com/iree-org/iree/actions/runs/37610937094/job/112760367824) | [56m13s](https://github.com/iree-org/iree/actions/runs/37610937094/job/112760367824) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 13 | 6 | [1h52m](https://github.com/iree-org/iree/actions/runs/37613511183/job/112772582476) | 2026-10-07 06:30 PDT | [5m18s](https://github.com/iree-org/iree/actions/runs/37601738063/job/112730309915) | [54m12s](https://github.com/iree-org/iree/actions/runs/37617348754/job/112782333593) | [54m12s](https://github.com/iree-org/iree/actions/runs/37617348754/job/112782333593) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 13 | 5 | [1h52m](https://github.com/iree-org/iree/actions/runs/37613511183/job/112772582329) | 2026-10-07 06:30 PDT | [20m21s](https://github.com/iree-org/iree/actions/runs/37617348754/job/112782333376) | [36m11s](https://github.com/iree-org/iree/actions/runs/37618793557/job/112786540254) | [36m11s](https://github.com/iree-org/iree/actions/runs/37618793557/job/112786540254) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 3 | 0 | — | — | [2m50s](https://github.com/iree-org/iree/actions/runs/37623004474/job/112810107683) | [9m46s](https://github.com/iree-org/iree/actions/runs/37618793557/job/112804399362) | [9m46s](https://github.com/iree-org/iree/actions/runs/37618793557/job/112804399362) | 3 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 11 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37613401366/job/112784954895) | [9m32s](https://github.com/iree-org/iree/actions/runs/37618793676/job/112804921095) | [9m32s](https://github.com/iree-org/iree/actions/runs/37618793676/job/112804921095) | 11 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 15 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37618793676/job/112783628562) | [9m13s](https://github.com/iree-org/iree/actions/runs/37623831770/job/112800535586) | [11m48s](https://github.com/iree-org/iree/actions/runs/37623978258/job/112802680759) | 14 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 15 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37624995196/job/112809218311) | [9m11s](https://github.com/iree-org/iree/actions/runs/37623831770/job/112800535356) | [10m54s](https://github.com/iree-org/iree/actions/runs/37623978258/job/112802680714) | 14 |
| `.github/workflows/clang_tidy.yml` | clang-tidy | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37623003977/job/112797674167) | [9m01s](https://github.com/iree-org/iree/actions/runs/37623977342/job/112800941459) | [9m01s](https://github.com/iree-org/iree/actions/runs/37623977342/job/112800941459) | 6 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | 15 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/37624995356/job/112808680394) | [6m51s](https://github.com/iree-org/iree/actions/runs/37625351063/job/112805583236) | [14m11s](https://github.com/iree-org/iree/actions/runs/37623978230/job/112800970616) | 15 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 14 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37624995196/job/112809218390) | [6m40s](https://github.com/iree-org/iree/actions/runs/37626670352/job/112811962520) | [13m18s](https://github.com/iree-org/iree/actions/runs/37623978258/job/112802680758) | 14 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 13 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37613511183/job/112772582253) | [6m39s](https://github.com/iree-org/iree/actions/runs/37624995356/job/112812640188) | [6m40s](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706227) | 13 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 368 | 0% (1/367) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 91 | 0% (0/91) |  | 6d17h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 23h17m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 23h17m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job observed waiting 2h03m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 2h25m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 23h17m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 23h17m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job observed waiting 2h03m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h36m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
