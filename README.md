# iree-ci-monitor

_Updated: 2026-10-24 13:54 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [1h18m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163846) | [1h22m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163827) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [50m04s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163745) | [50m04s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163745) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [27m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163883) | [44m40s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163872) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [39m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163718) | [39m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163718) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [7m17s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163866) | [22m13s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163890) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163755) | [5m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163695) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 8 | 0 | — | — | 0 | [1m33s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542507) | [1m43s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542363) | 0% (0/8) | 8 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [56s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542388) | [1m18s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542552) | 0% (0/3) | 3 |
| `macos-15` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542305) | [44s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542302) | 0% (0/3) | 3 |
| `ubuntu-24.04` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163804) | [43s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542283) | 0% (0/20) | 24 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [22s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163807) | [22s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163807) | 0% (0/1) | `shark55-ci` |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40101209105/job/120893560192) | [2s](https://github.com/iree-org/iree/actions/runs/40122367593/job/120956499442) | 0% (0/3) | 12 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542298) | [2s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542333) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542493) | [1s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542493) | 0% (0/1) | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [1h22m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163827) | [1h22m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163827) | [1h22m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163827) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [1h18m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163846) | [1h18m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163846) | [1h18m](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163846) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [50m04s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163745) | [50m04s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163745) | [50m04s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163745) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [44m40s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163872) | [44m40s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163872) | [44m40s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163872) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [39m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163718) | [39m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163718) | [39m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163718) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [27m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163883) | [27m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163883) | [27m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163883) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [22m13s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163890) | [22m13s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163890) | [22m13s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163890) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [7m17s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163866) | [7m17s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163866) | [7m17s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163866) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [5m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163695) | [5m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163695) | [5m10s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163695) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [2m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163755) | [2m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163755) | [2m16s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163755) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [1m43s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542363) | [1m43s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542363) | [1m43s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542363) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [1m37s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542512) | [1m37s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542512) | [1m37s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542512) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [1m34s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542489) | [1m34s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542489) | [1m34s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542489) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m33s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542507) | [1m33s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542507) | [1m33s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542507) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [1m32s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542515) | [1m32s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542515) | [1m32s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542515) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [1m28s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542438) | [1m28s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542438) | [1m28s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542438) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1m18s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542552) | [1m18s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542552) | [1m18s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542552) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 1 | 0 | — | — | [58s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542352) | [58s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542352) | [58s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542352) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [56s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542388) | [56s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542388) | [56s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542388) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 1 | 0 | — | — | [44s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542302) | [44s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542302) | [44s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120956542302) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 408 | 0% (0/408) |  | 15m23s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 338 | 2% (7/338) |  | 50m20s ago |

## Alerts

- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h22m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
