# iree-ci-monitor

_Updated: 2026-08-23 11:50 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/32640474551/job/97196682594) | [3s](https://github.com/iree-org/iree/actions/runs/32644264220/job/97205951698) | 0% (0/1) | 2 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32644595452/job/97206805285) | [3s](https://github.com/iree-org/iree/actions/runs/32644595452/job/97206805194) | — | 6 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32644264220/job/97205951698) | [3s](https://github.com/iree-org/iree/actions/runs/32644264220/job/97205951698) | [3s](https://github.com/iree-org/iree/actions/runs/32644264220/job/97205951698) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32640474551/job/97196682594) | [3s](https://github.com/iree-org/iree/actions/runs/32640474551/job/97196682594) | [3s](https://github.com/iree-org/iree/actions/runs/32640474551/job/97196682594) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32644595452/job/97206805194) | [3s](https://github.com/iree-org/iree/actions/runs/32644595452/job/97206805194) | [3s](https://github.com/iree-org/iree/actions/runs/32644595452/job/97206805194) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32644595105/job/97206832063) | [3s](https://github.com/iree-org/iree/actions/runs/32644595105/job/97206832063) | [3s](https://github.com/iree-org/iree/actions/runs/32644595105/job/97206832063) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32644595452/job/97206805285) | [2s](https://github.com/iree-org/iree/actions/runs/32644595452/job/97206805285) | [2s](https://github.com/iree-org/iree/actions/runs/32644595452/job/97206805285) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32644595452/job/97206805333) | [2s](https://github.com/iree-org/iree/actions/runs/32644595452/job/97206805333) | [2s](https://github.com/iree-org/iree/actions/runs/32644595452/job/97206805333) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32644595105/job/97206804391) | [2s](https://github.com/iree-org/iree/actions/runs/32644595105/job/97206804391) | [2s](https://github.com/iree-org/iree/actions/runs/32644595105/job/97206804391) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32644595105/job/97206832111) | [2s](https://github.com/iree-org/iree/actions/runs/32644595105/job/97206832111) | [2s](https://github.com/iree-org/iree/actions/runs/32644595105/job/97206832111) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | 0s | 0s | 0s | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 212 | 1% (3/211) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 153 | 0% (0/152) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 201 | 2% (5/200) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 148 | 0% (0/147) | yes | running |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
