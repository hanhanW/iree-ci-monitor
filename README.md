# iree-ci-monitor

_Updated: 2026-10-17 13:39 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39039415892/job/117415673820) | [3s](https://github.com/iree-org/iree/actions/runs/39039415452/job/117415713612) | — | 6 |
| `ubuntu-24.04` | github-hosted | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377904575) | [2s](https://github.com/iree-org/iree/actions/runs/39039091662/job/117414739062) | 0% (0/3) | 7 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39039415452/job/117415673224) | [3s](https://github.com/iree-org/iree/actions/runs/39039415452/job/117415673224) | [3s](https://github.com/iree-org/iree/actions/runs/39039415452/job/117415673224) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39039415452/job/117415713612) | [3s](https://github.com/iree-org/iree/actions/runs/39039415452/job/117415713612) | [3s](https://github.com/iree-org/iree/actions/runs/39039415452/job/117415713612) | 1 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/39032559749/job/117395811815) | [2s](https://github.com/iree-org/iree/actions/runs/39029694124/job/117387496744) | [2s](https://github.com/iree-org/iree/actions/runs/39029694124/job/117387496744) | 2 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39026329531/job/117377925622) | [2s](https://github.com/iree-org/iree/actions/runs/39039091662/job/117414739062) | [2s](https://github.com/iree-org/iree/actions/runs/39039091662/job/117414739062) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117377688428) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117377688428) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117377688428) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377904575) | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377904575) | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377904575) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377705328) | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377705328) | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377705328) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39039415892/job/117415673863) | [2s](https://github.com/iree-org/iree/actions/runs/39039415892/job/117415673863) | [2s](https://github.com/iree-org/iree/actions/runs/39039415892/job/117415673863) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39039415892/job/117415673707) | [2s](https://github.com/iree-org/iree/actions/runs/39039415892/job/117415673707) | [2s](https://github.com/iree-org/iree/actions/runs/39039415892/job/117415673707) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39039415892/job/117415673820) | [2s](https://github.com/iree-org/iree/actions/runs/39039415892/job/117415673820) | [2s](https://github.com/iree-org/iree/actions/runs/39039415892/job/117415673820) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39039415452/job/117415713644) | [2s](https://github.com/iree-org/iree/actions/runs/39039415452/job/117415713644) | [2s](https://github.com/iree-org/iree/actions/runs/39039415452/job/117415713644) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 261 | 4% (11/261) |  | 1d04h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 212 | 1% (2/212) |  | 1d04h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
