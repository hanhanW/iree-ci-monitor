# iree-ci-monitor

_Updated: 2026-08-15 11:48 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31889144773/job/95022703683) | [4s](https://github.com/iree-org/iree/actions/runs/31878566175/job/94997760982) | — | 15 |
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94997467406) | [4s](https://github.com/iree-org/iree/actions/runs/31888851601/job/95021972943) | 0% (0/1) | 6 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/31878566175/job/94997760982) | [4s](https://github.com/iree-org/iree/actions/runs/31889144773/job/95022703697) | [4s](https://github.com/iree-org/iree/actions/runs/31889144773/job/95022703697) | 3 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31878538415/job/94997692413) | [4s](https://github.com/iree-org/iree/actions/runs/31888851601/job/95021972943) | [4s](https://github.com/iree-org/iree/actions/runs/31888851601/job/95021972943) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31889144773/job/95022703683) | [3s](https://github.com/iree-org/iree/actions/runs/31878566175/job/94997760987) | [3s](https://github.com/iree-org/iree/actions/runs/31878566175/job/94997760987) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31878809038/job/94998366486) | [3s](https://github.com/iree-org/iree/actions/runs/31889144773/job/95022703660) | [3s](https://github.com/iree-org/iree/actions/runs/31889144773/job/95022703660) | 3 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31878808741/job/94998382581) | [3s](https://github.com/iree-org/iree/actions/runs/31889144097/job/95022722153) | [3s](https://github.com/iree-org/iree/actions/runs/31889144097/job/95022722153) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94997467406) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94997467406) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94997467406) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31878449394/job/94997679596) | [3s](https://github.com/iree-org/iree/actions/runs/31878449394/job/94997679596) | [3s](https://github.com/iree-org/iree/actions/runs/31878449394/job/94997679596) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31878808741/job/94998364793) | [2s](https://github.com/iree-org/iree/actions/runs/31889144097/job/95022702898) | [2s](https://github.com/iree-org/iree/actions/runs/31889144097/job/95022702898) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31878808741/job/94998382540) | [2s](https://github.com/iree-org/iree/actions/runs/31889144097/job/95022722166) | [2s](https://github.com/iree-org/iree/actions/runs/31889144097/job/95022722166) | 2 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31877596421/job/94995512376) | [2s](https://github.com/iree-org/iree/actions/runs/31877596421/job/94995512376) | [2s](https://github.com/iree-org/iree/actions/runs/31877596421/job/94995512376) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31878449394/job/94997483026) | [2s](https://github.com/iree-org/iree/actions/runs/31878449394/job/94997483026) | [2s](https://github.com/iree-org/iree/actions/runs/31878449394/job/94997483026) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 203 | 0% (0/203) |  | 23h21m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 167 | 7% (12/167) |  | 23h21m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 167 | 4% (6/167) |  | 23h27m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 138 | 9% (12/138) |  | 23h27m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
