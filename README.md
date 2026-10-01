# iree-ci-monitor

_Updated: 2026-09-30 23:02 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [7s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435429) | [8s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435357) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435318) | [4s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435358) | — | 3 |
| `ubuntu-24.04` | github-hosted | 12 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/36815105236/job/110220620763) | [3s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435526) | 0% (0/4) | 12 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435463) | [3s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435396) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435357) | [8s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435357) | [8s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435357) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435429) | [7s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435429) | [7s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435429) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435353) | [5s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435353) | [5s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435353) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435358) | [4s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435358) | [4s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435358) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435318) | [4s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435318) | [4s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435318) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435305) | [4s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435305) | [4s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435305) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435526) | [3s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435526) | [3s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435526) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435396) | [3s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435396) | [3s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435396) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36818985279/job/110230217735) | [3s](https://github.com/iree-org/iree/actions/runs/36818985279/job/110230217735) | [3s](https://github.com/iree-org/iree/actions/runs/36818985279/job/110230217735) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36741548409/job/110083612534) | [2s](https://github.com/iree-org/iree/actions/runs/36744576359/job/110084292466) | [2s](https://github.com/iree-org/iree/actions/runs/36744576359/job/110084292466) | 2 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435392) | [2s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435392) | [2s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435392) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435454) | [2s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435454) | [2s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435454) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435463) | [2s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435463) | [2s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230435463) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36744576058/job/110138173484) | [2s](https://github.com/iree-org/iree/actions/runs/36744576058/job/110138173484) | [2s](https://github.com/iree-org/iree/actions/runs/36744576058/job/110138173484) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36815105236/job/110218350374) | [2s](https://github.com/iree-org/iree/actions/runs/36815105236/job/110218350374) | [2s](https://github.com/iree-org/iree/actions/runs/36815105236/job/110218350374) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36815105236/job/110218350638) | [2s](https://github.com/iree-org/iree/actions/runs/36815105236/job/110218350638) | [2s](https://github.com/iree-org/iree/actions/runs/36815105236/job/110218350638) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36815105236/job/110220620763) | [2s](https://github.com/iree-org/iree/actions/runs/36815105236/job/110220620763) | [2s](https://github.com/iree-org/iree/actions/runs/36815105236/job/110220620763) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230393076) | [1s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230393076) | [1s](https://github.com/iree-org/iree/actions/runs/36819041467/job/110230393076) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 329 | 1% (2/329) |  | 9h31m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 244 | 3% (7/244) |  | 11h06m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
