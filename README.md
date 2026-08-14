# iree-ci-monitor

_Updated: 2026-08-14 06:46 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 1 | [57m24s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933138) | [1h34m](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695666) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 0 | — | — | 1 | [11m26s](https://github.com/iree-org/iree/actions/runs/31802509261/job/94775310387) | [1h19m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933292) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [15m05s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483387) | [1h17m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933134) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 1 | [11m26s](https://github.com/iree-org/iree/actions/runs/31804688323/job/94782771977) | 2026-08-14 06:45 PDT | 0 | [21m47s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483593) | [1h15m](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695457) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817248) | [56m55s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933190) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [13m10s](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695568) | [52m34s](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695445) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 1 | [11m19s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817186) | [52m20s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933109) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [7m57s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483339) | [50m35s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933165) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [20m49s](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695254) | [43m01s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933039) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [7m20s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817377) | [39m55s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933236) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [8m50s](https://github.com/iree-org/iree/actions/runs/31802509261/job/94775310606) | [23m06s](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695539) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 167 | 0 | — | — | 5 | [3s](https://github.com/iree-org/iree/actions/runs/31802509261/job/94775310511) | [6m12s](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695400) | 0% (0/41) | 154 |
| `windows-2022` | github-hosted | 26 | 0 | — | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/31804124582/job/94784490982) | [4m00s](https://github.com/iree-org/iree/actions/runs/31791187854/job/94739042691) | 0% (0/6) | 25 |
| `ubuntu-24.04-arm` | github-hosted | 27 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/31804688307/job/94781245011) | [3m33s](https://github.com/iree-org/iree/actions/runs/31791188108/job/94739001078) | 0% (0/6) | 25 |
| `macos-14` | github-hosted | 27 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/31804124582/job/94784491115) | [3m12s](https://github.com/iree-org/iree/actions/runs/31791075820/job/94737931730) | 0% (0/6) | 24 |
| `ubuntu-latest` | github-hosted | 42 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31791076557/job/94737891146) | [2m20s](https://github.com/iree-org/iree/actions/runs/31791432757/job/94739007092) | 0% (0/6) | 42 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m27s](https://github.com/iree-org/iree/actions/runs/31788809443/job/94730759832) | [1m27s](https://github.com/iree-org/iree/actions/runs/31788809443/job/94730759832) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 44 | 0 | — | — | 6 | [8s](https://github.com/iree-org/iree/actions/runs/31802509308/job/94773614863) | [53s](https://github.com/iree-org/iree/actions/runs/31791187854/job/94739042735) | 7% (1/14) | 40 |
| `azure-windows-scale` | ossci | 8 | 0 | — | — | 2 | [1s](https://github.com/iree-org/iree/actions/runs/31802509308/job/94773614898) | [2s](https://github.com/iree-org/iree/actions/runs/31804124582/job/94784491160) | 0% (0/2) | 8 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [11m26s](https://github.com/iree-org/iree/actions/runs/31804688323/job/94782771977) | 2026-08-14 06:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | `users/egebeysel/tiling-alignment-hint-2-packs` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [40m11s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483371) | [1h39m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933068) | [1h39m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933068) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [33m38s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483548) | [1h34m](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695666) | [1h34m](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695666) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 6 | 0 | — | — | [11m26s](https://github.com/iree-org/iree/actions/runs/31802509261/job/94775310387) | [1h19m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933292) | [1h19m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933292) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 6 | 0 | — | — | [15m05s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483387) | [1h17m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933134) | [1h17m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933134) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 6 | 1 | [11m26s](https://github.com/iree-org/iree/actions/runs/31804688323/job/94782771977) | 2026-08-14 06:45 PDT | [21m47s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483593) | [1h15m](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695457) | [1h15m](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695457) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31804688323/job/94782771890) | [1h03m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933155) | [1h03m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933155) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [2m22s](https://github.com/iree-org/iree/actions/runs/31804688323/job/94782771911) | [1h01m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933107) | [1h01m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933107) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817248) | [56m55s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933190) | [56m55s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933190) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 0 | — | — | [11m19s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817186) | [52m20s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933109) | [52m20s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933109) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [7m57s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483339) | [50m35s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933165) | [50m35s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933165) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [10m15s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483499) | [47m59s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817315) | [47m59s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817315) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [20m49s](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695254) | [43m01s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933039) | [43m01s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933039) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [6m24s](https://github.com/iree-org/iree/actions/runs/31802509261/job/94775310534) | [39m55s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933236) | [39m55s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933236) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [7m40s](https://github.com/iree-org/iree/actions/runs/31802509261/job/94775310373) | [25m18s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933097) | [25m18s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933097) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [7m20s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817211) | [23m06s](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695539) | [23m06s](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695539) | 3 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 10 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31804124582/job/94784490871) | [13m52s](https://github.com/iree-org/iree/actions/runs/31791188108/job/94739001073) | [13m52s](https://github.com/iree-org/iree/actions/runs/31791188108/job/94739001073) | 7 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 10 | 0 | — | — | [1m00s](https://github.com/iree-org/iree/actions/runs/31791077741/job/94737960755) | [13m16s](https://github.com/iree-org/iree/actions/runs/31791188108/job/94739001020) | [13m16s](https://github.com/iree-org/iree/actions/runs/31791188108/job/94739001020) | 8 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 6 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31802509261/job/94775310511) | [13m00s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817425) | [13m00s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817425) | 6 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31804688323/job/94782772005) | [9m59s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817346) | [9m59s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817346) | 6 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 6 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31802509261/job/94775310369) | [8m19s](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695240) | [8m19s](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695240) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 196 | 8% (15/195) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 198 | 5% (9/197) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 242 | 0% (0/241) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 163 | 10% (17/163) |  | 5m04s ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h34m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h19m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h15m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
