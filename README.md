# iree-ci-monitor

_Updated: 2026-08-16 11:48 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31951597938/job/95175765367) | [4s](https://github.com/iree-org/iree/actions/runs/31943232407/job/95155300116) | 0% (0/1) | 5 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31951895140/job/95176538883) | [3s](https://github.com/iree-org/iree/actions/runs/31952970783/job/95179202365) | 0% (0/3) | 15 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31951597938/job/95175765367) | [4s](https://github.com/iree-org/iree/actions/runs/31943232407/job/95155300116) | [4s](https://github.com/iree-org/iree/actions/runs/31943232407/job/95155300116) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31951895140/job/95176538883) | [3s](https://github.com/iree-org/iree/actions/runs/31952970783/job/95179202365) | [3s](https://github.com/iree-org/iree/actions/runs/31952970783/job/95179202365) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31943525649/job/95156038446) | [3s](https://github.com/iree-org/iree/actions/runs/31952970783/job/95179202371) | [3s](https://github.com/iree-org/iree/actions/runs/31952970783/job/95179202371) | 3 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31943524890/job/95156058272) | [3s](https://github.com/iree-org/iree/actions/runs/31951894741/job/95176561836) | [3s](https://github.com/iree-org/iree/actions/runs/31951894741/job/95176561836) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31943524890/job/95156058302) | [3s](https://github.com/iree-org/iree/actions/runs/31951894741/job/95176561826) | [3s](https://github.com/iree-org/iree/actions/runs/31951894741/job/95176561826) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31928371678/job/95155177209) | [3s](https://github.com/iree-org/iree/actions/runs/31928371678/job/95155177209) | [3s](https://github.com/iree-org/iree/actions/runs/31928371678/job/95155177209) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31951895140/job/95176538879) | [2s](https://github.com/iree-org/iree/actions/runs/31952970783/job/95179202400) | [2s](https://github.com/iree-org/iree/actions/runs/31952970783/job/95179202400) | 3 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31943524890/job/95156037631) | [2s](https://github.com/iree-org/iree/actions/runs/31951894741/job/95176537997) | [2s](https://github.com/iree-org/iree/actions/runs/31951894741/job/95176537997) | 2 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31943183690/job/95155288544) | [2s](https://github.com/iree-org/iree/actions/runs/31943183690/job/95155288544) | [2s](https://github.com/iree-org/iree/actions/runs/31943183690/job/95155288544) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31943183690/job/95155189905) | [1s](https://github.com/iree-org/iree/actions/runs/31943183690/job/95155189905) | [1s](https://github.com/iree-org/iree/actions/runs/31943183690/job/95155189905) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 203 | 0% (0/203) |  | 1d23h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 167 | 7% (12/167) |  | 1d23h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 167 | 4% (6/167) |  | 1d23h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 138 | 9% (12/138) |  | 1d23h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
