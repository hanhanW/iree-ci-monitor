# iree-ci-monitor

_Updated: 2026-11-13 22:33 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769068) | [5s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769104) | — | 3 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769079) | [3s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769230) | — | 2 |
| `ubuntu-24.04` | github-hosted | 15 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/43470421519/job/132161254416) | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769026) | 0% (0/3) | 15 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769016) | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769062) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769104) | [5s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769104) | [5s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769104) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769025) | [4s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769025) | [4s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769025) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769068) | [4s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769068) | [4s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769068) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769103) | [3s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769103) | [3s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769103) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769230) | [3s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769230) | [3s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769230) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769079) | [3s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769079) | [3s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769079) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43465894725/job/132184900043) | [2s](https://github.com/iree-org/iree/actions/runs/43494869895/job/132175992303) | [2s](https://github.com/iree-org/iree/actions/runs/43494869895/job/132175992303) | 9 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769003) | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769003) | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769003) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769026) | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769026) | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769026) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769005) | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769005) | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769005) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769016) | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769016) | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769016) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769062) | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769062) | [2s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341769062) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43560064548/job/132341534288) | [2s](https://github.com/iree-org/iree/actions/runs/43560064548/job/132341534288) | [2s](https://github.com/iree-org/iree/actions/runs/43560064548/job/132341534288) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341701488) | [1s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341701488) | [1s](https://github.com/iree-org/iree/actions/runs/43560117850/job/132341701488) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 381 | 1% (2/381) |  | 8h39m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 325 | 1% (3/325) |  | 9h10m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
