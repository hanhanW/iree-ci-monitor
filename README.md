# iree-ci-monitor

_Updated: 2026-06-12 06:29 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [11m56s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650536) | [21m27s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650498) | 0% (0/2) | `shark75-ci` |
| `azure-linux-scale` | ossci | 9 | 0 | — | — | 0 | [1m07s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958356) | [15m23s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958493) | 0% (0/9) | 9 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [14m40s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650471) | [14m40s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650471) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650539) | [8m19s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650499) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650682) | [7m24s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650455) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [7m01s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650444) | [7m01s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650444) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [2m10s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650507) | [6m28s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650478) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [3m52s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650320) | [3m52s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650320) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [3m01s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650450) | [3m01s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650450) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [3m00s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650483) | [3m00s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650483) | 0% (0/1) | `shark10-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m33s](https://github.com/iree-org/iree/actions/runs/27410716048/job/81011012870) | [1m33s](https://github.com/iree-org/iree/actions/runs/27410716048/job/81011012870) | 0% (0/1) | 1 |
| `ubuntu-24.04` | github-hosted | 33 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650610) | [44s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958241) | 9% (2/22) | 33 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650447) | [9s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650502) | 25% (1/4) | 4 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27405025517/job/80991924807) | [5s](https://github.com/iree-org/iree/actions/runs/27413364206/job/81019861455) | 0% (0/3) | 12 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958193) | [3s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792738) | 0% (0/3) | 5 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27410697977/job/81010953012) | [3s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958228) | 0% (0/3) | 6 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/27410695575/job/81010946472) | [3s](https://github.com/iree-org/iree/actions/runs/27410695575/job/81010946472) | — | 1 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792751) | [2s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958198) | 0% (0/3) | 6 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650319) | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650319) | 0% (0/1) | 1 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650433) | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650433) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650442) | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650442) | 0% (0/1) | `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650475) | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650475) | 0% (0/1) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958393) | [1s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958393) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [21m27s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650498) | [21m27s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650498) | [21m27s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650498) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [15m23s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958493) | [15m23s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958493) | [15m23s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958493) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [15m19s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958482) | [15m19s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958482) | [15m19s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958482) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [15m14s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958441) | [15m14s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958441) | [15m14s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958441) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [15m06s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958278) | [15m06s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958278) | [15m06s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958278) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [14m40s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650471) | [14m40s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650471) | [14m40s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650471) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [11m56s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650536) | [11m56s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650536) | [11m56s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650536) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [8m19s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650499) | [8m19s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650499) | [8m19s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650499) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [7m24s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650455) | [7m24s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650455) | [7m24s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650455) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [7m01s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650444) | [7m01s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650444) | [7m01s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650444) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [6m28s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650478) | [6m28s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650478) | [6m28s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650478) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [3m52s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650320) | [3m52s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650320) | [3m52s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650320) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [3m01s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650450) | [3m01s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650450) | [3m01s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650450) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [3m00s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650483) | [3m00s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650483) | [3m00s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650483) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [2m10s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650507) | [2m10s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650507) | [2m10s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650507) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m33s](https://github.com/iree-org/iree/actions/runs/27410716048/job/81011012870) | [1m33s](https://github.com/iree-org/iree/actions/runs/27410716048/job/81011012870) | [1m33s](https://github.com/iree-org/iree/actions/runs/27410716048/job/81011012870) | 1 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 1 | 0 | — | — | [1m15s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958147) | [1m15s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958147) | [1m15s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958147) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [1m07s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958356) | [1m07s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958356) | [1m07s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958356) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 1 | 0 | — | — | [59s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958218) | [59s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958218) | [59s](https://github.com/iree-org/iree/actions/runs/27405026871/job/80991958218) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [55s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80991955349) | [55s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80991955349) | [55s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80991955349) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 371 | 2% (8/371) |  | 3h49m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 312 | 7% (21/312) |  | 3h56m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 268 | 2% (5/268) |  | 3h57m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 88 | 1% (1/88) |  | 4h04m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 275 | 2% (5/275) |  | 4h05m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
