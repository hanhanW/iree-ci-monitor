# iree-ci-monitor

_Updated: 2026-11-01 22:16 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940049) | [4s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940093) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106883230) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940144) | 0% (0/4) | 9 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940061) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940096) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940077) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940079) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940093) | [4s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940093) | [4s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940093) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940049) | [4s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940049) | [4s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940049) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940048) | [4s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940048) | [4s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940048) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940144) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940144) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940144) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940142) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940142) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940142) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940058) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940058) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940058) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940132) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940132) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940132) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940061) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940061) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940061) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940096) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940096) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940096) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106883230) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106883230) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106883230) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940077) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940077) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940077) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940079) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940079) | [2s](https://github.com/iree-org/iree/actions/runs/41392544725/job/125106940079) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41387420634/job/125091244956) | [2s](https://github.com/iree-org/iree/actions/runs/41387420634/job/125091244956) | [2s](https://github.com/iree-org/iree/actions/runs/41387420634/job/125091244956) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41387420634/job/125094160447) | [2s](https://github.com/iree-org/iree/actions/runs/41387420634/job/125094160447) | [2s](https://github.com/iree-org/iree/actions/runs/41387420634/job/125094160447) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/41387420634/job/125091245248) | [1s](https://github.com/iree-org/iree/actions/runs/41387420634/job/125091245248) | [1s](https://github.com/iree-org/iree/actions/runs/41387420634/job/125091245248) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/41392498021/job/125106731219) | [1s](https://github.com/iree-org/iree/actions/runs/41392498021/job/125106731219) | [1s](https://github.com/iree-org/iree/actions/runs/41392498021/job/125106731219) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 238 | 3% (7/238) |  | 20h48m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 282 | 3% (8/282) |  | 20h50m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
