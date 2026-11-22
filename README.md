# iree-ci-monitor

_Updated: 2026-11-22 11:45 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45030594539/job/137233102803) | [3s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137185120159) | 0% (0/1) | 2 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45028099309/job/137225431245) | [2s](https://github.com/iree-org/iree/actions/runs/45031143272/job/137234797208) | 0% (0/3) | 9 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137185120159) | [3s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137185120159) | [3s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137185120159) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/45031143272/job/137234797000) | [2s](https://github.com/iree-org/iree/actions/runs/45028099309/job/137225430987) | [2s](https://github.com/iree-org/iree/actions/runs/45028099309/job/137225430987) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/45031143272/job/137234797191) | [2s](https://github.com/iree-org/iree/actions/runs/45028099309/job/137225431245) | [2s](https://github.com/iree-org/iree/actions/runs/45028099309/job/137225431245) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45028099309/job/137225431294) | [2s](https://github.com/iree-org/iree/actions/runs/45031143272/job/137234797208) | [2s](https://github.com/iree-org/iree/actions/runs/45031143272/job/137234797208) | 2 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45030594539/job/137233102803) | [2s](https://github.com/iree-org/iree/actions/runs/45030594539/job/137233102803) | [2s](https://github.com/iree-org/iree/actions/runs/45030594539/job/137233102803) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45031143117/job/137234796728) | [2s](https://github.com/iree-org/iree/actions/runs/45031143117/job/137234796728) | [2s](https://github.com/iree-org/iree/actions/runs/45031143117/job/137234796728) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45031143117/job/137234874308) | [2s](https://github.com/iree-org/iree/actions/runs/45031143117/job/137234874308) | [2s](https://github.com/iree-org/iree/actions/runs/45031143117/job/137234874308) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/45031143117/job/137234874321) | [1s](https://github.com/iree-org/iree/actions/runs/45031143117/job/137234874321) | [1s](https://github.com/iree-org/iree/actions/runs/45031143117/job/137234874321) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 151 | 3% (5/151) |  | 1d23h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 114 | 3% (3/114) |  | 1d23h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
