# iree-ci-monitor

_Updated: 2026-11-07 05:10 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028310) | [4s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028320) | — | 3 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028316) | [3s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028322) | — | 2 |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/42358920815/job/128362929972) | [2s](https://github.com/iree-org/iree/actions/runs/42358839014/job/128362904293) | 0% (0/1) | 10 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/42358979456/job/128363105282) | [2s](https://github.com/iree-org/iree/actions/runs/42358979456/job/128363105461) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028393) | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028396) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028310) | [4s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028310) | [4s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028310) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028282) | [4s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028282) | [4s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028282) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028320) | [4s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028320) | [4s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028320) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028322) | [3s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028322) | [3s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028322) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128362666404) | [2s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128362666404) | [2s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128362666404) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028332) | [2s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028332) | [2s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028332) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028316) | [2s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028316) | [2s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028316) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128309980162) | [2s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128309980162) | [2s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128309980162) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42341456737/job/128309831565) | [2s](https://github.com/iree-org/iree/actions/runs/42341456737/job/128309831565) | [2s](https://github.com/iree-org/iree/actions/runs/42341456737/job/128309831565) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42358839014/job/128362904293) | [2s](https://github.com/iree-org/iree/actions/runs/42358839014/job/128362904293) | [2s](https://github.com/iree-org/iree/actions/runs/42358839014/job/128362904293) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42358979456/job/128363105461) | [2s](https://github.com/iree-org/iree/actions/runs/42358979456/job/128363105461) | [2s](https://github.com/iree-org/iree/actions/runs/42358979456/job/128363105461) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42358979456/job/128363105086) | [2s](https://github.com/iree-org/iree/actions/runs/42358979456/job/128363105086) | [2s](https://github.com/iree-org/iree/actions/runs/42358979456/job/128363105086) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42358979456/job/128363105282) | [2s](https://github.com/iree-org/iree/actions/runs/42358979456/job/128363105282) | [2s](https://github.com/iree-org/iree/actions/runs/42358979456/job/128363105282) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028355) | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028355) | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028355) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028317) | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028317) | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028317) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028295) | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028295) | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028295) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028393) | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028393) | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028393) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028396) | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028396) | [1s](https://github.com/iree-org/iree/actions/runs/42341503754/job/128310028396) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/42358920815/job/128362929972) | [1s](https://github.com/iree-org/iree/actions/runs/42358920815/job/128362929972) | [1s](https://github.com/iree-org/iree/actions/runs/42358920815/job/128362929972) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/42358839014/job/128362688249) | [1s](https://github.com/iree-org/iree/actions/runs/42358839014/job/128362688249) | [1s](https://github.com/iree-org/iree/actions/runs/42358839014/job/128362688249) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 506 | 1% (4/506) |  | 17h46m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 398 | 1% (3/398) |  | 19h03m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
