# iree-ci-monitor

_Updated: 2026-11-07 22:09 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928054) | [4s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928076) | — | 3 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928013) | [3s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928092) | — | 2 |
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928029) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928081) | 0% (0/1) | 6 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928015) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928062) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928076) | [4s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928076) | [4s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928076) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928054) | [4s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928054) | [4s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928054) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928004) | [4s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928004) | [4s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928004) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928092) | [3s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928092) | [3s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928092) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928035) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928035) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928035) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928038) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928038) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928038) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928081) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928081) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928081) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928029) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928029) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928029) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928013) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928013) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928013) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635890917) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635890917) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635890917) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928015) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928015) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928015) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928062) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928062) | [2s](https://github.com/iree-org/iree/actions/runs/42449636210/job/128635928062) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/42449595096/job/128635763294) | [1s](https://github.com/iree-org/iree/actions/runs/42449595096/job/128635763294) | [1s](https://github.com/iree-org/iree/actions/runs/42449595096/job/128635763294) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 506 | 1% (4/506) |  | 1d10h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 398 | 1% (3/398) |  | 1d12h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
