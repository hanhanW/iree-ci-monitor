# iree-ci-monitor

_Updated: 2026-09-26 14:14 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36247201986/job/108418481995) | [2s](https://github.com/iree-org/iree/actions/runs/36247201986/job/108418481995) | 0% (0/1) | 1 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419476940) | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445581) | — | 6 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36247201986/job/108418481995) | [2s](https://github.com/iree-org/iree/actions/runs/36247201986/job/108418481995) | [2s](https://github.com/iree-org/iree/actions/runs/36247201986/job/108418481995) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445557) | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445557) | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445557) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445519) | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445519) | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445519) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445581) | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445581) | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445581) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419445977) | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419445977) | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419445977) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419476826) | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419476826) | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419476826) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419476940) | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419476940) | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419476940) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | 0s | 0s | 0s | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 307 | 2% (5/307) |  | 1d03h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 230 | 4% (10/230) |  | 1d03h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
