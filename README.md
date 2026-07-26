# iree-ci-monitor

_Updated: 2026-07-26 00:12 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550877) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762534108) | 0% (0/1) | 6 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550857) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550868) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550882) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550871) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550896) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550918) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550871) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550871) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550871) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550868) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550868) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550868) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762534108) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762534108) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762534108) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550918) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550918) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550918) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550882) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550882) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550882) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550879) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550879) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550879) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550887) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550887) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550887) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550877) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550877) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550877) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550890) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550890) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550890) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550864) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550864) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550864) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550857) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550857) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550857) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550896) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550896) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550896) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190387204/job/89762484443) | [2s](https://github.com/iree-org/iree/actions/runs/30190387204/job/89762484443) | [2s](https://github.com/iree-org/iree/actions/runs/30190387204/job/89762484443) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 269 | 1% (3/269) |  | 1d14h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 368 | 1% (5/368) |  | 1d14h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 300 | 5% (14/300) |  | 1d14h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 281 | 1% (2/281) |  | 1d14h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 84 | 1% (1/84) |  | 1d15h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
