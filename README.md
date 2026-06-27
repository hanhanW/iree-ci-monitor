# iree-ci-monitor

_Updated: 2026-06-27 00:24 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369806) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369808) | — | 3 |
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/28280892242/job/83796313502) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369820) | 0% (0/1) | 6 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369809) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369894) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369815) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369816) | — | 2 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 3 | 3 | [13h06m](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447477) | 2026-06-27 00:24 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [13h06m](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447477) | 2026-06-27 00:24 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/scalable_distribution_tiling` | pull_request |
| [13h05m](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677804) | 2026-06-27 00:24 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/scalable_vector_level_tiling` | pull_request |
| [13h03m](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722939709) | 2026-06-27 00:24 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/overload_iree_tiling_interface_ops` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 3 | 3 | [13h06m](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447477) | 2026-06-27 00:24 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369808) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369808) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369808) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369803) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369803) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369803) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369806) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369806) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369806) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369820) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369820) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369820) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796353903) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796353903) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796353903) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369813) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369813) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369813) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369815) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369815) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369815) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369816) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369816) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369816) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369894) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369894) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369894) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369809) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369809) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369809) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28280892242/job/83796313502) | [2s](https://github.com/iree-org/iree/actions/runs/28280892242/job/83796313502) | [2s](https://github.com/iree-org/iree/actions/runs/28280892242/job/83796313502) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369818) | [1s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369818) | [1s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369818) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369819) | [1s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369819) | [1s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369819) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 119 | 0% (0/119) |  | 12h14m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 95 | 8% (8/95) |  | 12h24m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 91 | 0% (0/91) |  | 12h26m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 85 | 0% (0/85) |  | 12h27m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 26 | 0% (0/26) |  | 12h35m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 13h06m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
