# iree-ci-monitor

_Updated: 2026-07-14 00:00 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [11m53s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907481) | [11m53s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907481) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [10m51s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907532) | [10m51s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907532) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [10m16s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907522) | [10m16s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907522) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [7m51s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907573) | [9m07s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907548) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907557) | [9m03s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907556) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [4m49s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907523) | [8m34s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907601) | 0% (0/2) | `shark01-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907503) | [7m16s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907620) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [4m33s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907452) | [4m33s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907452) | 100% (1/1) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [3m54s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907512) | [3m54s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907512) | 0% (0/1) | `shark01-ci` |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640844) | [1m50s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87009646410) | 0% (0/6) | 6 |
| `ubuntu-24.04` | github-hosted | 27 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907542) | [53s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907599) | 14% (3/22) | 27 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/29309536916/job/87010201933) | [7s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640742) | 0% (0/3) | 6 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907415) | [3s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907415) | 0% (0/1) | 1 |
| `ubuntu-latest` | github-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29309357037/job/87009614746) | [2s](https://github.com/iree-org/iree/actions/runs/29309357037/job/87009614747) | 0% (0/4) | 4 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640774) | [2s](https://github.com/iree-org/iree/actions/runs/29309536916/job/87010201941) | 0% (0/3) | 5 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640753) | [2s](https://github.com/iree-org/iree/actions/runs/29309536916/job/87010201988) | 0% (0/3) | 5 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907498) | [2s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907498) | 0% (0/1) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907520) | [2s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907520) | 0% (0/1) | `shark01-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907611) | [2s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907611) | 0% (0/1) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640875) | [1s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640875) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 2 | 2 | [19h47m](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801338899) | 2026-07-14 00:00 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [19h47m](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801338899) | 2026-07-14 00:00 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/rvv_tile_size_selection` | pull_request |
| [19h37m](https://github.com/iree-org/iree/actions/runs/29243839489/job/86803078372) | 2026-07-14 00:00 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/rvv_scalable_vectorization` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 2 | 2 | [19h47m](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801338899) | 2026-07-14 00:00 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [11m53s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907481) | [11m53s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907481) | [11m53s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907481) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [10m51s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907532) | [10m51s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907532) | [10m51s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907532) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [10m16s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907522) | [10m16s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907522) | [10m16s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907522) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [9m07s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907548) | [9m07s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907548) | [9m07s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907548) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [9m03s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907556) | [9m03s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907556) | [9m03s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907556) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [8m34s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907601) | [8m34s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907601) | [8m34s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907601) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [7m51s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907573) | [7m51s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907573) | [7m51s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907573) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [7m16s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907620) | [7m16s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907620) | [7m16s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907620) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [4m49s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907523) | [4m49s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907523) | [4m49s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907523) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [4m33s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907452) | [4m33s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907452) | [4m33s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907452) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [3m54s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907512) | [3m54s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907512) | [3m54s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907512) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [1m50s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87009646410) | [1m50s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87009646410) | [1m50s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87009646410) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 1 | 0 | — | — | [1m24s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907624) | [1m24s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907624) | [1m24s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907624) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 1 | 0 | — | — | [53s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907599) | [53s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907599) | [53s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907599) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640856) | [9s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640856) | [9s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640856) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640850) | [9s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640850) | [9s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640850) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640794) | [8s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640794) | [8s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640794) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640844) | [8s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640844) | [8s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640844) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640742) | [7s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640742) | [7s](https://github.com/iree-org/iree/actions/runs/29309357755/job/87009640742) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 166 | 2% (3/165) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 143 | 1% (1/142) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 133 | 11% (14/132) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 122 | 1% (1/121) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 39 | 13% (5/39) |  | 55m39s ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 19h47m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
