# iree-ci-monitor

_Updated: 2026-06-13 11:48 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27469937398/job/81198908255) | [8s](https://github.com/iree-org/iree/actions/runs/27469937570/job/81198898809) | — | 15 |
| `ubuntu-24.04` | github-hosted | 5 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27469808959/job/81198546300) | [2s](https://github.com/iree-org/iree/actions/runs/27466396683/job/81189356999) | 0% (0/1) | 5 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27466521353/job/81189694211) | [8s](https://github.com/iree-org/iree/actions/runs/27469937570/job/81198898809) | [8s](https://github.com/iree-org/iree/actions/runs/27469937570/job/81198898809) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/27466521353/job/81189694247) | [8s](https://github.com/iree-org/iree/actions/runs/27469937570/job/81198898840) | [8s](https://github.com/iree-org/iree/actions/runs/27469937570/job/81198898840) | 3 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27466521268/job/81189705733) | [3s](https://github.com/iree-org/iree/actions/runs/27469937398/job/81198908259) | [3s](https://github.com/iree-org/iree/actions/runs/27469937398/job/81198908259) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27466521353/job/81189694224) | [2s](https://github.com/iree-org/iree/actions/runs/27469937570/job/81198898816) | [2s](https://github.com/iree-org/iree/actions/runs/27469937570/job/81198898816) | 3 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27469808959/job/81198546300) | [2s](https://github.com/iree-org/iree/actions/runs/27466396683/job/81189356999) | [2s](https://github.com/iree-org/iree/actions/runs/27466396683/job/81189356999) | 2 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27466521268/job/81189694201) | [2s](https://github.com/iree-org/iree/actions/runs/27469937398/job/81198898850) | [2s](https://github.com/iree-org/iree/actions/runs/27469937398/job/81198898850) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27466521268/job/81189705723) | [2s](https://github.com/iree-org/iree/actions/runs/27469937398/job/81198908255) | [2s](https://github.com/iree-org/iree/actions/runs/27469937398/job/81198908255) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27459104109/job/81189280730) | [2s](https://github.com/iree-org/iree/actions/runs/27459104109/job/81189280730) | [2s](https://github.com/iree-org/iree/actions/runs/27459104109/job/81189280730) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27466369589/job/81189351255) | [1s](https://github.com/iree-org/iree/actions/runs/27466369589/job/81189351255) | [1s](https://github.com/iree-org/iree/actions/runs/27466369589/job/81189351255) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27466369589/job/81189287273) | [1s](https://github.com/iree-org/iree/actions/runs/27466369589/job/81189287273) | [1s](https://github.com/iree-org/iree/actions/runs/27466369589/job/81189287273) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 282 | 2% (7/282) |  | 1d03h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 239 | 8% (18/239) |  | 1d03h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 199 | 3% (5/199) |  | 1d03h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 209 | 2% (5/209) |  | 1d04h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 67 | 1% (1/67) |  | 1d04h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
