# iree-ci-monitor

_Updated: 2026-05-18 06:37 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `azure-linux-scale` | ossci | 18 | 9 | [32m30s](https://github.com/iree-org/iree/actions/runs/26035296996/job/76531655681) | 2026-05-18 06:37 PDT | 6 | [33m51s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76529426060) | [38m58s](https://github.com/iree-org/iree/actions/runs/26034656897/job/76529451600) | 0% (0/2) | 9 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 2 | [1m20s](https://github.com/iree-org/iree/actions/runs/26035296996/job/76531655585) | [4m17s](https://github.com/iree-org/iree/actions/runs/26036368760/job/76535560323) | — | 3 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 1 | [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292611) | 2026-05-18 06:37 PDT | 1 | [2m06s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292589) | [2m06s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292589) | — | `shark01-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 3 | [2m40s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292534) | 2026-05-18 06:37 PDT | 1 | [1m23s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292836) | [1m23s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292836) | — | 1 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m22s](https://github.com/iree-org/iree/actions/runs/26028567341/job/76508245620) | [1m22s](https://github.com/iree-org/iree/actions/runs/26028567341/job/76508245620) | 0% (0/1) | 1 |
| `ubuntu-24.04` | github-hosted | 51 | 2 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | 8 | [3s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76529383058) | [4s](https://github.com/iree-org/iree/actions/runs/26035297014/job/76531615077) | 18% (2/11) | 49 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26035296996/job/76531655343) | [4s](https://github.com/iree-org/iree/actions/runs/26034656897/job/76529451267) | 0% (0/3) | 12 |
| `macos-14` | github-hosted | 12 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426317) | [4s](https://github.com/iree-org/iree/actions/runs/26036368760/job/76535560024) | 0% (0/3) | 12 |
| `windows-2022` | github-hosted | 11 | 0 | — | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/26035296996/job/76531655266) | [4s](https://github.com/iree-org/iree/actions/runs/26036368760/job/76535559727) | 0% (0/1) | 11 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26029577124/job/76511711334) | [4s](https://github.com/iree-org/iree/actions/runs/26029576112/job/76511709088) | 0% (0/3) | 9 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292375) | [3s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292375) | — | `shark01-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292388) | [3s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292388) | — | `iree-mi308-1` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292453) | [3s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292453) | — | 1 |
| `Linux,X64,gfx1201` | self-hosted | 2 | 1 | [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292654) | 2026-05-18 06:37 PDT | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292629) | [2s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292629) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 1 | [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292721) | 2026-05-18 06:37 PDT | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292731) | [2s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292731) | — | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292872) | [2s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292872) | — | `shark55-ci` |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26028563968/job/76508234902) | [2s](https://github.com/iree-org/iree/actions/runs/26028563968/job/76508234902) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 1 | [2m40s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292457) | 2026-05-18 06:37 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 2 | 2 | [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292684) | 2026-05-18 06:37 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292718) | 2026-05-18 06:37 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 1 | [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292738) | 2026-05-18 06:37 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 1 | [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292768) | 2026-05-18 06:37 PDT | 0 | 0s | 0s | — | 0 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 1 | [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292967) | 2026-05-18 06:37 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [32m30s](https://github.com/iree-org/iree/actions/runs/26035296996/job/76531655681) | 2026-05-18 06:37 PDT | `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | `new-lds-promotion` | pull_request |
| [32m30s](https://github.com/iree-org/iree/actions/runs/26035296996/job/76531655753) | 2026-05-18 06:37 PDT | `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | `new-lds-promotion` | pull_request |
| [32m29s](https://github.com/iree-org/iree/actions/runs/26035297010/job/76531659482) | 2026-05-18 06:37 PDT | `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | `new-lds-promotion` | pull_request |
| [11m32s](https://github.com/iree-org/iree/actions/runs/26036368777/job/76535561822) | 2026-05-18 06:37 PDT | `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | `main` | push |
| [11m32s](https://github.com/iree-org/iree/actions/runs/26036368760/job/76535559820) | 2026-05-18 06:37 PDT | `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | `main` | push |
| [11m32s](https://github.com/iree-org/iree/actions/runs/26036368760/job/76535559999) | 2026-05-18 06:37 PDT | `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | `main` | push |
| [11m32s](https://github.com/iree-org/iree/actions/runs/26036368760/job/76535560016) | 2026-05-18 06:37 PDT | `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | `main` | push |
| [11m32s](https://github.com/iree-org/iree/actions/runs/26036368760/job/76535560099) | 2026-05-18 06:37 PDT | `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | `main` | push |
| [11m32s](https://github.com/iree-org/iree/actions/runs/26036368760/job/76535560285) | 2026-05-18 06:37 PDT | `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | `main` | push |
| [2m40s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292457) | 2026-05-18 06:37 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/keshavvinayak01/gpuvectoralloc-swizzle` | pull_request |
| [2m40s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292534) | 2026-05-18 06:37 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `users/keshavvinayak01/gpuvectoralloc-swizzle` | pull_request |
| [2m40s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292552) | 2026-05-18 06:37 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | `users/keshavvinayak01/gpuvectoralloc-swizzle` | pull_request |
| [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292611) | 2026-05-18 06:37 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | `users/keshavvinayak01/gpuvectoralloc-swizzle` | pull_request |
| [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292654) | 2026-05-18 06:37 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `users/keshavvinayak01/gpuvectoralloc-swizzle` | pull_request |
| [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292684) | 2026-05-18 06:37 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/keshavvinayak01/gpuvectoralloc-swizzle` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | 3 | 1 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | [3s](https://github.com/iree-org/iree/actions/runs/26034656920/job/76529382588) | [4s](https://github.com/iree-org/iree/actions/runs/26035297014/job/76531615077) | [4s](https://github.com/iree-org/iree/actions/runs/26035297014/job/76531615077) | 2 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 4 | 1 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295886/job/76143196900) | 2026-05-15 05:58 PDT | [3s](https://github.com/iree-org/iree/actions/runs/26035296996/job/76531655679) | [4s](https://github.com/iree-org/iree/actions/runs/26034656897/job/76529451226) | [4s](https://github.com/iree-org/iree/actions/runs/26034656897/job/76529451226) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 3 | 1 | [11m32s](https://github.com/iree-org/iree/actions/runs/26036368760/job/76535560016) | 2026-05-18 06:37 PDT | [27m21s](https://github.com/iree-org/iree/actions/runs/26035296996/job/76531655603) | [38m58s](https://github.com/iree-org/iree/actions/runs/26034656897/job/76529451600) | [38m58s](https://github.com/iree-org/iree/actions/runs/26034656897/job/76529451600) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 3 | 2 | [32m30s](https://github.com/iree-org/iree/actions/runs/26035296996/job/76531655753) | 2026-05-18 06:37 PDT | [38m53s](https://github.com/iree-org/iree/actions/runs/26034656897/job/76529451491) | [38m53s](https://github.com/iree-org/iree/actions/runs/26034656897/job/76529451491) | [38m53s](https://github.com/iree-org/iree/actions/runs/26034656897/job/76529451491) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 3 | 2 | [32m30s](https://github.com/iree-org/iree/actions/runs/26035296996/job/76531655681) | 2026-05-18 06:37 PDT | [38m23s](https://github.com/iree-org/iree/actions/runs/26034656897/job/76529451431) | [38m23s](https://github.com/iree-org/iree/actions/runs/26034656897/job/76529451431) | [38m23s](https://github.com/iree-org/iree/actions/runs/26034656897/job/76529451431) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 3 | 1 | [11m32s](https://github.com/iree-org/iree/actions/runs/26036368760/job/76535559999) | 2026-05-18 06:37 PDT | [26m52s](https://github.com/iree-org/iree/actions/runs/26035296996/job/76531655549) | [37m40s](https://github.com/iree-org/iree/actions/runs/26034656897/job/76529451346) | [37m40s](https://github.com/iree-org/iree/actions/runs/26034656897/job/76529451346) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 3 | 2 | [32m29s](https://github.com/iree-org/iree/actions/runs/26035297010/job/76531659482) | 2026-05-18 06:37 PDT | [33m51s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76529426060) | [33m51s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76529426060) | [33m51s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76529426060) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 1 | [11m32s](https://github.com/iree-org/iree/actions/runs/26036368760/job/76535560099) | 2026-05-18 06:37 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 3 | 0 | — | — | [1m20s](https://github.com/iree-org/iree/actions/runs/26035296996/job/76531655585) | [4m17s](https://github.com/iree-org/iree/actions/runs/26036368760/job/76535560323) | [4m17s](https://github.com/iree-org/iree/actions/runs/26036368760/job/76535560323) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 1 | [2m40s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292534) | 2026-05-18 06:37 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 1 | [2m40s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292457) | 2026-05-18 06:37 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 1 | [2m40s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292552) | 2026-05-18 06:37 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 1 | [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292768) | 2026-05-18 06:37 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 1 | [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292718) | 2026-05-18 06:37 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 1 | [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292738) | 2026-05-18 06:37 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 1 | [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292611) | 2026-05-18 06:37 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 1 | [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292736) | 2026-05-18 06:37 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 1 | [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292654) | 2026-05-18 06:37 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 1 | [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292684) | 2026-05-18 06:37 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 1 | [2m39s](https://github.com/iree-org/iree/actions/runs/26034656888/job/76537292815) | 2026-05-18 06:37 PDT | 0s | 0s | 0s | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark01-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 894 | 1% (11/893) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 973 | 6% (56/972) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1096 | 2% (22/1093) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark55-ci`, `self-hosted,persistent-cache,Linux,X64` | 857 | 1% (11/856) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 300 | 2% (5/299) | yes | running |

## Alerts

- **[stale-queued]** `ubuntu-24.04` oldest queued job observed waiting 4h53m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
