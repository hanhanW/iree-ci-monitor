# iree-ci-monitor

_Updated: 2026-07-19 00:09 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162896001) | [5s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162896010) | — | 3 |
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162896005) | [4s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895969) | 0% (0/1) | 6 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895976) | [3s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895982) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895990) | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162896020) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162896001) | [5s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162896001) | [5s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162896001) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162896010) | [5s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162896010) | [5s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162896010) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895975) | [5s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895975) | [5s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895975) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895969) | [4s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895969) | [4s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895969) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162879435) | [3s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162879435) | [3s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162879435) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895982) | [3s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895982) | [3s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895982) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895976) | [3s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895976) | [3s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895976) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29675766398/job/88162811554) | [3s](https://github.com/iree-org/iree/actions/runs/29675766398/job/88162811554) | [3s](https://github.com/iree-org/iree/actions/runs/29675766398/job/88162811554) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162896005) | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162896005) | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162896005) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895995) | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895995) | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895995) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895992) | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895992) | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895992) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162896020) | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162896020) | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162896020) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895990) | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895990) | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88162895990) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 175 | 1% (1/175) |  | 1d08h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 141 | 9% (13/141) |  | 1d08h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 150 | 1% (2/150) |  | 1d08h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 137 | 0% (0/137) |  | 1d08h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 41 | 0% (0/41) |  | 1d08h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
