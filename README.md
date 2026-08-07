# iree-ci-monitor

_Updated: 2026-08-06 17:16 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 15 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270784) | [19m36s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270852) | 15% (2/13) | 10 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [18m16s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270759) | [18m16s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270759) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [18m04s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270808) | [18m04s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270808) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [14m39s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270843) | [14m39s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270843) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [13m55s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270877) | [13m55s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270877) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [12m44s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270805) | [12m44s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270805) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [12m19s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270752) | [12m19s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270752) | 0% (0/1) | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [9m51s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270801) | [9m51s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270801) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270788) | [9m13s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270837) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270792) | [8m17s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270845) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270787) | [7m09s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270846) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270782) | [2m55s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270818) | 0% (0/2) | `shark55-ci` |
| `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92708855574) | [1s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92708855574) | 0% (0/1) | 1 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | 0s | 0s | 0% (0/3) | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 1 | 0 | — | — | [19m36s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270852) | [19m36s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270852) | [19m36s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270852) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [18m16s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270759) | [18m16s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270759) | [18m16s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270759) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [18m04s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270808) | [18m04s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270808) | [18m04s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270808) | 1 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 1 | 0 | — | — | [17m26s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270815) | [17m26s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270815) | [17m26s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270815) | 1 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 1 | 0 | — | — | [17m19s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270796) | [17m19s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270796) | [17m19s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270796) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [14m39s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270843) | [14m39s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270843) | [14m39s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270843) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [13m55s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270877) | [13m55s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270877) | [13m55s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270877) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [12m44s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270805) | [12m44s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270805) | [12m44s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270805) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [12m19s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270752) | [12m19s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270752) | [12m19s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270752) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [9m51s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270801) | [9m51s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270801) | [9m51s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270801) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [9m13s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270837) | [9m13s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270837) | [9m13s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270837) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [8m17s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270845) | [8m17s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270845) | [8m17s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270845) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [7m09s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270846) | [7m09s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270846) | [7m09s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270846) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [2m55s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270818) | [2m55s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270818) | [2m55s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270818) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270799) | [3s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270799) | [3s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270799) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270784) | [3s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270784) | [3s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270784) | 1 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270829) | [3s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270829) | [3s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270829) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31128374710/job/92709659505) | [2s](https://github.com/iree-org/iree/actions/runs/31128374710/job/92709659505) | [2s](https://github.com/iree-org/iree/actions/runs/31128374710/job/92709659505) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270782) | [2s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270782) | [2s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270782) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270787) | [2s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270787) | [2s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92709270787) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 129 | 0% (0/129) |  | 2h11m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 112 | 3% (3/112) |  | 2h13m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 101 | 0% (0/101) |  | 2h16m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 1% (1/102) |  | 2h17m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 13 | 0% (0/13) |  | 3d11h ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
