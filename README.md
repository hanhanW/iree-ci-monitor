# iree-ci-monitor

_Updated: 2026-09-06 04:02 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168082) | [9s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168093) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168140) | [6s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168102) | — | 3 |
| `ubuntu-24.04` | github-hosted | 7 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168077) | [3s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168070) | 0% (0/1) | 6 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168166) | [3s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168091) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168093) | [9s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168093) | [9s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168093) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168082) | [8s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168082) | [8s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168082) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168102) | [6s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168102) | [6s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168102) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168140) | [5s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168140) | [5s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168140) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168112) | [4s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168112) | [4s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168112) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168070) | [3s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168070) | [3s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168070) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168091) | [3s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168091) | [3s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168091) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168077) | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168077) | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168077) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168086) | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168086) | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168086) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168120) | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168120) | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168120) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168166) | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168166) | [2s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433168166) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34013449382/job/101433099744) | [2s](https://github.com/iree-org/iree/actions/runs/34013449382/job/101433099744) | [2s](https://github.com/iree-org/iree/actions/runs/34013449382/job/101433099744) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433152047) | [1s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433152047) | [1s](https://github.com/iree-org/iree/actions/runs/34013468858/job/101433152047) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | 0s | 0s | 0s | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 123 | 2% (2/123) |  | 1d23h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 103 | 5% (5/103) |  | 1d23h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 94 | 0% (0/94) |  | 1d23h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 84 | 0% (0/84) |  | 2d00h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
