# iree-ci-monitor

_Updated: 2026-06-03 01:03 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236411658) | [1m10s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433735) | 50% (2/4) | 9 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [20s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433577) | [35s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433612) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433548) | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433556) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433568) | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433578) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1m10s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433735) | [1m10s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433735) | [1m10s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433735) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [35s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433612) | [35s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433612) | [35s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433612) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [24s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433583) | [24s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433583) | [24s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433583) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [21s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433584) | [21s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433584) | [21s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433584) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [20s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433577) | [20s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433577) | [20s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433577) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [16s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433574) | [16s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433574) | [16s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433574) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433566) | [7s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433566) | [7s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433566) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433568) | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433568) | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433568) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433578) | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433578) | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433578) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236411658) | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236411658) | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236411658) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433548) | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433548) | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433548) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433556) | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433556) | [2s](https://github.com/iree-org/iree/actions/runs/26868124642/job/79236433556) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26866313778/job/79230682854) | [2s](https://github.com/iree-org/iree/actions/runs/26866313778/job/79230682854) | [2s](https://github.com/iree-org/iree/actions/runs/26866313778/job/79230682854) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26866313778/job/79230682820) | [2s](https://github.com/iree-org/iree/actions/runs/26866313778/job/79230682820) | [2s](https://github.com/iree-org/iree/actions/runs/26866313778/job/79230682820) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26866313778/job/79231604180) | [2s](https://github.com/iree-org/iree/actions/runs/26866313778/job/79231604180) | [2s](https://github.com/iree-org/iree/actions/runs/26866313778/job/79231604180) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26868099519/job/79236322159) | [2s](https://github.com/iree-org/iree/actions/runs/26868099519/job/79236322159) | [2s](https://github.com/iree-org/iree/actions/runs/26868099519/job/79236322159) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 260 | 5% (12/259) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 287 | 0% (1/287) |  | 10h35m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 195 | 1% (1/195) |  | 10h39m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 65 | 2% (1/65) |  | 10h43m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 207 | 0% (0/207) |  | 10h46m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
