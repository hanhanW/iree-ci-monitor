# iree-ci-monitor

_Updated: 2026-07-27 17:52 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 8 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30278078427/job/90017135820) | [9s](https://github.com/iree-org/iree/actions/runs/30307970636/job/90116682528) | 0% (0/2) | 8 |
| `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30277624429/job/90015579864) | [3s](https://github.com/iree-org/iree/actions/runs/30281193796/job/90027712718) | 0% (0/1) | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/dependabot/dependabot-updates` | Dependabot | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30307970635/job/90116681330) | [9s](https://github.com/iree-org/iree/actions/runs/30307970636/job/90116682528) | [9s](https://github.com/iree-org/iree/actions/runs/30307970636/job/90116682528) | 2 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30277624429/job/90015579864) | [3s](https://github.com/iree-org/iree/actions/runs/30277624429/job/90015579864) | [3s](https://github.com/iree-org/iree/actions/runs/30277624429/job/90015579864) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30281193796/job/90027712718) | [3s](https://github.com/iree-org/iree/actions/runs/30281193796/job/90027712718) | [3s](https://github.com/iree-org/iree/actions/runs/30281193796/job/90027712718) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30278078427/job/90017135820) | [3s](https://github.com/iree-org/iree/actions/runs/30278078427/job/90017135820) | [3s](https://github.com/iree-org/iree/actions/runs/30278078427/job/90017135820) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30278078427/job/90017183374) | [3s](https://github.com/iree-org/iree/actions/runs/30278078427/job/90017183374) | [3s](https://github.com/iree-org/iree/actions/runs/30278078427/job/90017183374) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30278078427/job/90017183340) | [3s](https://github.com/iree-org/iree/actions/runs/30278078427/job/90017183340) | [3s](https://github.com/iree-org/iree/actions/runs/30278078427/job/90017183340) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30278079298/job/90017141478) | [2s](https://github.com/iree-org/iree/actions/runs/30278079298/job/90017141478) | [2s](https://github.com/iree-org/iree/actions/runs/30278079298/job/90017141478) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30278079298/job/90017141308) | [2s](https://github.com/iree-org/iree/actions/runs/30278079298/job/90017141308) | [2s](https://github.com/iree-org/iree/actions/runs/30278079298/job/90017141308) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30278079298/job/90017141314) | [2s](https://github.com/iree-org/iree/actions/runs/30278079298/job/90017141314) | [2s](https://github.com/iree-org/iree/actions/runs/30278079298/job/90017141314) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 328 | 2% (5/328) |  | 13h26m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 252 | 1% (2/252) |  | 13h36m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 265 | 5% (14/265) |  | 13h38m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 238 | 2% (4/238) |  | 13h48m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 75 | 3% (2/75) |  | 13h49m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
