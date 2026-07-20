# iree-ci-monitor

_Updated: 2026-07-20 00:23 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [6s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968269) | [9s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968137) | — | 3 |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968199) | [4s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968147) | 50% (2/4) | 9 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968163) | [4s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968190) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968155) | [3s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968172) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968137) | [9s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968137) | [9s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968137) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968269) | [6s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968269) | [6s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968269) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968141) | [6s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968141) | [6s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968141) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968147) | [4s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968147) | [4s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968147) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968190) | [4s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968190) | [4s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968190) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968150) | [3s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968150) | [3s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968150) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968144) | [3s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968144) | [3s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968144) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968172) | [3s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968172) | [3s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968172) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968163) | [3s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968163) | [3s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968163) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29718910013/job/88278606163) | [3s](https://github.com/iree-org/iree/actions/runs/29718910013/job/88278606163) | [3s](https://github.com/iree-org/iree/actions/runs/29718910013/job/88278606163) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968199) | [2s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968199) | [2s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968199) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968155) | [2s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968155) | [2s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282968155) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282941720) | [2s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282941720) | [2s](https://github.com/iree-org/iree/actions/runs/29720682425/job/88282941720) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29718910013/job/88277505845) | [2s](https://github.com/iree-org/iree/actions/runs/29718910013/job/88277505845) | [2s](https://github.com/iree-org/iree/actions/runs/29718910013/job/88277505845) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29720654196/job/88282857808) | [2s](https://github.com/iree-org/iree/actions/runs/29720654196/job/88282857808) | [2s](https://github.com/iree-org/iree/actions/runs/29720654196/job/88282857808) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29718910013/job/88277505815) | [1s](https://github.com/iree-org/iree/actions/runs/29718910013/job/88277505815) | [1s](https://github.com/iree-org/iree/actions/runs/29718910013/job/88277505815) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | 0s | 0s | 0s | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 175 | 1% (1/175) |  | 2d08h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 141 | 9% (13/141) |  | 2d08h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 150 | 1% (2/150) |  | 2d08h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 137 | 0% (0/137) |  | 2d08h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 41 | 0% (0/41) |  | 2d08h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
