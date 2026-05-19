# iree-ci-monitor

_Updated: 2026-05-18 18:20 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 16 | 0 | — | — | 0 | [12m44s](https://github.com/iree-org/iree/actions/runs/26050063505/job/76585584711) | [1h35m](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796983) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 8 | 0 | — | — | 0 | [37m17s](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796743) | [1h23m](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596556936) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [13m28s](https://github.com/iree-org/iree/actions/runs/26048845196/job/76581320361) | [1h14m](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796954) | 0% (0/3) | `shark75-ci` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26036368777/job/76559818597) | [1h01m](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404222) | 0% (0/3) | 8 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 8 | 0 | — | — | 0 | [11m29s](https://github.com/iree-org/iree/actions/runs/26036368777/job/76559818787) | [59m28s](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404472) | 0% (0/3) | `shark10-ci` |
| `azure-windows-scale` | ossci | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26050068139/job/76585101691) | [59m09s](https://github.com/iree-org/iree/actions/runs/26053087706/job/76594378500) | 0% (0/2) | 7 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [15m06s](https://github.com/iree-org/iree/actions/runs/26048845196/job/76581320354) | [51m26s](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596557236) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 16 | 0 | — | — | 0 | [10m32s](https://github.com/iree-org/iree/actions/runs/26050063505/job/76585584786) | [50m15s](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596557254) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 8 | 0 | — | — | 0 | [11m38s](https://github.com/iree-org/iree/actions/runs/26050063505/job/76585584699) | [49m16s](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404327) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 8 | 0 | — | — | 0 | [8m08s](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796733) | [43m07s](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596557005) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 16 | 0 | — | — | 0 | [8m47s](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596557209) | [40m06s](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796880) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 16 | 0 | — | — | 0 | [7m05s](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404394) | [26m25s](https://github.com/iree-org/iree/actions/runs/26051354042/job/76594869767) | 0% (0/6) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 8 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26036368777/job/76559818717) | [22m57s](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404353) | 0% (0/3) | `iree-mi308-1` |
| `azure-linux-scale` | ossci | 39 | 0 | — | — | 0 | [3m55s](https://github.com/iree-org/iree/actions/runs/26053059866/job/76594271604) | [21m24s](https://github.com/iree-org/iree/actions/runs/26051343839/job/76588460708) | 0% (0/12) | 39 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [13s](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796925) | [18m52s](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596557386) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 32 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/26051354042/job/76594869875) | [8m37s](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596557359) | 8% (1/12) | 32 |
| `ubuntu-latest` | github-hosted | 27 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26059821160/job/76616904674) | [2m33s](https://github.com/iree-org/iree/actions/runs/26053318650/job/76595135406) | 0% (0/6) | 27 |
| `windows-2022` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26052394472/job/76592018933) | [2m18s](https://github.com/iree-org/iree/actions/runs/26053087706/job/76594378416) | 0% (0/6) | 21 |
| `ubuntu-24.04` | github-hosted | 151 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26051343839/job/76588460267) | [2m10s](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796927) | 12% (6/49) | 151 |
| `macos-14` | github-hosted | 22 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26053059866/job/76594271441) | [1m30s](https://github.com/iree-org/iree/actions/runs/26053087706/job/76594378454) | 0% (0/6) | 22 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m26s](https://github.com/iree-org/iree/actions/runs/26053087706/job/76594378496) | [1m26s](https://github.com/iree-org/iree/actions/runs/26053087706/job/76594378496) | — | 1 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26052394472/job/76592019163) | [1m08s](https://github.com/iree-org/iree/actions/runs/26053087706/job/76594378451) | 0% (0/6) | 21 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [12s](https://github.com/iree-org/iree/actions/runs/26053087706/job/76594378489) | [12s](https://github.com/iree-org/iree/actions/runs/26053087706/job/76594378489) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [19m23s](https://github.com/iree-org/iree/actions/runs/26036368777/job/76559818861) | [1h42m](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596557323) | [1h42m](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596557323) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [10m46s](https://github.com/iree-org/iree/actions/runs/26036368777/job/76559818914) | [1h35m](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796983) | [1h35m](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796983) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 8 | 0 | — | — | [37m17s](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796743) | [1h23m](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596556936) | [1h23m](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596556936) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 8 | 0 | — | — | [13m28s](https://github.com/iree-org/iree/actions/runs/26048845196/job/76581320361) | [1h14m](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796954) | [1h14m](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796954) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [8m51s](https://github.com/iree-org/iree/actions/runs/26051354042/job/76594869600) | [1h01m](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796936) | [1h01m](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796936) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 8 | 0 | — | — | [10m32s](https://github.com/iree-org/iree/actions/runs/26050063505/job/76585584786) | [1h01m](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404665) | [1h01m](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404665) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 8 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26036368777/job/76559818597) | [1h01m](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404222) | [1h01m](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404222) | 8 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 8 | 0 | — | — | [11m29s](https://github.com/iree-org/iree/actions/runs/26036368777/job/76559818787) | [59m28s](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404472) | [59m28s](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404472) | 1 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 7 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26050068139/job/76585101691) | [59m09s](https://github.com/iree-org/iree/actions/runs/26053087706/job/76594378500) | [59m09s](https://github.com/iree-org/iree/actions/runs/26053087706/job/76594378500) | 7 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 8 | 0 | — | — | [15m06s](https://github.com/iree-org/iree/actions/runs/26048845196/job/76581320354) | [51m26s](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596557236) | [51m26s](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596557236) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 8 | 0 | — | — | [11m38s](https://github.com/iree-org/iree/actions/runs/26050063505/job/76585584699) | [49m16s](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404327) | [49m16s](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404327) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 8 | 0 | — | — | [12m19s](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796876) | [46m08s](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404374) | [46m08s](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404374) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 8 | 0 | — | — | [8m08s](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796733) | [43m07s](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596557005) | [43m07s](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596557005) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [5m59s](https://github.com/iree-org/iree/actions/runs/26059564621/job/76617291600) | [40m06s](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796880) | [40m06s](https://github.com/iree-org/iree/actions/runs/26052396398/job/76595796880) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [7m05s](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404394) | [38m29s](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596557237) | [38m29s](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596557237) | 3 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 7 | 0 | — | — | [4m59s](https://github.com/iree-org/iree/actions/runs/26053063193/job/76594277147) | [29m17s](https://github.com/iree-org/iree/actions/runs/26051354042/job/76588496569) | [29m17s](https://github.com/iree-org/iree/actions/runs/26051354042/job/76588496569) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 7 | 0 | — | — | [3m25s](https://github.com/iree-org/iree/actions/runs/26050068139/job/76585101762) | [28m29s](https://github.com/iree-org/iree/actions/runs/26051343839/job/76588460504) | [28m29s](https://github.com/iree-org/iree/actions/runs/26051343839/job/76588460504) | 7 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [9m05s](https://github.com/iree-org/iree/actions/runs/26059564621/job/76617291563) | [23m51s](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596557392) | [23m51s](https://github.com/iree-org/iree/actions/runs/26053078643/job/76596557392) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 8 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26036368777/job/76559818717) | [22m57s](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404353) | [22m57s](https://github.com/iree-org/iree/actions/runs/26053063193/job/76596404353) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 7 | 0 | — | — | [5m14s](https://github.com/iree-org/iree/actions/runs/26048845177/job/76580065325) | [21m24s](https://github.com/iree-org/iree/actions/runs/26051343839/job/76588460708) | [21m24s](https://github.com/iree-org/iree/actions/runs/26051343839/job/76588460708) | 7 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 930 | 2% (19/929) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 818 | 5% (44/818) |  | 4h13m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 257 | 1% (3/257) |  | 4h14m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 747 | 1% (8/747) |  | 4h15m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 766 | 1% (11/766) |  | 4h15m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h14m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h35m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h23m (> 1h00m)
- **[queue-starved]** `linux-mi35x-1gpu-ossci-iree-org` p95 queue 1h01m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
