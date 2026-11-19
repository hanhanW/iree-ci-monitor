# iree-ci-monitor

_Updated: 2026-11-18 23:32 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147347) | [5s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147278) | — | 3 |
| `ubuntu-24.04` | github-hosted | 15 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/44463236495/job/135354790594) | [3s](https://github.com/iree-org/iree/actions/runs/44439277963/job/135275787995) | 0% (0/4) | 15 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147280) | [3s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147344) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147314) | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147400) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147278) | [5s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147278) | [5s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147278) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147347) | [4s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147347) | [4s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147347) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147216) | [4s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147216) | [4s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147216) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44364834103/job/135189637092) | [3s](https://github.com/iree-org/iree/actions/runs/44329483333/job/135156341831) | [3s](https://github.com/iree-org/iree/actions/runs/44329483333/job/135156341831) | 4 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44437217544/job/135269006307) | [3s](https://github.com/iree-org/iree/actions/runs/44439277963/job/135275787995) | [3s](https://github.com/iree-org/iree/actions/runs/44439277963/job/135275787995) | 2 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147331) | [3s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147331) | [3s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147331) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147344) | [3s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147344) | [3s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147344) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147251) | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147251) | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147251) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147233) | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147233) | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147233) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147321) | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147321) | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147321) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147280) | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147280) | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147280) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355065516) | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355065516) | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355065516) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147400) | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147400) | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147400) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147314) | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147314) | [2s](https://github.com/iree-org/iree/actions/runs/44463321744/job/135355147314) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44456969550/job/135334242943) | [2s](https://github.com/iree-org/iree/actions/runs/44456969550/job/135334242943) | [2s](https://github.com/iree-org/iree/actions/runs/44456969550/job/135334242943) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44456969550/job/135334243351) | [2s](https://github.com/iree-org/iree/actions/runs/44456969550/job/135334243351) | [2s](https://github.com/iree-org/iree/actions/runs/44456969550/job/135334243351) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44456969550/job/135337318062) | [2s](https://github.com/iree-org/iree/actions/runs/44456969550/job/135337318062) | [2s](https://github.com/iree-org/iree/actions/runs/44456969550/job/135337318062) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44463236495/job/135354790594) | [2s](https://github.com/iree-org/iree/actions/runs/44463236495/job/135354790594) | [2s](https://github.com/iree-org/iree/actions/runs/44463236495/job/135354790594) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 276 | 1% (2/276) |  | 8h46m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 332 | 0% (1/332) |  | 12h58m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
