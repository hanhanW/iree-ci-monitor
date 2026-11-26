# iree-ci-monitor

_Updated: 2026-11-26 00:28 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226819) | [9s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226638) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45759810862/job/139706907377) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226592) | 0% (0/4) | 9 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226569) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226632) | — | 2 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226610) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226641) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226638) | [9s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226638) | [9s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226638) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226556) | [4s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226556) | [4s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226556) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226819) | [4s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226819) | [4s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226819) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226525) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226525) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226525) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226592) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226592) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226592) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226551) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226551) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226551) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226641) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226641) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226641) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226610) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226610) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226610) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707152883) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707152883) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707152883) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226632) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226632) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226632) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226569) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226569) | [2s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226569) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45753989077/job/139688177209) | [2s](https://github.com/iree-org/iree/actions/runs/45753989077/job/139688177209) | [2s](https://github.com/iree-org/iree/actions/runs/45753989077/job/139688177209) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45753989077/job/139688177070) | [2s](https://github.com/iree-org/iree/actions/runs/45753989077/job/139688177070) | [2s](https://github.com/iree-org/iree/actions/runs/45753989077/job/139688177070) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45753989077/job/139691288298) | [2s](https://github.com/iree-org/iree/actions/runs/45753989077/job/139691288298) | [2s](https://github.com/iree-org/iree/actions/runs/45753989077/job/139691288298) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45759810862/job/139706907377) | [2s](https://github.com/iree-org/iree/actions/runs/45759810862/job/139706907377) | [2s](https://github.com/iree-org/iree/actions/runs/45759810862/job/139706907377) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226530) | [1s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226530) | [1s](https://github.com/iree-org/iree/actions/runs/45759886035/job/139707226530) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 77 | 6% (5/77) |  | 22h35m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 55 | 13% (7/55) |  | 22h42m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
