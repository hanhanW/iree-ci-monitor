# iree-ci-monitor

_Updated: 2026-10-03 22:59 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [3m05s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722089) | [14m10s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722043) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [6m31s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721993) | [11m58s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721928) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [4m30s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721916) | [4m30s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721916) | — | `shark75-ci` |
| `macos-14` | github-hosted | 6 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651814) | [9s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864341) | — | 6 |
| `azure-linux-scale` | ossci | 12 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651969) | [8s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864529) | — | 12 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651776) | [4s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864411) | — | 6 |
| `ubuntu-24.04` | github-hosted | 34 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37150629726/job/111283625719) | [3s](https://github.com/iree-org/iree/actions/runs/37150894328/job/111284405690) | 100% (1/1) | 34 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864364) | [3s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651759) | — | 6 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721896) | [1s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721896) | — | `shark75-ci` |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283652141) | [1s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864612) | — | 2 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 2 | [23h45m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173205) | 2026-10-03 22:59 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 2 | 2 | [23h45m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173088) | 2026-10-03 22:59 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 4 | 4 | [23h45m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173211) | 2026-10-03 22:59 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 4 | 4 | [23h45m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173141) | 2026-10-03 22:59 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [23h45m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173088) | 2026-10-03 22:59 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `feat-python-async-parameter-files` | pull_request |
| [23h45m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173141) | 2026-10-03 22:59 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `feat-python-async-parameter-files` | pull_request |
| [23h45m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173202) | 2026-10-03 22:59 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `feat-python-async-parameter-files` | pull_request |
| [23h45m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173205) | 2026-10-03 22:59 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `feat-python-async-parameter-files` | pull_request |
| [23h45m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173211) | 2026-10-03 22:59 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `feat-python-async-parameter-files` | pull_request |
| [23h45m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173214) | 2026-10-03 22:59 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `feat-python-async-parameter-files` | pull_request |
| [9h36m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721930) | 2026-10-03 22:59 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |
| [9h36m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721946) | 2026-10-03 22:59 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |
| [9h36m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721988) | 2026-10-03 22:59 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |
| [9h36m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722024) | 2026-10-03 22:59 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |
| [9h36m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722031) | 2026-10-03 22:59 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |
| [9h36m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722066) | 2026-10-03 22:59 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 2 | [23h45m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173205) | 2026-10-03 22:59 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 2 | 2 | [23h45m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173088) | 2026-10-03 22:59 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 2 | [23h45m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173141) | 2026-10-03 22:59 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 2 | [23h45m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173211) | 2026-10-03 22:59 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 2 | [23h45m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173202) | 2026-10-03 22:59 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 2 | [23h45m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173214) | 2026-10-03 22:59 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [14m10s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722043) | [14m10s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722043) | [14m10s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722043) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [11m58s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721928) | [11m58s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721928) | [11m58s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721928) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [6m31s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721993) | [6m31s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721993) | [6m31s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721993) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [4m30s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721916) | [4m30s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721916) | [4m30s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721916) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [3m05s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722089) | [3m05s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722089) | [3m05s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722089) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651635) | [9s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864341) | [9s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864341) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864505) | [8s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651952) | [8s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651952) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651858) | [8s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864504) | [8s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864504) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864526) | [8s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283652101) | [8s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283652101) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651969) | [8s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864763) | [8s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864763) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283652030) | [8s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864529) | [8s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864529) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 2 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864453) | [8s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651792) | [8s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651792) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37150629700/job/111283651814) | [7s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864443) | [7s](https://github.com/iree-org/iree/actions/runs/37150894642/job/111284864443) | 2 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37150629726/job/111284612797) | [4s](https://github.com/iree-org/iree/actions/runs/37067818568/job/111299746227) | [4s](https://github.com/iree-org/iree/actions/runs/37067818568/job/111299746227) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 296 | 1% (4/296) |  | 9h14m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 206 | 1% (2/206) |  | 3d09h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 23h45m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 23h45m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 23h45m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 23h45m (> 2h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
