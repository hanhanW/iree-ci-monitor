# iree-ci-monitor

_Updated: 2026-11-11 23:18 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316570) | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316764) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/43159487021/job/130987035658) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316622) | 0% (0/4) | 9 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316620) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316657) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316775) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316790) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316570) | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316570) | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316570) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316764) | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316764) | [5s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316764) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316566) | [4s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316566) | [4s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316566) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316622) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316622) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316622) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316657) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316657) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316657) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316620) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316620) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316620) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316790) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316790) | [3s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316790) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316678) | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316678) | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316678) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316545) | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316545) | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316545) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316592) | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316592) | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316592) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316775) | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316775) | [2s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987316775) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130968017954) | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130968017954) | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130968017954) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130968018181) | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130968018181) | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130968018181) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130971162447) | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130971162447) | [2s](https://github.com/iree-org/iree/actions/runs/43153513321/job/130971162447) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43159487021/job/130987035658) | [2s](https://github.com/iree-org/iree/actions/runs/43159487021/job/130987035658) | [2s](https://github.com/iree-org/iree/actions/runs/43159487021/job/130987035658) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987237139) | [1s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987237139) | [1s](https://github.com/iree-org/iree/actions/runs/43159550289/job/130987237139) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 314 | 1% (2/314) |  | 11h15m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 266 | 1% (2/266) |  | 11h30m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
