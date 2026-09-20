# iree-ci-monitor

_Updated: 2026-09-20 09:11 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35510074988/job/106076328551) | [3s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106055323466) | 0% (0/1) | 7 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35515594893/job/106090887366) | [3s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090909005) | 0% (0/3) | 9 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35515594893/job/106090887406) | [3s](https://github.com/iree-org/iree/actions/runs/35513885621/job/106086431666) | [3s](https://github.com/iree-org/iree/actions/runs/35513885621/job/106086431666) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106055323466) | [3s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106055323466) | [3s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106055323466) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/35444212759/job/106094721639) | [3s](https://github.com/iree-org/iree/actions/runs/35444212759/job/106094721639) | [3s](https://github.com/iree-org/iree/actions/runs/35444212759/job/106094721639) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090908972) | [3s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090908972) | [3s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090908972) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090909005) | [3s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090909005) | [3s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090909005) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35502073745/job/106055496041) | [2s](https://github.com/iree-org/iree/actions/runs/35515299901/job/106090107955) | [2s](https://github.com/iree-org/iree/actions/runs/35515299901/job/106090107955) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35513885621/job/106086431509) | [2s](https://github.com/iree-org/iree/actions/runs/35515594893/job/106090887170) | [2s](https://github.com/iree-org/iree/actions/runs/35515594893/job/106090887170) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35513885621/job/106086431329) | [2s](https://github.com/iree-org/iree/actions/runs/35515594893/job/106090887366) | [2s](https://github.com/iree-org/iree/actions/runs/35515594893/job/106090887366) | 2 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35510074988/job/106076328551) | [2s](https://github.com/iree-org/iree/actions/runs/35510074988/job/106076328551) | [2s](https://github.com/iree-org/iree/actions/runs/35510074988/job/106076328551) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055481141) | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055481141) | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055481141) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055339751) | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055339751) | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055339751) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090887014) | [2s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090887014) | [2s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090887014) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 322 | 0% (1/322) |  | 1d00h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 359 | 1% (3/359) |  | 1d00h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 230 | 2% (4/230) |  | 2d18h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 17 | 12% (2/17) |  | 6d00h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
