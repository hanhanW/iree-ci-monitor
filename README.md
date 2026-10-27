# iree-ci-monitor

_Updated: 2026-10-27 15:20 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 10 | 0 | — | — | 0 | [7m02s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401678) | [32m15s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401967) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [13m08s](https://github.com/iree-org/iree/actions/runs/40538362286/job/122314625600) | [26m58s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401917) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 10 | 0 | — | — | 0 | [11m56s](https://github.com/iree-org/iree/actions/runs/40538362286/job/122314624703) | [19m32s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332402439) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [7m11s](https://github.com/iree-org/iree/actions/runs/40553156058/job/122366773325) | [16m50s](https://github.com/iree-org/iree/actions/runs/40543249265/job/122332081997) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [9m23s](https://github.com/iree-org/iree/actions/runs/40533005154/job/122296061716) | [16m43s](https://github.com/iree-org/iree/actions/runs/40559417207/job/122389098155) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [3m32s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401599) | [11m03s](https://github.com/iree-org/iree/actions/runs/40533005154/job/122296061851) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [4m23s](https://github.com/iree-org/iree/actions/runs/40538362286/job/122314624434) | [9m07s](https://github.com/iree-org/iree/actions/runs/40553156058/job/122366773194) | 0% (0/1) | `shark55-ci` |
| `azure-linux-scale` | ossci | 49 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/40543401873/job/122329041930) | [42s](https://github.com/iree-org/iree/actions/runs/40532883505/job/122306231916) | 0% (0/7) | 49 |
| `macos-15` | github-hosted | 24 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/40546675557/job/122339139168) | [15s](https://github.com/iree-org/iree/actions/runs/40543401873/job/122329041177) | 0% (0/3) | 24 |
| `ubuntu-24.04` | github-hosted | 147 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40553156022/job/122362018807) | [8s](https://github.com/iree-org/iree/actions/runs/40543401873/job/122360805375) | 0% (0/20) | 144 |
| `ubuntu-24.04-arm` | github-hosted | 24 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/40559417248/job/122384237664) | [5s](https://github.com/iree-org/iree/actions/runs/40559417248/job/122384237617) | 0% (0/3) | 24 |
| `windows-2022` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40559417248/job/122384237264) | [3s](https://github.com/iree-org/iree/actions/runs/40546675557/job/122339139579) | 0% (0/3) | 24 |
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40543397314/job/122327467312) | [3s](https://github.com/iree-org/iree/actions/runs/40553154436/job/122362023010) | 0% (0/3) | 18 |
| `azure-windows-scale` | ossci | 8 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/40553156022/job/122362150348) | [2s](https://github.com/iree-org/iree/actions/runs/40533005483/job/122290747237) | 0% (0/1) | 8 |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [13m08s](https://github.com/iree-org/iree/actions/runs/40538362286/job/122314625600) | [35m28s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332402102) | [35m28s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332402102) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [11m24s](https://github.com/iree-org/iree/actions/runs/40533005154/job/122296062028) | [32m15s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401967) | [32m15s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401967) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [1m53s](https://github.com/iree-org/iree/actions/runs/40533005154/job/122296061729) | [26m58s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401917) | [26m58s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401917) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [15m15s](https://github.com/iree-org/iree/actions/runs/40559417207/job/122389098115) | [19m32s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332402439) | [19m32s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332402439) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [7m11s](https://github.com/iree-org/iree/actions/runs/40553156058/job/122366773325) | [16m50s](https://github.com/iree-org/iree/actions/runs/40543249265/job/122332081997) | [16m50s](https://github.com/iree-org/iree/actions/runs/40543249265/job/122332081997) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [7m02s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401678) | [16m46s](https://github.com/iree-org/iree/actions/runs/40553156058/job/122366772924) | [16m46s](https://github.com/iree-org/iree/actions/runs/40553156058/job/122366772924) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 5 | 0 | — | — | [9m23s](https://github.com/iree-org/iree/actions/runs/40533005154/job/122296061716) | [16m43s](https://github.com/iree-org/iree/actions/runs/40559417207/job/122389098155) | [16m43s](https://github.com/iree-org/iree/actions/runs/40559417207/job/122389098155) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [9m02s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401638) | [16m23s](https://github.com/iree-org/iree/actions/runs/40553156058/job/122366773001) | [16m23s](https://github.com/iree-org/iree/actions/runs/40553156058/job/122366773001) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40559417207/job/122389097704) | [13m13s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332402080) | [13m13s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332402080) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 5 | 0 | — | — | [4m23s](https://github.com/iree-org/iree/actions/runs/40538362286/job/122314624434) | [9m07s](https://github.com/iree-org/iree/actions/runs/40553156058/job/122366773194) | [9m07s](https://github.com/iree-org/iree/actions/runs/40553156058/job/122366773194) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [3m29s](https://github.com/iree-org/iree/actions/runs/40559417207/job/122389097962) | [7m24s](https://github.com/iree-org/iree/actions/runs/40533005154/job/122296061727) | [7m24s](https://github.com/iree-org/iree/actions/runs/40533005154/job/122296061727) | 2 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40553156058/job/122366773328) | [2m16s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401721) | [2m16s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401721) | 6 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40543249265/job/122332082826) | [2m01s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401802) | [2m01s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401802) | 6 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40543249265/job/122332082288) | [1m45s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401684) | [1m45s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401684) | 6 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 6 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40543249265/job/122332082237) | [1m18s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401953) | [1m18s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401953) | 6 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40559417207/job/122389097381) | [50s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401818) | [50s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401818) | 6 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 8 | 0 | — | — | [27s](https://github.com/iree-org/iree/actions/runs/40538362286/job/122309813498) | [43s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122327675392) | [43s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122327675392) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 8 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/40559417248/job/122384237664) | [42s](https://github.com/iree-org/iree/actions/runs/40538362216/job/122309791618) | [42s](https://github.com/iree-org/iree/actions/runs/40538362216/job/122309791618) | 8 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40553156058/job/122366772735) | [41s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401495) | [41s](https://github.com/iree-org/iree/actions/runs/40543402648/job/122332401495) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 8 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40543401873/job/122329041990) | [26s](https://github.com/iree-org/iree/actions/runs/40532883563/job/122306227980) | [26s](https://github.com/iree-org/iree/actions/runs/40532883563/job/122306227980) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 286 | 4% (12/286) |  | 3h29m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 352 | 1% (3/352) |  | 3h32m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
