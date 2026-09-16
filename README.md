# iree-ci-monitor

_Updated: 2026-09-16 10:05 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 20 | 10 | [4h53m](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787673263) | 2026-09-16 10:03 PDT | 1 | [2h09m](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787673046) | [4h43m](https://github.com/iree-org/iree/actions/runs/35093138856/job/104789629680) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 10 | 5 | [4h57m](https://github.com/iree-org/iree/actions/runs/35093131570/job/104786296006) | 2026-09-16 10:03 PDT | 0 | [3h18m](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787745442) | [4h30m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790276935) | — | `shark01-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 10 | 0 | — | — | 0 | [29m21s](https://github.com/iree-org/iree/actions/runs/35093139099/job/104791378467) | [4h26m](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787673037) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 20 | 0 | — | — | 0 | [1h01m](https://github.com/iree-org/iree/actions/runs/35098403907/job/104811488778) | [3h52m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790276896) | 0% (0/4) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 20 | 0 | — | — | 1 | [1h10m](https://github.com/iree-org/iree/actions/runs/35093131570/job/104786296096) | [3h46m](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787745958) | 0% (0/4) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [1h39m](https://github.com/iree-org/iree/actions/runs/35093139099/job/104791378666) | [3h25m](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163669) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 20 | 0 | — | — | 1 | [1h34m](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787746211) | [3h20m](https://github.com/iree-org/iree/actions/runs/35093138856/job/104789629539) | 0% (0/4) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [1h28m](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787745784) | [2h53m](https://github.com/iree-org/iree/actions/runs/35093139099/job/104791378606) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `ubuntu-24.04` | github-hosted | 253 | 0 | — | — | 0 | [3m52s](https://github.com/iree-org/iree/actions/runs/35090012233/job/104784391299) | [29m32s](https://github.com/iree-org/iree/actions/runs/35093081313/job/104786257769) | 9% (4/45) | 245 |
| `ubuntu-24.04-arm` | github-hosted | 36 | 0 | — | — | 0 | [1m15s](https://github.com/iree-org/iree/actions/runs/35093138816/job/104784686632) | [12m53s](https://github.com/iree-org/iree/actions/runs/35093138312/job/104785898744) | 0% (0/6) | 36 |
| `windows-2022` | github-hosted | 36 | 0 | — | — | 0 | [2m50s](https://github.com/iree-org/iree/actions/runs/35093138816/job/104784686620) | [12m23s](https://github.com/iree-org/iree/actions/runs/35093138784/job/104794233374) | 0% (0/6) | 36 |
| `macos-14` | github-hosted | 37 | 0 | — | — | 0 | [1m50s](https://github.com/iree-org/iree/actions/runs/35093131661/job/104784001285) | [10m44s](https://github.com/iree-org/iree/actions/runs/35093138784/job/104794233362) | 0% (0/7) | 37 |
| `ubuntu-latest` | github-hosted | 57 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/35093754940/job/104786232217) | [6m22s](https://github.com/iree-org/iree/actions/runs/35093135807/job/104783970587) | 0% (0/6) | 57 |
| `azure-linux-scale` | ossci | 72 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/35106796649/job/104830076397) | [4m55s](https://github.com/iree-org/iree/actions/runs/35093138312/job/104785898950) | 0% (0/14) | 72 |
| `azure-windows-scale` | ossci | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35106796649/job/104830076220) | [2m39s](https://github.com/iree-org/iree/actions/runs/35093138666/job/104785645020) | 0% (0/2) | 12 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m24s](https://github.com/iree-org/iree/actions/runs/35079464490/job/104739687878) | [1m24s](https://github.com/iree-org/iree/actions/runs/35079464490/job/104739687878) | 100% (1/1) | 1 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 12 | 12 | [15h24m](https://github.com/iree-org/iree/actions/runs/35044430244/job/104632578942) | 2026-09-16 10:03 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [15h24m](https://github.com/iree-org/iree/actions/runs/35044430244/job/104632578942) | 2026-09-16 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `ci-remove-w7900x2-package-jobs` | pull_request |
| [10h38m](https://github.com/iree-org/iree/actions/runs/35062939888/job/104689025165) | 2026-09-16 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [4h57m](https://github.com/iree-org/iree/actions/runs/35093131570/job/104786295964) | 2026-09-16 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [4h57m](https://github.com/iree-org/iree/actions/runs/35093131570/job/104786296006) | 2026-09-16 10:03 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `main` | push |
| [4h53m](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787672926) | 2026-09-16 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-3` | pull_request |
| [4h53m](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787673263) | 2026-09-16 10:03 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `users/jschuhmacher/dynamic-plugin-support-3` | pull_request |
| [4h53m](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787745903) | 2026-09-16 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-5` | pull_request |
| [4h48m](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163542) | 2026-09-16 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `users/jschuhmacher/dynamic-plugin-support-7` | pull_request |
| [4h48m](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163560) | 2026-09-16 10:03 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/jschuhmacher/dynamic-plugin-support-7` | pull_request |
| [4h48m](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163586) | 2026-09-16 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-7` | pull_request |
| [4h48m](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163609) | 2026-09-16 10:03 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `users/jschuhmacher/dynamic-plugin-support-7` | pull_request |
| [4h46m](https://github.com/iree-org/iree/actions/runs/35093138856/job/104789629597) | 2026-09-16 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [4h46m](https://github.com/iree-org/iree/actions/runs/35093138856/job/104789629936) | 2026-09-16 10:03 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [4h44m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277070) | 2026-09-16 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-6` | pull_request |
| [4h44m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277083) | 2026-09-16 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `users/jschuhmacher/dynamic-plugin-support-6` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 12 | 12 | [15h24m](https://github.com/iree-org/iree/actions/runs/35044430244/job/104632578942) | 2026-09-16 10:03 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 10 | 5 | [4h57m](https://github.com/iree-org/iree/actions/runs/35093131570/job/104786296006) | 2026-09-16 10:03 PDT | [3h18m](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787745442) | [4h30m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790276935) | [4h30m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790276935) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 10 | 6 | [4h53m](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787673263) | 2026-09-16 10:03 PDT | [2h37m](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787746156) | [3h43m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277221) | [3h43m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277221) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 10 | 4 | [4h48m](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163542) | 2026-09-16 10:03 PDT | [57m36s](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787745975) | [4h43m](https://github.com/iree-org/iree/actions/runs/35093138856/job/104789629680) | [4h43m](https://github.com/iree-org/iree/actions/runs/35093138856/job/104789629680) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 0 | — | — | [1h03m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277155) | [4h46m](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787746052) | [4h46m](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787746052) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [1h09m](https://github.com/iree-org/iree/actions/runs/35106797229/job/104833982326) | [4h43m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277389) | [4h43m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277389) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 10 | 0 | — | — | [29m21s](https://github.com/iree-org/iree/actions/runs/35093139099/job/104791378467) | [4h26m](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787673037) | [4h26m](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787673037) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [42m27s](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787745777) | [4h17m](https://github.com/iree-org/iree/actions/runs/35093138856/job/104789629656) | [4h17m](https://github.com/iree-org/iree/actions/runs/35093138856/job/104789629656) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [44m04s](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787672899) | [3h52m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790276896) | [3h52m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790276896) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [1h08m](https://github.com/iree-org/iree/actions/runs/35098403907/job/104811488945) | [3h46m](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787745958) | [3h46m](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787745958) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 10 | 0 | — | — | [1h39m](https://github.com/iree-org/iree/actions/runs/35093139099/job/104791378666) | [3h25m](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163669) | [3h25m](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163669) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 0 | — | — | [1h34m](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787746211) | [3h07m](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163650) | [3h07m](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163650) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 0 | — | — | [1h28m](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787745784) | [2h53m](https://github.com/iree-org/iree/actions/runs/35093139099/job/104791378606) | [2h53m](https://github.com/iree-org/iree/actions/runs/35093139099/job/104791378606) | 2 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 14 | 0 | — | — | [10m28s](https://github.com/iree-org/iree/actions/runs/35093131661/job/104784001065) | [36m02s](https://github.com/iree-org/iree/actions/runs/35093081313/job/104786257756) | [36m32s](https://github.com/iree-org/iree/actions/runs/35093139153/job/104787808092) | 12 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 12 | 0 | — | — | [20m59s](https://github.com/iree-org/iree/actions/runs/35093138784/job/104794233310) | [31m41s](https://github.com/iree-org/iree/actions/runs/35093081313/job/104786257922) | [33m01s](https://github.com/iree-org/iree/actions/runs/35093140002/job/104789419063) | 12 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 12 | 0 | — | — | [22m49s](https://github.com/iree-org/iree/actions/runs/35093138666/job/104785644752) | [31m33s](https://github.com/iree-org/iree/actions/runs/35093081313/job/104786258065) | [32m02s](https://github.com/iree-org/iree/actions/runs/35093140002/job/104789419165) | 12 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 10 | 0 | — | — | [9m20s](https://github.com/iree-org/iree/actions/runs/35093131570/job/104786296262) | [30m54s](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277136) | [30m54s](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277136) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 12 | 0 | — | — | [20m50s](https://github.com/iree-org/iree/actions/runs/35093131661/job/104784001346) | [29m51s](https://github.com/iree-org/iree/actions/runs/35093081313/job/104786257982) | [34m50s](https://github.com/iree-org/iree/actions/runs/35093140002/job/104789419335) | 12 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 10 | 0 | — | — | [15m00s](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787745503) | [28m31s](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163576) | [28m31s](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163576) | 10 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 10 | 0 | — | — | [11m23s](https://github.com/iree-org/iree/actions/runs/35093138856/job/104789629576) | [28m21s](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787673267) | [28m21s](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787673267) | 10 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 305 | 1% (3/304) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 374 | 2% (6/373) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 302 | 1% (4/301) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 228 | 9% (20/228) |  | 2d01h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 4h53m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job observed waiting 4h57m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 15h24m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h53m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 3h46m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 3h25m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 4h43m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 4h26m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 4h30m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 3h20m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 3h52m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
