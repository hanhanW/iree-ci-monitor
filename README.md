# iree-ci-monitor

_Updated: 2026-10-04 14:33 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37213420647/job/111469005821) | [4s](https://github.com/iree-org/iree/actions/runs/37213420196/job/111469042561) | — | 6 |
| `ubuntu-24.04` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111440452305) | [3s](https://github.com/iree-org/iree/actions/runs/37213000927/job/111467781779) | 0% (0/1) | 3 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/37213420196/job/111469042561) | [4s](https://github.com/iree-org/iree/actions/runs/37213420196/job/111469042561) | [4s](https://github.com/iree-org/iree/actions/runs/37213420196/job/111469042561) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37213000927/job/111467781779) | [3s](https://github.com/iree-org/iree/actions/runs/37213000927/job/111467781779) | [3s](https://github.com/iree-org/iree/actions/runs/37213000927/job/111467781779) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37213420647/job/111469005796) | [3s](https://github.com/iree-org/iree/actions/runs/37213420647/job/111469005796) | [3s](https://github.com/iree-org/iree/actions/runs/37213420647/job/111469005796) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37213420196/job/111469004516) | [3s](https://github.com/iree-org/iree/actions/runs/37213420196/job/111469004516) | [3s](https://github.com/iree-org/iree/actions/runs/37213420196/job/111469004516) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111440452305) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111440452305) | [2s](https://github.com/iree-org/iree/actions/runs/37184292035/job/111440452305) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111523208388) | [2s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111523208388) | [2s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111523208388) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37213420647/job/111469005653) | [2s](https://github.com/iree-org/iree/actions/runs/37213420647/job/111469005653) | [2s](https://github.com/iree-org/iree/actions/runs/37213420647/job/111469005653) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37213420647/job/111469005821) | [2s](https://github.com/iree-org/iree/actions/runs/37213420647/job/111469005821) | [2s](https://github.com/iree-org/iree/actions/runs/37213420647/job/111469005821) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37213420196/job/111469042625) | [2s](https://github.com/iree-org/iree/actions/runs/37213420196/job/111469042625) | [2s](https://github.com/iree-org/iree/actions/runs/37213420196/job/111469042625) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 296 | 1% (4/296) |  | 1d00h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 206 | 1% (2/206) |  | 4d01h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
