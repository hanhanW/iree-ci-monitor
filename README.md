# iree-ci-monitor

_Updated: 2026-05-31 00:35 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 2 | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738968) | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738972) | 0% (0/1) | 6 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738967) | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738976) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738971) | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738980) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738973) | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738984) | — | 2 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 1 | [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293013979) | 2026-05-28 06:38 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014052) | 2026-05-28 06:38 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 2 | [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296402) | 2026-05-28 06:38 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201` | self-hosted | 2 | 2 | [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296040) | 2026-05-28 06:38 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 1 | 1 | [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014224) | 2026-05-28 06:38 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 1 | [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014243) | 2026-05-28 06:38 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 2 | 2 | [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296086) | 2026-05-28 06:38 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296040) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296086) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296402) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293013979) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `main` | push |
| [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014052) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `main` | push |
| [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014176) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014210) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014224) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014243) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `main` | push |
| [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014246) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 2 | [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296402) | 2026-05-28 06:38 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 2 | [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296040) | 2026-05-28 06:38 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 2 | [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296086) | 2026-05-28 06:38 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 1 | [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293013979) | 2026-05-28 06:38 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 1 | [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014243) | 2026-05-28 06:38 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 1 | [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014052) | 2026-05-28 06:38 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 1 | [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014224) | 2026-05-28 06:38 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738976) | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738976) | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738976) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738972) | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738972) | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738972) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738984) | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738984) | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738984) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738973) | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738973) | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738973) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738980) | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738980) | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738980) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738971) | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738971) | [2s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738971) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26705431710/job/78705696655) | [2s](https://github.com/iree-org/iree/actions/runs/26705431710/job/78705696655) | [2s](https://github.com/iree-org/iree/actions/runs/26705431710/job/78705696655) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738960) | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738960) | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738960) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738967) | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738967) | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738967) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738956) | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738956) | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738956) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738968) | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738968) | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738968) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738977) | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738977) | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705738977) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705730355) | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705730355) | [1s](https://github.com/iree-org/iree/actions/runs/26705442487/job/78705730355) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 255 | 5% (12/254) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 278 | 1% (3/278) |  | 21h04m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 192 | 2% (3/192) |  | 21h13m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 198 | 0% (0/198) |  | 21h31m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 65 | 2% (1/65) |  | 21h51m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
