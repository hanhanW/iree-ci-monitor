# iree-ci-monitor

_Updated: 2026-09-17 04:48 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [44m16s](https://github.com/iree-org/iree/actions/runs/35193781189/job/105114614973) | [2h03m](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114601808) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [1h42m](https://github.com/iree-org/iree/actions/runs/35193781189/job/105114615051) | [1h59m](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447638) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [1h11m](https://github.com/iree-org/iree/actions/runs/35193780802/job/105114596497) | [1h47m](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602397) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [1h30m](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447514) | [1h37m](https://github.com/iree-org/iree/actions/runs/35193780802/job/105114596199) | — | `shark01-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [40m12s](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447871) | [1h33m](https://github.com/iree-org/iree/actions/runs/35193781189/job/105114615179) | — | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [51m08s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602164) | [1h25m](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447544) | — | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [50m44s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602322) | [1h19m](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447744) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [10m48s](https://github.com/iree-org/iree/actions/runs/35193781189/job/105114614975) | [44m01s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602168) | — | `shark01-ci`, `shark55-ci` |
| `ubuntu-24.04` | github-hosted | 120 | 0 | — | — | 2 | [56s](https://github.com/iree-org/iree/actions/runs/35193779923/job/105112114992) | [8m39s](https://github.com/iree-org/iree/actions/runs/35193780802/job/105114596195) | 20% (1/5) | 105 |
| `windows-2022` | github-hosted | 14 | 0 | — | — | 0 | [4m20s](https://github.com/iree-org/iree/actions/runs/35193780107/job/105112387309) | [6m29s](https://github.com/iree-org/iree/actions/runs/35193780787/job/105112421117) | — | 14 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 1 | [2m34s](https://github.com/iree-org/iree/actions/runs/35193780184/job/105112427177) | [6m09s](https://github.com/iree-org/iree/actions/runs/35193781224/job/105112473752) | — | 15 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [2m07s](https://github.com/iree-org/iree/actions/runs/35193780107/job/105112387218) | [5m20s](https://github.com/iree-org/iree/actions/runs/35193781224/job/105112473747) | — | 15 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m25s](https://github.com/iree-org/iree/actions/runs/35205260554/job/105149352035) | [1m25s](https://github.com/iree-org/iree/actions/runs/35205260554/job/105149352035) | 100% (1/1) | 1 |
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35211404056/job/105169528392) | [38s](https://github.com/iree-org/iree/actions/runs/35211404056/job/105169528563) | — | 18 |
| `azure-linux-scale` | ossci | 22 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/35193780787/job/105112421089) | [11s](https://github.com/iree-org/iree/actions/runs/35193781224/job/105112473922) | 0% (0/2) | 22 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/35193781224/job/105112474012) | [6s](https://github.com/iree-org/iree/actions/runs/35193780184/job/105112427201) | — | 4 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 14 | 14 | [23h41m](https://github.com/iree-org/iree/actions/runs/35093131570/job/104786295964) | 2026-09-17 04:47 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [23h41m](https://github.com/iree-org/iree/actions/runs/35093131570/job/104786295964) | 2026-09-17 04:47 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [22h25m](https://github.com/iree-org/iree/actions/runs/35098403907/job/104811488885) | 2026-09-17 04:47 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `integrates/llvm-20260916` | pull_request |
| [21h25m](https://github.com/iree-org/iree/actions/runs/35106797229/job/104833982219) | 2026-09-17 04:47 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [19h36m](https://github.com/iree-org/iree/actions/runs/35119277314/job/104875991730) | 2026-09-17 04:47 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/ziereis/qdq-integer-contractions` | pull_request |
| [17h19m](https://github.com/iree-org/iree/actions/runs/35133353598/job/104923411056) | 2026-09-17 04:47 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-3` | pull_request |
| [17h19m](https://github.com/iree-org/iree/actions/runs/35133349567/job/104923478700) | 2026-09-17 04:47 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [17h18m](https://github.com/iree-org/iree/actions/runs/35133351078/job/104923919050) | 2026-09-17 04:47 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-2` | pull_request |
| [17h17m](https://github.com/iree-org/iree/actions/runs/35133351483/job/104924409806) | 2026-09-17 04:47 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-6` | pull_request |
| [17h16m](https://github.com/iree-org/iree/actions/runs/35133353135/job/104924487535) | 2026-09-17 04:47 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-7` | pull_request |
| [17h16m](https://github.com/iree-org/iree/actions/runs/35133351343/job/104924553868) | 2026-09-17 04:47 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-5` | pull_request |
| [4h21m](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447705) | 2026-09-17 04:47 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/egebeysel/scalable-dist-2-distribution-tile-sizes` | pull_request |
| [4h20m](https://github.com/iree-org/iree/actions/runs/35193780802/job/105114596460) | 2026-09-17 04:47 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/egebeysel/scalable-dist-5-distribution-tiling-tests` | pull_request |
| [4h20m](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602166) | 2026-09-17 04:47 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/egebeysel/scalable-dist-1-vscale-range-target-field` | pull_request |
| [4h20m](https://github.com/iree-org/iree/actions/runs/35193781189/job/105114614976) | 2026-09-17 04:47 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/egebeysel/scalable-dist-3-unpack-distribution-hints` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 14 | 14 | [23h41m](https://github.com/iree-org/iree/actions/runs/35093131570/job/104786295964) | 2026-09-17 04:47 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [44m16s](https://github.com/iree-org/iree/actions/runs/35193781189/job/105114614973) | [2h03m](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114601808) | [2h03m](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114601808) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [1h42m](https://github.com/iree-org/iree/actions/runs/35193781189/job/105114615051) | [1h59m](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447638) | [1h59m](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447638) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [1h27m](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447777) | [1h47m](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602397) | [1h47m](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602397) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [1h30m](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447514) | [1h37m](https://github.com/iree-org/iree/actions/runs/35193780802/job/105114596199) | [1h37m](https://github.com/iree-org/iree/actions/runs/35193780802/job/105114596199) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [1h03m](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602367) | [1h33m](https://github.com/iree-org/iree/actions/runs/35193781189/job/105114615179) | [1h33m](https://github.com/iree-org/iree/actions/runs/35193781189/job/105114615179) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [54m13s](https://github.com/iree-org/iree/actions/runs/35193781189/job/105114615097) | [1h25m](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447544) | [1h25m](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447544) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [1h06m](https://github.com/iree-org/iree/actions/runs/35193780802/job/105114596527) | [1h21m](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602144) | [1h21m](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602144) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [35m00s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602323) | [1h20m](https://github.com/iree-org/iree/actions/runs/35193781189/job/105114615105) | [1h20m](https://github.com/iree-org/iree/actions/runs/35193781189/job/105114615105) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [1h12m](https://github.com/iree-org/iree/actions/runs/35193780802/job/105114596501) | [1h19m](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447744) | [1h19m](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447744) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [22m39s](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447662) | [1h00m](https://github.com/iree-org/iree/actions/runs/35193780802/job/105114596431) | [1h00m](https://github.com/iree-org/iree/actions/runs/35193780802/job/105114596431) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [39m19s](https://github.com/iree-org/iree/actions/runs/35193781189/job/105114615100) | [49m24s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602251) | [49m24s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602251) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [10m48s](https://github.com/iree-org/iree/actions/runs/35193781189/job/105114614975) | [44m01s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602168) | [44m01s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602168) | 2 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 4 | 0 | — | — | [9m27s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602041) | [9m59s](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447812) | [9m59s](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447812) | 4 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 4 | 0 | — | — | [6m50s](https://github.com/iree-org/iree/actions/runs/35193781189/job/105114614962) | [9m49s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602298) | [9m49s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602298) | 4 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 4 | 0 | — | — | [7m18s](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447516) | [9m47s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602253) | [9m47s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602253) | 4 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 4 | 0 | — | — | [6m54s](https://github.com/iree-org/iree/actions/runs/35193780802/job/105114596165) | [9m42s](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447867) | [9m42s](https://github.com/iree-org/iree/actions/runs/35193780196/job/105114447867) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 4 | 0 | — | — | [6m54s](https://github.com/iree-org/iree/actions/runs/35193780802/job/105114596441) | [8m35s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602216) | [8m35s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602216) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 4 | 0 | — | — | [5m57s](https://github.com/iree-org/iree/actions/runs/35193781189/job/105114615067) | [6m54s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602267) | [6m54s](https://github.com/iree-org/iree/actions/runs/35193780074/job/105114602267) | 4 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 4 | 0 | — | — | [4m34s](https://github.com/iree-org/iree/actions/runs/35193780787/job/105112420986) | [6m53s](https://github.com/iree-org/iree/actions/runs/35193781224/job/105112473796) | [6m53s](https://github.com/iree-org/iree/actions/runs/35193781224/job/105112473796) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 410 | 1% (6/410) |  | 2h11m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 326 | 2% (6/326) |  | 2h37m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 324 | 1% (3/324) |  | 2h38m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 208 | 9% (18/208) |  | 2d20h ago |

## Alerts

- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 23h41m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h33m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h59m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h47m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h03m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h37m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h19m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h25m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
