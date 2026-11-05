# iree-ci-monitor

_Updated: 2026-11-04 22:55 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220610) | [6s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220678) | — | 3 |
| `ubuntu-24.04` | github-hosted | 20 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/41966570817/job/127044842030) | [3s](https://github.com/iree-org/iree/actions/runs/41865135135/job/127014887818) | 0% (0/6) | 20 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220675) | [3s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220700) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220633) | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220696) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220678) | [6s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220678) | [6s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220678) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220587) | [5s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220587) | [5s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220587) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220610) | [5s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220610) | [5s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220610) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41848495501/job/126952012085) | [3s](https://github.com/iree-org/iree/actions/runs/41865135135/job/127014887818) | [3s](https://github.com/iree-org/iree/actions/runs/41865135135/job/127014887818) | 11 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220602) | [3s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220602) | [3s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220602) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220675) | [3s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220675) | [3s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220675) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220700) | [3s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220700) | [3s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220700) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220688) | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220688) | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220688) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220604) | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220604) | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220604) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220703) | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220703) | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220703) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220696) | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220696) | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220696) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220633) | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220633) | [2s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063220633) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41966570817/job/127044842030) | [2s](https://github.com/iree-org/iree/actions/runs/41966570817/job/127044842030) | [2s](https://github.com/iree-org/iree/actions/runs/41966570817/job/127044842030) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41966570817/job/127044842164) | [2s](https://github.com/iree-org/iree/actions/runs/41966570817/job/127044842164) | [2s](https://github.com/iree-org/iree/actions/runs/41966570817/job/127044842164) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41966570817/job/127048111826) | [2s](https://github.com/iree-org/iree/actions/runs/41966570817/job/127048111826) | [2s](https://github.com/iree-org/iree/actions/runs/41966570817/job/127048111826) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41972225530/job/127062882711) | [2s](https://github.com/iree-org/iree/actions/runs/41972225530/job/127062882711) | [2s](https://github.com/iree-org/iree/actions/runs/41972225530/job/127062882711) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063158528) | [1s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063158528) | [1s](https://github.com/iree-org/iree/actions/runs/41972315163/job/127063158528) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 386 | 1% (5/386) |  | 3h12m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 497 | 2% (8/497) |  | 12h15m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
