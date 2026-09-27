# iree-ci-monitor

_Updated: 2026-09-27 10:01 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36324826726/job/108635453973) | [10s](https://github.com/iree-org/iree/actions/runs/36322897450/job/108630032719) | 0% (0/3) | 9 |
| `ubuntu-24.04` | github-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/36324540304/job/108634634162) | [2s](https://github.com/iree-org/iree/actions/runs/36331572179/job/108654406260) | 0% (0/1) | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36324826726/job/108635453973) | [10s](https://github.com/iree-org/iree/actions/runs/36322897450/job/108630032719) | [10s](https://github.com/iree-org/iree/actions/runs/36322897450/job/108630032719) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/36324826646/job/108635479425) | [4s](https://github.com/iree-org/iree/actions/runs/36324826646/job/108635479425) | [4s](https://github.com/iree-org/iree/actions/runs/36324826646/job/108635479425) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36322897450/job/108630032552) | [2s](https://github.com/iree-org/iree/actions/runs/36324826726/job/108635454078) | [2s](https://github.com/iree-org/iree/actions/runs/36324826726/job/108635454078) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36322897450/job/108630032718) | [2s](https://github.com/iree-org/iree/actions/runs/36324826726/job/108635454090) | [2s](https://github.com/iree-org/iree/actions/runs/36324826726/job/108635454090) | 2 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36331572179/job/108654406260) | [2s](https://github.com/iree-org/iree/actions/runs/36331572179/job/108654406260) | [2s](https://github.com/iree-org/iree/actions/runs/36331572179/job/108654406260) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36324826646/job/108635453340) | [2s](https://github.com/iree-org/iree/actions/runs/36324826646/job/108635453340) | [2s](https://github.com/iree-org/iree/actions/runs/36324826646/job/108635453340) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36324826646/job/108635479364) | [2s](https://github.com/iree-org/iree/actions/runs/36324826646/job/108635479364) | [2s](https://github.com/iree-org/iree/actions/runs/36324826646/job/108635479364) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/36324540304/job/108634634162) | [1s](https://github.com/iree-org/iree/actions/runs/36324540304/job/108634634162) | [1s](https://github.com/iree-org/iree/actions/runs/36324540304/job/108634634162) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | 0s | 0s | 0s | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 296 | 2% (5/296) |  | 1d22h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 219 | 5% (10/219) |  | 1d23h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
