# iree-ci-monitor

_Updated: 2026-05-24 00:27 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913749) | [3s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913753) | 0% (0/1) | 6 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913767) | [3s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913751) | — | 3 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913775) | [3s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913766) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913770) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913772) | — | 2 |
| `azure-linux-scale` | ossci | 1 | 1 | [10m39s](https://github.com/iree-org/iree/actions/runs/26212319110/job/77181582238) | 2026-05-21 06:27 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [10m39s](https://github.com/iree-org/iree/actions/runs/26212319110/job/77181582238) | 2026-05-21 06:27 PDT | `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | `promote-contraction-outputs` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 1 | [10m39s](https://github.com/iree-org/iree/actions/runs/26212319110/job/77181582238) | 2026-05-21 06:27 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913751) | [3s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913751) | [3s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913751) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913753) | [3s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913753) | [3s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913753) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913766) | [3s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913766) | [3s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913766) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913767) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913767) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913767) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913744) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913744) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913744) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913778) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913778) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913778) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913749) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913749) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913749) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913776) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913776) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913776) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913775) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913775) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913775) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576905119) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576905119) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576905119) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913770) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913770) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913770) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913772) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913772) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77576913772) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26353847323/job/77576870670) | [1s](https://github.com/iree-org/iree/actions/runs/26353847323/job/77576870670) | [1s](https://github.com/iree-org/iree/actions/runs/26353847323/job/77576870670) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 300 | 2% (5/299) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 270 | 7% (20/269) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 229 | 3% (7/228) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 224 | 1% (2/223) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 71 | 3% (2/71) |  | 1d12h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
