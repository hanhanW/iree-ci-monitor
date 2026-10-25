# iree-ci-monitor

_Updated: 2026-10-24 21:49 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

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
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [22s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163807) | [22s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163807) | 0% (0/1) | `shark55-ci` |
| `ubuntu-24.04` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163823) | [2s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120968860330) | 0% (0/12) | 12 |
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
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [22s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163807) | [22s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163807) | [22s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163807) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120981696483) | [3s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120981696483) | [3s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120981696483) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120968860330) | [2s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120968860330) | [2s](https://github.com/iree-org/iree/actions/runs/40122367898/job/120968860330) | 1 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163720) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163720) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163720) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163776) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163776) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163776) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163848) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163848) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163848) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163865) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163865) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163865) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163804) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163804) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163804) | 1 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163736) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163736) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163736) | 1 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163713) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163713) | [2s](https://github.com/iree-org/iree/actions/runs/40122367842/job/120961163713) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 408 | 0% (0/408) |  | 8h10m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 338 | 2% (7/338) |  | 8h44m ago |

## Alerts

- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h22m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
