# iree-ci-monitor

_Updated: 2026-09-20 04:30 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279125) | [7s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279123) | — | 2 |
| `ubuntu-24.04` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055339751) | [4s](https://github.com/iree-org/iree/actions/runs/35416725134/job/106012960458) | 50% (1/2) | 11 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279191) | [4s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279210) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279114) | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279119) | — | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 1 | [20h52m](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640040) | 2026-09-20 04:30 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 1 | [20h52m](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640153) | 2026-09-20 04:30 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [20h52m](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640040) | 2026-09-20 04:30 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `stream-flush-invalidate-lowering` | pull_request |
| [20h52m](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640153) | 2026-09-20 04:30 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `stream-flush-invalidate-lowering` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 1 | [20h52m](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640040) | 2026-09-20 04:30 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 1 | [20h52m](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640153) | 2026-09-20 04:30 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279123) | [7s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279123) | [7s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279123) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279125) | [6s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279125) | [6s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279125) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279191) | [4s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279191) | [4s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279191) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279103) | [4s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279103) | [4s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279103) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279210) | [4s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279210) | [4s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279210) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/35416725134/job/106012960458) | [4s](https://github.com/iree-org/iree/actions/runs/35416725134/job/106012960458) | [4s](https://github.com/iree-org/iree/actions/runs/35416725134/job/106012960458) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106055323466) | [3s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106055323466) | [3s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106055323466) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/35491151709/job/106026192122) | [3s](https://github.com/iree-org/iree/actions/runs/35491151709/job/106026192122) | [3s](https://github.com/iree-org/iree/actions/runs/35491151709/job/106026192122) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279127) | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279127) | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279127) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279085) | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279085) | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279085) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279100) | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279100) | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279100) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279094) | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279094) | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279094) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026257821) | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026257821) | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026257821) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279119) | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279119) | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279119) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279114) | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279114) | [2s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106026279114) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35502073745/job/106055496041) | [2s](https://github.com/iree-org/iree/actions/runs/35502073745/job/106055496041) | [2s](https://github.com/iree-org/iree/actions/runs/35502073745/job/106055496041) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055481141) | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055481141) | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055481141) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055339751) | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055339751) | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055339751) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 322 | 0% (1/322) |  | 20h04m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 359 | 1% (3/359) |  | 20h09m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 230 | 2% (4/230) |  | 2d14h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 17 | 12% (2/17) |  | 5d19h ago |

## Alerts

- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job observed waiting 20h52m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 20h52m (> 2h00m)
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
