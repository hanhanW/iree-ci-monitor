# iree-ci-monitor

_Updated: 2026-08-09 06:17 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192026) | [4s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205510) | — | 6 |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31300078753/job/93211336687) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93237398831) | 0% (0/1) | 11 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625407) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625403) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625456) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625414) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625451) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625427) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205510) | [4s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205510) | [4s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205510) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93237398831) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93237398831) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93237398831) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625387) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625387) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625387) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625403) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625403) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625403) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31296581323/job/93202535787) | [3s](https://github.com/iree-org/iree/actions/runs/31296581323/job/93202535787) | [3s](https://github.com/iree-org/iree/actions/runs/31296581323/job/93202535787) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192054) | [3s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192054) | [3s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192054) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625414) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625414) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625414) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625433) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625433) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625433) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625420) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625420) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625420) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625407) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625407) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625407) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202607167) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202607167) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202607167) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625427) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625427) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625427) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31310511395/job/93237511997) | [2s](https://github.com/iree-org/iree/actions/runs/31310511395/job/93237511997) | [2s](https://github.com/iree-org/iree/actions/runs/31310511395/job/93237511997) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31300078753/job/93211336687) | [2s](https://github.com/iree-org/iree/actions/runs/31300078753/job/93211336687) | [2s](https://github.com/iree-org/iree/actions/runs/31300078753/job/93211336687) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31310469503/job/93237501391) | [2s](https://github.com/iree-org/iree/actions/runs/31310469503/job/93237501391) | [2s](https://github.com/iree-org/iree/actions/runs/31310469503/job/93237501391) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192036) | [2s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192036) | [2s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192036) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192026) | [2s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192026) | [2s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192026) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238190872) | [2s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238190872) | [2s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238190872) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205522) | [2s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205522) | [2s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205522) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625456) | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625456) | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625456) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 3% (3/102) |  | 1d13h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 116 | 3% (4/116) |  | 1d19h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 131 | 0% (0/131) |  | 1d19h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 100 | 5% (5/100) |  | 1d19h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
