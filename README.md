# iree-ci-monitor

_Updated: 2026-07-31 05:58 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 10 | 0 | — | — | 0 | [17m13s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514893) | [31m25s](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445046) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 5 | 0 | — | — | 0 | [21m52s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526264) | [26m08s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454920) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [14m38s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514858) | [25m44s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526395) | 0% (0/3) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 5 | 0 | — | — | 0 | [10m12s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91129775390) | [21m46s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514670) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 10 | 0 | — | — | 0 | [9m54s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91129775504) | [18m20s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526335) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 10 | 0 | — | — | 0 | [10m56s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454946) | [17m37s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122515038) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514590) | [15m45s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526193) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 10 | 0 | — | — | 0 | [4m38s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526384) | [13m56s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454997) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108444914) | [11m47s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91129775205) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [10m15s](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445019) | [11m12s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514861) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514567) | [10m29s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454794) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 30 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/30607758207/job/91085256085) | [1m50s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91119662725) | 0% (0/20) | 30 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m25s](https://github.com/iree-org/iree/actions/runs/30622422892/job/91129826260) | [1m25s](https://github.com/iree-org/iree/actions/runs/30622422892/job/91129826260) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 17 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30621832501/job/91127999687) | [1m13s](https://github.com/iree-org/iree/actions/runs/30610564282/job/91092203892) | 0% (0/9) | 17 |
| `macos-14` | github-hosted | 18 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/30608579302/job/91086136352) | [54s](https://github.com/iree-org/iree/actions/runs/30615166827/job/91106604234) | 0% (0/9) | 18 |
| `ubuntu-24.04` | github-hosted | 105 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91129775294) | [9s](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108444975) | 4% (2/56) | 105 |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30627239581/job/91145233697) | [9s](https://github.com/iree-org/iree/actions/runs/30622178588/job/91129059299) | 0% (0/9) | 24 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30610564282/job/91092203912) | [5s](https://github.com/iree-org/iree/actions/runs/30617667412/job/91119653806) | 0% (0/9) | 18 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/30622369603/job/91129661042) | [3s](https://github.com/iree-org/iree/actions/runs/30622369603/job/91129661042) | — | 1 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454863) | [2s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514530) | 0% (0/3) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 5 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30615166827/job/91106604273) | [1s](https://github.com/iree-org/iree/actions/runs/30621832501/job/91127999757) | 0% (0/3) | 5 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 5 | 5 | [6h50m](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454811) | 2026-07-31 05:57 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [6h50m](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454811) | 2026-07-31 05:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `fix/24751-tensor-slice-parameter-fold` | pull_request |
| [6h04m](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526156) | 2026-07-31 05:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [4h40m](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445151) | 2026-07-31 05:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [3h27m](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514612) | 2026-07-31 05:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `fix/23345-custom-op-static-loop-ranges` | pull_request |
| [2h50m](https://github.com/iree-org/iree/actions/runs/30621832279/job/91129775249) | 2026-07-31 05:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 5 | 5 | [6h50m](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454811) | 2026-07-31 05:57 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [17m13s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514893) | [31m25s](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445046) | [31m25s](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445046) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 5 | 0 | — | — | [21m52s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526264) | [26m08s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454920) | [26m08s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454920) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 5 | 0 | — | — | [14m38s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514858) | [25m44s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526395) | [25m44s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526395) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 5 | 0 | — | — | [10m12s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91129775390) | [21m46s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514670) | [21m46s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514670) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [17m45s](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445214) | [21m19s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454938) | [21m19s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454938) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 5 | 0 | — | — | [9m24s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454909) | [18m20s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526335) | [18m20s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526335) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [10m56s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454946) | [17m37s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122515038) | [17m37s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122515038) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [11m37s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91129775336) | [17m29s](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445034) | [17m29s](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445034) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 5 | 0 | — | — | [16m28s](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445169) | [17m08s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526388) | [17m08s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526388) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514590) | [15m45s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526193) | [15m45s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526193) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [6m30s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514819) | [13m56s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454997) | [13m56s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454997) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108444914) | [11m47s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91129775205) | [11m47s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91129775205) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 5 | 0 | — | — | [10m15s](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445019) | [11m12s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514861) | [11m12s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514861) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514567) | [10m29s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454794) | [10m29s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454794) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91129775370) | [7m58s](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108444985) | [7m58s](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108444985) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 5 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/30610564282/job/91092203970) | [1m50s](https://github.com/iree-org/iree/actions/runs/30617667412/job/91119654052) | [1m50s](https://github.com/iree-org/iree/actions/runs/30617667412/job/91119654052) | 5 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 5 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91128000356) | [1m50s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91119662725) | [1m50s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91119662725) | 5 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 5 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445137) | [1m47s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454960) | [1m47s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454960) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 5 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/30610564282/job/91092203961) | [1m35s](https://github.com/iree-org/iree/actions/runs/30617667412/job/91119654098) | [1m35s](https://github.com/iree-org/iree/actions/runs/30617667412/job/91119654098) | 5 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 121 | 1% (1/121) |  | 2h31m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 174 | 0% (0/174) |  | 2h34m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 125 | 1% (1/125) |  | 2h37m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 165 | 2% (4/165) |  | 2h38m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 39 | 3% (1/39) |  | 2h40m ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 6h50m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
