# iree-ci-monitor

_Updated: 2026-08-25 06:14 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [42m16s](https://github.com/iree-org/iree/actions/runs/32827777432/job/97741991865) | [1h40m](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986161) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [45m28s](https://github.com/iree-org/iree/actions/runs/32816833807/job/97708743753) | [1h32m](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782985951) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 0 | — | — | 0 | [44m21s](https://github.com/iree-org/iree/actions/runs/32827777432/job/97741991745) | [1h17m](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781331185) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [20m05s](https://github.com/iree-org/iree/actions/runs/32816833807/job/97708743785) | [1h06m](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986081) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [41m17s](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781331139) | [57m09s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986060) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | [31m23s](https://github.com/iree-org/iree/actions/runs/32816833807/job/97708743723) | [50m38s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782985760) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [9m15s](https://github.com/iree-org/iree/actions/runs/32824937355/job/97732899455) | [49m20s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986207) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 0 | — | — | 0 | [30m36s](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781331274) | [45m13s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986094) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [20m36s](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781331090) | [43m11s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986083) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [15m38s](https://github.com/iree-org/iree/actions/runs/32816833807/job/97708743901) | [41m33s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986104) | 0% (0/6) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [7m17s](https://github.com/iree-org/iree/actions/runs/32824937355/job/97732899361) | [29m41s](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781331131) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m36s](https://github.com/iree-org/iree/actions/runs/32831805181/job/97751954327) | [1m36s](https://github.com/iree-org/iree/actions/runs/32831805181/job/97751954327) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 40 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/32824937510/job/97730809305) | [1m28s](https://github.com/iree-org/iree/actions/runs/32840459774/job/97778634636) | 5% (1/20) | 40 |
| `azure-windows-scale` | ossci | 7 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/32827675645/job/97739258971) | [1m16s](https://github.com/iree-org/iree/actions/runs/32841171841/job/97780826006) | 0% (0/3) | 7 |
| `ubuntu-24.04-arm` | github-hosted | 24 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/32824937510/job/97730809316) | [1m10s](https://github.com/iree-org/iree/actions/runs/32841171841/job/97780825690) | 0% (0/9) | 24 |
| `ubuntu-24.04` | github-hosted | 185 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/32848664972/job/97804269604) | [46s](https://github.com/iree-org/iree/actions/runs/32827777330/job/97739682976) | 3% (2/58) | 169 |
| `windows-2022` | github-hosted | 23 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/32840459714/job/97778624397) | [34s](https://github.com/iree-org/iree/actions/runs/32827675645/job/97739258839) | 0% (0/9) | 22 |
| `macos-14` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32841171841/job/97780825922) | [3s](https://github.com/iree-org/iree/actions/runs/32841171841/job/97780825890) | 0% (0/10) | 24 |
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32841171602/job/97780782328) | [3s](https://github.com/iree-org/iree/actions/runs/32840459132/job/97778582532) | 0% (0/9) | 18 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [1h32m](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781331166) | [1h40m](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986161) | [1h40m](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986161) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [45m28s](https://github.com/iree-org/iree/actions/runs/32816833807/job/97708743753) | [1h32m](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782985951) | [1h32m](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782985951) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 6 | 0 | — | — | [44m21s](https://github.com/iree-org/iree/actions/runs/32827777432/job/97741991745) | [1h17m](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781331185) | [1h17m](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781331185) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 6 | 0 | — | — | [20m05s](https://github.com/iree-org/iree/actions/runs/32816833807/job/97708743785) | [1h06m](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986081) | [1h06m](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986081) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [41m17s](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781331139) | [57m09s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986060) | [57m09s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986060) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 0 | — | — | [31m23s](https://github.com/iree-org/iree/actions/runs/32816833807/job/97708743723) | [50m38s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782985760) | [50m38s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782985760) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [2m07s](https://github.com/iree-org/iree/actions/runs/32827777432/job/97741991780) | [49m20s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986207) | [49m20s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986207) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 6 | 0 | — | — | [30m36s](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781331274) | [45m13s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986094) | [45m13s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986094) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [18m31s](https://github.com/iree-org/iree/actions/runs/32816833807/job/97708743834) | [44m21s](https://github.com/iree-org/iree/actions/runs/32827777432/job/97741991682) | [44m21s](https://github.com/iree-org/iree/actions/runs/32827777432/job/97741991682) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [20m36s](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781331090) | [43m11s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986083) | [43m11s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986083) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [4m17s](https://github.com/iree-org/iree/actions/runs/32816833807/job/97708743842) | [41m33s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986104) | [41m33s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986104) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [10m09s](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781331132) | [36m58s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986173) | [36m58s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986173) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [5m06s](https://github.com/iree-org/iree/actions/runs/32824937355/job/97732899320) | [29m41s](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781331131) | [29m41s](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781331131) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [17m31s](https://github.com/iree-org/iree/actions/runs/32827777432/job/97741991884) | [17m53s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986159) | [17m53s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986159) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [7m17s](https://github.com/iree-org/iree/actions/runs/32824937355/job/97732899361) | [17m42s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782985991) | [17m42s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782985991) | 3 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 6 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32824937355/job/97732899552) | [2m53s](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781330903) | [2m53s](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781330903) | 6 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32841171908/job/97782986098) | [2m29s](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781331030) | [2m29s](https://github.com/iree-org/iree/actions/runs/32840459774/job/97781331030) | 6 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m36s](https://github.com/iree-org/iree/actions/runs/32831805181/job/97751954327) | [1m36s](https://github.com/iree-org/iree/actions/runs/32831805181/job/97751954327) | [1m36s](https://github.com/iree-org/iree/actions/runs/32831805181/job/97751954327) | 1 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 6 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32824937355/job/97732899266) | [1m35s](https://github.com/iree-org/iree/actions/runs/32816833807/job/97708743708) | [1m35s](https://github.com/iree-org/iree/actions/runs/32816833807/job/97708743708) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 7 | 0 | — | — | [24s](https://github.com/iree-org/iree/actions/runs/32827777330/job/97739683204) | [1m30s](https://github.com/iree-org/iree/actions/runs/32840459714/job/97778624449) | [1m30s](https://github.com/iree-org/iree/actions/runs/32840459714/job/97778624449) | 7 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 246 | 1% (3/245) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 228 | 3% (6/227) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 179 | 0% (0/178) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 171 | 0% (0/170) | yes | running |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h40m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h17m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
