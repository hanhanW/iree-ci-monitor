# iree-ci-monitor

_Updated: 2026-10-24 04:09 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665029) | [4s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665055) | — | 3 |
| `ubuntu-24.04` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665106) | [3s](https://github.com/iree-org/iree/actions/runs/40065406607/job/120787494241) | 0% (0/2) | 12 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665081) | [3s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665003) | — | 2 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40088167470/job/120855233590) | [2s](https://github.com/iree-org/iree/actions/runs/40088167470/job/120855233606) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665013) | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665067) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665055) | [4s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665055) | [4s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665055) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665029) | [4s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665029) | [4s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665029) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665024) | [4s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665024) | [4s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665024) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665003) | [3s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665003) | [3s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665003) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40070351503/job/120802253712) | [3s](https://github.com/iree-org/iree/actions/runs/40070351503/job/120802253712) | [3s](https://github.com/iree-org/iree/actions/runs/40070351503/job/120802253712) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40065406607/job/120787494241) | [3s](https://github.com/iree-org/iree/actions/runs/40065406607/job/120787494241) | [3s](https://github.com/iree-org/iree/actions/runs/40065406607/job/120787494241) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120854879545) | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120854879545) | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120854879545) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665075) | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665075) | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665075) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665106) | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665106) | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665106) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665081) | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665081) | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665081) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787624189) | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787624189) | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787624189) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665067) | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665067) | [2s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665067) | 1 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40070314099/job/120802139414) | [2s](https://github.com/iree-org/iree/actions/runs/40070314099/job/120802139414) | [2s](https://github.com/iree-org/iree/actions/runs/40070314099/job/120802139414) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40088049884/job/120855090089) | [2s](https://github.com/iree-org/iree/actions/runs/40088049884/job/120855090089) | [2s](https://github.com/iree-org/iree/actions/runs/40088049884/job/120855090089) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40088167470/job/120855233590) | [2s](https://github.com/iree-org/iree/actions/runs/40088167470/job/120855233590) | [2s](https://github.com/iree-org/iree/actions/runs/40088167470/job/120855233590) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40088167470/job/120855233606) | [2s](https://github.com/iree-org/iree/actions/runs/40088167470/job/120855233606) | [2s](https://github.com/iree-org/iree/actions/runs/40088167470/job/120855233606) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40088167470/job/120855233352) | [2s](https://github.com/iree-org/iree/actions/runs/40088167470/job/120855233352) | [2s](https://github.com/iree-org/iree/actions/runs/40088167470/job/120855233352) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665004) | [1s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665004) | [1s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665004) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665082) | [1s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665082) | [1s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665082) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665013) | [1s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665013) | [1s](https://github.com/iree-org/iree/actions/runs/40065448704/job/120787665013) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 402 | 0% (0/402) |  | 18h43m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 333 | 2% (7/333) |  | 18h49m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
