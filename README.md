# iree-ci-monitor

_Updated: 2026-06-28 00:39 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463969) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463979) | — | 3 |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/28299106146/job/83853587576) | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463974) | 0% (0/1) | 11 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463972) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463975) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463977) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463988) | — | 2 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 6 | [12h35m](https://github.com/iree-org/iree/actions/runs/28298636190/job/83843455562) | 2026-06-28 00:39 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [12h35m](https://github.com/iree-org/iree/actions/runs/28298636190/job/83843455562) | 2026-06-28 00:39 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/fill-buffer-1byte-edge` | pull_request |
| [12h17m](https://github.com/iree-org/iree/actions/runs/28299106146/job/83844610658) | 2026-06-28 00:39 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/copy-buffer-1byte-grid` | pull_request |
| [12h13m](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820560) | 2026-06-28 00:39 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/indirect-dispatch-stack-garbage` | pull_request |
| [12h11m](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978281) | 2026-06-28 00:39 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/staging-buffer-overflow` | pull_request |
| [12h10m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041346) | 2026-06-28 00:39 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/export-name-lookup` | pull_request |
| [12h09m](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077655) | 2026-06-28 00:39 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/indirect-dispatch-offset` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 6 | 6 | [12h35m](https://github.com/iree-org/iree/actions/runs/28298636190/job/83843455562) | 2026-06-28 00:39 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463967) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463967) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463967) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463969) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463969) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463969) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463979) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463979) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463979) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 5 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28299106146/job/83853587576) | [3s](https://github.com/iree-org/iree/actions/runs/28299152490/job/83856715118) | [3s](https://github.com/iree-org/iree/actions/runs/28299152490/job/83856715118) | 5 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463974) | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463974) | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463974) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883450588) | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883450588) | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883450588) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28313880526/job/83883403723) | [3s](https://github.com/iree-org/iree/actions/runs/28313880526/job/83883403723) | [3s](https://github.com/iree-org/iree/actions/runs/28313880526/job/83883403723) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463965) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463965) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463965) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463988) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463988) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463988) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463977) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463977) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463977) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463975) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463975) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463975) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463964) | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463964) | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463964) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463985) | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463985) | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463985) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463972) | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463972) | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463972) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 149 | 0% (0/149) |  | 8h47m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 122 | 7% (9/122) |  | 9h56m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 110 | 0% (0/110) |  | 10h02m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 106 | 0% (0/106) |  | 10h10m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 33 | 0% (0/33) |  | 11h25m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 12h35m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
