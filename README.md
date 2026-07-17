# iree-ci-monitor

_Updated: 2026-07-16 17:55 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-w7900` | self-hosted | 10 | 0 | — | — | 0 | [2m34s](https://github.com/iree-org/iree/actions/runs/29513788679/job/87681345452) | [34m11s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430115) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [8m25s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931498) | [32m28s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430210) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 10 | 0 | — | — | 0 | [16m04s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153280) | [27m09s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430222) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 10 | 0 | — | — | 0 | [20m23s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071537) | [26m10s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153792) | 0% (0/4) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [12m12s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153784) | [24m27s](https://github.com/iree-org/iree/actions/runs/29525664741/job/87715104688) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 20 | 0 | — | — | 0 | [5m52s](https://github.com/iree-org/iree/actions/runs/29516821044/job/87685784349) | [23m26s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931695) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 10 | 0 | — | — | 0 | [11m41s](https://github.com/iree-org/iree/actions/runs/29506149210/job/87682196182) | [22m41s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071535) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [5m00s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071516) | [22m22s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430404) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 20 | 0 | — | — | 0 | [7m05s](https://github.com/iree-org/iree/actions/runs/29516821044/job/87685784247) | [17m54s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153800) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 20 | 0 | — | — | 0 | [5m54s](https://github.com/iree-org/iree/actions/runs/29525664741/job/87715104735) | [16m07s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931641) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 20 | 0 | — | — | 0 | [4m58s](https://github.com/iree-org/iree/actions/runs/29516821044/job/87685784147) | [15m30s](https://github.com/iree-org/iree/actions/runs/29525664741/job/87715104724) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29525664741/job/87715104696) | [9m08s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071631) | 0% (0/4) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29525664741/job/87715104573) | [3m47s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071564) | 0% (0/4) | 10 |
| `azure-linux-scale` | ossci | 54 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/29516820995/job/87684321812) | [1m18s](https://github.com/iree-org/iree/actions/runs/29511466819/job/87665759843) | 0% (0/24) | 54 |
| `ubuntu-24.04` | github-hosted | 193 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87702690253) | [1m03s](https://github.com/iree-org/iree/actions/runs/29513901825/job/87674009565) | 0% (0/72) | 191 |
| `macos-14` | github-hosted | 30 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29518354633/job/87689412964) | [1m02s](https://github.com/iree-org/iree/actions/runs/29513901825/job/87674009516) | 0% (0/12) | 30 |
| `windows-2022` | github-hosted | 30 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29517692257/job/87690669390) | [45s](https://github.com/iree-org/iree/actions/runs/29513901825/job/87674009485) | 0% (0/12) | 30 |
| `ubuntu-24.04-arm` | github-hosted | 30 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/29506140961/job/87679878583) | [19s](https://github.com/iree-org/iree/actions/runs/29513901825/job/87674009480) | 0% (0/12) | 30 |
| `azure-windows-scale` | ossci | 10 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29517692257/job/87690669451) | [9s](https://github.com/iree-org/iree/actions/runs/29511466819/job/87665759814) | 0% (0/4) | 10 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29511462379/job/87665709816) | [3s](https://github.com/iree-org/iree/actions/runs/29525661999/job/87713343043) | 0% (0/12) | 12 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 10 | 0 | — | — | [2m34s](https://github.com/iree-org/iree/actions/runs/29513788679/job/87681345452) | [34m11s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430115) | [34m11s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430115) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [5m52s](https://github.com/iree-org/iree/actions/runs/29516821044/job/87685784349) | [33m10s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430406) | [33m10s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430406) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 10 | 0 | — | — | [8m25s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931498) | [32m28s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430210) | [32m28s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430210) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 10 | 0 | — | — | [16m04s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153280) | [27m09s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430222) | [27m09s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430222) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 10 | 0 | — | — | [20m23s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071537) | [26m10s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153792) | [26m10s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153792) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [7m07s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071525) | [26m02s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430501) | [26m02s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430501) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 10 | 0 | — | — | [12m12s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153784) | [24m27s](https://github.com/iree-org/iree/actions/runs/29525664741/job/87715104688) | [24m27s](https://github.com/iree-org/iree/actions/runs/29525664741/job/87715104688) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [10m48s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153460) | [23m26s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931695) | [23m26s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931695) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 10 | 0 | — | — | [11m41s](https://github.com/iree-org/iree/actions/runs/29506149210/job/87682196182) | [22m41s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071535) | [22m41s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071535) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 0 | — | — | [5m00s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071516) | [22m22s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430404) | [22m22s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430404) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 0 | — | — | [14m27s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153412) | [21m33s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931685) | [21m33s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931685) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 0 | — | — | [7m05s](https://github.com/iree-org/iree/actions/runs/29516821044/job/87685784247) | [17m54s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153800) | [17m54s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153800) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [4m35s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153393) | [16m07s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931641) | [16m07s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931641) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [9m42s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430539) | [15m38s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931526) | [15m38s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931526) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [4m58s](https://github.com/iree-org/iree/actions/runs/29516821044/job/87685784147) | [15m30s](https://github.com/iree-org/iree/actions/runs/29525664741/job/87715104724) | [15m30s](https://github.com/iree-org/iree/actions/runs/29525664741/job/87715104724) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29525664741/job/87715104696) | [9m08s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071631) | [9m08s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071631) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29513901825/job/87674009866) | [4m16s](https://github.com/iree-org/iree/actions/runs/29511466819/job/87665759985) | [4m16s](https://github.com/iree-org/iree/actions/runs/29511466819/job/87665759985) | 4 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29525664741/job/87715104573) | [3m47s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071564) | [3m47s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071564) | 10 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29525664741/job/87715104705) | [1m43s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931672) | [1m43s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931672) | 10 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 10 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430414) | [1m37s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931535) | [1m37s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931535) | 10 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 143 | 1% (1/143) |  | 5h25m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 112 | 11% (12/112) |  | 5h27m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 126 | 1% (1/126) |  | 5h30m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 113 | 0% (0/113) |  | 5h34m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 33 | 0% (0/33) |  | 5h45m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
