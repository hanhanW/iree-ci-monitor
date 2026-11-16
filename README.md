# iree-ci-monitor

_Updated: 2026-11-15 22:38 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150520) | [4s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150712) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150513) | [3s](https://github.com/iree-org/iree/actions/runs/43802990869/job/133089513963) | 0% (0/4) | 9 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150561) | [3s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150582) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150576) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150616) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150712) | [4s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150712) | [4s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150712) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150520) | [4s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150520) | [4s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150520) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150542) | [3s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150542) | [3s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150542) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150582) | [3s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150582) | [3s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150582) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/43802990869/job/133089513963) | [3s](https://github.com/iree-org/iree/actions/runs/43802990869/job/133089513963) | [3s](https://github.com/iree-org/iree/actions/runs/43802990869/job/133089513963) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150528) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150528) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150528) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150513) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150513) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150513) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150578) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150578) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150578) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150591) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150591) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150591) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150561) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150561) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150561) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105080672) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105080672) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105080672) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150576) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150576) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150576) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150616) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150616) | [2s](https://github.com/iree-org/iree/actions/runs/43808634238/job/133105150616) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43808567085/job/133104863019) | [2s](https://github.com/iree-org/iree/actions/runs/43808567085/job/133104863019) | [2s](https://github.com/iree-org/iree/actions/runs/43808567085/job/133104863019) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/43802990869/job/133087300268) | [1s](https://github.com/iree-org/iree/actions/runs/43802990869/job/133087300268) | [1s](https://github.com/iree-org/iree/actions/runs/43802990869/job/133087300268) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/43802990869/job/133087300701) | [1s](https://github.com/iree-org/iree/actions/runs/43802990869/job/133087300701) | [1s](https://github.com/iree-org/iree/actions/runs/43802990869/job/133087300701) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 346 | 1% (3/346) |  | 1d01h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 404 | 0% (2/404) |  | 1d01h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
