# iree-ci-monitor

_Updated: 2026-06-06 05:47 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812635) | [6s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812625) | — | 3 |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27061579995/job/79875238975) | [3s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79875180424) | 0% (0/1) | 10 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27061712143/job/79875531368) | [3s](https://github.com/iree-org/iree/actions/runs/27061712253/job/79875521280) | — | 9 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812651) | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812673) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812662) | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812674) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812625) | [6s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812625) | [6s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812625) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812628) | [5s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812628) | [5s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812628) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812635) | [5s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812635) | [5s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812635) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27061712253/job/79875521273) | [3s](https://github.com/iree-org/iree/actions/runs/27061617150/job/79875280540) | [3s](https://github.com/iree-org/iree/actions/runs/27061617150/job/79875280540) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27061617150/job/79875280520) | [3s](https://github.com/iree-org/iree/actions/runs/27061712253/job/79875521280) | [3s](https://github.com/iree-org/iree/actions/runs/27061712253/job/79875521280) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79875180424) | [3s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79875180424) | [3s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79875180424) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812619) | [3s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812619) | [3s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812619) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812655) | [3s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812655) | [3s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812655) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27054703738/job/79856753743) | [3s](https://github.com/iree-org/iree/actions/runs/27054703738/job/79856753743) | [3s](https://github.com/iree-org/iree/actions/runs/27054703738/job/79856753743) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812624) | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812624) | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812624) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812662) | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812662) | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812662) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812674) | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812674) | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812674) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812651) | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812651) | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812651) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812673) | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812673) | [2s](https://github.com/iree-org/iree/actions/runs/27054719619/job/79856812673) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27061603690/job/79875245573) | [2s](https://github.com/iree-org/iree/actions/runs/27061603690/job/79875245573) | [2s](https://github.com/iree-org/iree/actions/runs/27061603690/job/79875245573) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27061579995/job/79875238975) | [2s](https://github.com/iree-org/iree/actions/runs/27061579995/job/79875238975) | [2s](https://github.com/iree-org/iree/actions/runs/27061579995/job/79875238975) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27061712143/job/79875521203) | [2s](https://github.com/iree-org/iree/actions/runs/27061712143/job/79875521203) | [2s](https://github.com/iree-org/iree/actions/runs/27061712143/job/79875521203) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27061712143/job/79875531381) | [2s](https://github.com/iree-org/iree/actions/runs/27061712143/job/79875531381) | [2s](https://github.com/iree-org/iree/actions/runs/27061712143/job/79875531381) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27061712143/job/79875531368) | [2s](https://github.com/iree-org/iree/actions/runs/27061712143/job/79875531368) | [2s](https://github.com/iree-org/iree/actions/runs/27061712143/job/79875531368) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27061617150/job/79875280523) | [1s](https://github.com/iree-org/iree/actions/runs/27061712253/job/79875521289) | [1s](https://github.com/iree-org/iree/actions/runs/27061712253/job/79875521289) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 310 | 1% (2/310) |  | 13h54m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 262 | 4% (10/262) |  | 14h58m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 238 | 0% (1/238) |  | 15h00m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 222 | 0% (0/222) |  | 15h02m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 71 | 0% (0/71) |  | 16h36m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
