# iree-ci-monitor

_Updated: 2026-06-29 06:48 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 24 | 2 | [37m59s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200298) | 2026-06-29 06:47 PDT | 1 | [47m14s](https://github.com/iree-org/iree/actions/runs/28363238216/job/84024202847) | [2h21m](https://github.com/iree-org/iree/actions/runs/28354747999/job/83996599117) | 0% (0/15) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 12 | 0 | — | — | 0 | [36m01s](https://github.com/iree-org/iree/actions/runs/28356222270/job/84004676843) | [2h15m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334986) | 0% (0/9) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 12 | 0 | — | — | 1 | [38m16s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227215) | [1h56m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002335006) | 0% (0/8) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [35m01s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227092) | [1h52m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334960) | 0% (0/9) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 24 | 0 | — | — | 0 | [24m28s](https://github.com/iree-org/iree/actions/runs/28364024481/job/84026705742) | [1h38m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002335081) | 0% (0/18) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 12 | 1 | [37m59s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200218) | 2026-06-29 06:47 PDT | 0 | [16m15s](https://github.com/iree-org/iree/actions/runs/28364024481/job/84026705715) | [1h37m](https://github.com/iree-org/iree/actions/runs/28354926075/job/83997699380) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 24 | 0 | — | — | 0 | [16m37s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554555) | [1h27m](https://github.com/iree-org/iree/actions/runs/28354747999/job/83996598969) | 0% (0/18) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 24 | 0 | — | — | 0 | [11m22s](https://github.com/iree-org/iree/actions/runs/28354356008/job/83994807533) | [1h04m](https://github.com/iree-org/iree/actions/runs/28354747999/job/83996598959) | 6% (1/18) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [17m14s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200148) | [37m16s](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002335000) | 0% (0/9) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 12 | 0 | — | — | 0 | [25m19s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059226974) | [32m35s](https://github.com/iree-org/iree/actions/runs/28356222270/job/84004676954) | 11% (1/9) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 12 | 0 | — | — | 0 | [7m12s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227081) | [25m29s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200352) | 0% (0/9) | `shark01-ci`, `shark10-ci` |
| `ubuntu-24.04` | github-hosted | 243 | 0 | — | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/28373635525/job/84057647541) | [17m57s](https://github.com/iree-org/iree/actions/runs/28353471422/job/83999119247) | 2% (4/165) | 238 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28356222270/job/84004677012) | [13m35s](https://github.com/iree-org/iree/actions/runs/28354926075/job/83997699345) | 0% (0/9) | `iree-mi308-1` |
| `macos-14` | github-hosted | 43 | 0 | — | — | 1 | [2m07s](https://github.com/iree-org/iree/actions/runs/28356222269/job/84003120660) | [7m25s](https://github.com/iree-org/iree/actions/runs/28354925924/job/83996135823) | 0% (0/27) | 40 |
| `windows-2022` | github-hosted | 41 | 0 | — | — | 3 | [16s](https://github.com/iree-org/iree/actions/runs/28373635525/job/84057647673) | [5m32s](https://github.com/iree-org/iree/actions/runs/28373934390/job/84058602739) | 0% (0/27) | 38 |
| `ubuntu-24.04-arm` | github-hosted | 42 | 0 | — | — | 0 | [37s](https://github.com/iree-org/iree/actions/runs/28360021859/job/84012204137) | [5m27s](https://github.com/iree-org/iree/actions/runs/28373934390/job/84058602860) | 0% (0/27) | 39 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 48 | 0 | — | — | 0 | [11s](https://github.com/iree-org/iree/actions/runs/28363238216/job/84024202802) | [5m08s](https://github.com/iree-org/iree/actions/runs/28364228264/job/84027554592) | 8% (3/36) | 48 |
| `azure-linux-scale` | ossci | 77 | 0 | — | — | 4 | [9s](https://github.com/iree-org/iree/actions/runs/28356222269/job/84003120797) | [2m10s](https://github.com/iree-org/iree/actions/runs/28364228246/job/84026100976) | 0% (0/56) | 73 |
| `ubuntu-latest` | github-hosted | 34 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28368670084/job/84040752486) | [2m08s](https://github.com/iree-org/iree/actions/runs/28373974586/job/84058712358) | 0% (0/28) | 34 |
| `macos-15-intel` | github-hosted | 2 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/28366810717/job/84034617768) | [1m28s](https://github.com/iree-org/iree/actions/runs/28354747988/job/83995107874) | — | 2 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 2 | 0 | — | — | 0 | [1m18s](https://github.com/iree-org/iree/actions/runs/28354747988/job/83995107905) | [1m27s](https://github.com/iree-org/iree/actions/runs/28366853527/job/84034758103) | 0% (0/1) | 2 |
| `azure-windows-scale` | ossci | 13 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/28364228246/job/84026101016) | [39s](https://github.com/iree-org/iree/actions/runs/28373635525/job/84057647867) | 0% (0/9) | 12 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 1 | [5h53m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334980) | 2026-06-29 06:47 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [5h53m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334980) | 2026-06-29 06:47 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `implement-fpowi-in-vm` | pull_request |
| [37m59s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200218) | 2026-06-29 06:47 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `main` | push |
| [37m59s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200298) | 2026-06-29 06:47 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [37m59s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200301) | 2026-06-29 06:47 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 1 | 1 | [5h53m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334980) | 2026-06-29 06:47 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 12 | 1 | [37m59s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200301) | 2026-06-29 06:47 PDT | [43m11s](https://github.com/iree-org/iree/actions/runs/28356222270/job/84004677022) | [2h40m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002335074) | [2h40m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002335074) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 12 | 0 | — | — | [36m01s](https://github.com/iree-org/iree/actions/runs/28356222270/job/84004676843) | [2h15m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334986) | [2h24m](https://github.com/iree-org/iree/actions/runs/28354926075/job/83997699181) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 12 | 1 | [37m59s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200298) | 2026-06-29 06:47 PDT | [55m58s](https://github.com/iree-org/iree/actions/runs/28364024481/job/84026705635) | [1h57m](https://github.com/iree-org/iree/actions/runs/28360021890/job/84013672883) | [1h57m](https://github.com/iree-org/iree/actions/runs/28360021890/job/84013672883) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 12 | 0 | — | — | [38m16s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227215) | [1h56m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002335006) | [2h18m](https://github.com/iree-org/iree/actions/runs/28354926075/job/83997699413) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 12 | 0 | — | — | [35m01s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227092) | [1h52m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334960) | [2h26m](https://github.com/iree-org/iree/actions/runs/28354747999/job/83996598930) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 12 | 0 | — | — | [21m05s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227292) | [1h38m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002335081) | [1h44m](https://github.com/iree-org/iree/actions/runs/28354926075/job/83997699431) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 12 | 1 | [37m59s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200218) | 2026-06-29 06:47 PDT | [16m15s](https://github.com/iree-org/iree/actions/runs/28364024481/job/84026705715) | [1h37m](https://github.com/iree-org/iree/actions/runs/28354926075/job/83997699380) | [1h37m](https://github.com/iree-org/iree/actions/runs/28354926075/job/83997699380) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 12 | 0 | — | — | [16m11s](https://github.com/iree-org/iree/actions/runs/28360021890/job/84013672798) | [1h04m](https://github.com/iree-org/iree/actions/runs/28354747999/job/83996598959) | [1h13m](https://github.com/iree-org/iree/actions/runs/28354926075/job/83997699417) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 12 | 0 | — | — | [28m23s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227253) | [1h01m](https://github.com/iree-org/iree/actions/runs/28354356008/job/83994807602) | [1h13m](https://github.com/iree-org/iree/actions/runs/28354926075/job/83997699311) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 12 | 0 | — | — | [17m23s](https://github.com/iree-org/iree/actions/runs/28364024481/job/84026705604) | [58m19s](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002335099) | [1h27m](https://github.com/iree-org/iree/actions/runs/28354747999/job/83996598969) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 12 | 0 | — | — | [10m54s](https://github.com/iree-org/iree/actions/runs/28354356008/job/83994807547) | [55m49s](https://github.com/iree-org/iree/actions/runs/28354926075/job/83997699423) | [2h00m](https://github.com/iree-org/iree/actions/runs/28354747999/job/83996598954) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 12 | 0 | — | — | [17m14s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200148) | [37m16s](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002335000) | [48m53s](https://github.com/iree-org/iree/actions/runs/28354926075/job/83997699406) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 12 | 0 | — | — | [25m19s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059226974) | [32m35s](https://github.com/iree-org/iree/actions/runs/28356222270/job/84004676954) | [1h22m](https://github.com/iree-org/iree/actions/runs/28354926075/job/83997699194) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 12 | 0 | — | — | [7m12s](https://github.com/iree-org/iree/actions/runs/28373635534/job/84059227081) | [25m29s](https://github.com/iree-org/iree/actions/runs/28373934318/job/84060200352) | [36m14s](https://github.com/iree-org/iree/actions/runs/28356222270/job/84004676861) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 12 | 0 | — | — | [10m54s](https://github.com/iree-org/iree/actions/runs/28373584830/job/84058771757) | [25m01s](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334971) | [32m47s](https://github.com/iree-org/iree/actions/runs/28354926075/job/83997699322) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 12 | 0 | — | — | [52s](https://github.com/iree-org/iree/actions/runs/28364024481/job/84026705682) | [24m21s](https://github.com/iree-org/iree/actions/runs/28354926075/job/83997699414) | [27m16s](https://github.com/iree-org/iree/actions/runs/28354747999/job/83996598966) | 12 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 13 | 0 | — | — | [1m43s](https://github.com/iree-org/iree/actions/runs/28360021859/job/84012204140) | [17m57s](https://github.com/iree-org/iree/actions/runs/28353471422/job/83999119247) | [30m15s](https://github.com/iree-org/iree/actions/runs/28354925924/job/83996135793) | 12 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 13 | 0 | — | — | [54s](https://github.com/iree-org/iree/actions/runs/28356222269/job/84003120663) | [17m47s](https://github.com/iree-org/iree/actions/runs/28353471422/job/83999119238) | [24m19s](https://github.com/iree-org/iree/actions/runs/28354747988/job/83995107809) | 12 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 13 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28373635525/job/84057647541) | [17m42s](https://github.com/iree-org/iree/actions/runs/28353471422/job/83999119193) | [21m52s](https://github.com/iree-org/iree/actions/runs/28354925924/job/83996135724) | 12 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 201 | 0% (0/200) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 162 | 7% (12/161) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 152 | 0% (0/152) |  | 4m50s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 149 | 0% (0/149) |  | 10m13s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 45 | 0% (0/45) |  | 14m23s ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 5h53m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h38m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h37m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h21m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h15m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h52m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h56m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h27m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h04m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
