# iree-ci-monitor

_Updated: 2026-08-10 01:06 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 1 | [5s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958655) | [5s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958658) | — | 3 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958675) | [4s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958672) | — | 2 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363932672) | [3s](https://github.com/iree-org/iree/actions/runs/31356076232/job/93357119685) | 0% (0/4) | 9 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958656) | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958673) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958658) | [5s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958658) | [5s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958658) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958655) | [5s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958655) | [5s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958655) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958672) | [4s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958672) | [4s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958672) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31356076232/job/93357119685) | [3s](https://github.com/iree-org/iree/actions/runs/31356076232/job/93357119685) | [3s](https://github.com/iree-org/iree/actions/runs/31356076232/job/93357119685) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958665) | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958665) | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958665) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958663) | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958663) | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958663) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958679) | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958679) | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958679) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958718) | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958718) | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958718) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363932672) | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363932672) | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363932672) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958673) | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958673) | [2s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958673) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31356076232/job/93355906357) | [2s](https://github.com/iree-org/iree/actions/runs/31356076232/job/93355906357) | [2s](https://github.com/iree-org/iree/actions/runs/31356076232/job/93355906357) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31358947644/job/93363822211) | [2s](https://github.com/iree-org/iree/actions/runs/31358947644/job/93363822211) | [2s](https://github.com/iree-org/iree/actions/runs/31358947644/job/93363822211) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958647) | [1s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958647) | [1s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958647) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958675) | [1s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958675) | [1s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958675) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958656) | [1s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958656) | [1s](https://github.com/iree-org/iree/actions/runs/31358986334/job/93363958656) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31356076232/job/93355906420) | [1s](https://github.com/iree-org/iree/actions/runs/31356076232/job/93355906420) | [1s](https://github.com/iree-org/iree/actions/runs/31356076232/job/93355906420) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 3% (3/102) |  | 2d08h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 116 | 3% (4/116) |  | 2d14h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 131 | 0% (0/131) |  | 2d14h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 100 | 5% (5/100) |  | 2d14h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
