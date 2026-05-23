# iree-ci-monitor

_Updated: 2026-05-23 05:39 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 7 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26325338516/job/77501912743) | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964993) | 0% (0/1) | 6 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964997) | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964990) | — | 3 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964989) | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501965008) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501965001) | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501965004) | — | 2 |
| `azure-linux-scale` | ossci | 1 | 1 | [10m39s](https://github.com/iree-org/iree/actions/runs/26212319110/job/77181582238) | 2026-05-21 06:27 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [10m39s](https://github.com/iree-org/iree/actions/runs/26212319110/job/77181582238) | 2026-05-21 06:27 PDT | `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | `promote-contraction-outputs` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 1 | [10m39s](https://github.com/iree-org/iree/actions/runs/26212319110/job/77181582238) | 2026-05-21 06:27 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964990) | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964990) | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964990) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964967) | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964967) | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964967) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964974) | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964974) | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964974) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964993) | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964993) | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964993) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501965008) | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501965008) | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501965008) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501965004) | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501965004) | [3s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501965004) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26325338516/job/77501912743) | [3s](https://github.com/iree-org/iree/actions/runs/26325338516/job/77501912743) | [3s](https://github.com/iree-org/iree/actions/runs/26325338516/job/77501912743) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964987) | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964987) | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964987) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964997) | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964997) | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964997) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964975) | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964975) | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964975) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964989) | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964989) | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501964989) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501953662) | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501953662) | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501953662) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501965001) | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501965001) | [2s](https://github.com/iree-org/iree/actions/runs/26325352641/job/77501965001) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | 0s | 0s | 0s | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 316 | 2% (5/315) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 281 | 7% (20/280) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 238 | 3% (7/237) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 233 | 1% (2/232) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 74 | 3% (2/74) |  | 17h53m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
