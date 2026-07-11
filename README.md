# iree-ci-monitor

_Updated: 2026-07-11 05:37 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674785) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674791) | — | 3 |
| `ubuntu-24.04` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29151269439/job/86541102903) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674776) | 50% (1/2) | 12 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674795) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674804) | — | 2 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29151452695/job/86541489547) | [3s](https://github.com/iree-org/iree/actions/runs/29151452917/job/86541490028) | — | 9 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674793) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674797) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674791) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674791) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674791) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674783) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674783) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674783) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674785) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674785) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674785) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29089345918/job/86529298845) | [3s](https://github.com/iree-org/iree/actions/runs/29083604698/job/86528350519) | [3s](https://github.com/iree-org/iree/actions/runs/29083604698/job/86528350519) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29151313641/job/86541155351) | [3s](https://github.com/iree-org/iree/actions/runs/29151452917/job/86541490021) | [3s](https://github.com/iree-org/iree/actions/runs/29151452917/job/86541490021) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29151313641/job/86541155347) | [3s](https://github.com/iree-org/iree/actions/runs/29151452917/job/86541490028) | [3s](https://github.com/iree-org/iree/actions/runs/29151452917/job/86541490028) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86541037472) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86541037472) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86541037472) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674776) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674776) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674776) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674774) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674774) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674774) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674804) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674804) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674804) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29151313641/job/86541155346) | [2s](https://github.com/iree-org/iree/actions/runs/29151452917/job/86541490024) | [2s](https://github.com/iree-org/iree/actions/runs/29151452917/job/86541490024) | 2 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674792) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674792) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674792) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674788) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674788) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674788) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516660522) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516660522) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516660522) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674797) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674797) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674797) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674793) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674793) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674793) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29151295806/job/86541110474) | [2s](https://github.com/iree-org/iree/actions/runs/29151295806/job/86541110474) | [2s](https://github.com/iree-org/iree/actions/runs/29151295806/job/86541110474) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29141922849/job/86516605989) | [2s](https://github.com/iree-org/iree/actions/runs/29141922849/job/86516605989) | [2s](https://github.com/iree-org/iree/actions/runs/29141922849/job/86516605989) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29151269439/job/86541102903) | [2s](https://github.com/iree-org/iree/actions/runs/29151269439/job/86541102903) | [2s](https://github.com/iree-org/iree/actions/runs/29151269439/job/86541102903) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29151269439/job/86541046853) | [2s](https://github.com/iree-org/iree/actions/runs/29151269439/job/86541046853) | [2s](https://github.com/iree-org/iree/actions/runs/29151269439/job/86541046853) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 159 | 7% (11/158) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 202 | 1% (3/201) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 162 | 1% (1/161) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 150 | 1% (1/149) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 47 | 11% (5/47) |  | 1d00h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
