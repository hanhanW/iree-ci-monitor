# iree-ci-monitor

_Updated: 2026-10-20 14:41 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [50m45s](https://github.com/iree-org/iree/actions/runs/39423235040/job/118677868553) | [1h14m](https://github.com/iree-org/iree/actions/runs/39458481906/job/118763027636) | — | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 17 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | 0 | [28m28s](https://github.com/iree-org/iree/actions/runs/39427063922/job/118645989772) | [1h11m](https://github.com/iree-org/iree/actions/runs/39458482898/job/118756661382) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 18 | 2 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | 0 | [43m28s](https://github.com/iree-org/iree/actions/runs/39458482181/job/118758292425) | [1h02m](https://github.com/iree-org/iree/actions/runs/39432445171/job/118664594143) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 16 | 0 | — | — | 0 | [20m39s](https://github.com/iree-org/iree/actions/runs/39458482181/job/118758292568) | [46m30s](https://github.com/iree-org/iree/actions/runs/39414963317/job/118675676641) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [33m27s](https://github.com/iree-org/iree/actions/runs/39458486993/job/118768628604) | [46m04s](https://github.com/iree-org/iree/actions/runs/39432445171/job/118664593941) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 16 | 0 | — | — | 0 | [16m37s](https://github.com/iree-org/iree/actions/runs/39458486993/job/118768627829) | [35m44s](https://github.com/iree-org/iree/actions/runs/39423235040/job/118677868318) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 8 | 0 | — | — | 0 | [8m20s](https://github.com/iree-org/iree/actions/runs/39423235040/job/118677867706) | [23m08s](https://github.com/iree-org/iree/actions/runs/39427063922/job/118645989688) | — | `shark75-ci` |
| `macos-15` | github-hosted | 24 | 0 | — | — | 0 | [46s](https://github.com/iree-org/iree/actions/runs/39423234926/job/118674642886) | [6m19s](https://github.com/iree-org/iree/actions/runs/39458486787/job/118755186587) | — | 24 |
| `ubuntu-24.04-arm` | github-hosted | 24 | 0 | — | — | 0 | [1m30s](https://github.com/iree-org/iree/actions/runs/39423234926/job/118674642965) | [5m52s](https://github.com/iree-org/iree/actions/runs/39458486787/job/118755186572) | — | 24 |
| `ubuntu-24.04` | github-hosted | 227 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/39458486993/job/118768628399) | [5m23s](https://github.com/iree-org/iree/actions/runs/39458486787/job/118755186287) | 33% (1/3) | 202 |
| `ubuntu-latest` | github-hosted | 36 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39458478131/job/118751431404) | [3m05s](https://github.com/iree-org/iree/actions/runs/39458572535/job/118751748084) | — | 36 |
| `azure-linux-scale` | ossci | 48 | 0 | — | — | 0 | [21s](https://github.com/iree-org/iree/actions/runs/39414963317/job/118671493820) | [2m56s](https://github.com/iree-org/iree/actions/runs/39458482862/job/118752592894) | — | 48 |
| `windows-2022` | github-hosted | 24 | 0 | — | — | 0 | [11s](https://github.com/iree-org/iree/actions/runs/39458481894/job/118751881267) | [1m18s](https://github.com/iree-org/iree/actions/runs/39458486787/job/118755186620) | — | 24 |
| `azure-windows-scale` | ossci | 8 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/39458486787/job/118755186816) | [2s](https://github.com/iree-org/iree/actions/runs/39458481894/job/118751882442) | — | 8 |
| `Linux,X64,iree-w7900` | self-hosted | 8 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `fix-spirv-wide-elementwise` | pull_request |
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `fix-spirv-wide-elementwise` | pull_request |
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827580) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `fix-spirv-wide-elementwise` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 9 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | [28m28s](https://github.com/iree-org/iree/actions/runs/39427063922/job/118645989772) | [1h15m](https://github.com/iree-org/iree/actions/runs/39458482181/job/118758292364) | [1h15m](https://github.com/iree-org/iree/actions/runs/39458482181/job/118758292364) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 8 | 0 | — | — | [50m45s](https://github.com/iree-org/iree/actions/runs/39423235040/job/118677868553) | [1h14m](https://github.com/iree-org/iree/actions/runs/39458481906/job/118763027636) | [1h14m](https://github.com/iree-org/iree/actions/runs/39458481906/job/118763027636) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 8 | 0 | — | — | [37m35s](https://github.com/iree-org/iree/actions/runs/39414963317/job/118675676610) | [1h11m](https://github.com/iree-org/iree/actions/runs/39458482898/job/118756661382) | [1h11m](https://github.com/iree-org/iree/actions/runs/39458482898/job/118756661382) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 9 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | [39m39s](https://github.com/iree-org/iree/actions/runs/39458481906/job/118763027982) | [1h06m](https://github.com/iree-org/iree/actions/runs/39458482181/job/118758292609) | [1h06m](https://github.com/iree-org/iree/actions/runs/39458482181/job/118758292609) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 9 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827580) | 2026-10-19 06:26 PDT | [49m19s](https://github.com/iree-org/iree/actions/runs/39414963317/job/118675676954) | [1h02m](https://github.com/iree-org/iree/actions/runs/39432445171/job/118664594143) | [1h02m](https://github.com/iree-org/iree/actions/runs/39432445171/job/118664594143) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [26m38s](https://github.com/iree-org/iree/actions/runs/39458486993/job/118768628362) | [48m54s](https://github.com/iree-org/iree/actions/runs/39423235040/job/118677868706) | [48m54s](https://github.com/iree-org/iree/actions/runs/39423235040/job/118677868706) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [16m52s](https://github.com/iree-org/iree/actions/runs/39458482898/job/118756661247) | [46m26s](https://github.com/iree-org/iree/actions/runs/39414963317/job/118675676440) | [46m26s](https://github.com/iree-org/iree/actions/runs/39414963317/job/118675676440) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 8 | 0 | — | — | [33m27s](https://github.com/iree-org/iree/actions/runs/39458486993/job/118768628604) | [46m04s](https://github.com/iree-org/iree/actions/runs/39432445171/job/118664593941) | [46m04s](https://github.com/iree-org/iree/actions/runs/39432445171/job/118664593941) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [19m25s](https://github.com/iree-org/iree/actions/runs/39427063922/job/118645989680) | [45m23s](https://github.com/iree-org/iree/actions/runs/39414963317/job/118675676468) | [45m23s](https://github.com/iree-org/iree/actions/runs/39414963317/job/118675676468) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [16m37s](https://github.com/iree-org/iree/actions/runs/39458486993/job/118768627829) | [35m44s](https://github.com/iree-org/iree/actions/runs/39423235040/job/118677868318) | [35m44s](https://github.com/iree-org/iree/actions/runs/39423235040/job/118677868318) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 8 | 0 | — | — | [8m20s](https://github.com/iree-org/iree/actions/runs/39423235040/job/118677867706) | [23m08s](https://github.com/iree-org/iree/actions/runs/39427063922/job/118645989688) | [23m08s](https://github.com/iree-org/iree/actions/runs/39427063922/job/118645989688) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 8 | 0 | — | — | [4m23s](https://github.com/iree-org/iree/actions/runs/39458481894/job/118751881907) | [8m08s](https://github.com/iree-org/iree/actions/runs/39458486787/job/118755186524) | [8m08s](https://github.com/iree-org/iree/actions/runs/39458486787/job/118755186524) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 8 | 0 | — | — | [58s](https://github.com/iree-org/iree/actions/runs/39458481894/job/118751881763) | [7m40s](https://github.com/iree-org/iree/actions/runs/39458486787/job/118755186472) | [7m40s](https://github.com/iree-org/iree/actions/runs/39458486787/job/118755186472) | 8 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | 15 | 0 | — | — | [2m24s](https://github.com/iree-org/iree/actions/runs/39458485386/job/118751968121) | [6m37s](https://github.com/iree-org/iree/actions/runs/39458486351/job/118752360113) | [7m13s](https://github.com/iree-org/iree/actions/runs/39458486787/job/118751457581) | 12 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 15 | 0 | — | — | [3m13s](https://github.com/iree-org/iree/actions/runs/39458481894/job/118751881651) | [6m24s](https://github.com/iree-org/iree/actions/runs/39458482862/job/118752592736) | [6m24s](https://github.com/iree-org/iree/actions/runs/39458482862/job/118752592736) | 8 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 8 | 0 | — | — | [57s](https://github.com/iree-org/iree/actions/runs/39432445455/job/118660772601) | [6m23s](https://github.com/iree-org/iree/actions/runs/39458481991/job/118753452546) | [6m23s](https://github.com/iree-org/iree/actions/runs/39458481991/job/118753452546) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 8 | 0 | — | — | [50s](https://github.com/iree-org/iree/actions/runs/39458481991/job/118753452910) | [6m19s](https://github.com/iree-org/iree/actions/runs/39458486787/job/118755186587) | [6m19s](https://github.com/iree-org/iree/actions/runs/39458486787/job/118755186587) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 8 | 0 | — | — | [2m39s](https://github.com/iree-org/iree/actions/runs/39458481991/job/118753452752) | [6m15s](https://github.com/iree-org/iree/actions/runs/39458482862/job/118752592957) | [6m15s](https://github.com/iree-org/iree/actions/runs/39458482862/job/118752592957) | 8 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | 15 | 0 | — | — | [1m00s](https://github.com/iree-org/iree/actions/runs/39458482898/job/118751443680) | [6m10s](https://github.com/iree-org/iree/actions/runs/39458486993/job/118751456555) | [6m21s](https://github.com/iree-org/iree/actions/runs/39458486396/job/118751991881) | 12 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 8 | 0 | — | — | [39s](https://github.com/iree-org/iree/actions/runs/39427063722/job/118642275122) | [6m01s](https://github.com/iree-org/iree/actions/runs/39458486787/job/118755186555) | [6m01s](https://github.com/iree-org/iree/actions/runs/39458486787/job/118755186555) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 460 | 1% (6/460) |  | 3h27m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 384 | 2% (7/384) |  | 3h57m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h14m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h11m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
