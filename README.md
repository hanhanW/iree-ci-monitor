# iree-ci-monitor

_Updated: 2026-06-29 12:00 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [47m14s](https://github.com/iree-org/iree/actions/runs/28363238216/job/84024202847) | [57m08s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554476) | 0% (0/12) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [6m52s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200103) | [47m19s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554335) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [14m23s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227251) | [44m20s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200218) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 0 | — | — | 0 | [34m00s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554451) | [38m16s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227215) | 0% (0/6) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [31m09s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200071) | [35m01s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227092) | 0% (0/6) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | [25m19s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059226974) | [27m55s](https://github.com/iree-org/iree/actions/runs/28364024481/job/84026705535) | 17% (1/6) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [21m05s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227292) | [25m40s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200302) | 0% (0/12) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 0 | — | — | 0 | [6m42s](https://github.com/iree-org/iree/actions/runs/28363238216/job/84024202765) | [25m29s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200352) | 0% (0/6) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [13m27s](https://github.com/iree-org/iree/actions/runs/28363238216/job/84024202896) | [21m15s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554410) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [10m00s](https://github.com/iree-org/iree/actions/runs/28373584830/job/84058772000) | [16m45s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227153) | 0% (0/12) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28373584830/job/84058771751) | [14m07s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200040) | 0% (0/6) | `iree-mi308-1` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [7m14s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554408) | [11m47s](https://github.com/iree-org/iree/actions/runs/28373584830/job/84058772021) | 8% (1/12) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 150 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28363238216/job/84024202801) | [6m16s](https://github.com/iree-org/iree/actions/runs/28373584830/job/84058771718) | 3% (3/114) | 142 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 24 | 0 | — | — | 0 | [11s](https://github.com/iree-org/iree/actions/runs/28363238216/job/84024202802) | [5m08s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554592) | 4% (1/24) | 24 |
| `macos-14` | github-hosted | 19 | 0 | — | — | 0 | [1m15s](https://github.com/iree-org/iree/actions/runs/28364228246/job/84026100919) | [4m27s](https://github.com/iree-org/iree/actions/runs/28373635525/job/84057647749) | 0% (0/19) | 19 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28364228246/job/84026101016) | [3m48s](https://github.com/iree-org/iree/actions/runs/28373934390/job/84058602901) | 0% (0/6) | 6 |
| `ubuntu-latest` | github-hosted | 30 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28373583812/job/84057344843) | [2m46s](https://github.com/iree-org/iree/actions/runs/28373974586/job/84058712348) | 0% (0/18) | 30 |
| `azure-linux-scale` | ossci | 38 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/28363238266/job/84022746635) | [2m07s](https://github.com/iree-org/iree/actions/runs/28364228246/job/84026101116) | 0% (0/38) | 38 |
| `windows-2022` | github-hosted | 18 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28363238266/job/84022746518) | [2m03s](https://github.com/iree-org/iree/actions/runs/28373635525/job/84057647756) | 0% (0/18) | 18 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [26s](https://github.com/iree-org/iree/actions/runs/28373635525/job/84057647742) | [1m50s](https://github.com/iree-org/iree/actions/runs/28364024465/job/84025381736) | 0% (0/18) | 18 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m27s](https://github.com/iree-org/iree/actions/runs/28366853527/job/84034758103) | [1m27s](https://github.com/iree-org/iree/actions/runs/28366853527/job/84034758103) | 0% (0/1) | 1 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/28366810717/job/84034617768) | [4s](https://github.com/iree-org/iree/actions/runs/28366810717/job/84034617768) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 1 | [11h05m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334980) | 2026-06-29 11:59 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [11h05m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334980) | 2026-06-29 11:59 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `implement-fpowi-in-vm` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 1 | 1 | [11h05m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334980) | 2026-06-29 11:59 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [41m53s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227166) | [1h03m](https://github.com/iree-org/iree/actions/runs/28363238216/job/84024202793) | [1h03m](https://github.com/iree-org/iree/actions/runs/28363238216/job/84024202793) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [40m24s](https://github.com/iree-org/iree/actions/runs/28364024481/job/84026705702) | [57m08s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554476) | [57m08s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554476) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [6m52s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200103) | [47m19s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554335) | [47m19s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554335) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [14m23s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227251) | [44m20s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200218) | [44m20s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200218) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 6 | 0 | — | — | [34m00s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554451) | [38m16s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227215) | [38m16s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227215) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 6 | 0 | — | — | [31m09s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200071) | [35m01s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227092) | [35m01s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227092) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [22m01s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554546) | [28m23s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227253) | [28m23s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227253) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 0 | — | — | [25m19s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059226974) | [27m55s](https://github.com/iree-org/iree/actions/runs/28364024481/job/84026705535) | [27m55s](https://github.com/iree-org/iree/actions/runs/28364024481/job/84026705535) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 6 | 0 | — | — | [6m42s](https://github.com/iree-org/iree/actions/runs/28363238216/job/84024202765) | [25m29s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200352) | [25m29s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200352) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [15m59s](https://github.com/iree-org/iree/actions/runs/28373584830/job/84058772033) | [22m47s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554447) | [22m47s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554447) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [13m27s](https://github.com/iree-org/iree/actions/runs/28363238216/job/84024202896) | [21m15s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554410) | [21m15s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554410) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [14m44s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200338) | [17m23s](https://github.com/iree-org/iree/actions/runs/28364024481/job/84026705604) | [17m23s](https://github.com/iree-org/iree/actions/runs/28364024481/job/84026705604) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 6 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28373584830/job/84058771751) | [14m07s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200040) | [14m07s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200040) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [4m24s](https://github.com/iree-org/iree/actions/runs/28364024481/job/84026705751) | [13m55s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227263) | [13m55s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227263) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 6 | 0 | — | — | [20s](https://github.com/iree-org/iree/actions/runs/28373635525/job/84057647726) | [12m24s](https://github.com/iree-org/iree/actions/runs/28373934390/job/84058602788) | [12m24s](https://github.com/iree-org/iree/actions/runs/28373934390/job/84058602788) | 6 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [5m20s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200286) | [11m58s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554524) | [11m58s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554524) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [7m11s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200141) | [11m47s](https://github.com/iree-org/iree/actions/runs/28373584830/job/84058772021) | [11m47s](https://github.com/iree-org/iree/actions/runs/28373584830/job/84058772021) | 3 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 6 | 0 | — | — | [1m16s](https://github.com/iree-org/iree/actions/runs/28364024481/job/84026705640) | [8m54s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059226933) | [8m54s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059226933) | 6 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 6 | 0 | — | — | [1m49s](https://github.com/iree-org/iree/actions/runs/28364024481/job/84026705895) | [8m10s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227147) | [8m10s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227147) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 204 | 0% (0/204) |  | 4h51m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 162 | 7% (12/162) |  | 5h09m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 152 | 0% (0/152) |  | 5h16m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 149 | 0% (0/149) |  | 5h21m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 45 | 0% (0/45) |  | 5h25m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 11h05m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
