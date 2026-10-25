# iree-ci-monitor

_Updated: 2026-10-25 04:38 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604410) | [6s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604260) | — | 3 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604298) | [3s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604314) | — | 2 |
| `ubuntu-24.04` | github-hosted | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604257) | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604318) | 0% (0/1) | 6 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604269) | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604309) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604260) | [6s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604260) | [6s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604260) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604396) | [4s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604396) | [4s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604396) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604410) | [4s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604410) | [4s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604410) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604298) | [3s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604298) | [3s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604298) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604314) | [3s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604314) | [3s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604314) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604275) | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604275) | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604275) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604307) | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604307) | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604307) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604257) | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604257) | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604257) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604318) | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604318) | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604318) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083565719) | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083565719) | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083565719) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604309) | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604309) | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604309) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604269) | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604269) | [2s](https://github.com/iree-org/iree/actions/runs/40164804998/job/121083604269) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40164762624/job/121083438484) | [2s](https://github.com/iree-org/iree/actions/runs/40164762624/job/121083438484) | [2s](https://github.com/iree-org/iree/actions/runs/40164762624/job/121083438484) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | 0s | 0s | 0s | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 408 | 0% (0/408) |  | 14h59m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 338 | 2% (7/338) |  | 15h34m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
