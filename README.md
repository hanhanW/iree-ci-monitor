# iree-ci-monitor

_Updated: 2026-07-26 05:41 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550890) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762534108) | 0% (0/1) | 10 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550857) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550868) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550882) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550871) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550896) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550918) | — | 2 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30201166036/job/89791232654) | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246729) | — | 6 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550871) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550871) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550871) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550868) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550868) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550868) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762534108) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762534108) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762534108) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550918) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550918) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550918) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246729) | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246729) | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246729) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246703) | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246703) | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246703) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89790618255) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89790618255) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89790618255) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550882) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550882) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550882) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550879) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550879) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550879) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550887) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550887) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550887) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550877) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550877) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550877) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550890) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550890) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550890) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550864) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550864) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550864) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550857) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550857) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550857) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550896) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550896) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550896) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30200981179/job/89790751679) | [2s](https://github.com/iree-org/iree/actions/runs/30200981179/job/89790751679) | [2s](https://github.com/iree-org/iree/actions/runs/30200981179/job/89790751679) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190387204/job/89762484443) | [2s](https://github.com/iree-org/iree/actions/runs/30190387204/job/89762484443) | [2s](https://github.com/iree-org/iree/actions/runs/30190387204/job/89762484443) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790742626) | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790742626) | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790742626) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790627825) | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790627825) | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790627825) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30201166036/job/89791232679) | [2s](https://github.com/iree-org/iree/actions/runs/30201166036/job/89791232679) | [2s](https://github.com/iree-org/iree/actions/runs/30201166036/job/89791232679) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 269 | 1% (3/269) |  | 1d20h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 368 | 1% (5/368) |  | 1d20h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 300 | 5% (14/300) |  | 1d20h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 281 | 1% (2/281) |  | 1d20h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 84 | 1% (1/84) |  | 1d20h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
