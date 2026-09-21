# iree-ci-monitor

_Updated: 2026-09-21 05:55 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [16m13s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438853) | [32m02s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438563) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438512) | [23m39s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438564) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [4m39s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438431) | [16m45s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438588) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [4m26s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438560) | [13m07s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438499) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [11m59s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438322) | [11m59s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438322) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [7m42s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438622) | [7m42s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438622) | — | `shark75-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m29s](https://github.com/iree-org/iree/actions/runs/35583924332/job/106282762271) | [1m29s](https://github.com/iree-org/iree/actions/runs/35583924332/job/106282762271) | 100% (1/1) | 1 |
| `macos-14` | github-hosted | 4 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/35583922355/job/106282756707) | [11s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783207) | — | 4 |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783521) | [8s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276784071) | 50% (1/2) | 7 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783131) | [5s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783147) | — | 3 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/35581978173/job/106276704997) | [4s](https://github.com/iree-org/iree/actions/runs/35581978173/job/106276705455) | — | 3 |
| `ubuntu-24.04` | github-hosted | 27 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783172) | [3s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276782872) | 0% (0/3) | 26 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783069) | [3s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783135) | — | 3 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438477) | [2s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438477) | — | `shark55-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783955) | [2s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783955) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 1 | [3h32m](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438335) | 2026-09-21 05:54 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 1 | [3h32m](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438527) | 2026-09-21 05:54 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [3h32m](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438335) | 2026-09-21 05:54 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/ziereis/qdq-integer-contractions` | pull_request |
| [3h32m](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438527) | 2026-09-21 05:54 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/ziereis/qdq-integer-contractions` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 1 | [3h32m](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438335) | 2026-09-21 05:54 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 1 | [3h32m](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438527) | 2026-09-21 05:54 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [32m02s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438563) | [32m02s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438563) | [32m02s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438563) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [23m39s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438564) | [23m39s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438564) | [23m39s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438564) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [16m45s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438588) | [16m45s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438588) | [16m45s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438588) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [16m13s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438853) | [16m13s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438853) | [16m13s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438853) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [13m07s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438499) | [13m07s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438499) | [13m07s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438499) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [11m59s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438322) | [11m59s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438322) | [11m59s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438322) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [7m42s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438622) | [7m42s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438622) | [7m42s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438622) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [4m39s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438431) | [4m39s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438431) | [4m39s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438431) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [4m26s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438560) | [4m26s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438560) | [4m26s](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438560) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m29s](https://github.com/iree-org/iree/actions/runs/35583924332/job/106282762271) | [1m29s](https://github.com/iree-org/iree/actions/runs/35583924332/job/106282762271) | [1m29s](https://github.com/iree-org/iree/actions/runs/35583924332/job/106282762271) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 1 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783207) | [11s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783207) | [11s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783207) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783810) | [8s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783810) | [8s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783810) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276784071) | [8s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276784071) | [8s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276784071) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783948) | [8s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783948) | [8s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783948) | 1 |
| `.github/workflows/ci_macos_arm64_clang.yml` | macos_arm64_clang | `macos-14` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35583922355/job/106282756707) | [8s](https://github.com/iree-org/iree/actions/runs/35583922355/job/106282756707) | [8s](https://github.com/iree-org/iree/actions/runs/35583922355/job/106282756707) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783521) | [7s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783521) | [7s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783521) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276782964) | [7s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276782964) | [7s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276782964) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783284) | [7s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783284) | [7s](https://github.com/iree-org/iree/actions/runs/35581982870/job/106276783284) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 328 | 0% (1/328) |  | 2h57m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 364 | 1% (3/364) |  | 3h06m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 230 | 2% (4/230) |  | 3d15h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 17 | 12% (2/17) |  | 6d21h ago |

## Alerts

- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job observed waiting 3h32m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 3h32m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
