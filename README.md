# iree-ci-monitor

_Updated: 2026-09-27 22:29 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495779) | [9s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495761) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495860) | [5s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495874) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/36381261957/job/108797320414) | [3s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495829) | 0% (0/4) | 9 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495794) | [3s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495769) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495761) | [9s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495761) | [9s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495761) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495779) | [8s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495779) | [8s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495779) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495874) | [5s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495874) | [5s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495874) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495856) | [5s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495856) | [5s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495856) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495860) | [5s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495860) | [5s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495860) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495829) | [3s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495829) | [3s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495829) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495769) | [3s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495769) | [3s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495769) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495757) | [2s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495757) | [2s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495757) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495818) | [2s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495818) | [2s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495818) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495934) | [2s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495934) | [2s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495934) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495794) | [2s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495794) | [2s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495794) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36377816278/job/108787152169) | [2s](https://github.com/iree-org/iree/actions/runs/36377816278/job/108787152169) | [2s](https://github.com/iree-org/iree/actions/runs/36377816278/job/108787152169) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36377816278/job/108787152358) | [2s](https://github.com/iree-org/iree/actions/runs/36377816278/job/108787152358) | [2s](https://github.com/iree-org/iree/actions/runs/36377816278/job/108787152358) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36377816278/job/108788823605) | [2s](https://github.com/iree-org/iree/actions/runs/36377816278/job/108788823605) | [2s](https://github.com/iree-org/iree/actions/runs/36377816278/job/108788823605) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36381261957/job/108797320414) | [2s](https://github.com/iree-org/iree/actions/runs/36381261957/job/108797320414) | [2s](https://github.com/iree-org/iree/actions/runs/36381261957/job/108797320414) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797457978) | [1s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797457978) | [1s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797457978) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 296 | 2% (5/296) |  | 2d11h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 219 | 5% (10/219) |  | 2d11h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
