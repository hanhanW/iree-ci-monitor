# iree-ci-monitor

_Updated: 2026-06-05 00:48 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615122) | [6s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615106) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26997745957/job/79670982171) | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615135) | 50% (2/4) | 9 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615101) | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615116) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615111) | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615129) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615106) | [6s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615106) | [6s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615106) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615122) | [5s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615122) | [5s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615122) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615104) | [5s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615104) | [5s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615104) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615120) | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615120) | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615120) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615135) | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615135) | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615135) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615116) | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615116) | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615116) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676591352) | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676591352) | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676591352) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615111) | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615111) | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615111) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615129) | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615129) | [2s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615129) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26997745957/job/79670982171) | [2s](https://github.com/iree-org/iree/actions/runs/26997745957/job/79670982171) | [2s](https://github.com/iree-org/iree/actions/runs/26997745957/job/79670982171) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26997745957/job/79670982135) | [2s](https://github.com/iree-org/iree/actions/runs/26997745957/job/79670982135) | [2s](https://github.com/iree-org/iree/actions/runs/26997745957/job/79670982135) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26999503911/job/79676496451) | [2s](https://github.com/iree-org/iree/actions/runs/26999503911/job/79676496451) | [2s](https://github.com/iree-org/iree/actions/runs/26999503911/job/79676496451) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615123) | [1s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615123) | [1s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615123) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615127) | [1s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615127) | [1s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615127) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615101) | [1s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615101) | [1s](https://github.com/iree-org/iree/actions/runs/26999533411/job/79676615101) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26997745957/job/79671932335) | [1s](https://github.com/iree-org/iree/actions/runs/26997745957/job/79671932335) | [1s](https://github.com/iree-org/iree/actions/runs/26997745957/job/79671932335) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 273 | 0% (1/273) |  | 15h18m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 248 | 4% (10/248) |  | 15h32m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 194 | 1% (2/194) |  | 15h33m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 200 | 0% (0/200) |  | 15h43m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 62 | 0% (0/62) |  | 16h43m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
