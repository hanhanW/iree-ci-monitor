# iree-ci-monitor

_Updated: 2026-11-14 10:11 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [33m24s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171243) | [45m20s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630798) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [37m08s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630676) | [41m04s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171185) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [6m00s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630807) | [35m32s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171196) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [26m31s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171278) | [31m59s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630776) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630521) | [20m41s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171097) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [7m39s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630752) | [19m23s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630764) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [12m59s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171181) | [14m33s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630802) | — | `shark55-ci` |
| `azure-linux-scale` | ossci | 12 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371480) | [9s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675601) | — | 12 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675455) | [7s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371281) | — | 6 |
| `macos-15` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675357) | [4s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371372) | — | 6 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/43603303873/job/132472492512) | [4s](https://github.com/iree-org/iree/actions/runs/43603303670/job/132472491917) | — | 6 |
| `ubuntu-24.04` | github-hosted | 47 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/43608975833/job/132489590812) | [3s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371342) | 0% (0/1) | 44 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675381) | [3s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371275) | — | 6 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371431) | [1s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675551) | — | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [29m15s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171165) | [45m20s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630798) | [45m20s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630798) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [10m13s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630714) | [41m04s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171185) | [41m04s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171185) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [3m40s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171082) | [37m08s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630676) | [37m08s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630676) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [6m00s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630807) | [35m32s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171196) | [35m32s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171196) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630735) | [33m24s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171243) | [33m24s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171243) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [15m43s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171177) | [31m59s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630776) | [31m59s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630776) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [13m56s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630740) | [26m31s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171278) | [26m31s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171278) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630521) | [20m41s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171097) | [20m41s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171097) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [3m04s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171183) | [19m23s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630764) | [19m23s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630764) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [12m59s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171181) | [14m33s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630802) | [14m33s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630802) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [6m59s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132493171205) | [7m39s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630752) | [7m39s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132487630752) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371480) | [3m05s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675718) | [3m05s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675718) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675451) | [9s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371403) | [9s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371403) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371447) | [9s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675601) | [9s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675601) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675555) | [8s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371374) | [8s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371374) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371394) | [8s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675512) | [8s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675512) | 2 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 2 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675424) | [7s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371281) | [7s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371281) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/43608975900/job/132489643477) | [5s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132485386558) | [5s](https://github.com/iree-org/iree/actions/runs/43607532765/job/132485386558) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675463) | [4s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371372) | [4s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371372) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 2 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/43607532714/job/132485371357) | [4s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675503) | [4s](https://github.com/iree-org/iree/actions/runs/43608975837/job/132489675503) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 336 | 1% (3/336) |  | 1h59m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 392 | 1% (2/392) |  | 2h03m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
