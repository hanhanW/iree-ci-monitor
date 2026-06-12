# iree-ci-monitor

_Updated: 2026-06-11 18:29 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 22 | 0 | — | — | 0 | [34m31s](https://github.com/iree-org/iree/actions/runs/27360626370/job/80852592318) | [1h27m](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471685) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 11 | 0 | — | — | 0 | [1h09m](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852932018) | [1h19m](https://github.com/iree-org/iree/actions/runs/27361768667/job/80853784740) | — | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 22 | 0 | — | — | 0 | [29m04s](https://github.com/iree-org/iree/actions/runs/27357720080/job/80841221622) | [1h04m](https://github.com/iree-org/iree/actions/runs/27361768667/job/80853784749) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [37m43s](https://github.com/iree-org/iree/actions/runs/27361768667/job/80853784662) | [1h01m](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931862) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 11 | 0 | — | — | 0 | [32m35s](https://github.com/iree-org/iree/actions/runs/27357722610/job/80840141962) | [1h01m](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683194) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 11 | 0 | — | — | 0 | [32m00s](https://github.com/iree-org/iree/actions/runs/27357723771/job/80840176202) | [1h01m](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931922) | — | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 22 | 0 | — | — | 0 | [11m25s](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471656) | [55m20s](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683188) | — | `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [29m16s](https://github.com/iree-org/iree/actions/runs/27357720080/job/80841221666) | [51m49s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931957) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [35m52s](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683396) | [50m33s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852932097) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 22 | 0 | — | — | 0 | [15m15s](https://github.com/iree-org/iree/actions/runs/27357723771/job/80840176315) | [44m20s](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683552) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 11 | 0 | — | — | 0 | [20m33s](https://github.com/iree-org/iree/actions/runs/27357722610/job/80840142265) | [41m15s](https://github.com/iree-org/iree/actions/runs/27357723771/job/80840176418) | — | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27361767227/job/80850734191) | [31m30s](https://github.com/iree-org/iree/actions/runs/27357722925/job/80837949561) | — | 9 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 44 | 0 | — | — | 0 | [7m11s](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471737) | [24m55s](https://github.com/iree-org/iree/actions/runs/27357723771/job/80840176429) | — | 44 |
| `ubuntu-24.04` | github-hosted | 223 | 0 | — | — | 0 | [4m11s](https://github.com/iree-org/iree/actions/runs/27360626370/job/80852592278) | [16m12s](https://github.com/iree-org/iree/actions/runs/27360626370/job/80852592194) | 0% (0/2) | 205 |
| `Linux,X64,iree-w7900` | self-hosted | 11 | 0 | — | — | 0 | [5m16s](https://github.com/iree-org/iree/actions/runs/27361765800/job/80853262059) | [12m33s](https://github.com/iree-org/iree/actions/runs/27357723771/job/80840176021) | — | `shark01-ci`, `shark10-ci` |
| `windows-2022` | github-hosted | 27 | 0 | — | — | 0 | [2m34s](https://github.com/iree-org/iree/actions/runs/27357720650/job/80840077716) | [7m28s](https://github.com/iree-org/iree/actions/runs/27357722925/job/80837949542) | — | 27 |
| `macos-14` | github-hosted | 27 | 0 | — | — | 0 | [2m07s](https://github.com/iree-org/iree/actions/runs/27357720650/job/80840077622) | [6m54s](https://github.com/iree-org/iree/actions/runs/27361768069/job/80851296434) | — | 27 |
| `ubuntu-24.04-arm` | github-hosted | 27 | 0 | — | — | 0 | [1m42s](https://github.com/iree-org/iree/actions/runs/27357720650/job/80840077694) | [5m46s](https://github.com/iree-org/iree/actions/runs/27361769683/job/80851977381) | — | 27 |
| `azure-linux-scale` | ossci | 48 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/27361769683/job/80851977603) | [1m05s](https://github.com/iree-org/iree/actions/runs/27357720650/job/80840077807) | — | 48 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27357722610/job/80840141940) | [39s](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471568) | — | 11 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 11 | 0 | — | — | [26m12s](https://github.com/iree-org/iree/actions/runs/27376521929/job/80903323928) | [1h34m](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471769) | [1h34m](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471769) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 11 | 0 | — | — | [51m45s](https://github.com/iree-org/iree/actions/runs/27361765800/job/80853262633) | [1h27m](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471685) | [1h27m](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471685) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 11 | 0 | — | — | [1h09m](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852932018) | [1h19m](https://github.com/iree-org/iree/actions/runs/27361768667/job/80853784740) | [1h19m](https://github.com/iree-org/iree/actions/runs/27361768667/job/80853784740) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 11 | 0 | — | — | [25m18s](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683584) | [1h04m](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931901) | [1h04m](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931901) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 11 | 0 | — | — | [31m38s](https://github.com/iree-org/iree/actions/runs/27357723655/job/80841232519) | [1h04m](https://github.com/iree-org/iree/actions/runs/27361768667/job/80853784749) | [1h04m](https://github.com/iree-org/iree/actions/runs/27361768667/job/80853784749) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 11 | 0 | — | — | [37m43s](https://github.com/iree-org/iree/actions/runs/27361768667/job/80853784662) | [1h01m](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931862) | [1h01m](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931862) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 11 | 0 | — | — | [32m35s](https://github.com/iree-org/iree/actions/runs/27357722610/job/80840141962) | [1h01m](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683194) | [1h01m](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683194) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 11 | 0 | — | — | [32m00s](https://github.com/iree-org/iree/actions/runs/27357723771/job/80840176202) | [1h01m](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931922) | [1h01m](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931922) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 11 | 0 | — | — | [17m42s](https://github.com/iree-org/iree/actions/runs/27361765800/job/80853262694) | [57m28s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931910) | [57m28s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931910) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 11 | 0 | — | — | [29m16s](https://github.com/iree-org/iree/actions/runs/27357720080/job/80841221666) | [51m49s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931957) | [51m49s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931957) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 11 | 0 | — | — | [35m52s](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683396) | [50m33s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852932097) | [50m33s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852932097) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 11 | 0 | — | — | [8m25s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931958) | [45m25s](https://github.com/iree-org/iree/actions/runs/27361765800/job/80853262852) | [45m25s](https://github.com/iree-org/iree/actions/runs/27361765800/job/80853262852) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 11 | 0 | — | — | [40m18s](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471739) | [44m20s](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683552) | [44m20s](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683552) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 11 | 0 | — | — | [20m33s](https://github.com/iree-org/iree/actions/runs/27357722610/job/80840142265) | [41m15s](https://github.com/iree-org/iree/actions/runs/27357723771/job/80840176418) | [41m15s](https://github.com/iree-org/iree/actions/runs/27357723771/job/80840176418) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 11 | 0 | — | — | [3m47s](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683492) | [36m45s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931959) | [36m45s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931959) | 3 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27361767227/job/80850734191) | [31m30s](https://github.com/iree-org/iree/actions/runs/27357722925/job/80837949561) | [31m30s](https://github.com/iree-org/iree/actions/runs/27357722925/job/80837949561) | 9 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 11 | 0 | — | — | [12m44s](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471703) | [26m55s](https://github.com/iree-org/iree/actions/runs/27357723771/job/80840175945) | [26m55s](https://github.com/iree-org/iree/actions/runs/27357723771/job/80840175945) | 11 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 9 | 0 | — | — | [7m12s](https://github.com/iree-org/iree/actions/runs/27357720650/job/80840077653) | [25m10s](https://github.com/iree-org/iree/actions/runs/27361767872/job/80850784000) | [25m10s](https://github.com/iree-org/iree/actions/runs/27361767872/job/80850784000) | 9 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 11 | 0 | — | — | [10m06s](https://github.com/iree-org/iree/actions/runs/27357723655/job/80841232578) | [24m55s](https://github.com/iree-org/iree/actions/runs/27357723771/job/80840176429) | [24m55s](https://github.com/iree-org/iree/actions/runs/27357723771/job/80840176429) | 11 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 14 | 0 | — | — | [6m10s](https://github.com/iree-org/iree/actions/runs/27357722611/job/80837890287) | [24m47s](https://github.com/iree-org/iree/actions/runs/27357722925/job/80837949524) | [24m47s](https://github.com/iree-org/iree/actions/runs/27357722925/job/80837949524) | 9 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 366 | 2% (8/366) |  | 4h01m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 264 | 2% (5/264) |  | 4h09m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 308 | 7% (21/308) |  | 4h15m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 273 | 2% (5/273) |  | 4h17m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 87 | 1% (1/87) |  | 4h22m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h04m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h19m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h01m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
