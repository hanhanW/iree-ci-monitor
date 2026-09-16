# iree-ci-monitor

_Updated: 2026-09-16 14:23 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 32 | 0 | — | — | 0 | [1h41m](https://github.com/iree-org/iree/actions/runs/35133353135/job/104924487559) | [5h25m](https://github.com/iree-org/iree/actions/runs/35093138856/job/104789629936) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 16 | 0 | — | — | 0 | [1h57m](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787672854) | [5h01m](https://github.com/iree-org/iree/actions/runs/35093131570/job/104786296006) | 0% (0/2) | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 32 | 0 | — | — | 0 | [36m06s](https://github.com/iree-org/iree/actions/runs/35133353135/job/104924487551) | [3h49m](https://github.com/iree-org/iree/actions/runs/35093131570/job/104786295976) | 0% (0/4) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 32 | 0 | — | — | 0 | [51m42s](https://github.com/iree-org/iree/actions/runs/35119277314/job/104875992014) | [3h41m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277206) | 0% (0/4) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 16 | 0 | — | — | 0 | [34m53s](https://github.com/iree-org/iree/actions/runs/35133353135/job/104924487240) | [3h28m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277082) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 32 | 0 | — | — | 0 | [1h00m](https://github.com/iree-org/iree/actions/runs/35133351343/job/104924553823) | [3h07m](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163650) | 0% (0/4) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 16 | 0 | — | — | 0 | [1h33m](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787672954) | [3h01m](https://github.com/iree-org/iree/actions/runs/35098403907/job/104811488755) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 16 | 0 | — | — | 0 | [49m47s](https://github.com/iree-org/iree/actions/runs/35133351078/job/104923918884) | [2h49m](https://github.com/iree-org/iree/actions/runs/35098403907/job/104811488954) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `ubuntu-24.04` | github-hosted | 385 | 0 | — | — | 0 | [7m26s](https://github.com/iree-org/iree/actions/runs/35133353598/job/104923411001) | [28m21s](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787673267) | 3% (1/39) | 360 |
| `ubuntu-24.04-arm` | github-hosted | 54 | 0 | — | — | 0 | [1m17s](https://github.com/iree-org/iree/actions/runs/35093138816/job/104784686665) | [12m02s](https://github.com/iree-org/iree/actions/runs/35093138784/job/104794233392) | 0% (0/6) | 54 |
| `windows-2022` | github-hosted | 54 | 0 | — | — | 0 | [2m21s](https://github.com/iree-org/iree/actions/runs/35133350235/job/104920560509) | [9m13s](https://github.com/iree-org/iree/actions/runs/35093138666/job/104785644539) | 0% (0/6) | 54 |
| `ubuntu-latest` | github-hosted | 81 | 0 | — | — | 0 | [1m12s](https://github.com/iree-org/iree/actions/runs/35093755811/job/104785973401) | [9m05s](https://github.com/iree-org/iree/actions/runs/35133344203/job/104919473650) | 0% (0/6) | 81 |
| `macos-14` | github-hosted | 54 | 0 | — | — | 0 | [1m47s](https://github.com/iree-org/iree/actions/runs/35133351024/job/104923371340) | [8m41s](https://github.com/iree-org/iree/actions/runs/35093140002/job/104789419293) | 0% (0/6) | 54 |
| `azure-linux-scale` | ossci | 105 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/35106796649/job/104830076352) | [4m55s](https://github.com/iree-org/iree/actions/runs/35093138312/job/104785898763) | 0% (0/12) | 105 |
| `azure-windows-scale` | ossci | 18 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/35133351047/job/104919635851) | [2m39s](https://github.com/iree-org/iree/actions/runs/35093138666/job/104785645020) | 0% (0/2) | 18 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 18 | 12 | [19h42m](https://github.com/iree-org/iree/actions/runs/35044430244/job/104632578942) | 2026-09-16 14:21 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [19h42m](https://github.com/iree-org/iree/actions/runs/35044430244/job/104632578942) | 2026-09-16 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `ci-remove-w7900x2-package-jobs` | pull_request |
| [14h56m](https://github.com/iree-org/iree/actions/runs/35062939888/job/104689025165) | 2026-09-16 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [9h16m](https://github.com/iree-org/iree/actions/runs/35093131570/job/104786295964) | 2026-09-16 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [8h00m](https://github.com/iree-org/iree/actions/runs/35098403907/job/104811488885) | 2026-09-16 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `integrates/llvm-20260916` | pull_request |
| [7h00m](https://github.com/iree-org/iree/actions/runs/35106797229/job/104833982219) | 2026-09-16 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [5h10m](https://github.com/iree-org/iree/actions/runs/35119277314/job/104875991730) | 2026-09-16 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/ziereis/qdq-integer-contractions` | pull_request |
| [2h54m](https://github.com/iree-org/iree/actions/runs/35133353598/job/104923411056) | 2026-09-16 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-3` | pull_request |
| [2h54m](https://github.com/iree-org/iree/actions/runs/35133349567/job/104923478700) | 2026-09-16 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [2h52m](https://github.com/iree-org/iree/actions/runs/35133351078/job/104923919050) | 2026-09-16 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-2` | pull_request |
| [2h51m](https://github.com/iree-org/iree/actions/runs/35133351483/job/104924409806) | 2026-09-16 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-6` | pull_request |
| [2h51m](https://github.com/iree-org/iree/actions/runs/35133353135/job/104924487535) | 2026-09-16 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-7` | pull_request |
| [2h50m](https://github.com/iree-org/iree/actions/runs/35133351343/job/104924553868) | 2026-09-16 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-5` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 18 | 12 | [19h42m](https://github.com/iree-org/iree/actions/runs/35044430244/job/104632578942) | 2026-09-16 14:21 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 16 | 0 | — | — | [2h37m](https://github.com/iree-org/iree/actions/runs/35106797229/job/104833982333) | [5h25m](https://github.com/iree-org/iree/actions/runs/35093138856/job/104789629936) | [5h34m](https://github.com/iree-org/iree/actions/runs/35093139099/job/104791378825) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 16 | 0 | — | — | [1h24m](https://github.com/iree-org/iree/actions/runs/35133351078/job/104923918862) | [5h19m](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163542) | [5h28m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277083) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 16 | 0 | — | — | [1h57m](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787672854) | [5h01m](https://github.com/iree-org/iree/actions/runs/35093131570/job/104786296006) | [5h02m](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163560) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 16 | 0 | — | — | [38m01s](https://github.com/iree-org/iree/actions/runs/35133351343/job/104924553758) | [3h49m](https://github.com/iree-org/iree/actions/runs/35093131570/job/104786295976) | [4h17m](https://github.com/iree-org/iree/actions/runs/35093138856/job/104789629656) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 16 | 0 | — | — | [49m33s](https://github.com/iree-org/iree/actions/runs/35133351078/job/104923919015) | [3h41m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277206) | [3h46m](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787745958) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 16 | 0 | — | — | [34m53s](https://github.com/iree-org/iree/actions/runs/35133353135/job/104924487240) | [3h28m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277082) | [4h26m](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787673037) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 16 | 0 | — | — | [1h03m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277155) | [3h20m](https://github.com/iree-org/iree/actions/runs/35093138856/job/104789629539) | [4h46m](https://github.com/iree-org/iree/actions/runs/35093139935/job/104787746052) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 16 | 0 | — | — | [1h33m](https://github.com/iree-org/iree/actions/runs/35093139045/job/104787672954) | [3h01m](https://github.com/iree-org/iree/actions/runs/35098403907/job/104811488755) | [3h25m](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163669) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 16 | 0 | — | — | [29m55s](https://github.com/iree-org/iree/actions/runs/35119277314/job/104875991594) | [2h58m](https://github.com/iree-org/iree/actions/runs/35093138856/job/104789629616) | [3h52m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790276896) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 16 | 0 | — | — | [55m01s](https://github.com/iree-org/iree/actions/runs/35133353598/job/104923411190) | [2h51m](https://github.com/iree-org/iree/actions/runs/35093139099/job/104791378875) | [3h07m](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163650) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 16 | 0 | — | — | [49m47s](https://github.com/iree-org/iree/actions/runs/35133351078/job/104923918884) | [2h49m](https://github.com/iree-org/iree/actions/runs/35098403907/job/104811488954) | [2h53m](https://github.com/iree-org/iree/actions/runs/35093139099/job/104791378606) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 16 | 0 | — | — | [1h09m](https://github.com/iree-org/iree/actions/runs/35106797229/job/104833982326) | [2h25m](https://github.com/iree-org/iree/actions/runs/35093139099/job/104791378781) | [4h43m](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277389) | 2 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 25 | 0 | — | — | [4m03s](https://github.com/iree-org/iree/actions/runs/35093138816/job/104784686369) | [36m02s](https://github.com/iree-org/iree/actions/runs/35093081313/job/104786257756) | [36m32s](https://github.com/iree-org/iree/actions/runs/35093139153/job/104787808092) | 18 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 18 | 0 | — | — | [6m44s](https://github.com/iree-org/iree/actions/runs/35133353625/job/104920984160) | [31m41s](https://github.com/iree-org/iree/actions/runs/35093081313/job/104786257922) | [33m01s](https://github.com/iree-org/iree/actions/runs/35093140002/job/104789419063) | 18 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 18 | 0 | — | — | [16m43s](https://github.com/iree-org/iree/actions/runs/35133352660/job/104921390293) | [31m33s](https://github.com/iree-org/iree/actions/runs/35093081313/job/104786258065) | [32m02s](https://github.com/iree-org/iree/actions/runs/35093140002/job/104789419165) | 18 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 16 | 0 | — | — | [13m26s](https://github.com/iree-org/iree/actions/runs/35093138856/job/104789629676) | [30m33s](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163613) | [30m54s](https://github.com/iree-org/iree/actions/runs/35093138262/job/104790277136) | 16 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 18 | 0 | — | — | [15m27s](https://github.com/iree-org/iree/actions/runs/35133353625/job/104920984213) | [29m51s](https://github.com/iree-org/iree/actions/runs/35093081313/job/104786257982) | [34m50s](https://github.com/iree-org/iree/actions/runs/35093140002/job/104789419335) | 18 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 25 | 0 | — | — | [6m08s](https://github.com/iree-org/iree/actions/runs/35093131661/job/104784001157) | [28m13s](https://github.com/iree-org/iree/actions/runs/35093138816/job/104784686335) | [29m32s](https://github.com/iree-org/iree/actions/runs/35093081313/job/104786257769) | 18 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 16 | 0 | — | — | [13m32s](https://github.com/iree-org/iree/actions/runs/35133351343/job/104924553712) | [27m59s](https://github.com/iree-org/iree/actions/runs/35093139099/job/104791378526) | [28m31s](https://github.com/iree-org/iree/actions/runs/35093138405/job/104789163576) | 16 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 414 | 1% (6/414) |  | 1h03m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 328 | 2% (6/328) |  | 1h25m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 326 | 1% (3/326) |  | 1h35m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 228 | 9% (20/228) |  | 2d05h ago |

## Alerts

- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 19h42m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h49m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 3h41m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 3h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 5h25m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h28m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 5h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 3h07m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 3h49m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
