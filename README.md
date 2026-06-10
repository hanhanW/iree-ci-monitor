# iree-ci-monitor

_Updated: 2026-06-10 00:48 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [33m39s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753845) | [33m39s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753845) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [17m19s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753798) | [27m56s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753841) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [23m55s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753799) | [23m55s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753799) | 0% (0/1) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [19m12s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753728) | [19m12s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753728) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [14m02s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753644) | [14m02s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753644) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [9m25s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753806) | [10m25s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753765) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [9m46s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753579) | [9m46s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753579) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753804) | [7m14s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753830) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [3m54s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753789) | [3m54s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753789) | 0% (0/1) | `shark10-ci` |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 0 | [11s](https://github.com/iree-org/iree/actions/runs/27256906056/job/80493133618) | [27s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80493135659) | 0% (0/7) | 7 |
| `ubuntu-24.04` | github-hosted | 33 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80493114500) | [18s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753663) | 8% (2/24) | 33 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753665) | [8s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753719) | 0% (0/4) | 4 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27256906056/job/80493133545) | [4s](https://github.com/iree-org/iree/actions/runs/27257928303/job/80496453741) | 0% (0/3) | 5 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27256906056/job/80493133520) | [3s](https://github.com/iree-org/iree/actions/runs/27257928303/job/80496453746) | 0% (0/3) | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27256906056/job/80493133549) | [2s](https://github.com/iree-org/iree/actions/runs/27257928303/job/80496453766) | 0% (0/3) | 6 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27256905259/job/80493114196) | [2s](https://github.com/iree-org/iree/actions/runs/27256905259/job/80493114203) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27256906056/job/80493133674) | [1s](https://github.com/iree-org/iree/actions/runs/27256906056/job/80493133674) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753542) | [1s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753542) | 100% (1/1) | 1 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753674) | [1s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753674) | 0% (0/1) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753713) | [1s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753776) | 0% (0/2) | `shark01-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753715) | [1s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753715) | 0% (0/1) | `iree-mi308-1` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [33m39s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753845) | [33m39s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753845) | [33m39s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753845) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [27m56s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753841) | [27m56s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753841) | [27m56s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753841) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [23m55s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753799) | [23m55s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753799) | [23m55s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753799) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [19m12s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753728) | [19m12s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753728) | [19m12s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753728) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [17m19s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753798) | [17m19s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753798) | [17m19s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753798) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [14m02s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753644) | [14m02s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753644) | [14m02s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753644) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [10m25s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753765) | [10m25s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753765) | [10m25s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753765) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [9m46s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753579) | [9m46s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753579) | [9m46s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753579) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [9m25s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753806) | [9m25s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753806) | [9m25s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753806) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [7m14s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753830) | [7m14s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753830) | [7m14s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753830) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [3m54s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753789) | [3m54s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753789) | [3m54s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753789) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 1 | 0 | — | — | [45s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753814) | [45s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753814) | [45s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753814) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [27s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80493135659) | [27s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80493135659) | [27s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80493135659) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 1 | 0 | — | — | [25s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753827) | [25s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753827) | [25s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753827) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 1 | 0 | — | — | [18s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753663) | [18s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753663) | [18s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753663) | 1 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 1 | 0 | — | — | [16s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753698) | [16s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753698) | [16s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753698) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 1 | 0 | — | — | [15s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753673) | [15s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753673) | [15s](https://github.com/iree-org/iree/actions/runs/27256906096/job/80496753673) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [13s](https://github.com/iree-org/iree/actions/runs/27256906056/job/80493133637) | [13s](https://github.com/iree-org/iree/actions/runs/27256906056/job/80493133637) | [13s](https://github.com/iree-org/iree/actions/runs/27256906056/job/80493133637) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/27256906056/job/80493133574) | [12s](https://github.com/iree-org/iree/actions/runs/27256906056/job/80493133574) | [12s](https://github.com/iree-org/iree/actions/runs/27256906056/job/80493133574) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/27256906056/job/80493133618) | [11s](https://github.com/iree-org/iree/actions/runs/27256906056/job/80493133618) | [11s](https://github.com/iree-org/iree/actions/runs/27256906056/job/80493133618) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 320 | 2% (8/320) |  | 33m32s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 277 | 7% (19/277) |  | 43m52s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 241 | 2% (4/241) |  | 51m09s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 240 | 2% (5/240) |  | 57m22s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 75 | 1% (1/75) |  | 1h02m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
