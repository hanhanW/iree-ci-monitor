# iree-ci-monitor

_Updated: 2026-06-16 18:31 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [1h11m](https://github.com/iree-org/iree/actions/runs/27644835560/job/81755952629) | [1h20m](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034011) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [1h03m](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756027915) | [1h08m](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033760) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [39m18s](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014162) | [1h06m](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033912) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [58m31s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756028021) | [1h00m](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033926) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [40m29s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756027957) | [55m33s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034021) | — | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [50m16s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756028180) | [55m18s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034006) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [48m51s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033908) | [53m50s](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014180) | — | `shark01-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [38m25s](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014296) | [52m20s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034030) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [43m03s](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014164) | [44m03s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033934) | — | `shark01-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [29m35s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756027851) | [35m25s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033857) | — | `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [21m34s](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014346) | [31m54s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034046) | — | `iree-mi308-1` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [22m59s](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014140) | [28m31s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756027974) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | — | 0 | [10m14s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034004) | [27m13s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756028096) | — | 16 |
| `windows-2022` | github-hosted | 12 | 0 | — | — | 0 | [4m03s](https://github.com/iree-org/iree/actions/runs/27644836452/job/81754010378) | [9m01s](https://github.com/iree-org/iree/actions/runs/27644840622/job/81754092415) | — | 12 |
| `ubuntu-24.04` | github-hosted | 95 | 0 | — | — | 0 | [2m18s](https://github.com/iree-org/iree/actions/runs/27644837028/job/81754015907) | [8m36s](https://github.com/iree-org/iree/actions/runs/27644835560/job/81755952456) | 0% (0/1) | 91 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [3m41s](https://github.com/iree-org/iree/actions/runs/27644837028/job/81754016026) | [6m19s](https://github.com/iree-org/iree/actions/runs/27644840622/job/81754092590) | — | 12 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [4m24s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756027785) | [5m56s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033798) | — | 4 |
| `macos-14` | github-hosted | 12 | 0 | — | — | 0 | [4m20s](https://github.com/iree-org/iree/actions/runs/27644835834/job/81754007912) | [5m44s](https://github.com/iree-org/iree/actions/runs/27644840622/job/81754092400) | — | 12 |
| `azure-linux-scale` | ossci | 20 | 0 | — | — | 0 | [16s](https://github.com/iree-org/iree/actions/runs/27644836452/job/81754010603) | [1m14s](https://github.com/iree-org/iree/actions/runs/27644840622/job/81754092550) | — | 20 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27644829495/job/81753935631) | [13s](https://github.com/iree-org/iree/actions/runs/27629651046/job/81700890024) | — | 9 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/27644837028/job/81754016405) | [7s](https://github.com/iree-org/iree/actions/runs/27644836452/job/81754010591) | — | 4 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [1h12m](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014188) | [1h20m](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034011) | [1h20m](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034011) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [1h11m](https://github.com/iree-org/iree/actions/runs/27644835560/job/81755952629) | [1h19m](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756028006) | [1h19m](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756028006) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [1h03m](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756027915) | [1h08m](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033760) | [1h08m](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033760) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [39m18s](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014162) | [1h06m](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033912) | [1h06m](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033912) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [58m31s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756028021) | [1h00m](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033926) | [1h00m](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033926) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [40m54s](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014248) | [55m33s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034021) | [55m33s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034021) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [50m16s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756028180) | [55m18s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034006) | [55m18s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034006) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [48m51s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033908) | [53m50s](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014180) | [53m50s](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014180) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [39m16s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756028201) | [52m20s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034030) | [52m20s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034030) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [50m31s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034034) | [51m53s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756027972) | [51m53s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756027972) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [40m29s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756027957) | [50m27s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033940) | [50m27s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033940) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [38m25s](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014296) | [49m39s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756028116) | [49m39s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756028116) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [43m03s](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014164) | [44m03s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033934) | [44m03s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033934) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [29m35s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756027851) | [35m25s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033857) | [35m25s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033857) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 4 | 0 | — | — | [21m34s](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014346) | [31m54s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034046) | [31m54s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034046) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 0 | — | — | [22m19s](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014202) | [29m10s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033845) | [29m10s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033845) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [22m59s](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014140) | [28m31s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756027974) | [28m31s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756027974) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 0 | — | — | [26m04s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033984) | [27m13s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756028096) | [27m13s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756028096) | 4 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 0 | — | — | [19m25s](https://github.com/iree-org/iree/actions/runs/27644838491/job/81756027917) | [23m23s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033875) | [23m23s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756033875) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 0 | — | — | [8m18s](https://github.com/iree-org/iree/actions/runs/27644839435/job/81756014305) | [10m14s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034004) | [10m14s](https://github.com/iree-org/iree/actions/runs/27644835265/job/81756034004) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 233 | 0% (1/233) |  | 3h45m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 172 | 1% (2/172) |  | 4h09m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 183 | 5% (10/183) |  | 4h10m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 160 | 0% (0/160) |  | 4h16m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 53 | 0% (0/53) |  | 4h30m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h08m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h00m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
