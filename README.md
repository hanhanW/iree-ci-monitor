# iree-ci-monitor

_Updated: 2026-08-08 00:17 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 7 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934971) | [8s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934969) | 50% (1/2) | 7 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934984) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934993) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934965) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934968) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934970) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934982) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934969) | [8s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934969) | [8s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934969) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934967) | [8s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934967) | [8s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934967) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934960) | [3s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934960) | [3s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934960) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934971) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934971) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934971) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934984) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934984) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934984) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934993) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934993) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934993) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062917006) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062917006) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062917006) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31200173112/job/93022537522) | [2s](https://github.com/iree-org/iree/actions/runs/31200173112/job/93022537522) | [2s](https://github.com/iree-org/iree/actions/runs/31200173112/job/93022537522) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31241383999/job/93062848102) | [2s](https://github.com/iree-org/iree/actions/runs/31241383999/job/93062848102) | [2s](https://github.com/iree-org/iree/actions/runs/31241383999/job/93062848102) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934963) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934963) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934963) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934968) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934968) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934968) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934965) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934965) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934965) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934970) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934970) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934970) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934982) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934982) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934982) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 3% (3/102) |  | 7h58m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 116 | 3% (4/116) |  | 13h38m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 131 | 0% (0/131) |  | 13h48m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 100 | 5% (5/100) |  | 13h52m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
