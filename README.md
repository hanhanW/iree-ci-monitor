# iree-ci-monitor

_Updated: 2026-07-22 17:55 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 7 | 0 | — | — | 0 | [16m49s](https://github.com/iree-org/iree/actions/runs/29941978759/job/89000645143) | [1h50m](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962933041) | 0% (0/1) | `shark75-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 7 | 1 | [4h39m](https://github.com/iree-org/iree/actions/runs/29953845448/job/89039634046) | 2026-07-22 17:55 PDT | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962932914) | [1h40m](https://github.com/iree-org/iree/actions/runs/29946677218/job/89015847432) | 0% (0/1) | 6 |
| `Linux,X64,gfx1201` | self-hosted | 14 | 0 | — | — | 0 | [32m54s](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962933123) | [1h24m](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971517062) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [26m15s](https://github.com/iree-org/iree/actions/runs/29941978759/job/89000645563) | [58m57s](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971517187) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 7 | 0 | — | — | 0 | [16m24s](https://github.com/iree-org/iree/actions/runs/29941978759/job/89000645497) | [55m00s](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962933004) | 0% (0/1) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 7 | 0 | — | — | 0 | [8m12s](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971516819) | [45m51s](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962933228) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [3m14s](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962933225) | [25m52s](https://github.com/iree-org/iree/actions/runs/29946677218/job/89015847539) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [9m27s](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962933070) | [23m25s](https://github.com/iree-org/iree/actions/runs/29946677218/job/89015847418) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 14 | 0 | — | — | 0 | [7m58s](https://github.com/iree-org/iree/actions/runs/29941978759/job/89000645591) | [21m52s](https://github.com/iree-org/iree/actions/runs/29946338617/job/89014788833) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 14 | 0 | — | — | 0 | [7m46s](https://github.com/iree-org/iree/actions/runs/29953845448/job/89039634353) | [18m55s](https://github.com/iree-org/iree/actions/runs/29946338617/job/89014788666) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 7 | 0 | — | — | 0 | [12m04s](https://github.com/iree-org/iree/actions/runs/29941978759/job/89000645163) | [16m11s](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971516927) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 14 | 0 | — | — | 0 | [8m24s](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971517113) | [15m45s](https://github.com/iree-org/iree/actions/runs/29946338617/job/89014788550) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29941978759/job/89000645473) | [7m18s](https://github.com/iree-org/iree/actions/runs/29946677218/job/89015847448) | 0% (0/1) | `iree-mi308-1` |
| `azure-linux-scale` | ossci | 41 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/29940800089/job/88993901891) | [1m32s](https://github.com/iree-org/iree/actions/runs/29946677008/job/89013745066) | 0% (0/6) | 41 |
| `ubuntu-24.04-arm` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29953845395/job/89037958077) | [5s](https://github.com/iree-org/iree/actions/runs/29931058043/job/88960637828) | 0% (0/3) | 21 |
| `ubuntu-24.04` | github-hosted | 164 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29946677008/job/89013744978) | [4s](https://github.com/iree-org/iree/actions/runs/29941978759/job/89000645250) | 0% (0/20) | 156 |
| `windows-2022` | github-hosted | 24 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29941981551/job/88997921195) | [4s](https://github.com/iree-org/iree/actions/runs/29940800089/job/88993901611) | 0% (0/3) | 21 |
| `macos-14` | github-hosted | 24 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29930180513/job/88968825814) | [4s](https://github.com/iree-org/iree/actions/runs/29941981551/job/88997921053) | 0% (0/3) | 21 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29940796953/job/88993839095) | [3s](https://github.com/iree-org/iree/actions/runs/29940796953/job/88993839039) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29930180513/job/88968825993) | [2s](https://github.com/iree-org/iree/actions/runs/29953789567/job/89037704780) | 0% (0/1) | 8 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [4h39m](https://github.com/iree-org/iree/actions/runs/29953845448/job/89039634046) | 2026-07-22 17:55 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `pinned-transfer-execution-placement` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 7 | 1 | [4h39m](https://github.com/iree-org/iree/actions/runs/29953845448/job/89039634046) | 2026-07-22 17:55 PDT | [2s](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962932914) | [1h40m](https://github.com/iree-org/iree/actions/runs/29946677218/job/89015847432) | [1h40m](https://github.com/iree-org/iree/actions/runs/29946677218/job/89015847432) | 6 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 7 | 0 | — | — | [16m49s](https://github.com/iree-org/iree/actions/runs/29941978759/job/89000645143) | [1h50m](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962933041) | [1h50m](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962933041) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [30m32s](https://github.com/iree-org/iree/actions/runs/29946677218/job/89015847564) | [1h50m](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971517001) | [1h50m](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971517001) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [20m08s](https://github.com/iree-org/iree/actions/runs/29946338617/job/89014788475) | [1h24m](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971517062) | [1h24m](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971517062) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 7 | 0 | — | — | [26m15s](https://github.com/iree-org/iree/actions/runs/29941978759/job/89000645563) | [58m57s](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971517187) | [58m57s](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971517187) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 7 | 0 | — | — | [16m24s](https://github.com/iree-org/iree/actions/runs/29941978759/job/89000645497) | [55m00s](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962933004) | [55m00s](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962933004) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 7 | 0 | — | — | [8m12s](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971516819) | [45m51s](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962933228) | [45m51s](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962933228) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 7 | 0 | — | — | [7m58s](https://github.com/iree-org/iree/actions/runs/29941978759/job/89000645591) | [42m58s](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962933181) | [42m58s](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962933181) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 7 | 0 | — | — | [3m14s](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962933225) | [25m52s](https://github.com/iree-org/iree/actions/runs/29946677218/job/89015847539) | [25m52s](https://github.com/iree-org/iree/actions/runs/29946677218/job/89015847539) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 7 | 0 | — | — | [10m40s](https://github.com/iree-org/iree/actions/runs/29953845448/job/89039634350) | [24m00s](https://github.com/iree-org/iree/actions/runs/29946677218/job/89015847595) | [24m00s](https://github.com/iree-org/iree/actions/runs/29946677218/job/89015847595) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 7 | 0 | — | — | [9m27s](https://github.com/iree-org/iree/actions/runs/29931060884/job/88962933070) | [23m25s](https://github.com/iree-org/iree/actions/runs/29946677218/job/89015847418) | [23m25s](https://github.com/iree-org/iree/actions/runs/29946677218/job/89015847418) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 7 | 0 | — | — | [6m20s](https://github.com/iree-org/iree/actions/runs/29941978759/job/89000645547) | [18m55s](https://github.com/iree-org/iree/actions/runs/29946338617/job/89014788666) | [18m55s](https://github.com/iree-org/iree/actions/runs/29946338617/job/89014788666) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 7 | 0 | — | — | [12m04s](https://github.com/iree-org/iree/actions/runs/29941978759/job/89000645163) | [16m11s](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971516927) | [16m11s](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971516927) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 7 | 0 | — | — | [4m01s](https://github.com/iree-org/iree/actions/runs/29946677218/job/89015847594) | [16m03s](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971516952) | [16m03s](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971516952) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [8m24s](https://github.com/iree-org/iree/actions/runs/29930177813/job/88971517113) | [15m48s](https://github.com/iree-org/iree/actions/runs/29940799502/job/89017153537) | [15m48s](https://github.com/iree-org/iree/actions/runs/29940799502/job/89017153537) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [5m43s](https://github.com/iree-org/iree/actions/runs/29941978759/job/89000645512) | [15m45s](https://github.com/iree-org/iree/actions/runs/29946338617/job/89014788550) | [15m45s](https://github.com/iree-org/iree/actions/runs/29946338617/job/89014788550) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 7 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29941978759/job/89000645473) | [7m18s](https://github.com/iree-org/iree/actions/runs/29946677218/job/89015847448) | [7m18s](https://github.com/iree-org/iree/actions/runs/29946677218/job/89015847448) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 8 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29953789567/job/89037704727) | [1m55s](https://github.com/iree-org/iree/actions/runs/29946677008/job/89013745030) | [1m55s](https://github.com/iree-org/iree/actions/runs/29946677008/job/89013745030) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 8 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29931058043/job/88960638146) | [1m36s](https://github.com/iree-org/iree/actions/runs/29946677008/job/89013745128) | [1m36s](https://github.com/iree-org/iree/actions/runs/29946677008/job/89013745128) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 8 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/29941981551/job/88997921308) | [1m32s](https://github.com/iree-org/iree/actions/runs/29946677008/job/89013745066) | [1m32s](https://github.com/iree-org/iree/actions/runs/29946677008/job/89013745066) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 360 | 1% (3/360) |  | 4h19m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 285 | 4% (10/285) |  | 4h24m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 271 | 1% (2/271) |  | 4h25m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 277 | 1% (4/277) |  | 4h27m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 83 | 1% (1/83) |  | 4h28m ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 4h39m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h24m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h50m (> 1h00m)
- **[queue-starved]** `linux-mi325-1gpu-ossci-iree-org` p95 queue 1h40m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
