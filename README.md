# iree-ci-monitor

_Updated: 2026-07-28 11:49 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [11m39s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623670) | [26m03s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293728) | — | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [20m45s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298624011) | [22m09s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293689) | — | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [14m20s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293753) | [20m46s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623760) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [18m31s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623946) | [20m30s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293625) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [13m17s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623906) | [16m21s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298624083) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293029) | [15m21s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623445) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [6m02s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293610) | [14m34s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623697) | — | `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [6m16s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293508) | [11m20s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623865) | — | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [53s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623669) | [10m19s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623639) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293291) | [7m59s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298624016) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [4m55s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623846) | [7m06s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298624000) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293862) | [3m07s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623633) | — | `iree-mi308-1` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [2m21s](https://github.com/iree-org/iree/actions/runs/30349494988/job/90243373949) | [2m21s](https://github.com/iree-org/iree/actions/runs/30349494988/job/90243373949) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 12 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/30365073911/job/90294206510) | [1m55s](https://github.com/iree-org/iree/actions/runs/30365550826/job/90295843409) | 0% (0/2) | 12 |
| `ubuntu-24.04` | github-hosted | 47 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30365550826/job/90361229011) | [1m16s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293854) | 33% (1/3) | 47 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/30365073911/job/90294206463) | [25s](https://github.com/iree-org/iree/actions/runs/30365550826/job/90295843023) | — | 6 |
| `macos-14` | github-hosted | 7 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/30365073911/job/90294206398) | [10s](https://github.com/iree-org/iree/actions/runs/30365073911/job/90294206406) | 0% (0/1) | 7 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30370527235/job/90312906576) | [8s](https://github.com/iree-org/iree/actions/runs/30370526202/job/90313023430) | — | 15 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293109) | [6s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623694) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30365550826/job/90295843390) | [5s](https://github.com/iree-org/iree/actions/runs/30365550826/job/90295843391) | — | 6 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30349457314/job/90243249525) | [3s](https://github.com/iree-org/iree/actions/runs/30349457314/job/90243249525) | 0% (0/1) | 1 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30365073911/job/90294206600) | [2s](https://github.com/iree-org/iree/actions/runs/30365550826/job/90295843875) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [11m39s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623670) | [26m03s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293728) | [26m03s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293728) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [20m45s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298624011) | [22m09s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293689) | [22m09s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293689) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [14m20s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293753) | [20m46s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623760) | [20m46s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623760) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [18m31s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623946) | [20m30s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293625) | [20m30s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293625) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [10m30s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293730) | [16m21s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298624083) | [16m21s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298624083) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293029) | [15m21s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623445) | [15m21s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623445) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [6m02s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293610) | [14m34s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623697) | [14m34s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623697) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [9m44s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293752) | [13m17s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623906) | [13m17s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623906) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [6m16s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293508) | [11m20s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623865) | [11m20s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623865) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293650) | [10m19s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623639) | [10m19s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623639) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293291) | [7m59s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298624016) | [7m59s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298624016) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [3m53s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293718) | [7m06s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298624000) | [7m06s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298624000) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [3m16s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293668) | [4m55s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623846) | [4m55s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623846) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [3m03s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623885) | [3m28s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293607) | [3m28s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293607) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90296293862) | [3m07s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623633) | [3m07s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90298623633) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [2m21s](https://github.com/iree-org/iree/actions/runs/30349494988/job/90243373949) | [2m21s](https://github.com/iree-org/iree/actions/runs/30349494988/job/90243373949) | [2m21s](https://github.com/iree-org/iree/actions/runs/30349494988/job/90243373949) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/30365073648/job/90294224304) | [2m14s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90295849399) | [2m14s](https://github.com/iree-org/iree/actions/runs/30365550847/job/90295849399) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30365073911/job/90294206485) | [1m55s](https://github.com/iree-org/iree/actions/runs/30365550826/job/90295843409) | [1m55s](https://github.com/iree-org/iree/actions/runs/30365550826/job/90295843409) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30365073911/job/90294206400) | [1m29s](https://github.com/iree-org/iree/actions/runs/30365550826/job/90295843294) | [1m29s](https://github.com/iree-org/iree/actions/runs/30365550826/job/90295843294) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30365073911/job/90294206439) | [1m20s](https://github.com/iree-org/iree/actions/runs/30365550826/job/90295843322) | [1m20s](https://github.com/iree-org/iree/actions/runs/30365550826/job/90295843322) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 273 | 5% (14/273) |  | 4h23m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 336 | 1% (5/336) |  | 4h24m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 260 | 1% (2/260) |  | 4h24m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 244 | 2% (4/244) |  | 4h28m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 77 | 3% (2/77) |  | 4h32m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
