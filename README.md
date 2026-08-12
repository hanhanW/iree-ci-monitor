# iree-ci-monitor

_Updated: 2026-08-12 12:29 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 20 | 0 | — | — | 0 | [17m54s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070809961) | [59m24s](https://github.com/iree-org/iree/actions/runs/31615316522/job/94185307365) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 10 | 0 | — | — | 0 | [2m11s](https://github.com/iree-org/iree/actions/runs/31583219282/job/94079019241) | [58m26s](https://github.com/iree-org/iree/actions/runs/31615316522/job/94185307074) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 20 | 0 | — | — | 0 | [6m58s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169165) | [58m08s](https://github.com/iree-org/iree/actions/runs/31615316522/job/94185307217) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 10 | 0 | — | — | 0 | [9m56s](https://github.com/iree-org/iree/actions/runs/31614923996/job/94178486329) | [56m19s](https://github.com/iree-org/iree/actions/runs/31615316522/job/94185307041) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 10 | 0 | — | — | 0 | [18m14s](https://github.com/iree-org/iree/actions/runs/31614923996/job/94178486495) | [55m05s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169251) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [12m39s](https://github.com/iree-org/iree/actions/runs/31589330007/job/94092226500) | [53m47s](https://github.com/iree-org/iree/actions/runs/31615316522/job/94185306979) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 20 | 0 | — | — | 0 | [8m45s](https://github.com/iree-org/iree/actions/runs/31615322145/job/94185128788) | [44m32s](https://github.com/iree-org/iree/actions/runs/31615322145/job/94185129010) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 10 | 0 | — | — | 0 | [15m45s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531389) | [43m52s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169167) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [3m23s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531356) | [41m41s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169362) | 50% (1/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [14m19s](https://github.com/iree-org/iree/actions/runs/31605809229/job/94154291127) | [28m29s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169242) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 20 | 0 | — | — | 0 | [6m45s](https://github.com/iree-org/iree/actions/runs/31583219282/job/94079019333) | [24m38s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169263) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 209 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169474) | [4m47s](https://github.com/iree-org/iree/actions/runs/31615331775/job/94177926087) | 5% (2/39) | 203 |
| `windows-2022` | github-hosted | 30 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/31605809008/job/94145184163) | [4m42s](https://github.com/iree-org/iree/actions/runs/31615322150/job/94177103373) | 0% (0/6) | 30 |
| `macos-14` | github-hosted | 31 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/31589329864/job/94090451974) | [4m01s](https://github.com/iree-org/iree/actions/runs/31615316748/job/94176619531) | 0% (0/7) | 31 |
| `ubuntu-24.04-arm` | github-hosted | 30 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/31604781901/job/94140910107) | [3m55s](https://github.com/iree-org/iree/actions/runs/31615331775/job/94177926245) | 0% (0/6) | 30 |
| `azure-linux-scale` | ossci | 57 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/31583219161/job/94077093284) | [1m58s](https://github.com/iree-org/iree/actions/runs/31614924207/job/94175300947) | 0% (0/15) | 57 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m28s](https://github.com/iree-org/iree/actions/runs/31583860263/job/94073002035) | [1m28s](https://github.com/iree-org/iree/actions/runs/31583860263/job/94073002035) | 0% (0/1) | 1 |
| `ubuntu-latest` | github-hosted | 36 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31586384334/job/94081089434) | [42s](https://github.com/iree-org/iree/actions/runs/31615328658/job/94176596563) | 0% (0/6) | 36 |
| `azure-windows-scale` | ossci | 10 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31615316748/job/94176619708) | [2s](https://github.com/iree-org/iree/actions/runs/31615085538/job/94175844906) | 50% (1/2) | 10 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [20m56s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531483) | [59m44s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169499) | [59m44s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169499) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 0 | — | — | [6m58s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169165) | [58m40s](https://github.com/iree-org/iree/actions/runs/31615322145/job/94185129074) | [58m40s](https://github.com/iree-org/iree/actions/runs/31615322145/job/94185129074) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 10 | 0 | — | — | [2m11s](https://github.com/iree-org/iree/actions/runs/31583219282/job/94079019241) | [58m26s](https://github.com/iree-org/iree/actions/runs/31615316522/job/94185307074) | [58m26s](https://github.com/iree-org/iree/actions/runs/31615316522/job/94185307074) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 10 | 0 | — | — | [9m56s](https://github.com/iree-org/iree/actions/runs/31614923996/job/94178486329) | [56m19s](https://github.com/iree-org/iree/actions/runs/31615316522/job/94185307041) | [56m19s](https://github.com/iree-org/iree/actions/runs/31615316522/job/94185307041) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 10 | 0 | — | — | [18m14s](https://github.com/iree-org/iree/actions/runs/31614923996/job/94178486495) | [55m05s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169251) | [55m05s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169251) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 10 | 0 | — | — | [12m39s](https://github.com/iree-org/iree/actions/runs/31589330007/job/94092226500) | [53m47s](https://github.com/iree-org/iree/actions/runs/31615316522/job/94185306979) | [53m47s](https://github.com/iree-org/iree/actions/runs/31615316522/job/94185306979) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 0 | — | — | [10m50s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531399) | [53m24s](https://github.com/iree-org/iree/actions/runs/31615316522/job/94185307160) | [53m24s](https://github.com/iree-org/iree/actions/runs/31615316522/job/94185307160) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [10m34s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531524) | [49m14s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169318) | [49m14s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169318) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [17m36s](https://github.com/iree-org/iree/actions/runs/31583219282/job/94079019336) | [48m51s](https://github.com/iree-org/iree/actions/runs/31615322145/job/94185129060) | [48m51s](https://github.com/iree-org/iree/actions/runs/31615322145/job/94185129060) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 10 | 0 | — | — | [15m45s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531389) | [43m52s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169167) | [43m52s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169167) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 0 | — | — | [3m23s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531356) | [41m41s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169362) | [41m41s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169362) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [8m45s](https://github.com/iree-org/iree/actions/runs/31615322145/job/94185128788) | [40m44s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169460) | [40m44s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169460) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [7m45s](https://github.com/iree-org/iree/actions/runs/31615316522/job/94185306896) | [37m47s](https://github.com/iree-org/iree/actions/runs/31615322145/job/94185129018) | [37m47s](https://github.com/iree-org/iree/actions/runs/31615322145/job/94185129018) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 10 | 0 | — | — | [14m19s](https://github.com/iree-org/iree/actions/runs/31605809229/job/94154291127) | [28m29s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169242) | [28m29s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169242) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [6m45s](https://github.com/iree-org/iree/actions/runs/31583219282/job/94079019333) | [23m49s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169345) | [23m49s](https://github.com/iree-org/iree/actions/runs/31615331508/job/94187169345) | 4 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31614924207/job/94175300530) | [8m25s](https://github.com/iree-org/iree/actions/runs/31615322150/job/94177103340) | [8m25s](https://github.com/iree-org/iree/actions/runs/31615322150/job/94177103340) | 10 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31615085538/job/94175844524) | [8m09s](https://github.com/iree-org/iree/actions/runs/31615322150/job/94177103079) | [8m09s](https://github.com/iree-org/iree/actions/runs/31615322150/job/94177103079) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 10 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31605809008/job/94145184222) | [7m23s](https://github.com/iree-org/iree/actions/runs/31615331775/job/94177926247) | [7m23s](https://github.com/iree-org/iree/actions/runs/31615331775/job/94177926247) | 10 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31605809008/job/94145184028) | [7m15s](https://github.com/iree-org/iree/actions/runs/31615331775/job/94177926026) | [7m15s](https://github.com/iree-org/iree/actions/runs/31615331775/job/94177926026) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31605809008/job/94145184257) | [6m29s](https://github.com/iree-org/iree/actions/runs/31615316748/job/94176619712) | [6m29s](https://github.com/iree-org/iree/actions/runs/31615316748/job/94176619712) | 10 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 181 | 6% (11/181) |  | 1h12m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 218 | 0% (0/218) |  | 1h45m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 180 | 5% (9/180) |  | 1h59m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 155 | 11% (17/155) |  | 1h59m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
