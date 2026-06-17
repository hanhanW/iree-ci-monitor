# iree-ci-monitor

_Updated: 2026-06-17 12:10 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [19m44s](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911604766) | [2h01m](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913797) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 9 | 0 | — | — | 0 | [1h09m](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913796) | [1h48m](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657194) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [43m57s](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657588) | [1h34m](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911604963) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 18 | 0 | — | — | 0 | [22m24s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934545) | [1h22m](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922294873) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 9 | 0 | — | — | 0 | [11m24s](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922295088) | [1h22m](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913846) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [5m27s](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922294845) | [1h20m](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913757) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 9 | 0 | — | — | 0 | [25m19s](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657122) | [1h02m](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911604654) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 18 | 0 | — | — | 0 | [21m16s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230192) | [57m28s](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911605020) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 18 | 0 | — | — | 0 | [16m46s](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913971) | [42m11s](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922295250) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 18 | 0 | — | — | 0 | [9m08s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230115) | [27m52s](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913858) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230047) | [19m51s](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913569) | 0% (0/2) | `iree-mi308-1` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 9 | 0 | — | — | 0 | [5m29s](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911604734) | [17m44s](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922294819) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 36 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922294994) | [9m14s](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657520) | 12% (1/8) | 36 |
| `azure-windows-scale` | ossci | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27702567647/job/81942682309) | [8m20s](https://github.com/iree-org/iree/actions/runs/27693282616/job/81909735440) | 0% (0/1) | 8 |
| `windows-2022` | github-hosted | 24 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/27696295647/job/81920341337) | [7m29s](https://github.com/iree-org/iree/actions/runs/27693277975/job/81909734839) | 0% (0/3) | 24 |
| `ubuntu-24.04` | github-hosted | 190 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/27687237427/job/81889317934) | [6m14s](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911604856) | 3% (1/32) | 186 |
| `ubuntu-24.04-arm` | github-hosted | 24 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27702567647/job/81942681985) | [6m01s](https://github.com/iree-org/iree/actions/runs/27693280594/job/81909722302) | 0% (0/3) | 24 |
| `macos-14` | github-hosted | 25 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/27687237427/job/81889317884) | [5m57s](https://github.com/iree-org/iree/actions/runs/27693277975/job/81909734749) | 0% (0/4) | 25 |
| `azure-linux-scale` | ossci | 46 | 0 | — | — | 0 | [15s](https://github.com/iree-org/iree/actions/runs/27702567647/job/81942682217) | [1m47s](https://github.com/iree-org/iree/actions/runs/27693282616/job/81909735785) | 0% (0/9) | 46 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m29s](https://github.com/iree-org/iree/actions/runs/27683833835/job/81877628305) | [1m29s](https://github.com/iree-org/iree/actions/runs/27683833835/job/81877628305) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934128) | [11s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406645) | 0% (0/2) | 9 |
| `ubuntu-latest` | github-hosted | 30 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27689121536/job/81895202393) | [10s](https://github.com/iree-org/iree/actions/runs/27698926253/job/81929754789) | 0% (0/3) | 30 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/27683789205/job/81877481844) | [4s](https://github.com/iree-org/iree/actions/runs/27683789205/job/81877481844) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 9 | 0 | — | — | [19m44s](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911604766) | [2h01m](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913797) | [2h01m](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913797) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 9 | 0 | — | — | [1h09m](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913796) | [1h48m](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657194) | [1h48m](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657194) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 9 | 0 | — | — | [43m57s](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657588) | [1h34m](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911604963) | [1h34m](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911604963) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [24m10s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230237) | [1h29m](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657409) | [1h29m](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657409) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [22m24s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934545) | [1h22m](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922294873) | [1h22m](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922294873) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 9 | 0 | — | — | [11m24s](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922295088) | [1h22m](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913846) | [1h22m](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913846) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 9 | 0 | — | — | [5m27s](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922294845) | [1h20m](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913757) | [1h20m](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913757) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 9 | 0 | — | — | [17m02s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230097) | [1h16m](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657374) | [1h16m](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657374) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [21m16s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230192) | [1h07m](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911604857) | [1h07m](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911604857) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 9 | 0 | — | — | [25m19s](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657122) | [1h02m](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911604654) | [1h02m](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911604654) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [33m14s](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657288) | [57m28s](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911605020) | [57m28s](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911605020) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [13m36s](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657552) | [34m41s](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922294901) | [34m41s](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922294901) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 9 | 0 | — | — | [13m30s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230081) | [33m04s](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657379) | [33m04s](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657379) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [6m58s](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913538) | [24m27s](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922294584) | [24m27s](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922294584) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27702569069/job/81944230047) | [19m51s](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913569) | [19m51s](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913569) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 9 | 0 | — | — | [5m29s](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911604734) | [17m44s](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922294819) | [17m44s](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922294819) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 9 | 0 | — | — | [21s](https://github.com/iree-org/iree/actions/runs/27687237519/job/81890934546) | [12m33s](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657593) | [12m33s](https://github.com/iree-org/iree/actions/runs/27693279781/job/81911657593) | 9 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 9 | 0 | — | — | [20s](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922294977) | [10m00s](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913675) | [10m00s](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913675) | 9 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 9 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27696293271/job/81922294667) | [8m47s](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913345) | [8m47s](https://github.com/iree-org/iree/actions/runs/27693281821/job/81911913345) | 9 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 9 | 0 | — | — | [33s](https://github.com/iree-org/iree/actions/runs/27702568296/job/81944406866) | [8m25s](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911604811) | [8m25s](https://github.com/iree-org/iree/actions/runs/27693278982/job/81911604811) | 9 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 213 | 5% (11/213) |  | 2h24m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 274 | 0% (1/274) |  | 2h26m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 208 | 1% (2/208) |  | 2h26m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 192 | 0% (0/192) |  | 2h30m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 63 | 0% (0/63) |  | 2h37m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h22m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h48m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h34m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h22m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
