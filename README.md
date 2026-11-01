# iree-ci-monitor

_Updated: 2026-11-01 14:06 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/41311804331/job/124863563652) | [3s](https://github.com/iree-org/iree/actions/runs/41311804331/job/124863563644) | 0% (0/3) | 3 |
| `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/41338183346/job/124942374449) | [2s](https://github.com/iree-org/iree/actions/runs/41338183346/job/124942374449) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/41311804331/job/124863563644) | [3s](https://github.com/iree-org/iree/actions/runs/41311804331/job/124863563644) | [3s](https://github.com/iree-org/iree/actions/runs/41311804331/job/124863563644) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41338183346/job/124942374449) | [2s](https://github.com/iree-org/iree/actions/runs/41338183346/job/124942374449) | [2s](https://github.com/iree-org/iree/actions/runs/41338183346/job/124942374449) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41311804331/job/124863563359) | [2s](https://github.com/iree-org/iree/actions/runs/41311804331/job/124863563359) | [2s](https://github.com/iree-org/iree/actions/runs/41311804331/job/124863563359) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41311804331/job/124863563652) | [2s](https://github.com/iree-org/iree/actions/runs/41311804331/job/124863563652) | [2s](https://github.com/iree-org/iree/actions/runs/41311804331/job/124863563652) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 238 | 3% (7/238) |  | 12h38m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 282 | 3% (8/282) |  | 12h40m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
