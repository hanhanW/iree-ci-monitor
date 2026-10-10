# iree-ci-monitor

_Updated: 2026-10-09 22:58 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [5s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584318) | [6s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584358) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584349) | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584392) | — | 3 |
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584351) | [3s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584338) | 0% (0/1) | 6 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584321) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584342) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584358) | [6s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584358) | [6s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584358) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584318) | [5s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584318) | [5s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584318) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584392) | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584392) | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584392) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584313) | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584313) | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584313) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584349) | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584349) | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584349) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584317) | [3s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584317) | [3s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584317) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584338) | [3s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584338) | [3s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584338) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584351) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584351) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584351) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584384) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584384) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584384) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139554475) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139554475) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139554475) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584321) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584321) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584321) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584342) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584342) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584342) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38026862940/job/114139437254) | [2s](https://github.com/iree-org/iree/actions/runs/38026862940/job/114139437254) | [2s](https://github.com/iree-org/iree/actions/runs/38026862940/job/114139437254) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 219 | 15% (33/219) |  | 13h43m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 325 | 0% (0/325) |  | 13h48m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
