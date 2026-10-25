# iree-ci-monitor

_Updated: 2026-10-25 13:55 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40200871044/job/121191591022) | [3s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191625564) | 0% (0/3) | 9 |
| `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40200444630/job/121190298131) | [2s](https://github.com/iree-org/iree/actions/runs/40230273951/job/121280303351) | 0% (0/1) | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191625564) | [3s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191625564) | [3s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191625564) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40198120915/job/121183294019) | [2s](https://github.com/iree-org/iree/actions/runs/40200871044/job/121191591135) | [2s](https://github.com/iree-org/iree/actions/runs/40200871044/job/121191591135) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40198120915/job/121183294169) | [2s](https://github.com/iree-org/iree/actions/runs/40200871044/job/121191590940) | [2s](https://github.com/iree-org/iree/actions/runs/40200871044/job/121191590940) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40198120915/job/121183294159) | [2s](https://github.com/iree-org/iree/actions/runs/40200871044/job/121191591022) | [2s](https://github.com/iree-org/iree/actions/runs/40200871044/job/121191591022) | 2 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40200444630/job/121190298131) | [2s](https://github.com/iree-org/iree/actions/runs/40200444630/job/121190298131) | [2s](https://github.com/iree-org/iree/actions/runs/40200444630/job/121190298131) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40230273951/job/121280303351) | [2s](https://github.com/iree-org/iree/actions/runs/40230273951/job/121280303351) | [2s](https://github.com/iree-org/iree/actions/runs/40230273951/job/121280303351) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191590276) | [2s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191590276) | [2s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191590276) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191625591) | [2s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191625591) | [2s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191625591) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 408 | 0% (0/408) |  | 1d00h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 338 | 2% (7/338) |  | 1d00h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
