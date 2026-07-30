# iree-ci-monitor

_Updated: 2026-07-30 00:13 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 1 | [21m36s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312228) | [27m16s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312276) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [7m26s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312183) | [19m14s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738252073) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [4m20s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251930) | [18m28s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312341) | 0% (0/2) | `shark01-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [10m33s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312186) | [17m29s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738252195) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [8m25s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251964) | [15m01s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312244) | 0% (0/4) | `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [13m22s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312401) | [14m27s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312177) | 0% (0/4) | `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312158) | [12m45s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251955) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [8m14s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251999) | [10m11s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738252051) | 0% (0/4) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738252021) | [6m29s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312170) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [5m23s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251933) | [5m33s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312350) | 0% (0/2) | `shark10-ci` |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/30519533009/job/90796691352) | [1m25s](https://github.com/iree-org/iree/actions/runs/30519533009/job/90796691381) | 0% (0/9) | 9 |
| `windows-2022` | github-hosted | 11 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/30518079435/job/90792289126) | [1m24s](https://github.com/iree-org/iree/actions/runs/30519533009/job/90796691347) | 0% (0/9) | 8 |
| `azure-linux-scale` | ossci | 17 | 0 | — | — | 2 | [14s](https://github.com/iree-org/iree/actions/runs/30519533009/job/90796691389) | [1m16s](https://github.com/iree-org/iree/actions/runs/30499875150/job/90737010139) | 0% (0/15) | 13 |
| `macos-14` | github-hosted | 11 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/30519533009/job/90796691330) | [36s](https://github.com/iree-org/iree/actions/runs/30519533009/job/90796691362) | 0% (0/9) | 8 |
| `ubuntu-24.04` | github-hosted | 54 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/30519533009/job/90796691238) | [9s](https://github.com/iree-org/iree/actions/runs/30482553286/job/90712462214) | 0% (0/46) | 48 |
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30519814671/job/90797496484) | [7s](https://github.com/iree-org/iree/actions/runs/30519532450/job/90796661386) | 0% (0/6) | 18 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312297) | [3s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251859) | 0% (0/2) | 2 |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312147) | [2s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251894) | 0% (0/2) | `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312323) | [2s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251925) | 0% (0/2) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30499875150/job/90737010118) | [1s](https://github.com/iree-org/iree/actions/runs/30519533009/job/90796691458) | 0% (0/3) | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [8m58s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738252059) | [27m16s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312276) | [27m16s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312276) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [4m37s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738252040) | [21m36s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312228) | [21m36s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312228) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [7m26s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312183) | [19m14s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738252073) | [19m14s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738252073) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [4m20s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251930) | [18m28s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312341) | [18m28s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312341) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [10m33s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312186) | [17m29s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738252195) | [17m29s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738252195) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251993) | [15m01s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312244) | [15m01s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312244) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738252087) | [14m27s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312177) | [14m27s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312177) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [11m45s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251948) | [13m22s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312401) | [13m22s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312401) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312158) | [12m45s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251955) | [12m45s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251955) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [6m54s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312213) | [10m11s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738252051) | [10m11s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738252051) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312191) | [8m25s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251964) | [8m25s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251964) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312209) | [8m14s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251999) | [8m14s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251999) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738252021) | [6m29s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312170) | [6m29s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312170) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [5m23s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90738251933) | [5m33s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312350) | [5m33s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90798312350) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30499875089/job/90737005557) | [1m45s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90796693522) | [1m45s](https://github.com/iree-org/iree/actions/runs/30519533029/job/90796693522) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 3 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/30499875150/job/90737009973) | [1m25s](https://github.com/iree-org/iree/actions/runs/30519533009/job/90796691381) | [1m25s](https://github.com/iree-org/iree/actions/runs/30519533009/job/90796691381) | 2 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30499875150/job/90737009946) | [1m24s](https://github.com/iree-org/iree/actions/runs/30519533009/job/90796691347) | [1m24s](https://github.com/iree-org/iree/actions/runs/30519533009/job/90796691347) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 3 | 0 | — | — | [14s](https://github.com/iree-org/iree/actions/runs/30519533009/job/90796691507) | [1m16s](https://github.com/iree-org/iree/actions/runs/30499875150/job/90737010139) | [1m16s](https://github.com/iree-org/iree/actions/runs/30499875150/job/90737010139) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 3 | 0 | — | — | [13s](https://github.com/iree-org/iree/actions/runs/30519533009/job/90796691390) | [1m15s](https://github.com/iree-org/iree/actions/runs/30499875150/job/90737010134) | [1m15s](https://github.com/iree-org/iree/actions/runs/30499875150/job/90737010134) | 2 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30499875150/job/90737009950) | [1m13s](https://github.com/iree-org/iree/actions/runs/30519533009/job/90796691391) | [1m13s](https://github.com/iree-org/iree/actions/runs/30519533009/job/90796691391) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 197 | 1% (2/196) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 146 | 0% (0/146) |  | 10m36s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 177 | 5% (9/177) |  | 10m59s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 139 | 1% (2/139) |  | 13m30s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 44 | 2% (1/44) |  | 25m55s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
