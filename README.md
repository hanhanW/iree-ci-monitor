# iree-ci-monitor

_Updated: 2026-10-24 09:00 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40101209105/job/120893560192) | [3s](https://github.com/iree-org/iree/actions/runs/40101209752/job/120893602154) | — | 9 |
| `ubuntu-24.04` | github-hosted | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40070314099/job/120802139414) | [3s](https://github.com/iree-org/iree/actions/runs/40070351503/job/120802253712) | 0% (0/2) | 7 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40070351503/job/120802253712) | [3s](https://github.com/iree-org/iree/actions/runs/40070351503/job/120802253712) | [3s](https://github.com/iree-org/iree/actions/runs/40070351503/job/120802253712) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40101209752/job/120893602154) | [3s](https://github.com/iree-org/iree/actions/runs/40101209752/job/120893602154) | [3s](https://github.com/iree-org/iree/actions/runs/40101209752/job/120893602154) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/40088123660/job/120855108969) | [2s](https://github.com/iree-org/iree/actions/runs/40100790735/job/120892330309) | [2s](https://github.com/iree-org/iree/actions/runs/40100790735/job/120892330309) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40088167470/job/120855233590) | [2s](https://github.com/iree-org/iree/actions/runs/40101209105/job/120893560228) | [2s](https://github.com/iree-org/iree/actions/runs/40101209105/job/120893560228) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40088167470/job/120855233606) | [2s](https://github.com/iree-org/iree/actions/runs/40101209105/job/120893560192) | [2s](https://github.com/iree-org/iree/actions/runs/40101209105/job/120893560192) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40088167470/job/120855233352) | [2s](https://github.com/iree-org/iree/actions/runs/40101209105/job/120893559929) | [2s](https://github.com/iree-org/iree/actions/runs/40101209105/job/120893559929) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120854879545) | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120854879545) | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120854879545) | 1 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40070314099/job/120802139414) | [2s](https://github.com/iree-org/iree/actions/runs/40070314099/job/120802139414) | [2s](https://github.com/iree-org/iree/actions/runs/40070314099/job/120802139414) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40088049884/job/120855090089) | [2s](https://github.com/iree-org/iree/actions/runs/40088049884/job/120855090089) | [2s](https://github.com/iree-org/iree/actions/runs/40088049884/job/120855090089) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40101209752/job/120893562276) | [2s](https://github.com/iree-org/iree/actions/runs/40101209752/job/120893562276) | [2s](https://github.com/iree-org/iree/actions/runs/40101209752/job/120893562276) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40101209752/job/120893602172) | [2s](https://github.com/iree-org/iree/actions/runs/40101209752/job/120893602172) | [2s](https://github.com/iree-org/iree/actions/runs/40101209752/job/120893602172) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/40088049884/job/120854900425) | [1s](https://github.com/iree-org/iree/actions/runs/40088049884/job/120854900425) | [1s](https://github.com/iree-org/iree/actions/runs/40088049884/job/120854900425) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 402 | 0% (0/402) |  | 23h34m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 333 | 2% (7/333) |  | 23h41m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
