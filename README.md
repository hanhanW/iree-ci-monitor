# iree-ci-monitor

_Updated: 2026-08-14 12:16 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 18 | 1 | [20m14s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215483) | 2026-08-14 12:16 PDT | 1 | [14m59s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560239) | [1h34m](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695666) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 9 | 1 | [20m14s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215375) | 2026-08-14 12:16 PDT | 0 | [11m26s](https://github.com/iree-org/iree/actions/runs/31802509261/job/94775310387) | [1h19m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933292) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 9 | 0 | — | — | 1 | [15m05s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483387) | [1h17m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933134) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 9 | 0 | — | — | 0 | [12m01s](https://github.com/iree-org/iree/actions/runs/31804688323/job/94782771977) | [1h15m](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695457) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483325) | [56m55s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933190) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 18 | 0 | — | — | 1 | [7m38s](https://github.com/iree-org/iree/actions/runs/31802509261/job/94775310690) | [52m34s](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695445) | 0% (0/5) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 9 | 0 | — | — | 0 | [8m45s](https://github.com/iree-org/iree/actions/runs/31804688323/job/94782771841) | [52m20s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933109) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [7m57s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483339) | [50m35s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933165) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 9 | 0 | — | — | 0 | [11m58s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559933) | [43m01s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933039) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 18 | 0 | — | — | 1 | [6m24s](https://github.com/iree-org/iree/actions/runs/31802509261/job/94775310534) | [39m55s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933236) | 0% (0/5) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 18 | 0 | — | — | 0 | [7m20s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483373) | [23m06s](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695539) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 209 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31798470605/job/94760737449) | [6m02s](https://github.com/iree-org/iree/actions/runs/31791187854/job/94739042554) | 0% (0/56) | 195 |
| `windows-2022` | github-hosted | 30 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31804124582/job/94784490982) | [4m00s](https://github.com/iree-org/iree/actions/runs/31791187854/job/94739042691) | 0% (0/9) | 29 |
| `ubuntu-24.04-arm` | github-hosted | 30 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152726) | [3m33s](https://github.com/iree-org/iree/actions/runs/31791188108/job/94739001078) | 0% (0/9) | 28 |
| `macos-14` | github-hosted | 31 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/31798470605/job/94760737487) | [3m12s](https://github.com/iree-org/iree/actions/runs/31791075820/job/94737931730) | 0% (0/10) | 28 |
| `ubuntu-latest` | github-hosted | 51 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31791076559/job/94737890935) | [2m20s](https://github.com/iree-org/iree/actions/runs/31791432757/job/94739007092) | 0% (0/9) | 51 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m27s](https://github.com/iree-org/iree/actions/runs/31788809443/job/94730759832) | [1m27s](https://github.com/iree-org/iree/actions/runs/31788809443/job/94730759832) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 55 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/31804124582/job/94784491068) | [1m00s](https://github.com/iree-org/iree/actions/runs/31791187854/job/94739042706) | 5% (1/19) | 51 |
| `azure-windows-scale` | ossci | 10 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31802509308/job/94773614898) | [2s](https://github.com/iree-org/iree/actions/runs/31830290714/job/94864152986) | 0% (0/3) | 10 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [20m14s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215375) | 2026-08-14 12:16 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [20m14s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215483) | 2026-08-14 12:16 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [13m13s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215309) | [1h39m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933068) | [1h39m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933068) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 9 | 1 | [20m14s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215483) | 2026-08-14 12:16 PDT | [33m38s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483548) | [1h34m](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695666) | [1h34m](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695666) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 9 | 1 | [20m14s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215375) | 2026-08-14 12:16 PDT | [11m26s](https://github.com/iree-org/iree/actions/runs/31802509261/job/94775310387) | [1h19m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933292) | [1h19m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933292) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 9 | 0 | — | — | [15m05s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483387) | [1h17m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933134) | [1h17m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933134) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 9 | 0 | — | — | [12m01s](https://github.com/iree-org/iree/actions/runs/31804688323/job/94782771977) | [1h15m](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695457) | [1h15m](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695457) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [5m05s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215396) | [1h03m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933155) | [1h03m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933155) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 9 | 0 | — | — | [6m37s](https://github.com/iree-org/iree/actions/runs/31804124598/job/94786717707) | [1h01m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933107) | [1h01m](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933107) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483325) | [56m55s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933190) | [56m55s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933190) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 9 | 0 | — | — | [8m45s](https://github.com/iree-org/iree/actions/runs/31804688323/job/94782771841) | [52m20s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933109) | [52m20s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933109) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 9 | 0 | — | — | [7m57s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483339) | [50m35s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933165) | [50m35s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933165) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 9 | 0 | — | — | [10m15s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483499) | [47m59s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817315) | [47m59s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817315) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 9 | 0 | — | — | [11m58s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819559933) | [43m01s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933039) | [43m01s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933039) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [10m59s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560135) | [39m55s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933236) | [39m55s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933236) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [7m20s](https://github.com/iree-org/iree/actions/runs/31798470509/job/94762483373) | [25m18s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933097) | [25m18s](https://github.com/iree-org/iree/actions/runs/31791188161/job/94740933097) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [8m31s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215388) | [23m06s](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695539) | [23m06s](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695539) | 4 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 12 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31802509308/job/94773614679) | [13m52s](https://github.com/iree-org/iree/actions/runs/31791188108/job/94739001073) | [13m52s](https://github.com/iree-org/iree/actions/runs/31791188108/job/94739001073) | 9 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 12 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31804124582/job/94784490965) | [13m16s](https://github.com/iree-org/iree/actions/runs/31791188108/job/94739001020) | [13m16s](https://github.com/iree-org/iree/actions/runs/31791188108/job/94739001020) | 10 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 9 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31804124598/job/94786717650) | [13m00s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817425) | [13m00s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817425) | 9 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 9 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31815728252/job/94819560152) | [9m59s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817346) | [9m59s](https://github.com/iree-org/iree/actions/runs/31791075838/job/94739817346) | 9 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31830290757/job/94866215205) | [8m19s](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695240) | [8m19s](https://github.com/iree-org/iree/actions/runs/31791187795/job/94740695240) | 9 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 208 | 4% (9/207) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 174 | 10% (17/173) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 207 | 7% (15/206) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 254 | 0% (0/253) | yes | running |

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
