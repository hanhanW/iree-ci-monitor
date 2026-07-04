# iree-ci-monitor

_Updated: 2026-07-04 11:38 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28705529800/job/85130444627) | [3s](https://github.com/iree-org/iree/actions/runs/28709412841/job/85140365463) | — | 15 |
| `ubuntu-24.04` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28705376803/job/85130118102) | [2s](https://github.com/iree-org/iree/actions/runs/28709275125/job/85139994347) | 0% (0/1) | 5 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28709412939/job/85140351903) | [3s](https://github.com/iree-org/iree/actions/runs/28705414261/job/85130158726) | [3s](https://github.com/iree-org/iree/actions/runs/28705414261/job/85130158726) | 3 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28705529588/job/85130444305) | [3s](https://github.com/iree-org/iree/actions/runs/28709412841/job/85140351687) | [3s](https://github.com/iree-org/iree/actions/runs/28709412841/job/85140351687) | 2 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28705529588/job/85130455211) | [3s](https://github.com/iree-org/iree/actions/runs/28709412841/job/85140365463) | [3s](https://github.com/iree-org/iree/actions/runs/28709412841/job/85140365463) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28705529588/job/85130455227) | [3s](https://github.com/iree-org/iree/actions/runs/28709412841/job/85140365465) | [3s](https://github.com/iree-org/iree/actions/runs/28709412841/job/85140365465) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28705529800/job/85130444627) | [2s](https://github.com/iree-org/iree/actions/runs/28709412939/job/85140351882) | [2s](https://github.com/iree-org/iree/actions/runs/28709412939/job/85140351882) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28705529800/job/85130444610) | [2s](https://github.com/iree-org/iree/actions/runs/28709412939/job/85140351895) | [2s](https://github.com/iree-org/iree/actions/runs/28709412939/job/85140351895) | 3 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28705400757/job/85130123250) | [2s](https://github.com/iree-org/iree/actions/runs/28709275125/job/85139994347) | [2s](https://github.com/iree-org/iree/actions/runs/28709275125/job/85139994347) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85130060519) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85130060519) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85130060519) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28705376803/job/85130118102) | [2s](https://github.com/iree-org/iree/actions/runs/28705376803/job/85130118102) | [2s](https://github.com/iree-org/iree/actions/runs/28705376803/job/85130118102) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28705376803/job/85130065998) | [2s](https://github.com/iree-org/iree/actions/runs/28705376803/job/85130065998) | [2s](https://github.com/iree-org/iree/actions/runs/28705376803/job/85130065998) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 271 | 7% (20/271) |  | 21h05m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 210 | 1% (3/210) |  | 21h12m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 301 | 2% (7/301) |  | 21h13m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 234 | 1% (3/234) |  | 21h15m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 71 | 1% (1/71) |  | 21h34m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
