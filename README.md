# iree-ci-monitor

_Updated: 2026-08-23 06:03 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958655) | [5s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958601) | — | 3 |
| `ubuntu-24.04` | github-hosted | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958609) | [3s](https://github.com/iree-org/iree/actions/runs/32640474551/job/97196682594) | 0% (0/1) | 7 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958636) | [3s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958610) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958649) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958652) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958601) | [5s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958601) | [5s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958601) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958633) | [4s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958633) | [4s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958633) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958655) | [4s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958655) | [4s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958655) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958610) | [3s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958610) | [3s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958610) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32640474551/job/97196682594) | [3s](https://github.com/iree-org/iree/actions/runs/32640474551/job/97196682594) | [3s](https://github.com/iree-org/iree/actions/runs/32640474551/job/97196682594) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958640) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958640) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958640) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958606) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958606) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958606) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958646) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958646) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958646) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958609) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958609) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958609) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958636) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958636) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958636) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145939401) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145939401) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145939401) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958649) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958649) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958649) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958652) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958652) | [2s](https://github.com/iree-org/iree/actions/runs/32619726932/job/97145958652) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32619699972/job/97145869255) | [2s](https://github.com/iree-org/iree/actions/runs/32619699972/job/97145869255) | [2s](https://github.com/iree-org/iree/actions/runs/32619699972/job/97145869255) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | 0s | 0s | 0s | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 212 | 1% (3/211) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 153 | 0% (0/152) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 201 | 2% (5/200) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 148 | 0% (0/147) | yes | running |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
