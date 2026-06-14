# iree-ci-monitor

_Updated: 2026-06-14 11:47 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27502398117/job/81287538093) | [9s](https://github.com/iree-org/iree/actions/runs/27498705854/job/81277464550) | 0% (0/3) | 15 |
| `ubuntu-24.04` | github-hosted | 5 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81276947785) | [8s](https://github.com/iree-org/iree/actions/runs/27502267805/job/81287160705) | 0% (0/1) | 5 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27498705734/job/81277473156) | [10s](https://github.com/iree-org/iree/actions/runs/27502397933/job/81287553369) | [10s](https://github.com/iree-org/iree/actions/runs/27502397933/job/81287553369) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27502398117/job/81287538093) | [9s](https://github.com/iree-org/iree/actions/runs/27498705854/job/81277464550) | [9s](https://github.com/iree-org/iree/actions/runs/27498705854/job/81277464550) | 3 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27498563060/job/81277074733) | [8s](https://github.com/iree-org/iree/actions/runs/27502267805/job/81287160705) | [8s](https://github.com/iree-org/iree/actions/runs/27502267805/job/81287160705) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27502397933/job/81287553363) | [8s](https://github.com/iree-org/iree/actions/runs/27498705734/job/81277473138) | [8s](https://github.com/iree-org/iree/actions/runs/27498705734/job/81277473138) | 2 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27498705734/job/81277464601) | [4s](https://github.com/iree-org/iree/actions/runs/27502397933/job/81287538047) | [4s](https://github.com/iree-org/iree/actions/runs/27502397933/job/81287538047) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81276947785) | [3s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81276947785) | [3s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81276947785) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27498520263/job/81276957559) | [3s](https://github.com/iree-org/iree/actions/runs/27498520263/job/81276957559) | [3s](https://github.com/iree-org/iree/actions/runs/27498520263/job/81276957559) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27500476747/job/81282305622) | [2s](https://github.com/iree-org/iree/actions/runs/27502398117/job/81287538114) | [2s](https://github.com/iree-org/iree/actions/runs/27502398117/job/81287538114) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27500476747/job/81282305644) | [2s](https://github.com/iree-org/iree/actions/runs/27502398117/job/81287538097) | [2s](https://github.com/iree-org/iree/actions/runs/27502398117/job/81287538097) | 3 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27498520263/job/81277067605) | [2s](https://github.com/iree-org/iree/actions/runs/27498520263/job/81277067605) | [2s](https://github.com/iree-org/iree/actions/runs/27498520263/job/81277067605) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 282 | 2% (7/282) |  | 2d03h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 239 | 8% (18/239) |  | 2d03h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 199 | 3% (5/199) |  | 2d03h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 209 | 2% (5/209) |  | 2d03h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 67 | 1% (1/67) |  | 2d04h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
