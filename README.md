# iree-ci-monitor

_Updated: 2026-07-13 00:27 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976698) | [6s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976738) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976685) | [3s](https://github.com/iree-org/iree/actions/runs/29225944967/job/86739882296) | 50% (2/4) | 9 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976744) | [3s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976717) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976694) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976780) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976738) | [6s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976738) | [6s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976738) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976682) | [5s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976682) | [5s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976682) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976698) | [5s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976698) | [5s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976698) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976717) | [3s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976717) | [3s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976717) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29225944967/job/86739882296) | [3s](https://github.com/iree-org/iree/actions/runs/29225944967/job/86739882296) | [3s](https://github.com/iree-org/iree/actions/runs/29225944967/job/86739882296) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976685) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976685) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976685) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976736) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976736) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976736) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976707) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976707) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976707) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976752) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976752) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976752) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976744) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976744) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976744) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745948178) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745948178) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745948178) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976694) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976694) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976694) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976780) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976780) | [2s](https://github.com/iree-org/iree/actions/runs/29227954059/job/86745976780) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29227918947/job/86745844209) | [2s](https://github.com/iree-org/iree/actions/runs/29227918947/job/86745844209) | [2s](https://github.com/iree-org/iree/actions/runs/29227918947/job/86745844209) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29225944967/job/86739882289) | [1s](https://github.com/iree-org/iree/actions/runs/29225944967/job/86739882289) | [1s](https://github.com/iree-org/iree/actions/runs/29225944967/job/86739882289) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29225944967/job/86741038925) | [1s](https://github.com/iree-org/iree/actions/runs/29225944967/job/86741038925) | [1s](https://github.com/iree-org/iree/actions/runs/29225944967/job/86741038925) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 154 | 7% (11/153) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 198 | 2% (3/197) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 159 | 1% (1/158) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 147 | 1% (1/146) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 46 | 11% (5/46) |  | 2d19h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
