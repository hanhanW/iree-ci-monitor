# iree-ci-monitor

_Updated: 2026-09-05 13:25 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33970894619/job/101319095048) | [3s](https://github.com/iree-org/iree/actions/runs/33970894619/job/101319095015) | — | 15 |
| `ubuntu-24.04` | github-hosted | 5 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/33962066278/job/101295551204) | [2s](https://github.com/iree-org/iree/actions/runs/33970653017/job/101318444552) | 0% (0/1) | 5 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33962333185/job/101296286155) | [4s](https://github.com/iree-org/iree/actions/runs/33970894265/job/101319115890) | [4s](https://github.com/iree-org/iree/actions/runs/33970894265/job/101319115890) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33970894619/job/101319095049) | [3s](https://github.com/iree-org/iree/actions/runs/33962087054/job/101295611539) | [3s](https://github.com/iree-org/iree/actions/runs/33962087054/job/101295611539) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33970894619/job/101319095048) | [3s](https://github.com/iree-org/iree/actions/runs/33962087054/job/101295611415) | [3s](https://github.com/iree-org/iree/actions/runs/33962087054/job/101295611415) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33962333678/job/101296263895) | [3s](https://github.com/iree-org/iree/actions/runs/33970894619/job/101319095015) | [3s](https://github.com/iree-org/iree/actions/runs/33970894619/job/101319095015) | 3 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33962333185/job/101296286152) | [3s](https://github.com/iree-org/iree/actions/runs/33970894265/job/101319115927) | [3s](https://github.com/iree-org/iree/actions/runs/33970894265/job/101319115927) | 2 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/33962066278/job/101295551204) | [2s](https://github.com/iree-org/iree/actions/runs/33970653017/job/101318444552) | [2s](https://github.com/iree-org/iree/actions/runs/33970653017/job/101318444552) | 2 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33962333185/job/101296262250) | [2s](https://github.com/iree-org/iree/actions/runs/33970894265/job/101319093608) | [2s](https://github.com/iree-org/iree/actions/runs/33970894265/job/101319093608) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33946663716/job/101295382760) | [2s](https://github.com/iree-org/iree/actions/runs/33946663716/job/101295382760) | [2s](https://github.com/iree-org/iree/actions/runs/33946663716/job/101295382760) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/33962007662/job/101295540479) | [1s](https://github.com/iree-org/iree/actions/runs/33962007662/job/101295540479) | [1s](https://github.com/iree-org/iree/actions/runs/33962007662/job/101295540479) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/33962007662/job/101295394467) | [1s](https://github.com/iree-org/iree/actions/runs/33962007662/job/101295394467) | [1s](https://github.com/iree-org/iree/actions/runs/33962007662/job/101295394467) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 123 | 2% (2/123) |  | 1d09h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 103 | 5% (5/103) |  | 1d09h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 94 | 0% (0/94) |  | 1d09h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 84 | 0% (0/84) |  | 1d09h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
