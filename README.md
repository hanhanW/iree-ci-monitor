# iree-ci-monitor

_Updated: 2026-07-05 11:40 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28744204750/job/85232197048) | [3s](https://github.com/iree-org/iree/actions/runs/28742506675/job/85227658634) | 0% (0/3) | 15 |
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28740327885/job/85221812015) | [3s](https://github.com/iree-org/iree/actions/runs/28744038899/job/85231749338) | 0% (0/1) | 6 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28744204750/job/85232197048) | [4s](https://github.com/iree-org/iree/actions/runs/28742506675/job/85227658667) | [4s](https://github.com/iree-org/iree/actions/runs/28742506675/job/85227658667) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28744204750/job/85232197132) | [3s](https://github.com/iree-org/iree/actions/runs/28740504738/job/85222278487) | [3s](https://github.com/iree-org/iree/actions/runs/28740504738/job/85222278487) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28740504738/job/85222278483) | [3s](https://github.com/iree-org/iree/actions/runs/28742506675/job/85227658634) | [3s](https://github.com/iree-org/iree/actions/runs/28742506675/job/85227658634) | 3 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28740358060/job/85221890477) | [3s](https://github.com/iree-org/iree/actions/runs/28744038899/job/85231749338) | [3s](https://github.com/iree-org/iree/actions/runs/28744038899/job/85231749338) | 2 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28744204570/job/85232208084) | [3s](https://github.com/iree-org/iree/actions/runs/28740504509/job/85222286333) | [3s](https://github.com/iree-org/iree/actions/runs/28740504509/job/85222286333) | 2 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28740327885/job/85221881371) | [3s](https://github.com/iree-org/iree/actions/runs/28740327885/job/85221881371) | [3s](https://github.com/iree-org/iree/actions/runs/28740327885/job/85221881371) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28740504509/job/85222278244) | [2s](https://github.com/iree-org/iree/actions/runs/28744204570/job/85232196508) | [2s](https://github.com/iree-org/iree/actions/runs/28744204570/job/85232196508) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28740504509/job/85222286337) | [2s](https://github.com/iree-org/iree/actions/runs/28744204570/job/85232208110) | [2s](https://github.com/iree-org/iree/actions/runs/28744204570/job/85232208110) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28731838272/job/85221804734) | [2s](https://github.com/iree-org/iree/actions/runs/28731838272/job/85221804734) | [2s](https://github.com/iree-org/iree/actions/runs/28731838272/job/85221804734) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85223982776) | [2s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85223982776) | [2s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85223982776) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28740327885/job/85221812015) | [2s](https://github.com/iree-org/iree/actions/runs/28740327885/job/85221812015) | [2s](https://github.com/iree-org/iree/actions/runs/28740327885/job/85221812015) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 275 | 3% (7/275) |  | 10h37m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 194 | 2% (3/194) |  | 10h41m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 249 | 8% (19/249) |  | 10h42m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 216 | 1% (3/216) |  | 10h42m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 65 | 2% (1/65) |  | 10h59m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
