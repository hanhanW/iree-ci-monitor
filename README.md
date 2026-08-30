# iree-ci-monitor

_Updated: 2026-08-30 09:44 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33308181530/job/99248355800) | [3s](https://github.com/iree-org/iree/actions/runs/33316065613/job/99269632977) | — | 12 |
| `ubuntu-24.04` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99247597510) | [2s](https://github.com/iree-org/iree/actions/runs/33307904893/job/99247710452) | 0% (0/1) | 5 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33308181783/job/99248338243) | [7s](https://github.com/iree-org/iree/actions/runs/33316065613/job/99269633069) | [7s](https://github.com/iree-org/iree/actions/runs/33316065613/job/99269633069) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33308181783/job/99248338121) | [3s](https://github.com/iree-org/iree/actions/runs/33316065613/job/99269632977) | [3s](https://github.com/iree-org/iree/actions/runs/33316065613/job/99269632977) | 2 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33308181530/job/99248338734) | [3s](https://github.com/iree-org/iree/actions/runs/33316065006/job/99269631090) | [3s](https://github.com/iree-org/iree/actions/runs/33316065006/job/99269631090) | 2 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33316065006/job/99269657757) | [3s](https://github.com/iree-org/iree/actions/runs/33308181530/job/99248355800) | [3s](https://github.com/iree-org/iree/actions/runs/33308181530/job/99248355800) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33308181530/job/99248355705) | [3s](https://github.com/iree-org/iree/actions/runs/33316065006/job/99269657783) | [3s](https://github.com/iree-org/iree/actions/runs/33316065006/job/99269657783) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33308181783/job/99248338290) | [2s](https://github.com/iree-org/iree/actions/runs/33316065613/job/99269633086) | [2s](https://github.com/iree-org/iree/actions/runs/33316065613/job/99269633086) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99247597510) | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99247597510) | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99247597510) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33307904893/job/99247710452) | [2s](https://github.com/iree-org/iree/actions/runs/33307904893/job/99247710452) | [2s](https://github.com/iree-org/iree/actions/runs/33307904893/job/99247710452) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33307904893/job/99247611089) | [2s](https://github.com/iree-org/iree/actions/runs/33307904893/job/99247611089) | [2s](https://github.com/iree-org/iree/actions/runs/33307904893/job/99247611089) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/33307949247/job/99247725048) | [1s](https://github.com/iree-org/iree/actions/runs/33315808965/job/99268927617) | [1s](https://github.com/iree-org/iree/actions/runs/33315808965/job/99268927617) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 303 | 1% (2/303) |  | 1d22h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 260 | 3% (8/260) |  | 1d23h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 216 | 0% (1/216) |  | 1d23h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 212 | 0% (0/212) |  | 2d00h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
