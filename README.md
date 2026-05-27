# iree-ci-monitor

_Updated: 2026-05-26 18:22 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 8 | 0 | — | — | 0 | [12m27s](https://github.com/iree-org/iree/actions/runs/26459872570/job/77906246184) | [40m53s](https://github.com/iree-org/iree/actions/runs/26466777287/job/77930589200) | 0% (0/4) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 16 | 0 | — | — | 0 | [18m44s](https://github.com/iree-org/iree/actions/runs/26459872570/job/77906246675) | [27m23s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086554) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26466777287/job/77930588987) | [23m09s](https://github.com/iree-org/iree/actions/runs/26469458377/job/77939989252) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [7m09s](https://github.com/iree-org/iree/actions/runs/26465482440/job/77925832645) | [21m34s](https://github.com/iree-org/iree/actions/runs/26459872570/job/77906246363) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 8 | 0 | — | — | 0 | [6m06s](https://github.com/iree-org/iree/actions/runs/26459872570/job/77906246078) | [17m53s](https://github.com/iree-org/iree/actions/runs/26469458377/job/77939989271) | 0% (0/4) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 8 | 0 | — | — | 0 | [7m05s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086472) | [17m40s](https://github.com/iree-org/iree/actions/runs/26466777287/job/77930589159) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 16 | 0 | — | — | 0 | [5m20s](https://github.com/iree-org/iree/actions/runs/26457746368/job/77898141656) | [16m27s](https://github.com/iree-org/iree/actions/runs/26469458377/job/77939989436) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 16 | 0 | — | — | 0 | [6m15s](https://github.com/iree-org/iree/actions/runs/26466777287/job/77930589381) | [13m56s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086505) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [6m11s](https://github.com/iree-org/iree/actions/runs/26457746368/job/77898141825) | [11m04s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086616) | 0% (0/4) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 16 | 0 | — | — | 0 | [1m12s](https://github.com/iree-org/iree/actions/runs/26457746368/job/77898141613) | [8m59s](https://github.com/iree-org/iree/actions/runs/26465482440/job/77925832537) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086449) | [4m38s](https://github.com/iree-org/iree/actions/runs/26459872570/job/77906246065) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 41 | 0 | — | — | 0 | [11s](https://github.com/iree-org/iree/actions/runs/26457746368/job/77896566133) | [1m57s](https://github.com/iree-org/iree/actions/runs/26459872638/job/77904377283) | 0% (0/20) | 41 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 32 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/26459872570/job/77906246069) | [19s](https://github.com/iree-org/iree/actions/runs/26457746368/job/77898141653) | 0% (0/16) | 32 |
| `windows-2022` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26458921111/job/77900910803) | [4s](https://github.com/iree-org/iree/actions/runs/26466777261/job/77929529599) | 0% (0/9) | 21 |
| `ubuntu-24.04` | github-hosted | 145 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26466777287/job/77930589628) | [3s](https://github.com/iree-org/iree/actions/runs/26469458441/job/77938678864) | 0% (0/65) | 144 |
| `macos-14` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26457745820/job/77896571608) | [3s](https://github.com/iree-org/iree/actions/runs/26469458441/job/77938678270) | 0% (0/9) | 21 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26469458441/job/77938678070) | [3s](https://github.com/iree-org/iree/actions/runs/26472367852/job/77948971738) | 0% (0/9) | 21 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26457742702/job/77896526142) | [3s](https://github.com/iree-org/iree/actions/runs/26459870769/job/77904338816) | 0% (0/9) | 12 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26457746368/job/77898141437) | [2s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086441) | 0% (0/4) | 8 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 8 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26465482440/job/77925832469) | [2s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086446) | 0% (0/4) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 7 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26459872638/job/77904377318) | [1s](https://github.com/iree-org/iree/actions/runs/26472367852/job/77948972294) | 0% (0/3) | 7 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 8 | 0 | — | — | [12m27s](https://github.com/iree-org/iree/actions/runs/26459872570/job/77906246184) | [40m53s](https://github.com/iree-org/iree/actions/runs/26466777287/job/77930589200) | [40m53s](https://github.com/iree-org/iree/actions/runs/26466777287/job/77930589200) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [10m31s](https://github.com/iree-org/iree/actions/runs/26459872570/job/77906246372) | [27m23s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086554) | [27m23s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086554) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [19m37s](https://github.com/iree-org/iree/actions/runs/26466777287/job/77930589251) | [26m03s](https://github.com/iree-org/iree/actions/runs/26469458377/job/77939989350) | [26m03s](https://github.com/iree-org/iree/actions/runs/26469458377/job/77939989350) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26466777287/job/77930588987) | [23m09s](https://github.com/iree-org/iree/actions/runs/26469458377/job/77939989252) | [23m09s](https://github.com/iree-org/iree/actions/runs/26469458377/job/77939989252) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 8 | 0 | — | — | [7m09s](https://github.com/iree-org/iree/actions/runs/26465482440/job/77925832645) | [21m34s](https://github.com/iree-org/iree/actions/runs/26459872570/job/77906246363) | [21m34s](https://github.com/iree-org/iree/actions/runs/26459872570/job/77906246363) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [9m40s](https://github.com/iree-org/iree/actions/runs/26465482440/job/77925832652) | [18m06s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086572) | [18m06s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086572) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 8 | 0 | — | — | [6m06s](https://github.com/iree-org/iree/actions/runs/26459872570/job/77906246078) | [17m53s](https://github.com/iree-org/iree/actions/runs/26469458377/job/77939989271) | [17m53s](https://github.com/iree-org/iree/actions/runs/26469458377/job/77939989271) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 8 | 0 | — | — | [7m05s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086472) | [17m40s](https://github.com/iree-org/iree/actions/runs/26466777287/job/77930589159) | [17m40s](https://github.com/iree-org/iree/actions/runs/26466777287/job/77930589159) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 8 | 0 | — | — | [5m20s](https://github.com/iree-org/iree/actions/runs/26457746368/job/77898141656) | [16m27s](https://github.com/iree-org/iree/actions/runs/26469458377/job/77939989436) | [16m27s](https://github.com/iree-org/iree/actions/runs/26469458377/job/77939989436) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 8 | 0 | — | — | [4m37s](https://github.com/iree-org/iree/actions/runs/26457746368/job/77898141704) | [14m57s](https://github.com/iree-org/iree/actions/runs/26465482440/job/77925832639) | [14m57s](https://github.com/iree-org/iree/actions/runs/26465482440/job/77925832639) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [2m19s](https://github.com/iree-org/iree/actions/runs/26459872570/job/77906246596) | [13m56s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086505) | [13m56s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086505) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26465482440/job/77925832381) | [11m23s](https://github.com/iree-org/iree/actions/runs/26466777287/job/77930589141) | [11m23s](https://github.com/iree-org/iree/actions/runs/26466777287/job/77930589141) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 8 | 0 | — | — | [6m11s](https://github.com/iree-org/iree/actions/runs/26457746368/job/77898141825) | [11m04s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086616) | [11m04s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086616) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [4m39s](https://github.com/iree-org/iree/actions/runs/26469458377/job/77939989430) | [8m59s](https://github.com/iree-org/iree/actions/runs/26465482440/job/77925832537) | [8m59s](https://github.com/iree-org/iree/actions/runs/26465482440/job/77925832537) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26472367720/job/77954086449) | [4m38s](https://github.com/iree-org/iree/actions/runs/26459872570/job/77906246065) | [4m38s](https://github.com/iree-org/iree/actions/runs/26459872570/job/77906246065) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 8 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/26457746368/job/77896566133) | [2m15s](https://github.com/iree-org/iree/actions/runs/26459872570/job/77904383495) | [2m15s](https://github.com/iree-org/iree/actions/runs/26459872570/job/77904383495) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 7 | 0 | — | — | [13s](https://github.com/iree-org/iree/actions/runs/26457745820/job/77896571971) | [2m00s](https://github.com/iree-org/iree/actions/runs/26459872638/job/77904377190) | [2m00s](https://github.com/iree-org/iree/actions/runs/26459872638/job/77904377190) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 7 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/26472367852/job/77948971982) | [1m57s](https://github.com/iree-org/iree/actions/runs/26459872638/job/77904377283) | [1m57s](https://github.com/iree-org/iree/actions/runs/26459872638/job/77904377283) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 4 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/26458921111/job/77900911076) | [1m41s](https://github.com/iree-org/iree/actions/runs/26459872638/job/77904377466) | [1m41s](https://github.com/iree-org/iree/actions/runs/26459872638/job/77904377466) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 7 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/26469458441/job/77938678316) | [1m01s](https://github.com/iree-org/iree/actions/runs/26459872638/job/77904377219) | [1m01s](https://github.com/iree-org/iree/actions/runs/26459872638/job/77904377219) | 7 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 272 | 2% (6/272) |  | 4h03m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 201 | 1% (2/201) |  | 4h13m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 249 | 6% (14/249) |  | 4h15m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 196 | 4% (8/196) |  | 4h22m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 65 | 3% (2/65) |  | 4h32m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
