# iree-ci-monitor

_Updated: 2026-06-18 01:02 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698588) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698596) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698574) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698657) | — | 2 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698572) | [3s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698620) | 50% (2/4) | 9 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698603) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698686) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698588) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698588) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698588) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698596) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698596) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698596) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698566) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698566) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698566) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698657) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698657) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698657) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698620) | [3s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698620) | [3s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698620) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82063361011) | [3s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82063361011) | [3s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82063361011) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82064477870) | [3s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82064477870) | [3s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82064477870) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698572) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698572) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698572) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698592) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698592) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698592) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698603) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698603) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698603) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698686) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698686) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698686) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069675368) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069675368) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069675368) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698574) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698574) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698574) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27741514631/job/82069586801) | [2s](https://github.com/iree-org/iree/actions/runs/27741514631/job/82069586801) | [2s](https://github.com/iree-org/iree/actions/runs/27741514631/job/82069586801) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698580) | [1s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698580) | [1s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698580) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82063361021) | [1s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82063361021) | [1s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82063361021) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 171 | 5% (9/171) |  | 10h19m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 229 | 0% (0/229) |  | 10h23m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 175 | 1% (1/175) |  | 10h26m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 164 | 0% (0/164) |  | 10h28m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 52 | 0% (0/52) |  | 10h30m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
