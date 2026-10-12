# iree-ci-monitor

_Updated: 2026-10-11 23:04 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [7s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881336) | [10s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881476) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881297) | [4s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881305) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881368) | [3s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881467) | — | 2 |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/38207682829/job/114674699705) | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881409) | 0% (0/5) | 10 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881476) | [10s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881476) | [10s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881476) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881336) | [7s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881336) | [7s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881336) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881305) | [4s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881305) | [4s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881305) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881293) | [4s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881293) | [4s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881293) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881297) | [4s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881297) | [4s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881297) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881467) | [3s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881467) | [3s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881467) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881347) | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881347) | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881347) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881367) | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881367) | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881367) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881365) | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881365) | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881365) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881409) | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881409) | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881409) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674844406) | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674844406) | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674844406) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881368) | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881368) | [2s](https://github.com/iree-org/iree/actions/runs/38207729117/job/114674881368) | 1 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38185395840/job/114606509433) | [2s](https://github.com/iree-org/iree/actions/runs/38185395840/job/114606509433) | [2s](https://github.com/iree-org/iree/actions/runs/38185395840/job/114606509433) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38204202298/job/114663957704) | [2s](https://github.com/iree-org/iree/actions/runs/38204202298/job/114663957704) | [2s](https://github.com/iree-org/iree/actions/runs/38204202298/job/114663957704) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38207682829/job/114674699705) | [2s](https://github.com/iree-org/iree/actions/runs/38207682829/job/114674699705) | [2s](https://github.com/iree-org/iree/actions/runs/38207682829/job/114674699705) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/38204202298/job/114663957862) | [1s](https://github.com/iree-org/iree/actions/runs/38204202298/job/114663957862) | [1s](https://github.com/iree-org/iree/actions/runs/38204202298/job/114663957862) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/38204202298/job/114665419749) | [1s](https://github.com/iree-org/iree/actions/runs/38204202298/job/114665419749) | [1s](https://github.com/iree-org/iree/actions/runs/38204202298/job/114665419749) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 219 | 15% (33/219) |  | 2d13h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 297 | 0% (0/297) |  | 2d13h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
