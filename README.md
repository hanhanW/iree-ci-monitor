# iree-ci-monitor

_Updated: 2026-08-02 00:10 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655803) | [8s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655800) | 0% (0/1) | 6 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655816) | [3s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655796) | — | 3 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655806) | [3s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655815) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655808) | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655820) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655800) | [8s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655800) | [8s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655800) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462633959) | [8s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462633959) | [8s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462633959) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655817) | [4s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655817) | [4s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655817) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655796) | [3s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655796) | [3s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655796) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655803) | [3s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655803) | [3s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655803) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655815) | [3s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655815) | [3s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655815) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30735174231/job/91462567796) | [3s](https://github.com/iree-org/iree/actions/runs/30735174231/job/91462567796) | [3s](https://github.com/iree-org/iree/actions/runs/30735174231/job/91462567796) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655810) | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655810) | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655810) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655816) | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655816) | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655816) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655812) | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655812) | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655812) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655806) | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655806) | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655806) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655820) | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655820) | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655820) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655808) | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655808) | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91462655808) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 166 | 0% (0/166) |  | 1d10h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 118 | 1% (1/118) |  | 1d10h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 148 | 3% (4/148) |  | 1d10h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 123 | 1% (1/123) |  | 1d10h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 37 | 3% (1/37) |  | 1d11h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
