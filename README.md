# iree-ci-monitor

_Updated: 2026-07-22 00:12 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555205) | [4s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844518425) | 50% (2/4) | 9 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555192) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555280) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555201) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555219) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555246) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555216) | — | 3 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844518425) | [4s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844518425) | [4s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844518425) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555216) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555216) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555216) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555217) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555217) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555217) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555205) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555205) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555205) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555261) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555261) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555261) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555226) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555226) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555226) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555192) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555192) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555192) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555280) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555280) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555280) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555219) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555219) | [3s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555219) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29893008773/job/88837091248) | [3s](https://github.com/iree-org/iree/actions/runs/29893008773/job/88837091248) | [3s](https://github.com/iree-org/iree/actions/runs/29893008773/job/88837091248) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555203) | [2s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555203) | [2s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555203) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555246) | [2s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555246) | [2s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555246) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555201) | [2s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555201) | [2s](https://github.com/iree-org/iree/actions/runs/29895445547/job/88844555201) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29893008773/job/88837091238) | [2s](https://github.com/iree-org/iree/actions/runs/29893008773/job/88837091238) | [2s](https://github.com/iree-org/iree/actions/runs/29893008773/job/88837091238) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29893008773/job/88838521753) | [2s](https://github.com/iree-org/iree/actions/runs/29893008773/job/88838521753) | [2s](https://github.com/iree-org/iree/actions/runs/29893008773/job/88838521753) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29895406519/job/88844397480) | [2s](https://github.com/iree-org/iree/actions/runs/29895406519/job/88844397480) | [2s](https://github.com/iree-org/iree/actions/runs/29895406519/job/88844397480) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 266 | 0% (1/266) |  | 10h03m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 219 | 4% (8/219) |  | 10h11m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 207 | 1% (2/207) |  | 10h30m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 200 | 0% (0/200) |  | 10h38m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 62 | 0% (0/62) |  | 10h58m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
