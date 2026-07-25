# iree-ci-monitor

_Updated: 2026-07-25 05:41 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636857) | [4s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636944) | — | 3 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30156562912/job/89675352927) | [4s](https://github.com/iree-org/iree/actions/runs/30156418353/job/89674994274) | — | 9 |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30156349799/job/89674821579) | [3s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89674810918) | 0% (0/1) | 10 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636854) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636881) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636861) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636862) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30156563140/job/89675353613) | [4s](https://github.com/iree-org/iree/actions/runs/30156418353/job/89674994274) | [4s](https://github.com/iree-org/iree/actions/runs/30156418353/job/89674994274) | 2 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636944) | [4s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636944) | [4s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636944) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89674810918) | [3s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89674810918) | [3s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89674810918) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636876) | [3s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636876) | [3s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636876) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636869) | [3s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636869) | [3s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636869) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30156562912/job/89675362953) | [3s](https://github.com/iree-org/iree/actions/runs/30156562912/job/89675362953) | [3s](https://github.com/iree-org/iree/actions/runs/30156562912/job/89675362953) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30156562912/job/89675362964) | [3s](https://github.com/iree-org/iree/actions/runs/30156562912/job/89675362964) | [3s](https://github.com/iree-org/iree/actions/runs/30156562912/job/89675362964) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30156418353/job/89674994312) | [2s](https://github.com/iree-org/iree/actions/runs/30156563140/job/89675353643) | [2s](https://github.com/iree-org/iree/actions/runs/30156563140/job/89675353643) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30156563140/job/89675353647) | [2s](https://github.com/iree-org/iree/actions/runs/30156418353/job/89674994275) | [2s](https://github.com/iree-org/iree/actions/runs/30156418353/job/89674994275) | 2 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636851) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636851) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636851) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636857) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636857) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636857) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636849) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636849) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636849) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636888) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636888) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636888) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636862) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636862) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636862) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636861) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636861) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636861) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636881) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636881) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636881) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636854) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636854) | [2s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89649636854) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30156399834/job/89674947661) | [2s](https://github.com/iree-org/iree/actions/runs/30156399834/job/89674947661) | [2s](https://github.com/iree-org/iree/actions/runs/30156399834/job/89674947661) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30156349799/job/89674940871) | [2s](https://github.com/iree-org/iree/actions/runs/30156349799/job/89674940871) | [2s](https://github.com/iree-org/iree/actions/runs/30156349799/job/89674940871) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30156349799/job/89674821579) | [2s](https://github.com/iree-org/iree/actions/runs/30156349799/job/89674821579) | [2s](https://github.com/iree-org/iree/actions/runs/30156349799/job/89674821579) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 269 | 1% (3/269) |  | 20h17m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 368 | 1% (5/368) |  | 20h19m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 300 | 5% (14/300) |  | 20h20m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 281 | 1% (2/281) |  | 20h21m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 84 | 1% (1/84) |  | 20h34m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
