# iree-ci-monitor

_Updated: 2026-07-02 00:28 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704889997) | [6s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704889977) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704889999) | [3s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890009) | 50% (2/4) | 9 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890035) | [3s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890057) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890137) | [3s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890056) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704889977) | [6s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704889977) | [6s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704889977) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704889990) | [5s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704889990) | [5s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704889990) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704889997) | [5s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704889997) | [5s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704889997) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890009) | [3s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890009) | [3s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890009) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890056) | [3s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890056) | [3s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890056) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890057) | [3s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890057) | [3s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890057) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28567602696/job/84698058033) | [3s](https://github.com/iree-org/iree/actions/runs/28567602696/job/84698058033) | [3s](https://github.com/iree-org/iree/actions/runs/28567602696/job/84698058033) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890000) | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890000) | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890000) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704889999) | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704889999) | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704889999) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890002) | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890002) | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890002) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890137) | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890137) | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890137) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704866898) | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704866898) | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704866898) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890035) | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890035) | [2s](https://github.com/iree-org/iree/actions/runs/28569818936/job/84704890035) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28567602696/job/84699194885) | [2s](https://github.com/iree-org/iree/actions/runs/28567602696/job/84699194885) | [2s](https://github.com/iree-org/iree/actions/runs/28567602696/job/84699194885) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28567602696/job/84698058058) | [1s](https://github.com/iree-org/iree/actions/runs/28567602696/job/84698058058) | [1s](https://github.com/iree-org/iree/actions/runs/28567602696/job/84698058058) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28569791456/job/84704775784) | [1s](https://github.com/iree-org/iree/actions/runs/28569791456/job/84704775784) | [1s](https://github.com/iree-org/iree/actions/runs/28569791456/job/84704775784) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 198 | 8% (16/198) |  | 13h34m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 226 | 1% (2/226) |  | 13h48m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 159 | 1% (1/159) |  | 13h48m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 185 | 1% (1/185) |  | 13h56m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 52 | 0% (0/52) |  | 13h56m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
