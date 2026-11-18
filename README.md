# iree-ci-monitor

_Updated: 2026-11-17 23:36 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181431) | [5s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181442) | — | 3 |
| `ubuntu-24.04` | github-hosted | 15 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134575272978) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181398) | 0% (0/6) | 15 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181401) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181470) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181471) | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181535) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181442) | [5s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181442) | [5s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181442) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181431) | [4s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181431) | [4s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181431) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181395) | [4s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181395) | [4s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181395) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44101886801/job/134447047576) | [3s](https://github.com/iree-org/iree/actions/runs/44130381409/job/134441097183) | [3s](https://github.com/iree-org/iree/actions/runs/44130381409/job/134441097183) | 5 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181323) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181323) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181323) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181398) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181398) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181398) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181380) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181380) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181380) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181528) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181528) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181528) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181470) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181470) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181470) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181401) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181401) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181401) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593047805) | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593047805) | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593047805) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181471) | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181471) | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181471) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181535) | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181535) | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181535) | 1 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44228612446/job/134547846965) | [2s](https://github.com/iree-org/iree/actions/runs/44228612446/job/134547846965) | [2s](https://github.com/iree-org/iree/actions/runs/44228612446/job/134547846965) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134572037536) | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134572037536) | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134572037536) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134572037844) | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134572037844) | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134572037844) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134575272978) | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134575272978) | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134575272978) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44242266866/job/134592747071) | [2s](https://github.com/iree-org/iree/actions/runs/44242266866/job/134592747071) | [2s](https://github.com/iree-org/iree/actions/runs/44242266866/job/134592747071) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 363 | 0% (0/363) |  | 6h51m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 311 | 1% (2/311) |  | 12h51m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
