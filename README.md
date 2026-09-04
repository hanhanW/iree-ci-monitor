# iree-ci-monitor

_Updated: 2026-09-04 13:47 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33881554867/job/101051176658) | [8s](https://github.com/iree-org/iree/actions/runs/33864971709/job/100997646846) | 0% (0/2) | 6 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33882125954/job/101053097993) | [3s](https://github.com/iree-org/iree/actions/runs/33882127017/job/101053057300) | — | 15 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/33864971709/job/100997646846) | [8s](https://github.com/iree-org/iree/actions/runs/33864971709/job/100997646846) | [8s](https://github.com/iree-org/iree/actions/runs/33864971709/job/100997646846) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33865113524/job/100998088804) | [3s](https://github.com/iree-org/iree/actions/runs/33882127017/job/101053057502) | [3s](https://github.com/iree-org/iree/actions/runs/33882127017/job/101053057502) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33882127017/job/101053057532) | [3s](https://github.com/iree-org/iree/actions/runs/33865113524/job/100998089059) | [3s](https://github.com/iree-org/iree/actions/runs/33865113524/job/100998089059) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33865113524/job/100998089010) | [3s](https://github.com/iree-org/iree/actions/runs/33882127017/job/101053057300) | [3s](https://github.com/iree-org/iree/actions/runs/33882127017/job/101053057300) | 3 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33881554867/job/101051176658) | [3s](https://github.com/iree-org/iree/actions/runs/33865069105/job/100997947812) | [3s](https://github.com/iree-org/iree/actions/runs/33865069105/job/100997947812) | 2 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33864971709/job/100997919380) | [3s](https://github.com/iree-org/iree/actions/runs/33864971709/job/100997919380) | [3s](https://github.com/iree-org/iree/actions/runs/33864971709/job/100997919380) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33865516191/job/100999358006) | [2s](https://github.com/iree-org/iree/actions/runs/33882125954/job/101053052649) | [2s](https://github.com/iree-org/iree/actions/runs/33882125954/job/101053052649) | 2 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33865516191/job/100999408736) | [2s](https://github.com/iree-org/iree/actions/runs/33882125954/job/101053097993) | [2s](https://github.com/iree-org/iree/actions/runs/33882125954/job/101053097993) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33865516191/job/100999408651) | [2s](https://github.com/iree-org/iree/actions/runs/33882125954/job/101053098038) | [2s](https://github.com/iree-org/iree/actions/runs/33882125954/job/101053098038) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33839825350/job/100997615797) | [2s](https://github.com/iree-org/iree/actions/runs/33839825350/job/100997615797) | [2s](https://github.com/iree-org/iree/actions/runs/33839825350/job/100997615797) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33860609299/job/101005474839) | [2s](https://github.com/iree-org/iree/actions/runs/33860609299/job/101005474839) | [2s](https://github.com/iree-org/iree/actions/runs/33860609299/job/101005474839) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 213 | 1% (2/213) |  | 9h22m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 177 | 4% (7/177) |  | 9h35m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 155 | 1% (1/155) |  | 9h38m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 141 | 0% (0/141) |  | 9h46m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
