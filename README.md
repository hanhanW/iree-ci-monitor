# iree-ci-monitor

_Updated: 2026-06-15 01:30 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [5s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886953) | [6s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886947) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886957) | [3s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362887001) | — | 2 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362864250) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886948) | 50% (2/4) | 9 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886941) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886965) | — | 3 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886947) | [6s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886947) | [6s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886947) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886953) | [5s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886953) | [5s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886953) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886957) | [3s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886957) | [3s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886957) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362887001) | [3s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362887001) | [3s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362887001) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886933) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886933) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886933) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886965) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886965) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886965) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886941) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886941) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886941) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886948) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886948) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886948) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886942) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886942) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886942) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886939) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886939) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886939) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886943) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886943) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362886943) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362864250) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362864250) | [2s](https://github.com/iree-org/iree/actions/runs/27529164886/job/81362864250) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27527099632/job/81356602819) | [2s](https://github.com/iree-org/iree/actions/runs/27527099632/job/81356602819) | [2s](https://github.com/iree-org/iree/actions/runs/27527099632/job/81356602819) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27527099632/job/81356602808) | [2s](https://github.com/iree-org/iree/actions/runs/27527099632/job/81356602808) | [2s](https://github.com/iree-org/iree/actions/runs/27527099632/job/81356602808) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27527099632/job/81357601488) | [2s](https://github.com/iree-org/iree/actions/runs/27527099632/job/81357601488) | [2s](https://github.com/iree-org/iree/actions/runs/27527099632/job/81357601488) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27529137560/job/81362772925) | [2s](https://github.com/iree-org/iree/actions/runs/27529137560/job/81362772925) | [2s](https://github.com/iree-org/iree/actions/runs/27529137560/job/81362772925) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 282 | 2% (7/282) |  | 2d17h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 239 | 8% (18/239) |  | 2d17h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 199 | 3% (5/199) |  | 2d17h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 209 | 2% (5/209) |  | 2d17h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 67 | 1% (1/67) |  | 2d17h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
