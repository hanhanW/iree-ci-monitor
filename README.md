# iree-ci-monitor

_Updated: 2026-06-03 18:33 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 10 | 0 | — | — | 0 | [20m49s](https://github.com/iree-org/iree/actions/runs/26910132556/job/79387101594) | [53m10s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672613) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 5 | 0 | — | — | 0 | [14m11s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672440) | [53m09s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576164) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [26m40s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672641) | [44m40s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461949) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 5 | 0 | — | — | 0 | [21m43s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576412) | [40m45s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461973) | 0% (0/2) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 5 | 0 | — | — | 0 | [16m14s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576245) | [34m02s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672710) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 10 | 0 | — | — | 0 | [9m35s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576389) | [31m29s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672537) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [21m32s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672571) | [31m07s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461761) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26910132556/job/79387101578) | [27m05s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461998) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 10 | 0 | — | — | 0 | [8m53s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576348) | [19m56s](https://github.com/iree-org/iree/actions/runs/26905809982/job/79372010906) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [4m49s](https://github.com/iree-org/iree/actions/runs/26910132556/job/79387101641) | [19m33s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576531) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 5 | 0 | — | — | 0 | [6m06s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461758) | [18m26s](https://github.com/iree-org/iree/actions/runs/26910132556/job/79387101357) | 50% (1/2) | `shark01-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26910132556/job/79387101474) | [17m54s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672570) | 0% (0/2) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 20 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/26910132556/job/79387101484) | [6m45s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461937) | 0% (0/8) | 20 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/26910131815/job/79385647362) | [5m14s](https://github.com/iree-org/iree/actions/runs/26905810563/job/79370320462) | 0% (0/6) | 18 |
| `macos-14` | github-hosted | 18 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26896415691/job/79336606493) | [5m08s](https://github.com/iree-org/iree/actions/runs/26905807113/job/79370328114) | 0% (0/6) | 18 |
| `windows-2022` | github-hosted | 18 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26910131815/job/79385647456) | [4m06s](https://github.com/iree-org/iree/actions/runs/26905807711/job/79370358341) | 0% (0/6) | 18 |
| `azure-linux-scale` | ossci | 32 | 0 | — | — | 0 | [43s](https://github.com/iree-org/iree/actions/runs/26905807113/job/79370328097) | [3m54s](https://github.com/iree-org/iree/actions/runs/26896415691/job/79336606457) | 0% (0/12) | 32 |
| `ubuntu-24.04` | github-hosted | 130 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26912355793/job/79394572370) | [2m18s](https://github.com/iree-org/iree/actions/runs/26905807113/job/79370328009) | 5% (2/40) | 121 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26910131815/job/79385647649) | [42s](https://github.com/iree-org/iree/actions/runs/26905807711/job/79370358626) | 0% (0/2) | 6 |
| `ubuntu-latest` | github-hosted | 19 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26895477163/job/79333122350) | [4s](https://github.com/iree-org/iree/actions/runs/26896719830/job/79337674500) | 0% (0/7) | 19 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26905809982/job/79372010351) | [3s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576098) | 50% (1/2) | 5 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [38m28s](https://github.com/iree-org/iree/actions/runs/26905809982/job/79372010848) | [53m10s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672613) | [53m10s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672613) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 5 | 0 | — | — | [14m11s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672440) | [53m09s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576164) | [53m09s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576164) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [17m23s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576381) | [49m12s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372462076) | [49m12s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372462076) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 5 | 0 | — | — | [26m40s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672641) | [44m40s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461949) | [44m40s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461949) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 5 | 0 | — | — | [21m43s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576412) | [40m45s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461973) | [40m45s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461973) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 5 | 0 | — | — | [16m14s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576245) | [34m02s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672710) | [34m02s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672710) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [11m10s](https://github.com/iree-org/iree/actions/runs/26910132556/job/79387101461) | [31m29s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672537) | [31m29s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672537) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 5 | 0 | — | — | [21m32s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672571) | [31m07s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461761) | [31m07s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461761) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26910132556/job/79387101578) | [27m05s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461998) | [27m05s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461998) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 5 | 0 | — | — | [4m45s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576322) | [25m31s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672803) | [25m31s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672803) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [9m16s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576424) | [20m31s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461803) | [20m31s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461803) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [9m18s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672828) | [19m56s](https://github.com/iree-org/iree/actions/runs/26905809982/job/79372010906) | [19m56s](https://github.com/iree-org/iree/actions/runs/26905809982/job/79372010906) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 5 | 0 | — | — | [4m49s](https://github.com/iree-org/iree/actions/runs/26910132556/job/79387101641) | [19m33s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576531) | [19m33s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576531) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 5 | 0 | — | — | [6m06s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461758) | [18m26s](https://github.com/iree-org/iree/actions/runs/26910132556/job/79387101357) | [18m26s](https://github.com/iree-org/iree/actions/runs/26910132556/job/79387101357) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26910132556/job/79387101474) | [17m54s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672570) | [17m54s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672570) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [8m53s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576348) | [17m41s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672626) | [17m41s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672626) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 5 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576410) | [10m32s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672802) | [10m32s](https://github.com/iree-org/iree/actions/runs/26905807143/job/79372672802) | 5 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 6 | 0 | — | — | [42s](https://github.com/iree-org/iree/actions/runs/26910132556/job/79385660561) | [6m51s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79336609462) | [6m51s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79336609462) | 6 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 5 | 0 | — | — | [13s](https://github.com/iree-org/iree/actions/runs/26896415979/job/79339576364) | [6m45s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461937) | [6m45s](https://github.com/iree-org/iree/actions/runs/26905807550/job/79372461937) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 6 | 0 | — | — | [43s](https://github.com/iree-org/iree/actions/runs/26905810563/job/79370320643) | [6m37s](https://github.com/iree-org/iree/actions/runs/26896415691/job/79336606719) | [6m37s](https://github.com/iree-org/iree/actions/runs/26896415691/job/79336606719) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 274 | 4% (11/273) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 301 | 0% (1/301) |  | 4h47m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 208 | 1% (2/208) |  | 4h52m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 212 | 0% (0/212) |  | 5h01m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 68 | 1% (1/68) |  | 5h04m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
