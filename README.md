# iree-ci-monitor

_Updated: 2026-10-18 04:14 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `macos-15` | github-hosted | 2 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694614) | [7s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694588) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694584) | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694636) | — | 3 |
| `ubuntu-24.04` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694620) | [2s](https://github.com/iree-org/iree/actions/runs/39122038036/job/117659416281) | 0% (0/1) | 15 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39107612288/job/117616756233) | [2s](https://github.com/iree-org/iree/actions/runs/39107612288/job/117616756260) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694637) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694652) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694588) | [7s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694588) | [7s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694588) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694614) | [5s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694614) | [5s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694614) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694636) | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694636) | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694636) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694550) | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694550) | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694550) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694584) | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694584) | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694584) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39107614557/job/117616799835) | [3s](https://github.com/iree-org/iree/actions/runs/39107614557/job/117616799835) | [3s](https://github.com/iree-org/iree/actions/runs/39107614557/job/117616799835) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694580) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694580) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694580) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694620) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694620) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694620) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694586) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694586) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694586) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694587) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694587) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694587) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593665274) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593665274) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593665274) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694652) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694652) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694652) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694637) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694637) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694637) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39107614566/job/117616803338) | [2s](https://github.com/iree-org/iree/actions/runs/39107614566/job/117616803338) | [2s](https://github.com/iree-org/iree/actions/runs/39107614566/job/117616803338) | 1 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39107614566/job/117616761827) | [2s](https://github.com/iree-org/iree/actions/runs/39107614566/job/117616761827) | [2s](https://github.com/iree-org/iree/actions/runs/39107614566/job/117616761827) | 1 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39107614557/job/117616761670) | [2s](https://github.com/iree-org/iree/actions/runs/39107614557/job/117616761670) | [2s](https://github.com/iree-org/iree/actions/runs/39107614557/job/117616761670) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39122038036/job/117659416281) | [2s](https://github.com/iree-org/iree/actions/runs/39122038036/job/117659416281) | [2s](https://github.com/iree-org/iree/actions/runs/39122038036/job/117659416281) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39099797306/job/117593542213) | [2s](https://github.com/iree-org/iree/actions/runs/39099797306/job/117593542213) | [2s](https://github.com/iree-org/iree/actions/runs/39099797306/job/117593542213) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39121971417/job/117659394540) | [2s](https://github.com/iree-org/iree/actions/runs/39121971417/job/117659394540) | [2s](https://github.com/iree-org/iree/actions/runs/39121971417/job/117659394540) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39121971417/job/117659229578) | [2s](https://github.com/iree-org/iree/actions/runs/39121971417/job/117659229578) | [2s](https://github.com/iree-org/iree/actions/runs/39121971417/job/117659229578) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 261 | 4% (11/261) |  | 1d18h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 212 | 1% (2/212) |  | 1d18h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
