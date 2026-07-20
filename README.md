# iree-ci-monitor

_Updated: 2026-07-20 11:58 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 22 | 0 | — | — | 0 | [1h11m](https://github.com/iree-org/iree/actions/runs/29740509077/job/88347607802) | [3h18m](https://github.com/iree-org/iree/actions/runs/29732965749/job/88344524235) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 11 | 0 | — | — | 0 | [39m31s](https://github.com/iree-org/iree/actions/runs/29760869641/job/88417585104) | [2h32m](https://github.com/iree-org/iree/actions/runs/29722156559/job/88347082040) | 0% (0/4) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 11 | 0 | — | — | 0 | [10m37s](https://github.com/iree-org/iree/actions/runs/29751572209/job/88385368930) | [2h06m](https://github.com/iree-org/iree/actions/runs/29740509077/job/88347607574) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 11 | 0 | — | — | 0 | [28m22s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702452) | [2h00m](https://github.com/iree-org/iree/actions/runs/29722156559/job/88347081904) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [26m07s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784248) | [1h40m](https://github.com/iree-org/iree/actions/runs/29741530783/job/88350544266) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [51m38s](https://github.com/iree-org/iree/actions/runs/29740509077/job/88347607760) | [1h25m](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702402) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 22 | 0 | — | — | 0 | [18m51s](https://github.com/iree-org/iree/actions/runs/29722156559/job/88347082138) | [52m16s](https://github.com/iree-org/iree/actions/runs/29760869641/job/88417585175) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 11 | 0 | — | — | 0 | [24m46s](https://github.com/iree-org/iree/actions/runs/29722156559/job/88347082041) | [47m58s](https://github.com/iree-org/iree/actions/runs/29744160852/job/88359845454) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 22 | 0 | — | — | 0 | [10m44s](https://github.com/iree-org/iree/actions/runs/29760869641/job/88417584946) | [47m44s](https://github.com/iree-org/iree/actions/runs/29744160852/job/88359845751) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [11m15s](https://github.com/iree-org/iree/actions/runs/29751572209/job/88385368855) | [31m45s](https://github.com/iree-org/iree/actions/runs/29722156559/job/88347082062) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 22 | 0 | — | — | 0 | [9m19s](https://github.com/iree-org/iree/actions/runs/29722156559/job/88347082060) | [30m19s](https://github.com/iree-org/iree/actions/runs/29741530783/job/88350544288) | 12% (1/8) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29751572209/job/88385368811) | [24m42s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784306) | 0% (0/4) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702264) | [7m35s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784440) | 0% (0/4) | 11 |
| `ubuntu-24.04-arm` | github-hosted | 45 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/29760706070/job/88414478467) | [4m43s](https://github.com/iree-org/iree/actions/runs/29761249319/job/88416279708) | 0% (0/12) | 44 |
| `ubuntu-24.04` | github-hosted | 266 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29741530783/job/88350544243) | [3m52s](https://github.com/iree-org/iree/actions/runs/29760869641/job/88417584991) | 3% (2/75) | 261 |
| `windows-2022` | github-hosted | 45 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/29722156553/job/88345149384) | [2m21s](https://github.com/iree-org/iree/actions/runs/29761064240/job/88416236558) | 0% (0/12) | 45 |
| `macos-14` | github-hosted | 46 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29746095702/job/88364363308) | [2m08s](https://github.com/iree-org/iree/actions/runs/29760868342/job/88415063568) | 0% (0/13) | 42 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m21s](https://github.com/iree-org/iree/actions/runs/29734619934/job/88326896169) | [1m21s](https://github.com/iree-org/iree/actions/runs/29734619934/job/88326896169) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 81 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/29760706070/job/88414478701) | [1m16s](https://github.com/iree-org/iree/actions/runs/29760830366/job/88414791214) | 0% (0/26) | 75 |
| `ubuntu-latest` | github-hosted | 25 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29752252893/job/88385515016) | [10s](https://github.com/iree-org/iree/actions/runs/29752252308/job/88385566424) | 0% (0/13) | 25 |
| `azure-windows-scale` | ossci | 15 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29761249319/job/88416279904) | [2s](https://github.com/iree-org/iree/actions/runs/29760830366/job/88414791199) | 0% (0/4) | 15 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29734617281/job/88326887245) | [2s](https://github.com/iree-org/iree/actions/runs/29734617281/job/88326887245) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 11 | 0 | — | — | [1h24m](https://github.com/iree-org/iree/actions/runs/29760869641/job/88417585143) | [3h24m](https://github.com/iree-org/iree/actions/runs/29732965749/job/88344524079) | [3h24m](https://github.com/iree-org/iree/actions/runs/29732965749/job/88344524079) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 11 | 0 | — | — | [1h11m](https://github.com/iree-org/iree/actions/runs/29740509077/job/88347607802) | [3h18m](https://github.com/iree-org/iree/actions/runs/29732965749/job/88344524235) | [3h18m](https://github.com/iree-org/iree/actions/runs/29732965749/job/88344524235) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 11 | 0 | — | — | [39m31s](https://github.com/iree-org/iree/actions/runs/29760869641/job/88417585104) | [2h32m](https://github.com/iree-org/iree/actions/runs/29722156559/job/88347082040) | [2h32m](https://github.com/iree-org/iree/actions/runs/29722156559/job/88347082040) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 11 | 0 | — | — | [10m37s](https://github.com/iree-org/iree/actions/runs/29751572209/job/88385368930) | [2h06m](https://github.com/iree-org/iree/actions/runs/29740509077/job/88347607574) | [2h06m](https://github.com/iree-org/iree/actions/runs/29740509077/job/88347607574) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 11 | 0 | — | — | [28m22s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702452) | [2h00m](https://github.com/iree-org/iree/actions/runs/29722156559/job/88347081904) | [2h00m](https://github.com/iree-org/iree/actions/runs/29722156559/job/88347081904) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 11 | 0 | — | — | [26m07s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784248) | [1h40m](https://github.com/iree-org/iree/actions/runs/29741530783/job/88350544266) | [1h40m](https://github.com/iree-org/iree/actions/runs/29741530783/job/88350544266) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 11 | 0 | — | — | [51m38s](https://github.com/iree-org/iree/actions/runs/29740509077/job/88347607760) | [1h25m](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702402) | [1h25m](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702402) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 11 | 0 | — | — | [20m52s](https://github.com/iree-org/iree/actions/runs/29744160852/job/88359845739) | [57m38s](https://github.com/iree-org/iree/actions/runs/29741530783/job/88350544238) | [57m38s](https://github.com/iree-org/iree/actions/runs/29741530783/job/88350544238) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 11 | 0 | — | — | [16m11s](https://github.com/iree-org/iree/actions/runs/29760869641/job/88417585071) | [52m00s](https://github.com/iree-org/iree/actions/runs/29741530783/job/88350544239) | [52m00s](https://github.com/iree-org/iree/actions/runs/29741530783/job/88350544239) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 11 | 0 | — | — | [18m51s](https://github.com/iree-org/iree/actions/runs/29722156559/job/88347082138) | [48m20s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702442) | [48m20s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702442) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 11 | 0 | — | — | [24m46s](https://github.com/iree-org/iree/actions/runs/29722156559/job/88347082041) | [47m58s](https://github.com/iree-org/iree/actions/runs/29744160852/job/88359845454) | [47m58s](https://github.com/iree-org/iree/actions/runs/29744160852/job/88359845454) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 11 | 0 | — | — | [9m33s](https://github.com/iree-org/iree/actions/runs/29722156559/job/88347082081) | [41m49s](https://github.com/iree-org/iree/actions/runs/29741530783/job/88350544391) | [41m49s](https://github.com/iree-org/iree/actions/runs/29741530783/job/88350544391) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 11 | 0 | — | — | [15m59s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784271) | [37m18s](https://github.com/iree-org/iree/actions/runs/29744160852/job/88359846045) | [37m18s](https://github.com/iree-org/iree/actions/runs/29744160852/job/88359846045) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 11 | 0 | — | — | [11m15s](https://github.com/iree-org/iree/actions/runs/29751572209/job/88385368855) | [31m45s](https://github.com/iree-org/iree/actions/runs/29722156559/job/88347082062) | [31m45s](https://github.com/iree-org/iree/actions/runs/29722156559/job/88347082062) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 11 | 0 | — | — | [9m07s](https://github.com/iree-org/iree/actions/runs/29740509077/job/88347607792) | [30m19s](https://github.com/iree-org/iree/actions/runs/29741530783/job/88350544288) | [30m19s](https://github.com/iree-org/iree/actions/runs/29741530783/job/88350544288) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29751572209/job/88385368811) | [24m42s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784306) | [24m42s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784306) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 11 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29722156559/job/88347082045) | [7m59s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769765) | [7m59s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769765) | 11 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 11 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29751572209/job/88385368932) | [7m48s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769714) | [7m48s](https://github.com/iree-org/iree/actions/runs/29760830518/job/88416769714) | 11 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29761062908/job/88418702264) | [7m35s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784440) | [7m35s](https://github.com/iree-org/iree/actions/runs/29761249758/job/88418784440) | 11 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 15 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29751550716/job/88383120348) | [4m47s](https://github.com/iree-org/iree/actions/runs/29760868342/job/88415063573) | [8m03s](https://github.com/iree-org/iree/actions/runs/29761249319/job/88416279811) | 14 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 224 | 0% (1/224) |  | 14m18s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 184 | 8% (14/184) |  | 41m52s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 175 | 0% (0/175) |  | 1h00m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 185 | 1% (2/185) |  | 1h18m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 52 | 0% (0/52) |  | 1h21m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h25m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h18m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h40m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h32m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h06m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
