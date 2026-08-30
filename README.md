# iree-ci-monitor

_Updated: 2026-08-29 22:28 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 3 | [4s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081546) | [4s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081550) | — | 3 |
| `ubuntu-24.04` | github-hosted | 7 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081553) | [3s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081557) | 0% (0/1) | 6 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081563) | [3s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081573) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081567) | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081587) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081550) | [4s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081550) | [4s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081550) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081545) | [4s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081545) | [4s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081545) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081546) | [4s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081546) | [4s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081546) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081557) | [3s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081557) | [3s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081557) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081573) | [3s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081573) | [3s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081573) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211060856) | [3s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211060856) | [3s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211060856) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081575) | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081575) | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081575) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081553) | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081553) | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081553) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081527) | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081527) | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081527) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081563) | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081563) | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081563) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081567) | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081567) | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081567) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081587) | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081587) | [2s](https://github.com/iree-org/iree/actions/runs/33294240130/job/99211081587) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33294220137/job/99211004922) | [2s](https://github.com/iree-org/iree/actions/runs/33294220137/job/99211004922) | [2s](https://github.com/iree-org/iree/actions/runs/33294220137/job/99211004922) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | 0s | 0s | 0s | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 303 | 1% (2/303) |  | 1d10h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 260 | 3% (8/260) |  | 1d12h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 216 | 0% (1/216) |  | 1d12h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 212 | 0% (0/212) |  | 1d12h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
