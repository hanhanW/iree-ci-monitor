# iree-ci-monitor

_Updated: 2026-10-10 05:38 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `macos-15` | github-hosted | 2 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584318) | [6s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584358) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584349) | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584392) | — | 3 |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584351) | [3s](https://github.com/iree-org/iree/actions/runs/38045276916/job/114193609722) | 0% (0/1) | 11 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584321) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584342) | — | 2 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/38045384559/job/114193749931) | [2s](https://github.com/iree-org/iree/actions/runs/38045384559/job/114193749969) | — | 3 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584358) | [6s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584358) | [6s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584358) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584318) | [5s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584318) | [5s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584318) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584392) | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584392) | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584392) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584313) | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584313) | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584313) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584349) | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584349) | [4s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584349) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584317) | [3s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584317) | [3s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584317) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584338) | [3s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584338) | [3s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584338) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/38045276916/job/114193609722) | [3s](https://github.com/iree-org/iree/actions/runs/38045276916/job/114193609722) | [3s](https://github.com/iree-org/iree/actions/runs/38045276916/job/114193609722) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114193419524) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114193419524) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114193419524) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584351) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584351) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584351) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584384) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584384) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584384) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139554475) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139554475) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139554475) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584321) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584321) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584321) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584342) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584342) | [2s](https://github.com/iree-org/iree/actions/runs/38026903723/job/114139584342) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38026862940/job/114139437254) | [2s](https://github.com/iree-org/iree/actions/runs/38026862940/job/114139437254) | [2s](https://github.com/iree-org/iree/actions/runs/38026862940/job/114139437254) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38045384559/job/114193749969) | [2s](https://github.com/iree-org/iree/actions/runs/38045384559/job/114193749969) | [2s](https://github.com/iree-org/iree/actions/runs/38045384559/job/114193749969) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/38045343446/job/114193628802) | [1s](https://github.com/iree-org/iree/actions/runs/38045343446/job/114193628802) | [1s](https://github.com/iree-org/iree/actions/runs/38045343446/job/114193628802) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/38049255770/job/114204897555) | [1s](https://github.com/iree-org/iree/actions/runs/38049255770/job/114204897555) | [1s](https://github.com/iree-org/iree/actions/runs/38049255770/job/114204897555) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/38045276916/job/114193438006) | [1s](https://github.com/iree-org/iree/actions/runs/38045276916/job/114193438006) | [1s](https://github.com/iree-org/iree/actions/runs/38045276916/job/114193438006) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/38045384559/job/114193749761) | [1s](https://github.com/iree-org/iree/actions/runs/38045384559/job/114193749761) | [1s](https://github.com/iree-org/iree/actions/runs/38045384559/job/114193749761) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 219 | 15% (33/219) |  | 20h23m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 325 | 0% (0/325) |  | 20h28m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
