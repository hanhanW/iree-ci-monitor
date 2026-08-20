# iree-ci-monitor

_Updated: 2026-08-20 00:08 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 1 | [5s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869835) | [6s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869844) | — | 3 |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869855) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869935) | 0% (0/4) | 11 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870009) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869893) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870005) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869928) | — | 2 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759524) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759599) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759660) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759688) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | — | 0 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759971) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759524) | 2026-08-19 00:07 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `main` | push |
| [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759599) | 2026-08-19 00:07 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759660) | 2026-08-19 00:07 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `main` | push |
| [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759688) | 2026-08-19 00:07 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759971) | 2026-08-19 00:07 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759524) | 2026-08-19 00:07 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759660) | 2026-08-19 00:07 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759599) | 2026-08-19 00:07 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759971) | 2026-08-19 00:07 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759688) | 2026-08-19 00:07 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869844) | [6s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869844) | [6s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869844) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869835) | [5s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869835) | [5s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869835) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869830) | [4s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869830) | [4s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869830) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869881) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869881) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869881) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869815) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869815) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869815) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869935) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869935) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869935) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869893) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869893) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869893) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869928) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869928) | [3s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869928) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32274087599/job/96243015344) | [3s](https://github.com/iree-org/iree/actions/runs/32274087599/job/96243015344) | [3s](https://github.com/iree-org/iree/actions/runs/32274087599/job/96243015344) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32332975306/job/96317020402) | [3s](https://github.com/iree-org/iree/actions/runs/32332975306/job/96317020402) | [3s](https://github.com/iree-org/iree/actions/runs/32332975306/job/96317020402) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869855) | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869855) | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325869855) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870009) | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870009) | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870009) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325839192) | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325839192) | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325839192) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870005) | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870005) | [2s](https://github.com/iree-org/iree/actions/runs/32336088852/job/96325870005) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32274087453/job/96244813282) | [2s](https://github.com/iree-org/iree/actions/runs/32274087453/job/96244813282) | [2s](https://github.com/iree-org/iree/actions/runs/32274087453/job/96244813282) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 212 | 0% (1/211) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 158 | 0% (0/157) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 192 | 3% (6/191) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 150 | 0% (0/149) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
