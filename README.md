# iree-ci-monitor

_Updated: 2026-06-20 11:49 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27874542208/job/82491737084) | [3s](https://github.com/iree-org/iree/actions/runs/27870370691/job/82481195383) | — | 15 |
| `ubuntu-24.04` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27870199870/job/82480770067) | [2s](https://github.com/iree-org/iree/actions/runs/27874415132/job/82491403480) | 0% (0/1) | 5 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27870244656/job/82480877204) | [3s](https://github.com/iree-org/iree/actions/runs/27874542423/job/82491737551) | [3s](https://github.com/iree-org/iree/actions/runs/27874542423/job/82491737551) | 3 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27874542208/job/82491745922) | [3s](https://github.com/iree-org/iree/actions/runs/27870370691/job/82481195383) | [3s](https://github.com/iree-org/iree/actions/runs/27870370691/job/82481195383) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27870370947/job/82481188040) | [2s](https://github.com/iree-org/iree/actions/runs/27874542423/job/82491737552) | [2s](https://github.com/iree-org/iree/actions/runs/27874542423/job/82491737552) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27870370947/job/82481188050) | [2s](https://github.com/iree-org/iree/actions/runs/27874542423/job/82491737563) | [2s](https://github.com/iree-org/iree/actions/runs/27874542423/job/82491737563) | 3 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27870231483/job/82480843276) | [2s](https://github.com/iree-org/iree/actions/runs/27874415132/job/82491403480) | [2s](https://github.com/iree-org/iree/actions/runs/27874415132/job/82491403480) | 2 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27870370691/job/82481187654) | [2s](https://github.com/iree-org/iree/actions/runs/27874542208/job/82491737084) | [2s](https://github.com/iree-org/iree/actions/runs/27874542208/job/82491737084) | 2 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27870370691/job/82481195387) | [2s](https://github.com/iree-org/iree/actions/runs/27874542208/job/82491745912) | [2s](https://github.com/iree-org/iree/actions/runs/27874542208/job/82491745912) | 2 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27870199870/job/82480770067) | [2s](https://github.com/iree-org/iree/actions/runs/27870199870/job/82480770067) | [2s](https://github.com/iree-org/iree/actions/runs/27870199870/job/82480770067) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27863015405/job/82480763538) | [1s](https://github.com/iree-org/iree/actions/runs/27863015405/job/82480763538) | [1s](https://github.com/iree-org/iree/actions/runs/27863015405/job/82480763538) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27870199870/job/82480838072) | [1s](https://github.com/iree-org/iree/actions/runs/27870199870/job/82480838072) | [1s](https://github.com/iree-org/iree/actions/runs/27870199870/job/82480838072) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 156 | 0% (0/156) |  | 1d04h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 118 | 5% (6/118) |  | 1d04h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 128 | 0% (0/128) |  | 1d04h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 112 | 0% (0/112) |  | 1d04h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 35 | 0% (0/35) |  | 1d04h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
