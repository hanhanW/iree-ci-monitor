# iree-ci-monitor

_Updated: 2026-06-14 00:54 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 2 | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381475) | [7s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381461) | 0% (0/1) | 6 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381464) | [3s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381465) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381434) | [2s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381439) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381466) | [2s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381460) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381461) | [7s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381461) | [7s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381461) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381433) | [3s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381433) | [3s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381433) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381465) | [3s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381465) | [3s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381465) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381434) | [2s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381434) | [2s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381434) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381439) | [2s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381439) | [2s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381439) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381464) | [2s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381464) | [2s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381464) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381460) | [2s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381460) | [2s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381460) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27490780453/job/81255329286) | [2s](https://github.com/iree-org/iree/actions/runs/27490780453/job/81255329286) | [2s](https://github.com/iree-org/iree/actions/runs/27490780453/job/81255329286) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381429) | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381429) | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381429) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381432) | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381432) | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381432) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381475) | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381475) | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381475) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255372536) | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255372536) | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255372536) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381466) | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381466) | [1s](https://github.com/iree-org/iree/actions/runs/27490794430/job/81255381466) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 282 | 2% (7/282) |  | 1d16h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 239 | 8% (18/239) |  | 1d16h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 199 | 3% (5/199) |  | 1d17h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 209 | 2% (5/209) |  | 1d17h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 67 | 1% (1/67) |  | 1d17h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
