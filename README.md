# iree-ci-monitor

_Updated: 2026-06-08 01:06 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630367) | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630461) | — | 3 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630340) | [3s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630593) | — | 2 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035607418) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630390) | 50% (2/4) | 9 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630347) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630434) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630461) | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630461) | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630461) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630338) | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630338) | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630338) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630367) | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630367) | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630367) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630340) | [3s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630340) | [3s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630340) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630593) | [3s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630593) | [3s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630593) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630390) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630390) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630390) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630354) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630354) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630354) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630344) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630344) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630344) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630382) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630382) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630382) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035607418) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035607418) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035607418) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630347) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630347) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630347) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630434) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630434) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630434) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27118497495/job/80030177510) | [2s](https://github.com/iree-org/iree/actions/runs/27118497495/job/80030177510) | [2s](https://github.com/iree-org/iree/actions/runs/27118497495/job/80030177510) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27118497495/job/80030177491) | [2s](https://github.com/iree-org/iree/actions/runs/27118497495/job/80030177491) | [2s](https://github.com/iree-org/iree/actions/runs/27118497495/job/80030177491) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27118497495/job/80031096415) | [2s](https://github.com/iree-org/iree/actions/runs/27118497495/job/80031096415) | [2s](https://github.com/iree-org/iree/actions/runs/27118497495/job/80031096415) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27120261298/job/80035518258) | [1s](https://github.com/iree-org/iree/actions/runs/27120261298/job/80035518258) | [1s](https://github.com/iree-org/iree/actions/runs/27120261298/job/80035518258) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 292 | 1% (2/292) |  | 2d09h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 247 | 3% (8/247) |  | 2d10h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 224 | 0% (1/224) |  | 2d10h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 209 | 0% (0/209) |  | 2d10h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 67 | 0% (0/67) |  | 2d11h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
