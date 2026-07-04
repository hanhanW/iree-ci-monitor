# iree-ci-monitor

_Updated: 2026-07-04 05:43 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761311) | [6s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761333) | — | 3 |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85130060519) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761330) | 0% (0/1) | 10 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761317) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761324) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761319) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761332) | — | 2 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28705529588/job/85130455227) | [3s](https://github.com/iree-org/iree/actions/runs/28705414261/job/85130158726) | — | 9 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761311) | [6s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761311) | [6s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761311) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761333) | [6s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761333) | [6s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761333) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761323) | [5s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761323) | [5s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761323) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28705529800/job/85130444617) | [3s](https://github.com/iree-org/iree/actions/runs/28705414261/job/85130158726) | [3s](https://github.com/iree-org/iree/actions/runs/28705414261/job/85130158726) | 2 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761327) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761327) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761327) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761330) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761330) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761330) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761324) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761324) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761324) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761332) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761332) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761332) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28705414261/job/85130158719) | [2s](https://github.com/iree-org/iree/actions/runs/28705529800/job/85130444627) | [2s](https://github.com/iree-org/iree/actions/runs/28705529800/job/85130444627) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28705414261/job/85130158721) | [2s](https://github.com/iree-org/iree/actions/runs/28705529800/job/85130444610) | [2s](https://github.com/iree-org/iree/actions/runs/28705529800/job/85130444610) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85130060519) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85130060519) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85130060519) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761328) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761328) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761328) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761321) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761321) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761321) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761317) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761317) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761317) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761319) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761319) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761319) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28705400757/job/85130123250) | [2s](https://github.com/iree-org/iree/actions/runs/28705400757/job/85130123250) | [2s](https://github.com/iree-org/iree/actions/runs/28705400757/job/85130123250) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28705376803/job/85130118102) | [2s](https://github.com/iree-org/iree/actions/runs/28705376803/job/85130118102) | [2s](https://github.com/iree-org/iree/actions/runs/28705376803/job/85130118102) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28705376803/job/85130065998) | [2s](https://github.com/iree-org/iree/actions/runs/28705376803/job/85130065998) | [2s](https://github.com/iree-org/iree/actions/runs/28705376803/job/85130065998) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28705529588/job/85130455211) | [2s](https://github.com/iree-org/iree/actions/runs/28705529588/job/85130455211) | [2s](https://github.com/iree-org/iree/actions/runs/28705529588/job/85130455211) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28705529588/job/85130455227) | [2s](https://github.com/iree-org/iree/actions/runs/28705529588/job/85130455227) | [2s](https://github.com/iree-org/iree/actions/runs/28705529588/job/85130455227) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 271 | 7% (20/271) |  | 15h10m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 210 | 1% (3/210) |  | 15h17m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 301 | 2% (7/301) |  | 15h18m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 234 | 1% (3/234) |  | 15h21m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 71 | 1% (1/71) |  | 15h39m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
