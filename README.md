# iree-ci-monitor

_Updated: 2026-06-30 11:58 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 11 | 0 | — | — | 0 | [33m21s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618652) | [2h00m](https://github.com/iree-org/iree/actions/runs/28454907011/job/84329599875) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 22 | 0 | — | — | 0 | [44m03s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954784) | [1h37m](https://github.com/iree-org/iree/actions/runs/28454890894/job/84328887666) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [11m44s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618637) | [1h28m](https://github.com/iree-org/iree/actions/runs/28454907011/job/84329599987) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 22 | 0 | — | — | 0 | [43m11s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954787) | [1h23m](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950620) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 11 | 0 | — | — | 0 | [24m39s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618534) | [44m25s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950570) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [18m34s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954721) | [43m43s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981355) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 22 | 0 | — | — | 0 | [15m59s](https://github.com/iree-org/iree/actions/runs/28441302173/job/84281463160) | [43m25s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950779) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [10m04s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954767) | [40m37s](https://github.com/iree-org/iree/actions/runs/28454907011/job/84329600013) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 11 | 0 | — | — | 0 | [6m40s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950454) | [37m54s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618278) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 44 | 0 | — | — | 0 | [6m52s](https://github.com/iree-org/iree/actions/runs/28454890894/job/84328887248) | [34m19s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981332) | 25% (1/4) | 44 |
| `Linux,X64,iree-r9700` | self-hosted | 11 | 0 | — | — | 0 | [16m38s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618295) | [33m09s](https://github.com/iree-org/iree/actions/runs/28454890894/job/84328887309) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 22 | 0 | — | — | 1 | [11m32s](https://github.com/iree-org/iree/actions/runs/28446889874/job/84300219024) | [32m44s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950629) | 50% (1/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981395) | [27m01s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954861) | 0% (0/1) | `iree-mi308-1` |
| `ubuntu-24.04-arm` | github-hosted | 36 | 0 | — | — | 0 | [40s](https://github.com/iree-org/iree/actions/runs/28454907099/job/84328149459) | [6m16s](https://github.com/iree-org/iree/actions/runs/28457588344/job/84336648592) | 0% (0/3) | 36 |
| `ubuntu-24.04` | github-hosted | 232 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28446889874/job/84300218716) | [4m57s](https://github.com/iree-org/iree/actions/runs/28454907099/job/84326907867) | 10% (2/21) | 232 |
| `azure-linux-scale` | ossci | 64 | 0 | — | — | 0 | [40s](https://github.com/iree-org/iree/actions/runs/28457505639/job/84336386111) | [4m46s](https://github.com/iree-org/iree/actions/runs/28457562355/job/84337141615) | 0% (0/8) | 64 |
| `ubuntu-latest` | github-hosted | 27 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28441300991/job/84279676978) | [4m23s](https://github.com/iree-org/iree/actions/runs/28454902704/job/84326904401) | 0% (0/3) | 27 |
| `windows-2022` | github-hosted | 36 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28458788483/job/84340751083) | [4m00s](https://github.com/iree-org/iree/actions/runs/28457505639/job/84336385900) | 0% (0/3) | 36 |
| `macos-14` | github-hosted | 37 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/28454907099/job/84328149504) | [2m05s](https://github.com/iree-org/iree/actions/runs/28457588344/job/84336648745) | 0% (0/4) | 37 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m36s](https://github.com/iree-org/iree/actions/runs/28437557493/job/84267080606) | [1m36s](https://github.com/iree-org/iree/actions/runs/28437557493/job/84267080606) | 0% (0/1) | 1 |
| `azure-windows-scale` | ossci | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28454890073/job/84326895333) | [12s](https://github.com/iree-org/iree/actions/runs/28457505639/job/84336386069) | 0% (0/1) | 12 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28437498613/job/84266891308) | [3s](https://github.com/iree-org/iree/actions/runs/28437498613/job/84266891308) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 3 | 3 | [2h50m](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981214) | 2026-06-30 11:57 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [2h50m](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981214) | 2026-06-30 11:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/overload_iree_tiling_interface_ops` | pull_request |
| [2h46m](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954579) | 2026-06-30 11:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/scalable_vector_level_tiling` | pull_request |
| [2h42m](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707596) | 2026-06-30 11:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/scalable_distribution_tiling` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 3 | 3 | [2h50m](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981214) | 2026-06-30 11:57 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 11 | 0 | — | — | [33m21s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618652) | [2h00m](https://github.com/iree-org/iree/actions/runs/28454907011/job/84329599875) | [2h00m](https://github.com/iree-org/iree/actions/runs/28454907011/job/84329599875) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 11 | 0 | — | — | [50m36s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618704) | [1h42m](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950529) | [1h42m](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950529) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 11 | 0 | — | — | [31m06s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954831) | [1h41m](https://github.com/iree-org/iree/actions/runs/28454890894/job/84328887539) | [1h41m](https://github.com/iree-org/iree/actions/runs/28454890894/job/84328887539) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 11 | 0 | — | — | [11m44s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618637) | [1h28m](https://github.com/iree-org/iree/actions/runs/28454907011/job/84329599987) | [1h28m](https://github.com/iree-org/iree/actions/runs/28454907011/job/84329599987) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 11 | 0 | — | — | [28m26s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618563) | [1h19m](https://github.com/iree-org/iree/actions/runs/28454907011/job/84329600053) | [1h19m](https://github.com/iree-org/iree/actions/runs/28454907011/job/84329600053) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 11 | 0 | — | — | [43m11s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954787) | [1h01m](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707759) | [1h01m](https://github.com/iree-org/iree/actions/runs/28457588532/job/84341707759) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 11 | 0 | — | — | [15m59s](https://github.com/iree-org/iree/actions/runs/28441302173/job/84281463160) | [46m40s](https://github.com/iree-org/iree/actions/runs/28454890894/job/84328887642) | [46m40s](https://github.com/iree-org/iree/actions/runs/28454890894/job/84328887642) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 11 | 0 | — | — | [24m39s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618534) | [44m25s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950570) | [44m25s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950570) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 11 | 0 | — | — | [18m34s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954721) | [43m43s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981355) | [43m43s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981355) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 11 | 0 | — | — | [10m35s](https://github.com/iree-org/iree/actions/runs/28446889874/job/84300218958) | [43m25s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950779) | [43m25s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950779) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 11 | 0 | — | — | [10m04s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954767) | [40m37s](https://github.com/iree-org/iree/actions/runs/28454907011/job/84329600013) | [40m37s](https://github.com/iree-org/iree/actions/runs/28454907011/job/84329600013) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 11 | 0 | — | — | [6m52s](https://github.com/iree-org/iree/actions/runs/28454890894/job/84328887248) | [39m24s](https://github.com/iree-org/iree/actions/runs/28454907011/job/84329599815) | [39m24s](https://github.com/iree-org/iree/actions/runs/28454907011/job/84329599815) | 11 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 11 | 0 | — | — | [6m40s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950454) | [37m54s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618278) | [37m54s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618278) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 11 | 0 | — | — | [11m18s](https://github.com/iree-org/iree/actions/runs/28444248409/job/84292173109) | [35m53s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950396) | [35m53s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950396) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 11 | 0 | — | — | [3m30s](https://github.com/iree-org/iree/actions/runs/28454890894/job/84328887765) | [34m26s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950606) | [34m26s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950606) | 11 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 11 | 0 | — | — | [16m38s](https://github.com/iree-org/iree/actions/runs/28458788426/job/84342618295) | [33m09s](https://github.com/iree-org/iree/actions/runs/28454890894/job/84328887309) | [33m09s](https://github.com/iree-org/iree/actions/runs/28454890894/job/84328887309) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 11 | 0 | — | — | [10m10s](https://github.com/iree-org/iree/actions/runs/28441302173/job/84281463074) | [32m44s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950629) | [32m44s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950629) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 11 | 0 | — | — | [7m57s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981490) | [32m36s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950685) | [32m36s](https://github.com/iree-org/iree/actions/runs/28454890093/job/84328950685) | 11 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28457505709/job/84339981395) | [27m01s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954861) | [27m01s](https://github.com/iree-org/iree/actions/runs/28457562309/job/84340954861) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 165 | 0% (0/164) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 232 | 0% (0/232) |  | 1h33m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 198 | 8% (15/198) |  | 1h33m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 190 | 0% (0/190) |  | 1h44m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 53 | 0% (0/53) |  | 2h09m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 2h50m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h37m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h28m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h23m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h00m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
