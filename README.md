# iree-ci-monitor

_Updated: 2026-09-06 08:30 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101475725899) | [3s](https://github.com/iree-org/iree/actions/runs/34030303831/job/101478468373) | 0% (0/1) | 6 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34038240075/job/101500173634) | [3s](https://github.com/iree-org/iree/actions/runs/34038240075/job/101500152846) | — | 12 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34029648105/job/101476741700) | [37s](https://github.com/iree-org/iree/actions/runs/34038240075/job/101500173627) | [37s](https://github.com/iree-org/iree/actions/runs/34038240075/job/101500173627) | 2 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34030303831/job/101478468373) | [3s](https://github.com/iree-org/iree/actions/runs/34030303831/job/101478468373) | [3s](https://github.com/iree-org/iree/actions/runs/34030303831/job/101478468373) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34029648105/job/101476719632) | [3s](https://github.com/iree-org/iree/actions/runs/34038240075/job/101500152846) | [3s](https://github.com/iree-org/iree/actions/runs/34038240075/job/101500152846) | 2 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/34037953126/job/101499371583) | [2s](https://github.com/iree-org/iree/actions/runs/34029343727/job/101475894395) | [2s](https://github.com/iree-org/iree/actions/runs/34029343727/job/101475894395) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34029648442/job/101476722264) | [2s](https://github.com/iree-org/iree/actions/runs/34038241030/job/101500155815) | [2s](https://github.com/iree-org/iree/actions/runs/34038241030/job/101500155815) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34029648442/job/101476722101) | [2s](https://github.com/iree-org/iree/actions/runs/34038241030/job/101500155841) | [2s](https://github.com/iree-org/iree/actions/runs/34038241030/job/101500155841) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/34038241030/job/101500155724) | [2s](https://github.com/iree-org/iree/actions/runs/34029648442/job/101476722179) | [2s](https://github.com/iree-org/iree/actions/runs/34029648442/job/101476722179) | 2 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34029648105/job/101476741692) | [2s](https://github.com/iree-org/iree/actions/runs/34038240075/job/101500173634) | [2s](https://github.com/iree-org/iree/actions/runs/34038240075/job/101500173634) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101475725899) | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101475725899) | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101475725899) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34029283549/job/101475739582) | [2s](https://github.com/iree-org/iree/actions/runs/34029283549/job/101475739582) | [2s](https://github.com/iree-org/iree/actions/runs/34029283549/job/101475739582) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/34029283549/job/101475882442) | [1s](https://github.com/iree-org/iree/actions/runs/34029283549/job/101475882442) | [1s](https://github.com/iree-org/iree/actions/runs/34029283549/job/101475882442) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 123 | 2% (2/123) |  | 2d04h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 103 | 5% (5/103) |  | 2d04h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 94 | 0% (0/94) |  | 2d04h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 84 | 0% (0/84) |  | 2d04h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
