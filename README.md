# iree-ci-monitor

_Updated: 2026-10-28 06:04 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 20 | 6 | [2h33m](https://github.com/iree-org/iree/actions/runs/40671181611/job/122762427807) | 2026-10-28 06:02 PDT | 1 | [31m38s](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925530) | [2h38m](https://github.com/iree-org/iree/actions/runs/40670133757/job/122757674303) | 0% (0/4) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 20 | 5 | [2h17m](https://github.com/iree-org/iree/actions/runs/40670762825/job/122769876620) | 2026-10-28 06:02 PDT | 1 | [42m58s](https://github.com/iree-org/iree/actions/runs/40680186137/job/122793087063) | [2h24m](https://github.com/iree-org/iree/actions/runs/40670133757/job/122757674310) | 0% (0/7) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 20 | 9 | [2h44m](https://github.com/iree-org/iree/actions/runs/40670133757/job/122757674253) | 2026-10-28 06:02 PDT | 0 | [33m05s](https://github.com/iree-org/iree/actions/runs/40663982897/job/122745374091) | [2h10m](https://github.com/iree-org/iree/actions/runs/40663982897/job/122745374159) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 10 | 2 | [1h52m](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925334) | 2026-10-28 06:02 PDT | 0 | [32m39s](https://github.com/iree-org/iree/actions/runs/40670133757/job/122757674401) | [2h01m](https://github.com/iree-org/iree/actions/runs/40671181611/job/122762427814) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [44m14s](https://github.com/iree-org/iree/actions/runs/40680186137/job/122793087180) | [1h42m](https://github.com/iree-org/iree/actions/runs/40671181611/job/122762427811) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 20 | 6 | [2h44m](https://github.com/iree-org/iree/actions/runs/40670133757/job/122757674408) | 2026-10-28 06:02 PDT | 0 | [23m53s](https://github.com/iree-org/iree/actions/runs/40670762825/job/122769876676) | [1h23m](https://github.com/iree-org/iree/actions/runs/40663982897/job/122745374188) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 10 | 0 | — | — | 0 | [9m04s](https://github.com/iree-org/iree/actions/runs/40686515704/job/122815095000) | [37m07s](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925008) | 0% (0/4) | `shark75-ci` |
| `azure-linux-scale` | ossci | 87 | 0 | — | — | 9 | [9s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829887254) | [2m14s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822129158) | 6% (2/35) | 87 |
| `ubuntu-24.04-arm` | github-hosted | 42 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/40686515652/job/122810245771) | [2m03s](https://github.com/iree-org/iree/actions/runs/40663982906/job/122734467069) | 0% (0/15) | 42 |
| `macos-15` | github-hosted | 42 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/40670762704/job/122766836808) | [1m50s](https://github.com/iree-org/iree/actions/runs/40663982906/job/122734466877) | 0% (0/15) | 42 |
| `windows-2022` | github-hosted | 41 | 0 | — | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/40664983499/job/122776853373) | [1m41s](https://github.com/iree-org/iree/actions/runs/40663982906/job/122734466905) | 0% (0/15) | 41 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m29s](https://github.com/iree-org/iree/actions/runs/40663611062/job/122732471733) | [1m29s](https://github.com/iree-org/iree/actions/runs/40663611062/job/122732471733) | 100% (1/1) | 1 |
| `ubuntu-24.04` | github-hosted | 238 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/40671181611/job/122762427765) | [1m16s](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925523) | 2% (2/88) | 236 |
| `ubuntu-latest` | github-hosted | 30 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/40671958936/job/122760782116) | [1m11s](https://github.com/iree-org/iree/actions/runs/40663976881/job/122733707609) | 0% (0/15) | 30 |
| `azure-windows-scale` | ossci | 13 | 0 | — | — | 2 | [1s](https://github.com/iree-org/iree/actions/runs/40671181470/job/122758334607) | [2s](https://github.com/iree-org/iree/actions/runs/40691960841/job/122829887331) | 0% (0/4) | 13 |
| `Linux,X64,iree-w7900` | self-hosted | 10 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [2h44m](https://github.com/iree-org/iree/actions/runs/40670133757/job/122757674253) | 2026-10-28 06:02 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [2h44m](https://github.com/iree-org/iree/actions/runs/40670133757/job/122757674408) | 2026-10-28 06:02 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [2h33m](https://github.com/iree-org/iree/actions/runs/40671181611/job/122762427779) | 2026-10-28 06:02 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [2h33m](https://github.com/iree-org/iree/actions/runs/40671181611/job/122762427807) | 2026-10-28 06:02 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [2h33m](https://github.com/iree-org/iree/actions/runs/40671181611/job/122762427972) | 2026-10-28 06:02 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [2h17m](https://github.com/iree-org/iree/actions/runs/40670762825/job/122769876597) | 2026-10-28 06:02 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `fix-webgpu-mapped-buffer-access` | pull_request |
| [2h17m](https://github.com/iree-org/iree/actions/runs/40670762825/job/122769876604) | 2026-10-28 06:02 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `fix-webgpu-mapped-buffer-access` | pull_request |
| [2h17m](https://github.com/iree-org/iree/actions/runs/40670762825/job/122769876620) | 2026-10-28 06:02 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | `fix-webgpu-mapped-buffer-access` | pull_request |
| [2h17m](https://github.com/iree-org/iree/actions/runs/40670762825/job/122769876700) | 2026-10-28 06:02 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `fix-webgpu-mapped-buffer-access` | pull_request |
| [2h17m](https://github.com/iree-org/iree/actions/runs/40670762825/job/122769876923) | 2026-10-28 06:02 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `fix-webgpu-mapped-buffer-access` | pull_request |
| [1h52m](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925009) | 2026-10-28 06:02 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | `users/rpqt/fix-llvmcpu-obj-write` | pull_request |
| [1h52m](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925334) | 2026-10-28 06:02 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `users/rpqt/fix-llvmcpu-obj-write` | pull_request |
| [1h52m](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925388) | 2026-10-28 06:02 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `users/rpqt/fix-llvmcpu-obj-write` | pull_request |
| [1h52m](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925437) | 2026-10-28 06:02 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `users/rpqt/fix-llvmcpu-obj-write` | pull_request |
| [1h24m](https://github.com/iree-org/iree/actions/runs/40680186137/job/122793086936) | 2026-10-28 06:02 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 2 | [1h52m](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925009) | 2026-10-28 06:02 PDT | [22m56s](https://github.com/iree-org/iree/actions/runs/40670133757/job/122757674238) | [3h11m](https://github.com/iree-org/iree/actions/runs/40663982897/job/122745374012) | [3h11m](https://github.com/iree-org/iree/actions/runs/40663982897/job/122745374012) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 10 | 6 | [2h44m](https://github.com/iree-org/iree/actions/runs/40670133757/job/122757674253) | 2026-10-28 06:02 PDT | [19m02s](https://github.com/iree-org/iree/actions/runs/40666157756/job/122746308765) | [33m05s](https://github.com/iree-org/iree/actions/runs/40663982897/job/122745374091) | [33m05s](https://github.com/iree-org/iree/actions/runs/40663982897/job/122745374091) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 5 | [2h44m](https://github.com/iree-org/iree/actions/runs/40670133757/job/122757674408) | 2026-10-28 06:02 PDT | [30m40s](https://github.com/iree-org/iree/actions/runs/40666157756/job/122746308432) | [1h21m](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925296) | [1h21m](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925296) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 4 | [2h33m](https://github.com/iree-org/iree/actions/runs/40671181611/job/122762427807) | 2026-10-28 06:02 PDT | [31m38s](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925530) | [2h38m](https://github.com/iree-org/iree/actions/runs/40670133757/job/122757674303) | [2h38m](https://github.com/iree-org/iree/actions/runs/40670133757/job/122757674303) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 3 | [2h17m](https://github.com/iree-org/iree/actions/runs/40670762825/job/122769876620) | 2026-10-28 06:02 PDT | [1h13m](https://github.com/iree-org/iree/actions/runs/40663982897/job/122745374003) | [2h24m](https://github.com/iree-org/iree/actions/runs/40670133757/job/122757674310) | [2h24m](https://github.com/iree-org/iree/actions/runs/40670133757/job/122757674310) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 10 | 3 | [2h17m](https://github.com/iree-org/iree/actions/runs/40670762825/job/122769876597) | 2026-10-28 06:02 PDT | [1h00m](https://github.com/iree-org/iree/actions/runs/40671181611/job/122762427886) | [2h10m](https://github.com/iree-org/iree/actions/runs/40663982897/job/122745374159) | [2h10m](https://github.com/iree-org/iree/actions/runs/40663982897/job/122745374159) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 10 | 2 | [1h52m](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925334) | 2026-10-28 06:02 PDT | [32m39s](https://github.com/iree-org/iree/actions/runs/40670133757/job/122757674401) | [2h01m](https://github.com/iree-org/iree/actions/runs/40671181611/job/122762427814) | [2h01m](https://github.com/iree-org/iree/actions/runs/40671181611/job/122762427814) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 0 | — | — | [44m14s](https://github.com/iree-org/iree/actions/runs/40680186137/job/122793087180) | [1h42m](https://github.com/iree-org/iree/actions/runs/40671181611/job/122762427811) | [1h42m](https://github.com/iree-org/iree/actions/runs/40671181611/job/122762427811) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 1 | [1h24m](https://github.com/iree-org/iree/actions/runs/40680186137/job/122793087212) | 2026-10-28 06:02 PDT | [18m54s](https://github.com/iree-org/iree/actions/runs/40660371052/job/122725296185) | [1h41m](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925551) | [1h41m](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925551) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 2 | [1h24m](https://github.com/iree-org/iree/actions/runs/40680186137/job/122793086960) | 2026-10-28 06:02 PDT | [13m42s](https://github.com/iree-org/iree/actions/runs/40670133757/job/122757674312) | [1h36m](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925360) | [1h36m](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925360) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 10 | 0 | — | — | [9m04s](https://github.com/iree-org/iree/actions/runs/40686515704/job/122815095000) | [37m07s](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925008) | [37m07s](https://github.com/iree-org/iree/actions/runs/40664983518/job/122780925008) | 1 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40670762825/job/122769876644) | [2m30s](https://github.com/iree-org/iree/actions/runs/40666157756/job/122746308578) | [2m30s](https://github.com/iree-org/iree/actions/runs/40666157756/job/122746308578) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 13 | 0 | — | — | [1m17s](https://github.com/iree-org/iree/actions/runs/40670133825/job/122754584908) | [2m22s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822128908) | [2m48s](https://github.com/iree-org/iree/actions/runs/40673981646/job/122767667057) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 13 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/40666157789/job/122742258716) | [2m19s](https://github.com/iree-org/iree/actions/runs/40663982906/job/122734467128) | [3m15s](https://github.com/iree-org/iree/actions/runs/40671181470/job/122758334282) | 13 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40671181611/job/122762427816) | [2m14s](https://github.com/iree-org/iree/actions/runs/40666157756/job/122746308487) | [2m14s](https://github.com/iree-org/iree/actions/runs/40666157756/job/122746308487) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 6 | 0 | — | — | [24s](https://github.com/iree-org/iree/actions/runs/40663982906/job/122734467142) | [2m14s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822129158) | [2m14s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822129158) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 13 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40666157789/job/122742258591) | [2m06s](https://github.com/iree-org/iree/actions/runs/40663982906/job/122734466991) | [3m06s](https://github.com/iree-org/iree/actions/runs/40671181470/job/122758334206) | 13 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 13 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40666157789/job/122742258988) | [2m03s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822129309) | [2m11s](https://github.com/iree-org/iree/actions/runs/40663982906/job/122734467143) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 13 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822128759) | [2m03s](https://github.com/iree-org/iree/actions/runs/40663982906/job/122734467069) | [3m33s](https://github.com/iree-org/iree/actions/runs/40671181470/job/122758334351) | 13 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 13 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/40670762704/job/122766837079) | [2m02s](https://github.com/iree-org/iree/actions/runs/40689988417/job/122822129139) | [2m48s](https://github.com/iree-org/iree/actions/runs/40673981646/job/122767667079) | 13 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 238 | 3% (7/237) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 285 | 1% (3/284) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 2h33m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 2h44m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 2h44m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job observed waiting 2h17m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h42m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h38m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h10m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h23m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h24m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
