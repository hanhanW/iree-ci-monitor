# iree-ci-monitor

_Updated: 2026-10-11 05:57 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `macos-15` | github-hosted | 2 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897633) | [9s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897658) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897627) | [6s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897699) | — | 3 |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897563) | [2s](https://github.com/iree-org/iree/actions/runs/38129355536/job/114440264044) | 0% (0/1) | 11 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897572) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897626) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897633) | [9s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897633) | [9s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897633) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897658) | [9s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897658) | [9s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897658) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897699) | [6s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897699) | [6s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897699) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897627) | [4s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897627) | [4s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897627) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897621) | [4s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897621) | [4s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897621) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114439956905) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114439956905) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114439956905) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897625) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897625) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897625) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897550) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897550) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897550) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897563) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897563) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897563) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897561) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897561) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897561) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395864604) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395864604) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395864604) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897626) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897626) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897626) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897572) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897572) | [2s](https://github.com/iree-org/iree/actions/runs/38114249817/job/114395897572) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38129355536/job/114440264044) | [2s](https://github.com/iree-org/iree/actions/runs/38129355536/job/114440264044) | [2s](https://github.com/iree-org/iree/actions/runs/38129355536/job/114440264044) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38126915784/job/114433082849) | [2s](https://github.com/iree-org/iree/actions/runs/38126915784/job/114433082849) | [2s](https://github.com/iree-org/iree/actions/runs/38126915784/job/114433082849) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38114217186/job/114395765000) | [2s](https://github.com/iree-org/iree/actions/runs/38114217186/job/114395765000) | [2s](https://github.com/iree-org/iree/actions/runs/38114217186/job/114395765000) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38129255637/job/114439975115) | [2s](https://github.com/iree-org/iree/actions/runs/38129255637/job/114439975115) | [2s](https://github.com/iree-org/iree/actions/runs/38129255637/job/114439975115) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/38129255637/job/114440243812) | [1s](https://github.com/iree-org/iree/actions/runs/38129255637/job/114440243812) | [1s](https://github.com/iree-org/iree/actions/runs/38129255637/job/114440243812) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 219 | 15% (33/219) |  | 1d20h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 297 | 0% (0/297) |  | 1d20h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
