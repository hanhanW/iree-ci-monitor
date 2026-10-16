# iree-ci-monitor

_Updated: 2026-10-16 04:30 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m27s](https://github.com/iree-org/iree/actions/runs/38880538118/job/116905924365) | [1m27s](https://github.com/iree-org/iree/actions/runs/38880538118/job/116905924365) | 100% (1/1) | 1 |
| `macos-15` | github-hosted | 3 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914572) | [9s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914622) | — | 3 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914490) | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914547) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914514) | [3s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914553) | — | 2 |
| `ubuntu-24.04` | github-hosted | 15 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914463) | [2s](https://github.com/iree-org/iree/actions/runs/38889579599/job/116935541697) | 0% (0/4) | 15 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38889652351/job/116935775545) | [2s](https://github.com/iree-org/iree/actions/runs/38889652351/job/116935775598) | — | 3 |
| `azure-linux-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/38880407535/job/116905500361) | [1s](https://github.com/iree-org/iree/actions/runs/38880527065/job/116905889447) | 50% (1/2) | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m27s](https://github.com/iree-org/iree/actions/runs/38880538118/job/116905924365) | [1m27s](https://github.com/iree-org/iree/actions/runs/38880538118/job/116905924365) | [1m27s](https://github.com/iree-org/iree/actions/runs/38880538118/job/116905924365) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914622) | [9s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914622) | [9s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914622) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914572) | [8s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914572) | [8s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914572) | 1 |
| `.github/workflows/ci_macos_arm64_clang.yml` | macos_arm64_clang | `macos-15` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/38880503077/job/116905814179) | [5s](https://github.com/iree-org/iree/actions/runs/38880503077/job/116905814179) | [5s](https://github.com/iree-org/iree/actions/runs/38880503077/job/116905814179) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914547) | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914547) | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914547) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914485) | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914485) | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914485) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914490) | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914490) | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914490) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914553) | [3s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914553) | [3s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914553) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/38889459393/job/116935497970) | [3s](https://github.com/iree-org/iree/actions/runs/38889459393/job/116935497970) | [3s](https://github.com/iree-org/iree/actions/runs/38889459393/job/116935497970) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116935108768) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116935108768) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116935108768) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914463) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914463) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914463) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914509) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914509) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914509) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914541) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914541) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914541) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914462) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914462) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914462) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914514) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914514) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914514) | 1 |
| `.github/workflows/ci_linux_x64_clang_byollvm.yml` | linux_x64_clang_byollvm | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38880544587/job/116905946887) | [2s](https://github.com/iree-org/iree/actions/runs/38880544587/job/116905946887) | [2s](https://github.com/iree-org/iree/actions/runs/38880544587/job/116905946887) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38889579599/job/116935541697) | [2s](https://github.com/iree-org/iree/actions/runs/38889579599/job/116935541697) | [2s](https://github.com/iree-org/iree/actions/runs/38889579599/job/116935541697) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116809753046) | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116809753046) | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116809753046) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116809753158) | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116809753158) | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116809753158) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116811684268) | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116811684268) | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116811684268) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 243 | 1% (2/243) |  | 12h04m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 303 | 6% (18/303) |  | 12h12m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
