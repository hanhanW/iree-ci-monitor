# iree-ci-monitor

_Updated: 2026-08-12 00:54 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020723691) | [10s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761537) | 0% (0/4) | 9 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761466) | [4s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761396) | — | 3 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761380) | [3s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761389) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761384) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761421) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761537) | [10s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761537) | [10s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761537) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761396) | [4s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761396) | [4s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761396) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761389) | [3s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761389) | [3s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761389) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761466) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761466) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761466) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761377) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761377) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761377) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761473) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761473) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761473) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761455) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761455) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761455) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761403) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761403) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761403) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761380) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761380) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761380) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020723691) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020723691) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020723691) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761384) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761384) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761384) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761421) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761421) | [2s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761421) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31563967765/job/94011896193) | [2s](https://github.com/iree-org/iree/actions/runs/31563967765/job/94011896193) | [2s](https://github.com/iree-org/iree/actions/runs/31563967765/job/94011896193) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31563967765/job/94011896109) | [2s](https://github.com/iree-org/iree/actions/runs/31563967765/job/94011896109) | [2s](https://github.com/iree-org/iree/actions/runs/31563967765/job/94011896109) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31563967765/job/94012982100) | [2s](https://github.com/iree-org/iree/actions/runs/31563967765/job/94012982100) | [2s](https://github.com/iree-org/iree/actions/runs/31563967765/job/94012982100) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31566948185/job/94020606805) | [2s](https://github.com/iree-org/iree/actions/runs/31566948185/job/94020606805) | [2s](https://github.com/iree-org/iree/actions/runs/31566948185/job/94020606805) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 148 | 6% (9/148) |  | 12h39m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 173 | 0% (0/173) |  | 12h59m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 141 | 4% (5/141) |  | 13h01m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 122 | 12% (15/122) |  | 13h05m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
