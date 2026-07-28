# iree-ci-monitor

_Updated: 2026-07-28 00:13 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30307970635/job/90116681330) | [9s](https://github.com/iree-org/iree/actions/runs/30307970636/job/90116682528) | 0% (0/2) | 2 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993293) | [9s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993236) | 0% (0/4) | 9 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993221) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993235) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993226) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993391) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993250) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993260) | — | 3 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/dependabot/dependabot-updates` | Dependabot | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30307970635/job/90116681330) | [9s](https://github.com/iree-org/iree/actions/runs/30307970636/job/90116682528) | [9s](https://github.com/iree-org/iree/actions/runs/30307970636/job/90116682528) | 2 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993236) | [9s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993236) | [9s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993236) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993206) | [8s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993206) | [8s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993206) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273679) | [8s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273679) | [8s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273679) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273750) | [7s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273750) | [7s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273750) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993391) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993391) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993391) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993235) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993235) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993235) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993245) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993245) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993245) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993260) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993260) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993260) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993250) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993250) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993250) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993293) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993293) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993293) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993203) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993203) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993203) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993226) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993226) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993226) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993221) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993221) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993221) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30333301869/job/90192849746) | [2s](https://github.com/iree-org/iree/actions/runs/30333301869/job/90192849746) | [2s](https://github.com/iree-org/iree/actions/runs/30333301869/job/90192849746) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192962381) | [1s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192962381) | [1s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192962381) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90186585501) | [1s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90186585501) | [1s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90186585501) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 328 | 2% (5/328) |  | 19h47m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 252 | 1% (2/252) |  | 19h57m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 265 | 5% (14/265) |  | 20h00m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 238 | 2% (4/238) |  | 20h09m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 75 | 3% (2/75) |  | 20h11m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
