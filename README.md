# iree-ci-monitor

_Updated: 2026-10-30 22:51 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087882) | [5s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087933) | 0% (0/1) | 6 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087906) | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087962) | — | 3 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087894) | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087932) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087914) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087936) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087933) | [5s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087933) | [5s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087933) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087906) | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087906) | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087906) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087962) | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087962) | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087962) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087877) | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087877) | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087877) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087894) | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087894) | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087894) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087932) | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087932) | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087932) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/41171390063/job/124449897128) | [3s](https://github.com/iree-org/iree/actions/runs/41171390063/job/124449897128) | [3s](https://github.com/iree-org/iree/actions/runs/41171390063/job/124449897128) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087882) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087882) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087882) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087943) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087943) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087943) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087874) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087874) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087874) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450050929) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450050929) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450050929) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087936) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087936) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087936) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087914) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087914) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087914) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 265 | 3% (8/265) |  | 17h29m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 222 | 3% (7/222) |  | 17h39m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
