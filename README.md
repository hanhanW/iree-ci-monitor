# iree-ci-monitor

_Updated: 2026-06-27 05:46 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369806) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369808) | — | 3 |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369813) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83816303965) | 0% (0/1) | 10 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28288606734/job/83816692581) | [3s](https://github.com/iree-org/iree/actions/runs/28288606832/job/83816683747) | — | 6 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369809) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369894) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369815) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369816) | — | 2 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 3 | 3 | [18h28m](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447477) | 2026-06-27 05:46 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [18h28m](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447477) | 2026-06-27 05:46 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/scalable_distribution_tiling` | pull_request |
| [18h27m](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677804) | 2026-06-27 05:46 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/scalable_vector_level_tiling` | pull_request |
| [18h25m](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722939709) | 2026-06-27 05:46 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/overload_iree_tiling_interface_ops` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 3 | 3 | [18h28m](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447477) | 2026-06-27 05:46 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369808) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369808) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369808) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369803) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369803) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369803) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369806) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369806) | [5s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369806) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83816303965) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83816303965) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83816303965) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369820) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369820) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369820) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796353903) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796353903) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796353903) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28288606832/job/83816683747) | [3s](https://github.com/iree-org/iree/actions/runs/28288606832/job/83816683747) | [3s](https://github.com/iree-org/iree/actions/runs/28288606832/job/83816683747) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369813) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369813) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369813) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369815) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369815) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369815) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369816) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369816) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369816) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369894) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369894) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369894) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369809) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369809) | [2s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83796369809) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28288489550/job/83816387516) | [2s](https://github.com/iree-org/iree/actions/runs/28288489550/job/83816387516) | [2s](https://github.com/iree-org/iree/actions/runs/28288489550/job/83816387516) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28280892242/job/83796313502) | [2s](https://github.com/iree-org/iree/actions/runs/28280892242/job/83796313502) | [2s](https://github.com/iree-org/iree/actions/runs/28280892242/job/83796313502) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28288458973/job/83816310448) | [2s](https://github.com/iree-org/iree/actions/runs/28288458973/job/83816310448) | [2s](https://github.com/iree-org/iree/actions/runs/28288458973/job/83816310448) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28288606832/job/83816683748) | [2s](https://github.com/iree-org/iree/actions/runs/28288606832/job/83816683748) | [2s](https://github.com/iree-org/iree/actions/runs/28288606832/job/83816683748) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28288606832/job/83816683755) | [2s](https://github.com/iree-org/iree/actions/runs/28288606832/job/83816683755) | [2s](https://github.com/iree-org/iree/actions/runs/28288606832/job/83816683755) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28288606734/job/83816692575) | [2s](https://github.com/iree-org/iree/actions/runs/28288606734/job/83816692575) | [2s](https://github.com/iree-org/iree/actions/runs/28288606734/job/83816692575) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28288606734/job/83816692581) | [2s](https://github.com/iree-org/iree/actions/runs/28288606734/job/83816692581) | [2s](https://github.com/iree-org/iree/actions/runs/28288606734/job/83816692581) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 119 | 0% (0/119) |  | 17h36m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 95 | 8% (8/95) |  | 17h46m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 91 | 0% (0/91) |  | 17h48m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 85 | 0% (0/85) |  | 17h49m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 26 | 0% (0/26) |  | 17h57m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 18h28m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
