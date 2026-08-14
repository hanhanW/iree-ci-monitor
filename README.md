# iree-ci-monitor

_Updated: 2026-08-14 00:52 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683846446) | [4s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877730) | 0% (0/4) | 9 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877811) | [4s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877703) | — | 3 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877724) | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877733) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877797) | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877834) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877703) | [4s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877703) | [4s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877703) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877730) | [4s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877730) | [4s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877730) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877773) | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877773) | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877773) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877847) | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877847) | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877847) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877733) | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877733) | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877733) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877724) | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877724) | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877724) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877834) | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877834) | [3s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877834) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877723) | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877723) | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877723) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877811) | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877811) | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877811) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877772) | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877772) | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877772) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683846446) | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683846446) | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683846446) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877797) | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877797) | [2s](https://github.com/iree-org/iree/actions/runs/31773433507/job/94683877797) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31770557911/job/94675427861) | [2s](https://github.com/iree-org/iree/actions/runs/31770557911/job/94675427861) | [2s](https://github.com/iree-org/iree/actions/runs/31770557911/job/94675427861) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31770557911/job/94675427844) | [2s](https://github.com/iree-org/iree/actions/runs/31770557911/job/94675427844) | [2s](https://github.com/iree-org/iree/actions/runs/31770557911/job/94675427844) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31770557911/job/94676749837) | [2s](https://github.com/iree-org/iree/actions/runs/31770557911/job/94676749837) | [2s](https://github.com/iree-org/iree/actions/runs/31770557911/job/94676749837) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31773395706/job/94683734124) | [2s](https://github.com/iree-org/iree/actions/runs/31773395706/job/94683734124) | [2s](https://github.com/iree-org/iree/actions/runs/31773395706/job/94683734124) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 173 | 8% (14/173) |  | 12h20m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 214 | 0% (0/214) |  | 12h33m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 177 | 5% (9/177) |  | 12h35m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 146 | 12% (17/146) |  | 12h41m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
