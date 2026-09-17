# iree-ci-monitor

_Updated: 2026-09-17 14:28 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-w7900` | self-hosted | 18 | 0 | — | — | 0 | [1h22m](https://github.com/iree-org/iree/actions/runs/35244084342/job/105282771797) | [3h00m](https://github.com/iree-org/iree/actions/runs/35235955045/job/105255380814) | 0% (0/3) | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 36 | 6 | [2h40m](https://github.com/iree-org/iree/actions/runs/35257416856/job/105335534589) | 2026-09-17 14:26 PDT | 0 | [1h16m](https://github.com/iree-org/iree/actions/runs/35244090870/job/105282958058) | [2h33m](https://github.com/iree-org/iree/actions/runs/35235985605/job/105255432795) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 18 | 0 | — | — | 1 | [41m06s](https://github.com/iree-org/iree/actions/runs/35245416206/job/105294110471) | [2h15m](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964344) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 18 | 0 | — | — | 0 | [1h15m](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964446) | [2h05m](https://github.com/iree-org/iree/actions/runs/35235976348/job/105257101062) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 18 | 0 | — | — | 0 | [41m08s](https://github.com/iree-org/iree/actions/runs/35235965858/job/105255188253) | [1h51m](https://github.com/iree-org/iree/actions/runs/35259670726/job/105339834755) | 0% (0/3) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 36 | 0 | — | — | 0 | [51m38s](https://github.com/iree-org/iree/actions/runs/35235947162/job/105255076291) | [1h47m](https://github.com/iree-org/iree/actions/runs/35259694388/job/105344024793) | 0% (0/6) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 36 | 0 | — | — | 0 | [1h00m](https://github.com/iree-org/iree/actions/runs/35245416206/job/105294110337) | [1h36m](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342033078) | 0% (0/6) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 36 | 0 | — | — | 0 | [31m03s](https://github.com/iree-org/iree/actions/runs/35235947162/job/105255075711) | [1h34m](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458341) | 0% (0/6) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 385 | 0 | — | — | 0 | [2m03s](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458733) | [13m40s](https://github.com/iree-org/iree/actions/runs/35244084342/job/105282772127) | 10% (6/58) | 376 |
| `macos-14` | github-hosted | 54 | 0 | — | — | 0 | [2m59s](https://github.com/iree-org/iree/actions/runs/35259694435/job/105332858527) | [10m59s](https://github.com/iree-org/iree/actions/runs/35259694435/job/105332858507) | 0% (0/9) | 54 |
| `ubuntu-24.04-arm` | github-hosted | 54 | 0 | — | — | 0 | [1m38s](https://github.com/iree-org/iree/actions/runs/35244090797/job/105281015560) | [10m19s](https://github.com/iree-org/iree/actions/runs/35259694435/job/105332858482) | 0% (0/9) | 54 |
| `windows-2022` | github-hosted | 54 | 0 | — | — | 0 | [1m12s](https://github.com/iree-org/iree/actions/runs/35244089903/job/105280142576) | [8m12s](https://github.com/iree-org/iree/actions/runs/35235985575/job/105253824947) | 11% (1/9) | 54 |
| `ubuntu-latest` | github-hosted | 54 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/35259664223/job/105331913365) | [6m23s](https://github.com/iree-org/iree/actions/runs/35235983761/job/105251883678) | 0% (0/9) | 54 |
| `azure-windows-scale` | ossci | 18 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/35260594101/job/105337315750) | [5m18s](https://github.com/iree-org/iree/actions/runs/35235955032/job/105251870216) | 0% (0/3) | 18 |
| `azure-linux-scale` | ossci | 95 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/35257416795/job/105324438016) | [2m35s](https://github.com/iree-org/iree/actions/runs/35244089958/job/105280207076) | 0% (0/19) | 95 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 19 | 14 | [13h59m](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602166) | 2026-09-17 14:26 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [13h59m](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602166) | 2026-09-17 14:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/egebeysel/scalable-dist-1-vscale-range-target-field` | pull_request |
| [5h15m](https://github.com/iree-org/iree/actions/runs/35244084342/job/105282772106) | 2026-09-17 14:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [5h14m](https://github.com/iree-org/iree/actions/runs/35244090870/job/105282957801) | 2026-09-17 14:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/egebeysel/scalable-dist-3-unpack-distribution-hints` | pull_request |
| [5h12m](https://github.com/iree-org/iree/actions/runs/35244089937/job/105283906279) | 2026-09-17 14:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/egebeysel/scalable-dist-2-distribution-tile-sizes` | pull_request |
| [5h07m](https://github.com/iree-org/iree/actions/runs/35244090100/job/105285600898) | 2026-09-17 14:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/egebeysel/scalable-dist-5-distribution-tiling-tests` | pull_request |
| [4h42m](https://github.com/iree-org/iree/actions/runs/35245416206/job/105294110239) | 2026-09-17 14:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `integrates/llvm-20260916` | pull_request |
| [3h26m](https://github.com/iree-org/iree/actions/runs/35251598607/job/105320096896) | 2026-09-17 14:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `add-fma-math-vm-lowringg` | pull_request |
| [2h40m](https://github.com/iree-org/iree/actions/runs/35257416856/job/105335534589) | 2026-09-17 14:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [2h40m](https://github.com/iree-org/iree/actions/runs/35257416856/job/105335534767) | 2026-09-17 14:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [2h29m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360642) | 2026-09-17 14:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [2h29m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360868) | 2026-09-17 14:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [2h29m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360869) | 2026-09-17 14:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [2h28m](https://github.com/iree-org/iree/actions/runs/35259670726/job/105339834679) | 2026-09-17 14:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_canonicalize_dynamism` | pull_request |
| [2h26m](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458710) | 2026-09-17 14:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/stablehlo_dynamic_gather_broadcast` | pull_request |
| [2h26m](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458854) | 2026-09-17 14:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `users/jschuhmacher/stablehlo_dynamic_gather_broadcast` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 19 | 14 | [13h59m](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602166) | 2026-09-17 14:26 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 18 | 0 | — | — | [1h22m](https://github.com/iree-org/iree/actions/runs/35244084342/job/105282771797) | [3h00m](https://github.com/iree-org/iree/actions/runs/35235955045/job/105255380814) | [3h19m](https://github.com/iree-org/iree/actions/runs/35235985605/job/105255432929) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 18 | 4 | [2h40m](https://github.com/iree-org/iree/actions/runs/35257416856/job/105335534589) | 2026-09-17 14:26 PDT | [1h08m](https://github.com/iree-org/iree/actions/runs/35245416206/job/105294110517) | [2h16m](https://github.com/iree-org/iree/actions/runs/35244089937/job/105283906712) | [2h46m](https://github.com/iree-org/iree/actions/runs/35235976348/job/105257101209) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 18 | 2 | [2h29m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360869) | 2026-09-17 14:26 PDT | [1h35m](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458959) | [2h21m](https://github.com/iree-org/iree/actions/runs/35257416856/job/105335534804) | [2h33m](https://github.com/iree-org/iree/actions/runs/35235985605/job/105255432795) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 18 | 0 | — | — | [41m06s](https://github.com/iree-org/iree/actions/runs/35245416206/job/105294110471) | [2h15m](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964344) | [2h19m](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342032886) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 18 | 0 | — | — | [1h15m](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964446) | [2h05m](https://github.com/iree-org/iree/actions/runs/35235976348/job/105257101062) | [2h19m](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360862) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 18 | 0 | — | — | [50m22s](https://github.com/iree-org/iree/actions/runs/35235955045/job/105255381030) | [1h54m](https://github.com/iree-org/iree/actions/runs/35235985605/job/105255432998) | [2h30m](https://github.com/iree-org/iree/actions/runs/35235947162/job/105255076268) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 18 | 0 | — | — | [41m08s](https://github.com/iree-org/iree/actions/runs/35235965858/job/105255188253) | [1h51m](https://github.com/iree-org/iree/actions/runs/35259670726/job/105339834755) | [2h23m](https://github.com/iree-org/iree/actions/runs/35235947162/job/105255075959) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 18 | 0 | — | — | [1h01m](https://github.com/iree-org/iree/actions/runs/35244084342/job/105282772247) | [1h36m](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342033078) | [1h47m](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458734) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 18 | 0 | — | — | [28m31s](https://github.com/iree-org/iree/actions/runs/35260594164/job/105339360613) | [1h34m](https://github.com/iree-org/iree/actions/runs/35259683825/job/105340458341) | [1h36m](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342033221) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 18 | 0 | — | — | [30m33s](https://github.com/iree-org/iree/actions/runs/35244090870/job/105282957786) | [1h26m](https://github.com/iree-org/iree/actions/runs/35235976348/job/105257101052) | [1h39m](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964640) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 18 | 0 | — | — | [50m17s](https://github.com/iree-org/iree/actions/runs/35245416206/job/105294110513) | [1h26m](https://github.com/iree-org/iree/actions/runs/35235976348/job/105257101325) | [1h47m](https://github.com/iree-org/iree/actions/runs/35259694388/job/105344024793) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 18 | 0 | — | — | [52m30s](https://github.com/iree-org/iree/actions/runs/35235965858/job/105255188472) | [1h14m](https://github.com/iree-org/iree/actions/runs/35245416206/job/105294110556) | [1h42m](https://github.com/iree-org/iree/actions/runs/35259675070/job/105341964412) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 18 | 0 | — | — | [6m09s](https://github.com/iree-org/iree/actions/runs/35235976332/job/105255056477) | [19m13s](https://github.com/iree-org/iree/actions/runs/35259691708/job/105332393903) | [21m07s](https://github.com/iree-org/iree/actions/runs/35259670788/job/105331990889) | 18 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 18 | 0 | — | — | [5m50s](https://github.com/iree-org/iree/actions/runs/35260594101/job/105337315465) | [17m12s](https://github.com/iree-org/iree/actions/runs/35259670788/job/105331990785) | [17m52s](https://github.com/iree-org/iree/actions/runs/35259691708/job/105332393818) | 18 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 18 | 0 | — | — | [7m31s](https://github.com/iree-org/iree/actions/runs/35235965805/job/105251906687) | [15m50s](https://github.com/iree-org/iree/actions/runs/35259670788/job/105331990814) | [18m01s](https://github.com/iree-org/iree/actions/runs/35259691708/job/105332393784) | 18 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 18 | 0 | — | — | [2m28s](https://github.com/iree-org/iree/actions/runs/35244089937/job/105283906364) | [14m35s](https://github.com/iree-org/iree/actions/runs/35235955045/job/105255381228) | [15m54s](https://github.com/iree-org/iree/actions/runs/35235965858/job/105255188288) | 18 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 18 | 0 | — | — | [2m55s](https://github.com/iree-org/iree/actions/runs/35259691182/job/105342033534) | [13m46s](https://github.com/iree-org/iree/actions/runs/35235955045/job/105255381321) | [14m08s](https://github.com/iree-org/iree/actions/runs/35244084342/job/105282772260) | 18 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 19 | 0 | — | — | [3m15s](https://github.com/iree-org/iree/actions/runs/35259674988/job/105332021937) | [13m24s](https://github.com/iree-org/iree/actions/runs/35259691708/job/105332393691) | [14m49s](https://github.com/iree-org/iree/actions/runs/35244089958/job/105280205673) | 18 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 18 | 0 | — | — | [5m16s](https://github.com/iree-org/iree/actions/runs/35244089937/job/105283906447) | [13m13s](https://github.com/iree-org/iree/actions/runs/35244090870/job/105282957827) | [15m18s](https://github.com/iree-org/iree/actions/runs/35235965858/job/105255188228) | 18 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 487 | 1% (6/486) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 387 | 2% (6/387) |  | 11m08s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 395 | 1% (3/395) |  | 28m37s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 208 | 9% (18/208) |  | 3d05h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 2h40m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 13h59m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h51m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h47m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h05m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h33m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h15m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 3h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h36m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h34m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
