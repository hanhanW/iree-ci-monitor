# iree-ci-monitor

_Updated: 2026-09-25 10:16 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [33m24s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611730) | [43m19s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611780) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [40m57s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611809) | [42m07s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611769) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [17m42s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808045) | [37m50s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611594) | — | `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [6m47s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611743) | [36m14s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808052) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 1 | [49m03s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611992) | 2026-09-25 10:15 PDT | 0 | [22m38s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808044) | [31m45s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808076) | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [8m36s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611478) | [29m32s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807982) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [23m19s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808115) | [26m22s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611673) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [12m43s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611761) | [14m44s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808154) | — | `shark55-ci`, `shark75-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m32s](https://github.com/iree-org/iree/actions/runs/36118611019/job/108018494577) | [1m32s](https://github.com/iree-org/iree/actions/runs/36118611019/job/108018494577) | 100% (1/1) | 1 |
| `azure-linux-scale` | ossci | 12 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108044434792) | [19s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154140113) | 50% (1/2) | 12 |
| `macos-14` | github-hosted | 7 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423338) | [10s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139854) | 0% (0/1) | 7 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139781) | [5s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423423) | — | 6 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/36127894339/job/108048147436) | [3s](https://github.com/iree-org/iree/actions/runs/36145819953/job/108106615870) | — | 9 |
| `ubuntu-24.04` | github-hosted | 47 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36127845010/job/108047980888) | [3s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139701) | 33% (1/3) | 46 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139909) | [3s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139833) | — | 6 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423507) | [2s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154140265) | — | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [49m03s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611992) | 2026-09-25 10:15 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/tmahlatini/riscv-cpu-features-declobber` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 1 | [49m03s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611992) | 2026-09-25 10:15 PDT | [22m38s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808044) | [22m38s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808044) | [22m38s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808044) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808169) | [43m19s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611780) | [43m19s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611780) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [9m48s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808133) | [42m07s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611769) | [42m07s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611769) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808021) | [40m57s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611809) | [40m57s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611809) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [17m42s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808045) | [37m50s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611594) | [37m50s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611594) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 2 | 0 | — | — | [6m47s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611743) | [36m14s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808052) | [36m14s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808052) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [4m31s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808041) | [33m24s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611730) | [33m24s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611730) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [22m17s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611964) | [31m45s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808076) | [31m45s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808076) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [8m36s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611478) | [29m32s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807982) | [29m32s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807982) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [23m19s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808115) | [26m22s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611673) | [26m22s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611673) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [12m43s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611761) | [14m44s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808154) | [14m44s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808154) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [16s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611508) | [4m24s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807958) | [4m24s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807958) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m32s](https://github.com/iree-org/iree/actions/runs/36118611019/job/108018494577) | [1m32s](https://github.com/iree-org/iree/actions/runs/36118611019/job/108018494577) | [1m32s](https://github.com/iree-org/iree/actions/runs/36118611019/job/108018494577) | 1 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36159468912/job/108156611516) | [39s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807991) | [39s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807991) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423508) | [21s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154140335) | [21s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154140335) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423428) | [19s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139995) | [19s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139995) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423542) | [19s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139939) | [19s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139939) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423576) | [19s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154140113) | [19s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154140113) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423375) | [10s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139854) | [10s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139854) | 2 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423338) | [9s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139643) | [9s](https://github.com/iree-org/iree/actions/runs/36159468989/job/108154139643) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 371 | 1% (5/371) |  | 2m40s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 285 | 3% (9/285) |  | 4m47s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
