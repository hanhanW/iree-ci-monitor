# iree-ci-monitor

_Updated: 2026-07-16 11:43 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-w7900` | self-hosted | 10 | 0 | — | — | 0 | [9m35s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153017) | [34m11s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430115) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [8m25s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931498) | [32m28s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430210) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 10 | 0 | — | — | 0 | [4m53s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931546) | [27m09s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430222) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 10 | 0 | — | — | 0 | [8m22s](https://github.com/iree-org/iree/actions/runs/29516821044/job/87685784229) | [26m10s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153792) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 20 | 0 | — | — | 0 | [10m48s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153460) | [23m26s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931695) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 10 | 0 | — | — | 0 | [5m24s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430254) | [22m41s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071535) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [4m59s](https://github.com/iree-org/iree/actions/runs/29506149210/job/87682196237) | [22m22s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430404) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [12m12s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153784) | [22m05s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531129) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 20 | 0 | — | — | 0 | [7m07s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071525) | [19m42s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531244) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 20 | 0 | — | — | 0 | [8m44s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430429) | [17m54s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153800) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 20 | 0 | — | — | 0 | [4m02s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071701) | [15m38s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931526) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29516821044/job/87685784207) | [9m08s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071631) | 0% (0/3) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430202) | [3m47s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071564) | 0% (0/3) | 10 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m26s](https://github.com/iree-org/iree/actions/runs/29488923147/job/87590019866) | [1m26s](https://github.com/iree-org/iree/actions/runs/29488923147/job/87590019866) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 55 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/29518354633/job/87689413338) | [1m18s](https://github.com/iree-org/iree/actions/runs/29511466819/job/87665759843) | 0% (0/20) | 55 |
| `ubuntu-24.04` | github-hosted | 205 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29517692257/job/87690669402) | [1m00s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931349) | 2% (1/58) | 202 |
| `macos-14` | github-hosted | 31 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29517692257/job/87690669424) | [57s](https://github.com/iree-org/iree/actions/runs/29513901825/job/87674009543) | 10% (1/10) | 31 |
| `windows-2022` | github-hosted | 30 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29511466819/job/87665759725) | [45s](https://github.com/iree-org/iree/actions/runs/29513901825/job/87674009485) | 0% (0/9) | 30 |
| `ubuntu-24.04-arm` | github-hosted | 30 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/29506140961/job/87679878580) | [19s](https://github.com/iree-org/iree/actions/runs/29513901825/job/87674009480) | 0% (0/9) | 30 |
| `azure-windows-scale` | ossci | 10 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29516820995/job/87684321792) | [9s](https://github.com/iree-org/iree/actions/runs/29511466819/job/87665759814) | 0% (0/3) | 10 |
| `ubuntu-latest` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29495515504/job/87611420599) | [4s](https://github.com/iree-org/iree/actions/runs/29507866094/job/87653264480) | 0% (0/9) | 21 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29488888041/job/87589912024) | [3s](https://github.com/iree-org/iree/actions/runs/29488888041/job/87589912024) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 10 | 0 | — | — | [9m35s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153017) | [34m11s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430115) | [34m11s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430115) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [6m35s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531389) | [33m10s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430406) | [33m10s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430406) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 10 | 0 | — | — | [8m25s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931498) | [32m28s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430210) | [32m28s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430210) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 10 | 0 | — | — | [4m53s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931546) | [27m09s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430222) | [27m09s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430222) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 10 | 0 | — | — | [8m22s](https://github.com/iree-org/iree/actions/runs/29516821044/job/87685784229) | [26m10s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153792) | [26m10s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153792) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [7m17s](https://github.com/iree-org/iree/actions/runs/29506149210/job/87682196357) | [26m02s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430501) | [26m02s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430501) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [11m33s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071708) | [23m26s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931695) | [23m26s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931695) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 10 | 0 | — | — | [5m24s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430254) | [22m41s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071535) | [22m41s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071535) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 0 | — | — | [4m59s](https://github.com/iree-org/iree/actions/runs/29506149210/job/87682196237) | [22m22s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430404) | [22m22s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430404) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 10 | 0 | — | — | [12m12s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153784) | [22m05s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531129) | [22m05s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531129) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 0 | — | — | [14m27s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153412) | [21m33s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931685) | [21m33s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931685) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [5m16s](https://github.com/iree-org/iree/actions/runs/29506149210/job/87682196312) | [19m42s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531244) | [19m42s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531244) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 0 | — | — | [8m44s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430429) | [17m54s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153800) | [17m54s](https://github.com/iree-org/iree/actions/runs/29511465096/job/87668153800) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [9m42s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430539) | [16m09s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531161) | [16m09s](https://github.com/iree-org/iree/actions/runs/29503815445/job/87641531161) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [4m02s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071701) | [12m41s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430228) | [12m41s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430228) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29516821044/job/87685784207) | [9m08s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071631) | [9m08s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071631) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29513901825/job/87674009866) | [4m16s](https://github.com/iree-org/iree/actions/runs/29511466819/job/87665759985) | [4m16s](https://github.com/iree-org/iree/actions/runs/29511466819/job/87665759985) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430202) | [3m47s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071564) | [3m47s](https://github.com/iree-org/iree/actions/runs/29513903342/job/87676071564) | 10 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29517692265/job/87692430485) | [1m43s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931672) | [1m43s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931672) | 10 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 10 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29516212616/job/87683627978) | [1m37s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931535) | [1m37s](https://github.com/iree-org/iree/actions/runs/29510394923/job/87665931535) | 10 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 152 | 1% (1/152) |  | 37m38s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 199 | 1% (2/199) |  | 37m39s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 156 | 9% (14/156) |  | 43m02s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 169 | 1% (2/169) |  | 43m57s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 46 | 0% (0/46) |  | 1h07m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
