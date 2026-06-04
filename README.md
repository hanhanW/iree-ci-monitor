# iree-ci-monitor

_Updated: 2026-06-04 00:57 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [6s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277161) | [7s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277202) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463251509) | [4s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277291) | 50% (2/4) | 9 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277144) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277165) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277185) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277188) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277202) | [7s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277202) | [7s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277202) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277161) | [6s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277161) | [6s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277161) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277226) | [5s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277226) | [5s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277226) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277291) | [4s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277291) | [4s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277291) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277206) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277206) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277206) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277180) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277180) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277180) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277165) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277165) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277165) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277188) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277188) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277188) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277185) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277185) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277185) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277145) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277145) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277145) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277144) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277144) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277144) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463251509) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463251509) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463251509) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79457641566) | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79457641566) | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79457641566) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79457641603) | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79457641603) | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79457641603) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79458665926) | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79458665926) | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79458665926) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26935194498/job/79463161859) | [2s](https://github.com/iree-org/iree/actions/runs/26935194498/job/79463161859) | [2s](https://github.com/iree-org/iree/actions/runs/26935194498/job/79463161859) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 274 | 4% (11/273) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 301 | 0% (1/301) |  | 11h11m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 208 | 1% (2/208) |  | 11h16m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 212 | 0% (0/212) |  | 11h25m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 68 | 1% (1/68) |  | 11h28m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
