# iree-ci-monitor

_Updated: 2026-07-18 05:37 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823754) | [6s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823755) | — | 3 |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074477306) | [3s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823764) | 0% (0/2) | 11 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29642447636/job/88075083613) | [3s](https://github.com/iree-org/iree/actions/runs/29642447636/job/88075083603) | — | 6 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823741) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823746) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823752) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823756) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823755) | [6s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823755) | [6s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823755) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823754) | [5s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823754) | [5s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823754) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823731) | [5s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823731) | [5s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823731) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823764) | [3s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823764) | [3s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823764) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049804696) | [3s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049804696) | [3s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049804696) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29642447636/job/88075083603) | [3s](https://github.com/iree-org/iree/actions/runs/29642447636/job/88075083603) | [3s](https://github.com/iree-org/iree/actions/runs/29642447636/job/88075083603) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29642447320/job/88075098537) | [3s](https://github.com/iree-org/iree/actions/runs/29642447320/job/88075098537) | [3s](https://github.com/iree-org/iree/actions/runs/29642447320/job/88075098537) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29642447320/job/88075098531) | [3s](https://github.com/iree-org/iree/actions/runs/29642447320/job/88075098531) | [3s](https://github.com/iree-org/iree/actions/runs/29642447320/job/88075098531) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88074470123) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88074470123) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88074470123) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823724) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823724) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823724) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823759) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823759) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823759) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823730) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823730) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823730) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823741) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823741) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823741) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823746) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823746) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823746) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823756) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823756) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823756) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823752) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823752) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88049823752) | 1 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29642912538/job/88076264915) | [2s](https://github.com/iree-org/iree/actions/runs/29642912538/job/88076264915) | [2s](https://github.com/iree-org/iree/actions/runs/29642912538/job/88076264915) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29642278730/job/88074641463) | [2s](https://github.com/iree-org/iree/actions/runs/29642278730/job/88074641463) | [2s](https://github.com/iree-org/iree/actions/runs/29642278730/job/88074641463) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29632826519/job/88049743306) | [2s](https://github.com/iree-org/iree/actions/runs/29632826519/job/88049743306) | [2s](https://github.com/iree-org/iree/actions/runs/29632826519/job/88049743306) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074634926) | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074634926) | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074634926) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 175 | 1% (1/175) |  | 13h47m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 141 | 9% (13/141) |  | 13h47m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 150 | 1% (2/150) |  | 13h53m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 137 | 0% (0/137) |  | 13h56m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 41 | 0% (0/41) |  | 14h06m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
