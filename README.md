# iree-ci-monitor

_Updated: 2026-10-15 10:05 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [27m41s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891615) | [35m34s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891426) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [13m19s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065235) | [33m16s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065533) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [23m53s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891752) | [30m38s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065254) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [6m01s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891591) | [21m18s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065120) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [8m43s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065116) | [10m45s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891525) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065055) | [8m56s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891567) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [1m37s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891624) | [5m35s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065237) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m27s](https://github.com/iree-org/iree/actions/runs/38713201392/job/116349449223) | [1m27s](https://github.com/iree-org/iree/actions/runs/38713201392/job/116349449223) | 100% (1/1) | 1 |
| `azure-linux-scale` | ossci | 15 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/38764327569/job/116523569270) | [1m19s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486790701) | 11% (1/9) | 15 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38764327569/job/116523569285) | [38s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486789341) | 0% (0/3) | 6 |
| `macos-15` | github-hosted | 7 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486789578) | [8s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486789730) | 0% (0/4) | 7 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486789754) | [5s](https://github.com/iree-org/iree/actions/runs/38764327569/job/116523569364) | 0% (0/3) | 6 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38753752500/job/116486628315) | [3s](https://github.com/iree-org/iree/actions/runs/38749004108/job/116470130325) | 0% (0/3) | 15 |
| `ubuntu-24.04` | github-hosted | 52 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38757052171/job/116498127537) | [3s](https://github.com/iree-org/iree/actions/runs/38764327569/job/116523569267) | 0% (0/23) | 50 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486790757) | [1s](https://github.com/iree-org/iree/actions/runs/38764327569/job/116523569528) | 0% (0/1) | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [26m20s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065324) | [35m34s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891426) | [35m34s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891426) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891605) | [33m16s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065533) | [33m16s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065533) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [23m53s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891752) | [30m38s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065254) | [30m38s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065254) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [10m50s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065155) | [27m41s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891615) | [27m41s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891615) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [6m01s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891591) | [21m18s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065120) | [21m18s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065120) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [4m06s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891977) | [21m16s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065244) | [21m16s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065244) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [12m36s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891767) | [13m19s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065235) | [13m19s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065235) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [8m43s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065116) | [10m45s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891525) | [10m45s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891525) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065055) | [8m56s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891567) | [8m56s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891567) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [1m37s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116527891624) | [5m35s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065237) | [5m35s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116492065237) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/38764327569/job/116523569453) | [2m31s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486790966) | [2m31s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486790966) | 2 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m27s](https://github.com/iree-org/iree/actions/runs/38713201392/job/116349449223) | [1m27s](https://github.com/iree-org/iree/actions/runs/38713201392/job/116349449223) | [1m27s](https://github.com/iree-org/iree/actions/runs/38713201392/job/116349449223) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [1m19s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486790701) | [1m19s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486790701) | [1m19s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486790701) | 1 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38764327569/job/116523568984) | [38s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486789341) | [38s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486789341) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486790127) | [12s](https://github.com/iree-org/iree/actions/runs/38764327569/job/116523569621) | [12s](https://github.com/iree-org/iree/actions/runs/38764327569/job/116523569621) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/38753753363/job/116486734349) | [11s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116523578843) | [11s](https://github.com/iree-org/iree/actions/runs/38764327682/job/116523578843) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38764327569/job/116523569270) | [10s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486790769) | [10s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486790769) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486790413) | [9s](https://github.com/iree-org/iree/actions/runs/38764327569/job/116523569450) | [9s](https://github.com/iree-org/iree/actions/runs/38764327569/job/116523569450) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 2 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/38764327569/job/116523569435) | [8s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486789730) | [8s](https://github.com/iree-org/iree/actions/runs/38753753067/job/116486789730) | 2 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38724743630/job/116388307790) | [8s](https://github.com/iree-org/iree/actions/runs/38724743630/job/116388307790) | [8s](https://github.com/iree-org/iree/actions/runs/38724743630/job/116388307790) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 291 | 1% (2/291) |  | 24m37s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 377 | 8% (30/377) |  | 37m34s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
