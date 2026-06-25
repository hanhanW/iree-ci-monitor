# iree-ci-monitor

_Updated: 2026-06-25 00:31 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402049) | [6s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402024) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83362517534) | [3s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402047) | 50% (2/4) | 9 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402058) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402108) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402094) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402110) | — | 2 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 6 | [20h06m](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261695) | 2026-06-25 00:30 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [20h06m](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261695) | 2026-06-25 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `flow_empty_fold` | pull_request |
| [19h25m](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554091) | 2026-06-25 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [17h51m](https://github.com/iree-org/iree/actions/runs/28102210744/job/83208735459) | 2026-06-25 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [17h44m](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184300) | 2026-06-25 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/bjacob/cpu-ukernel-bodies` | pull_request |
| [16h59m](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582315) | 2026-06-25 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `fix-24624-raise-special-ops-memref-crash` | pull_request |
| [16h24m](https://github.com/iree-org/iree/actions/runs/28107886109/job/83228908779) | 2026-06-25 00:30 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 6 | 6 | [20h06m](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261695) | 2026-06-25 00:30 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402024) | [6s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402024) | [6s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402024) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402049) | [5s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402049) | [5s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402049) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402038) | [5s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402038) | [5s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402038) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402047) | [3s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402047) | [3s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402047) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369376612) | [3s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369376612) | [3s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369376612) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402070) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402070) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402070) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402058) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402058) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402058) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402108) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402108) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402108) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402110) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402110) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402110) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402094) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402094) | [2s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402094) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83362517534) | [2s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83362517534) | [2s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83362517534) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83362517517) | [2s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83362517517) | [2s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83362517517) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28151259678/job/83369276881) | [2s](https://github.com/iree-org/iree/actions/runs/28151259678/job/83369276881) | [2s](https://github.com/iree-org/iree/actions/runs/28151259678/job/83369276881) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402078) | [1s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402078) | [1s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402078) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402073) | [1s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402073) | [1s](https://github.com/iree-org/iree/actions/runs/28151290097/job/83369402073) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83363567561) | [1s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83363567561) | [1s](https://github.com/iree-org/iree/actions/runs/28149098755/job/83363567561) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 87 | 7% (6/87) |  | 15h52m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 76 | 0% (0/76) |  | 16h01m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 111 | 0% (0/111) |  | 16h04m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 86 | 0% (0/86) |  | 16h07m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 24 | 0% (0/24) |  | 16h14m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 20h06m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
