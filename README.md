# iree-ci-monitor

_Updated: 2026-11-19 23:23 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548420) | [4s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548458) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548340) | [3s](https://github.com/iree-org/iree/actions/runs/44679181661/job/136098213814) | 0% (0/4) | 9 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548403) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548506) | — | 2 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548405) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548565) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548386) | [4s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548386) | [4s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548386) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548420) | [4s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548420) | [4s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548420) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548458) | [4s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548458) | [4s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548458) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/44679181661/job/136098213814) | [3s](https://github.com/iree-org/iree/actions/runs/44679181661/job/136098213814) | [3s](https://github.com/iree-org/iree/actions/runs/44679181661/job/136098213814) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548340) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548340) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548340) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548381) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548381) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548381) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548434) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548434) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548434) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548447) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548447) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548447) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548565) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548565) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548565) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548405) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548405) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548405) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098477354) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098477354) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098477354) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548506) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548506) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548506) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548403) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548403) | [2s](https://github.com/iree-org/iree/actions/runs/44679263331/job/136098548403) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44673120712/job/136078516088) | [2s](https://github.com/iree-org/iree/actions/runs/44673120712/job/136078516088) | [2s](https://github.com/iree-org/iree/actions/runs/44673120712/job/136078516088) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44673120712/job/136078516455) | [2s](https://github.com/iree-org/iree/actions/runs/44673120712/job/136078516455) | [2s](https://github.com/iree-org/iree/actions/runs/44673120712/job/136078516455) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44673120712/job/136081260455) | [2s](https://github.com/iree-org/iree/actions/runs/44673120712/job/136081260455) | [2s](https://github.com/iree-org/iree/actions/runs/44673120712/job/136081260455) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 264 | 2% (4/264) |  | 13h24m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 216 | 1% (3/216) |  | 13h28m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
