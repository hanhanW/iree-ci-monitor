# iree-ci-monitor

_Updated: 2026-10-03 14:22 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [6m19s](https://github.com/iree-org/iree/actions/runs/37138166416/job/111248141253) | [40m44s](https://github.com/iree-org/iree/actions/runs/37140389111/job/111254772568) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [4m30s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721916) | [34m26s](https://github.com/iree-org/iree/actions/runs/37140389111/job/111254772910) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [11m58s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721928) | [27m55s](https://github.com/iree-org/iree/actions/runs/37140389111/job/111254772676) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [12m22s](https://github.com/iree-org/iree/actions/runs/37138166416/job/111248141125) | [20m32s](https://github.com/iree-org/iree/actions/runs/37140389111/job/111254772576) | — | `shark75-ci` |
| `azure-linux-scale` | ossci | 24 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864526) | [9s](https://github.com/iree-org/iree/actions/runs/37138166290/job/111246895904) | — | 24 |
| `macos-14` | github-hosted | 12 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/37138166290/job/111246895870) | [9s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864341) | — | 12 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864411) | [5s](https://github.com/iree-org/iree/actions/runs/37140389021/job/111253602379) | — | 12 |
| `ubuntu-24.04` | github-hosted | 77 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37140389111/job/111254772655) | [3s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651751) | 50% (1/2) | 77 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37131310269/job/111226822511) | [3s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226847576) | — | 6 |
| `windows-2022` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651772) | [3s](https://github.com/iree-org/iree/actions/runs/37138166290/job/111246895830) | — | 12 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283652141) | [1s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864612) | — | 4 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 4 | [23h38m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257394) | 2026-10-03 14:21 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 6 | 4 | [23h38m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257364) | 2026-10-03 14:21 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 12 | 8 | [23h38m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257428) | 2026-10-03 14:21 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 12 | 8 | [23h38m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257509) | 2026-10-03 14:21 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [23h38m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257364) | 2026-10-03 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [23h38m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257394) | 2026-10-03 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [23h38m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257428) | 2026-10-03 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [23h38m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257509) | 2026-10-03 14:21 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [23h38m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257562) | 2026-10-03 14:21 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [23h38m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257835) | 2026-10-03 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [20h53m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943478) | 2026-10-03 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [20h53m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943507) | 2026-10-03 14:21 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [20h53m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943522) | 2026-10-03 14:21 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [20h53m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943553) | 2026-10-03 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [20h53m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943557) | 2026-10-03 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [20h53m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943578) | 2026-10-03 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [15h08m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173088) | 2026-10-03 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `feat-python-async-parameter-files` | pull_request |
| [15h08m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173141) | 2026-10-03 14:21 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `feat-python-async-parameter-files` | pull_request |
| [15h08m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173202) | 2026-10-03 14:21 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `feat-python-async-parameter-files` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 4 | [23h38m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257394) | 2026-10-03 14:21 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 6 | 4 | [23h38m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257364) | 2026-10-03 14:21 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 4 | [23h38m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257835) | 2026-10-03 14:21 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 4 | [23h38m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257428) | 2026-10-03 14:21 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 4 | [23h38m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257509) | 2026-10-03 14:21 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 4 | [23h38m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257562) | 2026-10-03 14:21 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [6m19s](https://github.com/iree-org/iree/actions/runs/37138166416/job/111248141253) | [40m44s](https://github.com/iree-org/iree/actions/runs/37140389111/job/111254772568) | [40m44s](https://github.com/iree-org/iree/actions/runs/37140389111/job/111254772568) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [4m30s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721916) | [34m26s](https://github.com/iree-org/iree/actions/runs/37140389111/job/111254772910) | [34m26s](https://github.com/iree-org/iree/actions/runs/37140389111/job/111254772910) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [11m58s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721928) | [27m55s](https://github.com/iree-org/iree/actions/runs/37140389111/job/111254772676) | [27m55s](https://github.com/iree-org/iree/actions/runs/37140389111/job/111254772676) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [12m22s](https://github.com/iree-org/iree/actions/runs/37138166416/job/111248141125) | [20m32s](https://github.com/iree-org/iree/actions/runs/37140389111/job/111254772576) | [20m32s](https://github.com/iree-org/iree/actions/runs/37140389111/job/111254772576) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [14m10s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722043) | [19m44s](https://github.com/iree-org/iree/actions/runs/37138166416/job/111248141140) | [19m44s](https://github.com/iree-org/iree/actions/runs/37138166416/job/111248141140) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [6m31s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721993) | [11m07s](https://github.com/iree-org/iree/actions/runs/37140389111/job/111254772658) | [11m07s](https://github.com/iree-org/iree/actions/runs/37140389111/job/111254772658) | 1 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37140389111/job/111254772586) | [38s](https://github.com/iree-org/iree/actions/runs/37138166416/job/111248141052) | [38s](https://github.com/iree-org/iree/actions/runs/37138166416/job/111248141052) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 4 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651792) | [10s](https://github.com/iree-org/iree/actions/runs/37140389021/job/111253602444) | [10s](https://github.com/iree-org/iree/actions/runs/37140389021/job/111253602444) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 4 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/37138166290/job/111246895834) | [10s](https://github.com/iree-org/iree/actions/runs/37140389021/job/111253602417) | [10s](https://github.com/iree-org/iree/actions/runs/37140389021/job/111253602417) | 4 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 4 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651952) | [9s](https://github.com/iree-org/iree/actions/runs/37138166290/job/111246895954) | [9s](https://github.com/iree-org/iree/actions/runs/37138166290/job/111246895954) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 4 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864529) | [9s](https://github.com/iree-org/iree/actions/runs/37138166290/job/111246895904) | [9s](https://github.com/iree-org/iree/actions/runs/37138166290/job/111246895904) | 4 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 4 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37140389021/job/111253602328) | [9s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864341) | [9s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864341) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 4 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651858) | [8s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864504) | [8s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864504) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 4 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37138166290/job/111246895828) | [8s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283652101) | [8s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283652101) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 296 | 1% (4/296) |  | 37m45s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 206 | 1% (2/206) |  | 3d00h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 23h38m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 23h38m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 23h38m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 23h38m (> 2h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
