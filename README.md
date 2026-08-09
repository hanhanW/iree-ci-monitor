# iree-ci-monitor

_Updated: 2026-08-09 12:03 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31316124630/job/93251541727) | [3s](https://github.com/iree-org/iree/actions/runs/31318019872/job/93256369847) | 0% (0/3) | 15 |
| `ubuntu-24.04` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31310511395/job/93237511997) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93237398831) | 0% (0/1) | 5 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31318019872/job/93256369847) | [4s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205510) | [4s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205510) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31318020001/job/93256349068) | [3s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192054) | [3s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192054) | 3 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205522) | [3s](https://github.com/iree-org/iree/actions/runs/31318019872/job/93256369817) | [3s](https://github.com/iree-org/iree/actions/runs/31318019872/job/93256369817) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93237398831) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93237398831) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93237398831) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192036) | [2s](https://github.com/iree-org/iree/actions/runs/31316124630/job/93251541686) | [2s](https://github.com/iree-org/iree/actions/runs/31316124630/job/93251541686) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31316124630/job/93251541727) | [2s](https://github.com/iree-org/iree/actions/runs/31318020001/job/93256349069) | [2s](https://github.com/iree-org/iree/actions/runs/31318020001/job/93256349069) | 3 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31310511395/job/93237511997) | [2s](https://github.com/iree-org/iree/actions/runs/31317762345/job/93255662595) | [2s](https://github.com/iree-org/iree/actions/runs/31317762345/job/93255662595) | 2 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238190872) | [2s](https://github.com/iree-org/iree/actions/runs/31318019872/job/93256348506) | [2s](https://github.com/iree-org/iree/actions/runs/31318019872/job/93256348506) | 2 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31310469503/job/93237501391) | [2s](https://github.com/iree-org/iree/actions/runs/31310469503/job/93237501391) | [2s](https://github.com/iree-org/iree/actions/runs/31310469503/job/93237501391) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31310469503/job/93237410616) | [1s](https://github.com/iree-org/iree/actions/runs/31310469503/job/93237410616) | [1s](https://github.com/iree-org/iree/actions/runs/31310469503/job/93237410616) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 3% (3/102) |  | 1d19h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 116 | 3% (4/116) |  | 2d01h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 131 | 0% (0/131) |  | 2d01h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 100 | 5% (5/100) |  | 2d01h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
