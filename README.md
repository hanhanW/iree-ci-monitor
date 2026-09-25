# iree-ci-monitor

_Updated: 2026-09-25 04:55 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [36m14s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808052) | [36m14s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808052) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [22m38s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808044) | [31m45s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808076) | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [29m32s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807982) | [29m32s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807982) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [23m19s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808115) | [23m19s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808115) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [17m42s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808045) | [17m42s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808045) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [4m24s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807958) | [14m44s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808154) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808021) | [9m48s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808133) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808169) | [4m31s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808041) | — | `shark75-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m32s](https://github.com/iree-org/iree/actions/runs/36118611019/job/108018494577) | [1m32s](https://github.com/iree-org/iree/actions/runs/36118611019/job/108018494577) | 100% (1/1) | 1 |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423542) | [9s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423428) | 50% (1/2) | 7 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/36118589395/job/108018425521) | [9s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423375) | — | 6 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/36097861299/job/107953869331) | [5s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423423) | — | 6 |
| `ubuntu-24.04` | github-hosted | 38 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108044372043) | [3s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808181) | 0% (0/4) | 36 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/36127894339/job/108048147317) | [3s](https://github.com/iree-org/iree/actions/runs/36127894339/job/108048147436) | — | 3 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423297) | [3s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423381) | — | 5 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423507) | [2s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423507) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 1 | 0 | — | — | [36m14s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808052) | [36m14s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808052) | [36m14s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808052) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [31m45s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808076) | [31m45s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808076) | [31m45s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808076) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [29m32s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807982) | [29m32s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807982) | [29m32s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807982) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [23m19s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808115) | [23m19s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808115) | [23m19s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808115) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [22m38s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808044) | [22m38s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808044) | [22m38s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808044) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [17m42s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808045) | [17m42s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808045) | [17m42s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808045) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [14m44s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808154) | [14m44s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808154) | [14m44s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808154) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [9m48s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808133) | [9m48s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808133) | [9m48s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808133) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [4m31s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808041) | [4m31s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808041) | [4m31s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046808041) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [4m24s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807958) | [4m24s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807958) | [4m24s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807958) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m32s](https://github.com/iree-org/iree/actions/runs/36118611019/job/108018494577) | [1m32s](https://github.com/iree-org/iree/actions/runs/36118611019/job/108018494577) | [1m32s](https://github.com/iree-org/iree/actions/runs/36118611019/job/108018494577) | 1 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 1 | 0 | — | — | [39s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807991) | [39s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807991) | [39s](https://github.com/iree-org/iree/actions/runs/36126704733/job/108046807991) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [37s](https://github.com/iree-org/iree/actions/runs/36097861299/job/107953869312) | [37s](https://github.com/iree-org/iree/actions/runs/36097861299/job/107953869312) | [37s](https://github.com/iree-org/iree/actions/runs/36097861299/job/107953869312) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423428) | [9s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423428) | [9s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423428) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423338) | [9s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423338) | [9s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423338) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423375) | [9s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423375) | [9s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423375) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423542) | [8s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423542) | [8s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423542) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423576) | [8s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423576) | [8s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423576) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423501) | [8s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423501) | [8s](https://github.com/iree-org/iree/actions/runs/36126704661/job/108044423501) | 1 |
| `.github/workflows/ci_macos_arm64_clang.yml` | macos_arm64_clang | `macos-14` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36118589395/job/108018425521) | [8s](https://github.com/iree-org/iree/actions/runs/36118589395/job/108018425521) | [8s](https://github.com/iree-org/iree/actions/runs/36118589395/job/108018425521) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 364 | 1% (5/364) |  | 9m07s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 281 | 3% (9/281) |  | 15m54s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
