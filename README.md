# iree-ci-monitor

_Updated: 2026-09-14 05:55 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 7 | 1 | [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | 0 | [10m16s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550653) | [36m20s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550832) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [13m23s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213460) | [29m54s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550723) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [20m13s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550860) | [22m06s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776291) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213353) | [21m59s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550631) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [9m02s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213627) | [20m34s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213778) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [10m35s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550755) | [20m18s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213622) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [15m07s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550678) | [15m56s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213658) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [9m32s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213564) | [15m39s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776293) | — | `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213497) | [14m42s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776319) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [4m47s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776176) | [10m54s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213679) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213419) | [6m46s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776008) | — | `shark01-ci`, `shark10-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m21s](https://github.com/iree-org/iree/actions/runs/34828564102/job/103926243040) | [1m21s](https://github.com/iree-org/iree/actions/runs/34828564102/job/103926243040) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34827922300/job/103924314456) | [1m14s](https://github.com/iree-org/iree/actions/runs/34819013135/job/103896060873) | — | 9 |
| `azure-linux-scale` | ossci | 17 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103896063740) | [9s](https://github.com/iree-org/iree/actions/runs/34823581562/job/103910506331) | 0% (0/2) | 17 |
| `macos-14` | github-hosted | 10 | 0 | — | — | 1 | [7s](https://github.com/iree-org/iree/actions/runs/34827922300/job/103924314711) | [9s](https://github.com/iree-org/iree/actions/runs/34827922300/job/103924314466) | — | 10 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/34819013135/job/103896060885) | [5s](https://github.com/iree-org/iree/actions/runs/34827922300/job/103924314529) | — | 9 |
| `ubuntu-24.04` | github-hosted | 71 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213516) | [4s](https://github.com/iree-org/iree/actions/runs/34827922300/job/103924314626) | 0% (0/3) | 70 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/34827922300/job/103924314879) | [2s](https://github.com/iree-org/iree/actions/runs/34819013135/job/103896061150) | — | 3 |
| `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34822970260/job/103908523045) | [2s](https://github.com/iree-org/iree/actions/runs/34822970260/job/103908523045) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 1 | [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | [8m00s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213616) | [36m20s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550832) | [36m20s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550832) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [13m23s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213460) | [29m54s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550723) | [29m54s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550723) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [20m13s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550860) | [22m06s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776291) | [22m06s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776291) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213353) | [21m59s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550631) | [21m59s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550631) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [15m22s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776356) | [20m34s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213778) | [20m34s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213778) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [10m35s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550755) | [20m18s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213622) | [20m18s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213622) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [19m04s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213526) | [19m37s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776244) | [19m37s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776244) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [15m07s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550678) | [15m56s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213658) | [15m56s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213658) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [12m25s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213548) | [15m39s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776293) | [15m39s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776293) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213497) | [14m42s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776319) | [14m42s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776319) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213614) | [13m49s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550829) | [13m49s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550829) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [9m02s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213627) | [13m48s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550763) | [13m48s](https://github.com/iree-org/iree/actions/runs/34823581434/job/103912550763) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [4m47s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776176) | [10m54s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213679) | [10m54s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213679) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [9m32s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213564) | [9m36s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776303) | [9m36s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776303) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34827922353/job/103926213419) | [6m46s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776008) | [6m46s](https://github.com/iree-org/iree/actions/runs/34819013210/job/103897776008) | 2 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m21s](https://github.com/iree-org/iree/actions/runs/34828564102/job/103926243040) | [1m21s](https://github.com/iree-org/iree/actions/runs/34828564102/job/103926243040) | [1m21s](https://github.com/iree-org/iree/actions/runs/34828564102/job/103926243040) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34827922300/job/103924314545) | [1m18s](https://github.com/iree-org/iree/actions/runs/34819013135/job/103896060808) | [1m18s](https://github.com/iree-org/iree/actions/runs/34819013135/job/103896060808) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 3 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/34827922300/job/103924314574) | [1m14s](https://github.com/iree-org/iree/actions/runs/34819013135/job/103896060873) | [1m14s](https://github.com/iree-org/iree/actions/runs/34819013135/job/103896060873) | 3 |
| `.github/workflows/clang_tidy.yml` | clang-tidy | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34819012816/job/103896008585) | [27s](https://github.com/iree-org/iree/actions/runs/34827922037/job/103924232625) | [27s](https://github.com/iree-org/iree/actions/runs/34827922037/job/103924232625) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 3 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/34827922300/job/103924314909) | [9s](https://github.com/iree-org/iree/actions/runs/34823581562/job/103910506331) | [9s](https://github.com/iree-org/iree/actions/runs/34823581562/job/103910506331) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 291 | 1% (4/291) |  | 2h53m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 220 | 2% (4/220) |  | 2h57m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 264 | 8% (21/264) |  | 2h57m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 215 | 1% (2/215) |  | 3h00m ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 2h00m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
