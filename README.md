# iree-ci-monitor

_Updated: 2026-08-17 00:18 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202286) | [5s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202451) | — | 3 |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291172310) | [3s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202341) | 0% (0/4) | 10 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202295) | [3s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202299) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202355) | [3s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202297) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202286) | [5s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202286) | [5s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202286) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202451) | [5s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202451) | [5s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202451) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202288) | [4s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202288) | [4s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202288) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202341) | [3s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202341) | [3s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202341) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202299) | [3s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202299) | [3s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202299) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202297) | [3s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202297) | [3s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202297) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202314) | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202314) | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202314) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202328) | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202328) | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202328) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202275) | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202275) | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202275) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202295) | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202295) | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202295) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291172310) | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291172310) | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291172310) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202355) | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202355) | [2s](https://github.com/iree-org/iree/actions/runs/31997315737/job/95291202355) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32004645601/job/95311568310) | [2s](https://github.com/iree-org/iree/actions/runs/32004645601/job/95311568310) | [2s](https://github.com/iree-org/iree/actions/runs/32004645601/job/95311568310) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31994124147/job/95282694282) | [2s](https://github.com/iree-org/iree/actions/runs/31994124147/job/95282694282) | [2s](https://github.com/iree-org/iree/actions/runs/31994124147/job/95282694282) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31994124147/job/95282694320) | [2s](https://github.com/iree-org/iree/actions/runs/31994124147/job/95282694320) | [2s](https://github.com/iree-org/iree/actions/runs/31994124147/job/95282694320) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31994124147/job/95284056876) | [2s](https://github.com/iree-org/iree/actions/runs/31994124147/job/95284056876) | [2s](https://github.com/iree-org/iree/actions/runs/31994124147/job/95284056876) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31997280204/job/95291069045) | [2s](https://github.com/iree-org/iree/actions/runs/31997280204/job/95291069045) | [2s](https://github.com/iree-org/iree/actions/runs/31997280204/job/95291069045) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 203 | 0% (0/203) |  | 2d11h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 167 | 7% (12/167) |  | 2d11h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 167 | 4% (6/167) |  | 2d11h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 138 | 9% (12/138) |  | 2d11h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
