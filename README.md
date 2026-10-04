# iree-ci-monitor

_Updated: 2026-10-04 05:27 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943099) | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943088) | — | 3 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943107) | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943087) | — | 2 |
| `ubuntu-24.04` | github-hosted | 7 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943077) | [3s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943092) | 0% (0/1) | 7 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943082) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943113) | — | 2 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 1 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721930) | 2026-10-04 05:27 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 1 | 1 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721946) | 2026-10-04 05:27 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 2 | 2 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721988) | 2026-10-04 05:27 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 2 | 2 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722024) | 2026-10-04 05:27 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721930) | 2026-10-04 05:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |
| [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721946) | 2026-10-04 05:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |
| [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721988) | 2026-10-04 05:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |
| [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722024) | 2026-10-04 05:27 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |
| [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722031) | 2026-10-04 05:27 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |
| [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722066) | 2026-10-04 05:27 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/MaheshRavishankar/blockSparseCommitsPR4` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 1 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721930) | 2026-10-04 05:27 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 1 | 1 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721946) | 2026-10-04 05:27 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 1 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722024) | 2026-10-04 05:27 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 1 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285721988) | 2026-10-04 05:27 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 1 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722066) | 2026-10-04 05:27 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 1 | [16h04m](https://github.com/iree-org/iree/actions/runs/37150894632/job/111285722031) | 2026-10-04 05:27 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943088) | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943088) | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943088) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943087) | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943087) | [7s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943087) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943107) | [6s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943107) | [6s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943107) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943099) | [4s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943099) | [4s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943099) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943046) | [4s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943046) | [4s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943046) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943092) | [3s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943092) | [3s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943092) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943096) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943096) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943096) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943083) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943083) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943083) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943077) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943077) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943077) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382915478) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382915478) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382915478) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943113) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943113) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943113) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943082) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943082) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111382943082) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111376769824) | [2s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111376769824) | [2s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111376769824) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37184259141/job/111382816759) | [2s](https://github.com/iree-org/iree/actions/runs/37184259141/job/111382816759) | [2s](https://github.com/iree-org/iree/actions/runs/37184259141/job/111382816759) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 296 | 1% (4/296) |  | 15h42m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 206 | 1% (2/206) |  | 3d15h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 16h04m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 16h04m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 16h04m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 16h04m (> 2h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
