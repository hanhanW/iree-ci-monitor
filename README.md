# iree-ci-monitor

_Updated: 2026-06-12 00:57 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792734) | [3s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792738) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792739) | [3s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792756) | — | 2 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972763773) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792767) | 50% (2/4) | 9 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792735) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792751) | — | 3 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792756) | [3s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792756) | [3s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792756) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792734) | [3s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792734) | [3s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792734) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792738) | [3s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792738) | [3s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792738) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792726) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792726) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792726) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792735) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792735) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792735) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792751) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792751) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792751) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792741) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792741) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792741) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792767) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792767) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792767) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792737) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792737) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792737) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792753) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792753) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792753) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792739) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792739) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972792739) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972763773) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972763773) | [2s](https://github.com/iree-org/iree/actions/runs/27399106220/job/80972763773) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27397186656/job/80966867454) | [2s](https://github.com/iree-org/iree/actions/runs/27397186656/job/80966867454) | [2s](https://github.com/iree-org/iree/actions/runs/27397186656/job/80966867454) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27397186656/job/80966867447) | [2s](https://github.com/iree-org/iree/actions/runs/27397186656/job/80966867447) | [2s](https://github.com/iree-org/iree/actions/runs/27397186656/job/80966867447) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27397186656/job/80967864648) | [2s](https://github.com/iree-org/iree/actions/runs/27397186656/job/80967864648) | [2s](https://github.com/iree-org/iree/actions/runs/27397186656/job/80967864648) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27399080516/job/80972679661) | [1s](https://github.com/iree-org/iree/actions/runs/27399080516/job/80972679661) | [1s](https://github.com/iree-org/iree/actions/runs/27399080516/job/80972679661) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 366 | 2% (8/366) |  | 10h30m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 264 | 2% (5/264) |  | 10h37m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 308 | 7% (21/308) |  | 10h44m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 273 | 2% (5/273) |  | 10h45m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 87 | 1% (1/87) |  | 10h50m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
