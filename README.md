# iree-ci-monitor

_Updated: 2026-06-17 06:33 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [19m29s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714975) | [22m24s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934545) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934494) | [20m45s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714983) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [14m58s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714904) | [17m10s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934572) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [4m48s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934369) | [15m57s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714862) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [10m15s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934567) | [13m25s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934510) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [6m26s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934564) | [13m11s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714958) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [9m24s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934547) | [10m37s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714970) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714844) | [9m38s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934230) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934525) | [6m14s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714856) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714968) | [4m39s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934496) | 0% (0/1) | `shark01-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 31 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/27687237427/job/81889317974) | [2m21s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559418) | 0% (0/8) | 30 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m29s](https://github.com/iree-org/iree/actions/runs/27683833835/job/81877628305) | [1m29s](https://github.com/iree-org/iree/actions/runs/27683833835/job/81877628305) | 0% (0/1) | 1 |
| `ubuntu-24.04` | github-hosted | 105 | 0 | — | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/27671013698/job/81835165358) | [39s](https://github.com/iree-org/iree/actions/runs/27685657635/job/81883659367) | 9% (2/23) | 104 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27685657711/job/81888443279) | [19s](https://github.com/iree-org/iree/actions/runs/27685657711/job/81888443305) | 0% (0/4) | 16 |
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27687233253/job/81888854029) | [9s](https://github.com/iree-org/iree/actions/runs/27687233253/job/81888854049) | 0% (0/3) | 18 |
| `macos-14` | github-hosted | 18 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559229) | [7s](https://github.com/iree-org/iree/actions/runs/27687237427/job/81889317884) | 0% (0/3) | 18 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27687237427/job/81889317948) | [6s](https://github.com/iree-org/iree/actions/runs/27685657635/job/81883659424) | 0% (0/3) | 18 |
| `windows-2022` | github-hosted | 17 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27671013698/job/81835165379) | [6s](https://github.com/iree-org/iree/actions/runs/27687237427/job/81889317932) | 0% (0/3) | 17 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/27683789205/job/81877481844) | [4s](https://github.com/iree-org/iree/actions/runs/27683789205/job/81877481844) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27685657711/job/81888443219) | [2s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934128) | 0% (0/1) | 4 |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714838) | [2s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934205) | 0% (0/1) | `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27685657711/job/81888443228) | [2s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934630) | 0% (0/1) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 5 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559490) | [1s](https://github.com/iree-org/iree/actions/runs/27687237427/job/81889318010) | 0% (0/1) | 5 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [7m23s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714861) | [22m24s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934545) | [22m24s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934545) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934385) | [20m45s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714983) | [20m45s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714983) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [11m45s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934492) | [19m29s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714975) | [19m29s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714975) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [7m30s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833715055) | [17m10s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934572) | [17m10s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934572) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [4m48s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934369) | [15m57s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714862) | [15m57s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714862) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934494) | [15m26s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714895) | [15m26s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714895) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [14m58s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714904) | [15m04s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934617) | [15m04s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934617) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [5m17s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714971) | [13m25s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934510) | [13m25s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934510) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [6m26s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934564) | [13m11s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714958) | [13m11s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714958) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [9m24s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934547) | [10m37s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714970) | [10m37s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714970) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714866) | [10m15s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934567) | [10m15s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934567) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714844) | [9m38s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934230) | [9m38s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934230) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934525) | [6m14s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714856) | [6m14s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714856) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714968) | [4m39s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934496) | [4m39s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934496) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 5 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/27685657635/job/81883659443) | [2m28s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559579) | [2m28s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559579) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 5 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27669973842/job/81831955584) | [2m21s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559418) | [2m21s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559418) | 5 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 5 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/27687237427/job/81889317947) | [2m03s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559368) | [2m03s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559368) | 5 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 5 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27669973842/job/81831955557) | [1m35s](https://github.com/iree-org/iree/actions/runs/27685657635/job/81883659355) | [1m35s](https://github.com/iree-org/iree/actions/runs/27685657635/job/81883659355) | 5 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m29s](https://github.com/iree-org/iree/actions/runs/27683833835/job/81877628305) | [1m29s](https://github.com/iree-org/iree/actions/runs/27683833835/job/81877628305) | [1m29s](https://github.com/iree-org/iree/actions/runs/27683833835/job/81877628305) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 5 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27687237427/job/81889317934) | [1m24s](https://github.com/iree-org/iree/actions/runs/27685657635/job/81883659390) | [1m24s](https://github.com/iree-org/iree/actions/runs/27685657635/job/81883659390) | 5 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 246 | 0% (1/246) |  | 56m38s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 173 | 0% (0/173) |  | 56m46s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 184 | 1% (2/184) |  | 59m59s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 194 | 5% (10/194) |  | 1h00m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 57 | 0% (0/57) |  | 1h13m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
