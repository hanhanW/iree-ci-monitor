# iree-ci-monitor

_Updated: 2026-07-17 17:51 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `azure-windows-scale` | ossci | 11 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059099) | [1h40m](https://github.com/iree-org/iree/actions/runs/29606211799/job/87970371080) | 100% (1/1) | 6 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [31m54s](https://github.com/iree-org/iree/actions/runs/29590130059/job/87919369329) | [48m07s](https://github.com/iree-org/iree/actions/runs/29606211750/job/87971808811) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 8 | 0 | — | — | 0 | [1m49s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913141) | [36m36s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435299) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 8 | 0 | — | — | 0 | [25m08s](https://github.com/iree-org/iree/actions/runs/29590130059/job/87919369111) | [34m32s](https://github.com/iree-org/iree/actions/runs/29606211750/job/87971808673) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 16 | 0 | — | — | 0 | [15m55s](https://github.com/iree-org/iree/actions/runs/29612157490/job/87990707330) | [31m28s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913292) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 8 | 0 | — | — | 0 | [27m14s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549691) | [30m42s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913254) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 16 | 0 | — | — | 0 | [10m09s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913329) | [29m05s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435588) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 8 | 0 | — | — | 0 | [2m43s](https://github.com/iree-org/iree/actions/runs/29596128645/job/87943109536) | [27m25s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913406) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [7m45s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549681) | [24m57s](https://github.com/iree-org/iree/actions/runs/29606211750/job/87971808850) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 16 | 0 | — | — | 0 | [7m34s](https://github.com/iree-org/iree/actions/runs/29606211750/job/87971808955) | [18m31s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435471) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 16 | 0 | — | — | 0 | [9m03s](https://github.com/iree-org/iree/actions/runs/29596128645/job/87943109631) | [16m10s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549683) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [1m06s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913277) | [11m21s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435554) | 0% (0/1) | `shark01-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29590130059/job/87919369512) | [8m07s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913349) | 0% (0/1) | `iree-mi308-1` |
| `azure-linux-scale` | ossci | 57 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/29605325030/job/87967402950) | [1m37s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059054) | 0% (0/7) | 57 |
| `ubuntu-24.04-arm` | github-hosted | 33 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059042) | [53s](https://github.com/iree-org/iree/actions/runs/29605030076/job/87966238425) | 0% (0/3) | 33 |
| `windows-2022` | github-hosted | 33 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059125) | [33s](https://github.com/iree-org/iree/actions/runs/29605030076/job/87966238121) | 0% (0/3) | 33 |
| `macos-14` | github-hosted | 33 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059105) | [27s](https://github.com/iree-org/iree/actions/runs/29605002828/job/87966039019) | 0% (0/3) | 33 |
| `ubuntu-24.04` | github-hosted | 202 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29606211799/job/87970323811) | [16s](https://github.com/iree-org/iree/actions/runs/29605002828/job/87966038931) | 5% (1/20) | 196 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29605485738/job/87969511238) | [3s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549610) | 0% (0/1) | 8 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29596126404/job/87936839398) | [3s](https://github.com/iree-org/iree/actions/runs/29596126404/job/87936839409) | 0% (0/3) | 3 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 11 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059099) | [1h40m](https://github.com/iree-org/iree/actions/runs/29606211799/job/87970371080) | [1h40m](https://github.com/iree-org/iree/actions/runs/29606211799/job/87970371080) | 6 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 8 | 0 | — | — | [31m54s](https://github.com/iree-org/iree/actions/runs/29590130059/job/87919369329) | [48m07s](https://github.com/iree-org/iree/actions/runs/29606211750/job/87971808811) | [48m07s](https://github.com/iree-org/iree/actions/runs/29606211750/job/87971808811) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [10m59s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913275) | [39m57s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435604) | [39m57s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435604) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 8 | 0 | — | — | [1m49s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913141) | [36m36s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435299) | [36m36s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435299) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 8 | 0 | — | — | [25m08s](https://github.com/iree-org/iree/actions/runs/29590130059/job/87919369111) | [34m32s](https://github.com/iree-org/iree/actions/runs/29606211750/job/87971808673) | [34m32s](https://github.com/iree-org/iree/actions/runs/29606211750/job/87971808673) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [23m29s](https://github.com/iree-org/iree/actions/runs/29606211750/job/87971808897) | [31m28s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913292) | [31m28s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913292) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 8 | 0 | — | — | [27m14s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549691) | [30m42s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913254) | [30m42s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913254) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [10m09s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913329) | [29m22s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435611) | [29m22s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435611) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [10m49s](https://github.com/iree-org/iree/actions/runs/29612157490/job/87990707284) | [29m05s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435588) | [29m05s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435588) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 8 | 0 | — | — | [2m43s](https://github.com/iree-org/iree/actions/runs/29596128645/job/87943109536) | [27m25s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913406) | [27m25s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913406) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 8 | 0 | — | — | [7m45s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88005549681) | [24m57s](https://github.com/iree-org/iree/actions/runs/29606211750/job/87971808850) | [24m57s](https://github.com/iree-org/iree/actions/runs/29606211750/job/87971808850) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [8m40s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913268) | [20m49s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435562) | [20m49s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435562) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 8 | 0 | — | — | [9m03s](https://github.com/iree-org/iree/actions/runs/29596128645/job/87943109631) | [19m35s](https://github.com/iree-org/iree/actions/runs/29606211750/job/87971809000) | [19m35s](https://github.com/iree-org/iree/actions/runs/29606211750/job/87971809000) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [7m34s](https://github.com/iree-org/iree/actions/runs/29606211750/job/87971808955) | [18m31s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435471) | [18m31s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435471) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 8 | 0 | — | — | [10m59s](https://github.com/iree-org/iree/actions/runs/29606211750/job/87971808975) | [16m02s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435589) | [16m02s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435589) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 8 | 0 | — | — | [1m06s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913277) | [11m21s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435554) | [11m21s](https://github.com/iree-org/iree/actions/runs/29605878622/job/87974435554) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29590130059/job/87919369512) | [8m07s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913349) | [8m07s](https://github.com/iree-org/iree/actions/runs/29589096444/job/87919913349) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 11 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/29612157490/job/87989095306) | [1m48s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88004060018) | [1m48s](https://github.com/iree-org/iree/actions/runs/29616965805/job/88004060018) | 11 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 11 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29605325030/job/87967403062) | [1m41s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059128) | [1m41s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059128) | 11 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 11 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29605485814/job/87967682789) | [1m38s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059088) | [1m38s](https://github.com/iree-org/iree/actions/runs/29616965855/job/88004059088) | 11 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 175 | 1% (1/175) |  | 2h01m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 141 | 9% (13/141) |  | 2h02m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 150 | 1% (2/150) |  | 2h08m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 137 | 0% (0/137) |  | 2h11m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 41 | 0% (0/41) |  | 2h21m ago |

## Alerts

- **[queue-starved]** `azure-windows-scale` p95 queue 1h40m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
