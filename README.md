# iree-ci-monitor

_Updated: 2026-05-29 00:40 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [1m06s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284391) | [1m43s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284377) | — | 5 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284349) | [1m27s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284328) | — | 5 |
| `ubuntu-24.04` | github-hosted | 54 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26612030594/job/78419835848) | [3s](https://github.com/iree-org/iree/actions/runs/26621978557/job/78449846285) | 50% (2/4) | 44 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26611835316/job/78419225966) | [3s](https://github.com/iree-org/iree/actions/runs/26611835316/job/78419225977) | — | 15 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/26621978557/job/78449846269) | [3s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284272) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284317) | [3s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284311) | — | 6 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284408) | [1s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284408) | — | 1 |
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
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [1m43s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284377) | [1m43s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284377) | [1m43s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284377) | 1 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 1 | 0 | — | — | [1m27s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284328) | [1m27s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284328) | [1m27s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284328) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [1m25s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284342) | [1m25s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284342) | [1m25s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284342) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 1 | 0 | — | — | [1m12s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284358) | [1m12s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284358) | [1m12s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284358) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m06s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284391) | [1m06s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284391) | [1m06s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284391) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [52s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284331) | [52s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284331) | [52s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454284331) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [34s](https://github.com/iree-org/iree/actions/runs/26623378411/job/78454283171) | [34s](https://github.com/iree-org/iree/actions/runs/26623378411/job/78454283171) | [34s](https://github.com/iree-org/iree/actions/runs/26623378411/job/78454283171) | 1 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26611837895/job/78419230975) | [4s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454253497) | [4s](https://github.com/iree-org/iree/actions/runs/26623378523/job/78454253497) | 6 |
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26611890891/job/78419392425) | [3s](https://github.com/iree-org/iree/actions/runs/26612030446/job/78419811520) | [3s](https://github.com/iree-org/iree/actions/runs/26612030446/job/78419811520) | 6 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26611890967/job/78419392984) | [3s](https://github.com/iree-org/iree/actions/runs/26623378411/job/78454253488) | [3s](https://github.com/iree-org/iree/actions/runs/26623378411/job/78454253488) | 6 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26612028667/job/78419809323) | [3s](https://github.com/iree-org/iree/actions/runs/26611889286/job/78419389761) | [3s](https://github.com/iree-org/iree/actions/runs/26611889286/job/78419389761) | 5 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26611453273/job/78418050366) | [3s](https://github.com/iree-org/iree/actions/runs/26611835316/job/78419225915) | [3s](https://github.com/iree-org/iree/actions/runs/26611835316/job/78419225915) | 5 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26621978557/job/78449846271) | [3s](https://github.com/iree-org/iree/actions/runs/26621978557/job/78449846271) | [3s](https://github.com/iree-org/iree/actions/runs/26621978557/job/78449846271) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 218 | 4% (9/217) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 185 | 2% (4/185) |  | 15h01m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 245 | 1% (3/245) |  | 16h53m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 170 | 0% (0/170) |  | 17h58m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 58 | 2% (1/58) |  | 18h46m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
