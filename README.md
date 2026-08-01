# iree-ci-monitor

_Updated: 2026-07-31 17:58 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [15m53s](https://github.com/iree-org/iree/actions/runs/30646844543/job/91217330220) | [58m44s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264408) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [8m11s](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783675) | [55m44s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264186) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 0 | — | — | 0 | [21m50s](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783842) | [46m55s](https://github.com/iree-org/iree/actions/runs/30658571489/job/91250481549) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [25m07s](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783767) | [43m19s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264401) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [15m01s](https://github.com/iree-org/iree/actions/runs/30655580496/job/91241055676) | [43m15s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264361) | 0% (0/6) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [20m05s](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783877) | [42m59s](https://github.com/iree-org/iree/actions/runs/30658571489/job/91250481480) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 0 | — | — | 0 | [11m42s](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783806) | [40m13s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264202) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [10m17s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001250) | [36m22s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264317) | 0% (0/3) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | [5m43s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264120) | [34m04s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001221) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [11m18s](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783812) | [32m49s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264345) | 33% (2/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [13m38s](https://github.com/iree-org/iree/actions/runs/30655580496/job/91241055720) | [31m33s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264346) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30655580496/job/91241055447) | [20m20s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001301) | 0% (0/3) | `iree-mi308-1` |
| `ubuntu-24.04` | github-hosted | 121 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/30658571489/job/91249004235) | [2m12s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001309) | 0% (0/52) | 119 |
| `azure-linux-scale` | ossci | 40 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/30646568812/job/91215821386) | [1m27s](https://github.com/iree-org/iree/actions/runs/30646568869/job/91215836868) | 0% (0/18) | 40 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30655580551/job/91239075899) | [1m23s](https://github.com/iree-org/iree/actions/runs/30658666818/job/91249361243) | 0% (0/9) | 21 |
| `windows-2022` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30646845660/job/91215448819) | [33s](https://github.com/iree-org/iree/actions/runs/30658666818/job/91249361175) | 0% (0/9) | 21 |
| `macos-14` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30658571525/job/91249037785) | [31s](https://github.com/iree-org/iree/actions/runs/30646568812/job/91215821292) | 0% (0/9) | 21 |
| `ubuntu-latest` | github-hosted | 21 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/30658234757/job/91247894948) | [9s](https://github.com/iree-org/iree/actions/runs/30658234757/job/91247894883) | 0% (0/9) | 21 |
| `azure-windows-scale` | ossci | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30646568812/job/91215821547) | [8s](https://github.com/iree-org/iree/actions/runs/30658666818/job/91249361290) | 0% (0/3) | 7 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 11 | 11 | [18h50m](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454811) | 2026-07-31 17:57 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [18h50m](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454811) | 2026-07-31 17:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `fix/24751-tensor-slice-parameter-fold` | pull_request |
| [18h04m](https://github.com/iree-org/iree/actions/runs/30610564201/job/91093526156) | 2026-07-31 17:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [16h40m](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445151) | 2026-07-31 17:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [15h27m](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514612) | 2026-07-31 17:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `fix/23345-custom-op-static-loop-ranges` | pull_request |
| [14h50m](https://github.com/iree-org/iree/actions/runs/30621832279/job/91129775249) | 2026-07-31 17:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [8h03m](https://github.com/iree-org/iree/actions/runs/30646844543/job/91217330080) | 2026-07-31 17:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `fix-stablehlo-scatter` | pull_request |
| [8h01m](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783698) | 2026-07-31 17:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `fix-slo-composite` | pull_request |
| [6h15m](https://github.com/iree-org/iree/actions/runs/30655580496/job/91241055463) | 2026-07-31 17:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [5h32m](https://github.com/iree-org/iree/actions/runs/30658571489/job/91250481355) | 2026-07-31 17:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [5h29m](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001169) | 2026-07-31 17:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `integrates/llvm-20260731-cleanup` | pull_request |
| [5h28m](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264223) | 2026-07-31 17:57 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 11 | 11 | [18h50m](https://github.com/iree-org/iree/actions/runs/30607758195/job/91086454811) | 2026-07-31 17:57 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [15m53s](https://github.com/iree-org/iree/actions/runs/30646844543/job/91217330220) | [58m44s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264408) | [58m44s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264408) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [8m11s](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783675) | [55m44s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264186) | [55m44s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264186) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [17m28s](https://github.com/iree-org/iree/actions/runs/30655580496/job/91241055655) | [54m28s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264326) | [54m28s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264326) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 6 | 0 | — | — | [21m50s](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783842) | [46m55s](https://github.com/iree-org/iree/actions/runs/30658571489/job/91250481549) | [46m55s](https://github.com/iree-org/iree/actions/runs/30658571489/job/91250481549) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [15m01s](https://github.com/iree-org/iree/actions/runs/30655580496/job/91241055676) | [43m21s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264365) | [43m21s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264365) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [18m25s](https://github.com/iree-org/iree/actions/runs/30646844543/job/91217330284) | [43m19s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264401) | [43m19s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264401) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [5m12s](https://github.com/iree-org/iree/actions/runs/30646844543/job/91217330259) | [43m15s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264361) | [43m15s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264361) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 6 | 0 | — | — | [20m05s](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783877) | [42m59s](https://github.com/iree-org/iree/actions/runs/30658571489/job/91250481480) | [42m59s](https://github.com/iree-org/iree/actions/runs/30658571489/job/91250481480) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [11m18s](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783812) | [40m54s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001253) | [40m54s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001253) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 6 | 0 | — | — | [11m42s](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783806) | [40m13s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264202) | [40m13s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264202) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [15m52s](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783902) | [39m30s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001348) | [39m30s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001348) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [10m17s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001250) | [36m22s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264317) | [36m22s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264317) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 0 | — | — | [5m43s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264120) | [34m04s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001221) | [34m04s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001221) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30655580496/job/91241055447) | [20m20s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001301) | [20m20s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001301) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [2m00s](https://github.com/iree-org/iree/actions/runs/30646844543/job/91217330078) | [15m59s](https://github.com/iree-org/iree/actions/runs/30658571489/job/91250481530) | [15m59s](https://github.com/iree-org/iree/actions/runs/30658571489/job/91250481530) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [6m19s](https://github.com/iree-org/iree/actions/runs/30646844543/job/91217330244) | [14m01s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264387) | [14m01s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264387) | 3 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 6 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30658571489/job/91250481429) | [3m17s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264414) | [3m17s](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264414) | 6 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 6 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/30646844543/job/91217330268) | [2m19s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001242) | [2m19s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001242) | 6 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 6 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783769) | [2m13s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001257) | [2m13s](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001257) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 166 | 0% (0/166) |  | 4h28m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 118 | 1% (1/118) |  | 4h39m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 148 | 3% (4/148) |  | 4h40m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 123 | 1% (1/123) |  | 4h44m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 37 | 3% (1/37) |  | 4h58m ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 18h50m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
