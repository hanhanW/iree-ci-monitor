# iree-ci-monitor

_Updated: 2026-11-21 11:22 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/44912240980/job/136870310899) | [4s](https://github.com/iree-org/iree/actions/runs/44912239929/job/136870357355) | — | 6 |
| `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/44869538505/job/136816349416) | [2s](https://github.com/iree-org/iree/actions/runs/44911834657/job/136869090542) | 0% (0/1) | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44912239929/job/136870357355) | [4s](https://github.com/iree-org/iree/actions/runs/44912239929/job/136870357355) | [4s](https://github.com/iree-org/iree/actions/runs/44912239929/job/136870357355) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44911834657/job/136869090542) | [2s](https://github.com/iree-org/iree/actions/runs/44911834657/job/136869090542) | [2s](https://github.com/iree-org/iree/actions/runs/44911834657/job/136869090542) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44912240980/job/136870310899) | [2s](https://github.com/iree-org/iree/actions/runs/44912240980/job/136870310899) | [2s](https://github.com/iree-org/iree/actions/runs/44912240980/job/136870310899) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44912240980/job/136870311091) | [2s](https://github.com/iree-org/iree/actions/runs/44912240980/job/136870311091) | [2s](https://github.com/iree-org/iree/actions/runs/44912240980/job/136870311091) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44912240980/job/136870311069) | [2s](https://github.com/iree-org/iree/actions/runs/44912240980/job/136870311069) | [2s](https://github.com/iree-org/iree/actions/runs/44912240980/job/136870311069) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44912239929/job/136870306892) | [2s](https://github.com/iree-org/iree/actions/runs/44912239929/job/136870306892) | [2s](https://github.com/iree-org/iree/actions/runs/44912239929/job/136870306892) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44912239929/job/136870357415) | [2s](https://github.com/iree-org/iree/actions/runs/44912239929/job/136870357415) | [2s](https://github.com/iree-org/iree/actions/runs/44912239929/job/136870357415) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/44869538505/job/136816349416) | [1s](https://github.com/iree-org/iree/actions/runs/44869538505/job/136816349416) | [1s](https://github.com/iree-org/iree/actions/runs/44869538505/job/136816349416) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 162 | 3% (5/162) |  | 23h22m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 125 | 2% (3/125) |  | 23h34m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
