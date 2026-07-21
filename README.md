# iree-ci-monitor

_Updated: 2026-07-20 17:54 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [27m34s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769681) | [1h25m](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702402) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [26m44s](https://github.com/iree-org/iree/actions/runs/29774921418/job/88463781619) | [1h24m](https://github.com/iree-org/iree/actions/runs/29760869641/job/88417585143) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 0 | — | — | 0 | [38m41s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769750) | [1h09m](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784378) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [17m02s](https://github.com/iree-org/iree/actions/runs/29760869641/job/88417585147) | [48m20s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702442) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [13m37s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769654) | [33m42s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784545) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [10m44s](https://github.com/iree-org/iree/actions/runs/29760869641/job/88417584946) | [33m01s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702457) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772140) | [28m22s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702452) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [2m21s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769695) | [26m07s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784248) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772300) | [24m42s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784306) | 0% (0/1) | `iree-mi308-1` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [4m41s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769701) | [22m31s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784428) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [5m24s](https://github.com/iree-org/iree/actions/runs/29774921418/job/88463781408) | [17m50s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702472) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 0 | — | — | 0 | [5m08s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772350) | [15m47s](https://github.com/iree-org/iree/actions/runs/29774921418/job/88463781384) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772130) | [7m35s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784440) | 0% (0/1) | 6 |
| `ubuntu-24.04-arm` | github-hosted | 27 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/29781695181/job/88484237806) | [4m47s](https://github.com/iree-org/iree/actions/runs/29761064240/job/88416236535) | 0% (0/3) | 27 |
| `ubuntu-24.04` | github-hosted | 159 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/29781695181/job/88484237854) | [4m40s](https://github.com/iree-org/iree/actions/runs/29760868342/job/88415063610) | 0% (0/20) | 154 |
| `windows-2022` | github-hosted | 27 | 0 | — | — | 0 | [13s](https://github.com/iree-org/iree/actions/runs/29760830366/job/88414790847) | [3m05s](https://github.com/iree-org/iree/actions/runs/29761249319/job/88416279766) | 0% (0/3) | 27 |
| `macos-14` | github-hosted | 28 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/29760706070/job/88414478547) | [2m15s](https://github.com/iree-org/iree/actions/runs/29760868342/job/88415063620) | 0% (0/3) | 25 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m44s](https://github.com/iree-org/iree/actions/runs/29781695181/job/88484238293) | [1m44s](https://github.com/iree-org/iree/actions/runs/29781695181/job/88484238293) | — | 1 |
| `azure-linux-scale` | ossci | 48 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/29781695181/job/88484238058) | [1m16s](https://github.com/iree-org/iree/actions/runs/29760830366/job/88414791100) | 0% (0/6) | 46 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/29781695181/job/88484238263) | [4s](https://github.com/iree-org/iree/actions/runs/29781695181/job/88484238263) | — | 1 |
| `ubuntu-latest` | github-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29781237064/job/88482732454) | [4s](https://github.com/iree-org/iree/actions/runs/29774920751/job/88461895548) | 0% (0/4) | 4 |
| `azure-windows-scale` | ossci | 9 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29781695181/job/88484238327) | [2s](https://github.com/iree-org/iree/actions/runs/29761064240/job/88416236732) | 0% (0/1) | 9 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [7m40s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784453) | [1h31m](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702443) | [1h31m](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702443) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [27m34s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769681) | [1h25m](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702402) | [1h25m](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702402) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [31m46s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769633) | [1h24m](https://github.com/iree-org/iree/actions/runs/29760869641/job/88417585143) | [1h24m](https://github.com/iree-org/iree/actions/runs/29760869641/job/88417585143) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 6 | 0 | — | — | [38m41s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769750) | [1h09m](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784378) | [1h09m](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784378) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [15m03s](https://github.com/iree-org/iree/actions/runs/29774921418/job/88463781449) | [52m16s](https://github.com/iree-org/iree/actions/runs/29760869641/job/88417585175) | [52m16s](https://github.com/iree-org/iree/actions/runs/29760869641/job/88417585175) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [7m42s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784457) | [48m20s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702442) | [48m20s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702442) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [13m19s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772401) | [34m13s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702545) | [34m13s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702545) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [13m37s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769654) | [33m42s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784545) | [33m42s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784545) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [6m40s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784421) | [33m01s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702457) | [33m01s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702457) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [3m41s](https://github.com/iree-org/iree/actions/runs/29760869641/job/88417584969) | [29m34s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784360) | [29m34s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784360) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772140) | [28m22s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702452) | [28m22s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702452) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 6 | 0 | — | — | [2m21s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769695) | [26m07s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784248) | [26m07s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784248) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772300) | [24m42s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784306) | [24m42s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784306) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [4m41s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769701) | [22m31s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784428) | [22m31s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784428) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [4m01s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772253) | [17m50s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702472) | [17m50s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702472) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 6 | 0 | — | — | [5m08s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772350) | [15m47s](https://github.com/iree-org/iree/actions/runs/29774921418/job/88463781384) | [15m47s](https://github.com/iree-org/iree/actions/runs/29774921418/job/88463781384) | 2 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 9 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29781695181/job/88484237787) | [9m09s](https://github.com/iree-org/iree/actions/runs/29761249319/job/88416279658) | [9m09s](https://github.com/iree-org/iree/actions/runs/29761249319/job/88416279658) | 9 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 9 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29774921306/job/88461929971) | [8m03s](https://github.com/iree-org/iree/actions/runs/29761249319/job/88416279811) | [8m03s](https://github.com/iree-org/iree/actions/runs/29761249319/job/88416279811) | 8 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772535) | [7m59s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769765) | [7m59s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769765) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 9 | 0 | — | — | [21s](https://github.com/iree-org/iree/actions/runs/29760830366/job/88414790910) | [7m49s](https://github.com/iree-org/iree/actions/runs/29761249319/job/88416279715) | [7m49s](https://github.com/iree-org/iree/actions/runs/29761249319/job/88416279715) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 186 | 0% (0/186) |  | 2h31m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 157 | 4% (7/157) |  | 2h33m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 146 | 0% (0/146) |  | 2h34m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 145 | 1% (2/145) |  | 2h38m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 43 | 0% (0/43) |  | 2h45m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h25m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h24m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h09m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
