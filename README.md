# iree-ci-monitor

_Updated: 2026-10-04 22:47 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187668) | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187670) | — | 2 |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187564) | [4s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111616357388) | 0% (0/4) | 10 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187620) | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187648) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187659) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187742) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187670) | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187670) | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187670) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187668) | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187668) | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187668) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187620) | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187620) | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187620) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187648) | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187648) | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187648) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187582) | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187582) | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187582) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111616357388) | [4s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111616357388) | [4s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111616357388) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111618270081) | [3s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111618270081) | [3s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111618270081) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187564) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187564) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187564) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187680) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187680) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187680) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187596) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187596) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187596) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187656) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187656) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187656) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629145544) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629145544) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629145544) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187659) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187659) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187659) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187742) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187742) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187742) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111523208388) | [2s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111523208388) | [2s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111523208388) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111616357217) | [2s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111616357217) | [2s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111616357217) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37268057383/job/111628965884) | [2s](https://github.com/iree-org/iree/actions/runs/37268057383/job/111628965884) | [2s](https://github.com/iree-org/iree/actions/runs/37268057383/job/111628965884) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 296 | 1% (4/296) |  | 1d09h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 206 | 1% (2/206) |  | 4d09h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
