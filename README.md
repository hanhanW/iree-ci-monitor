# iree-ci-monitor

_Updated: 2026-08-01 00:09 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 8 | 0 | — | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91335039950) | [8s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639290) | 50% (1/2) | 8 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639296) | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639281) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639284) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639287) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639302) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639303) | — | 2 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 9 | 9 | [22h51m](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445151) | 2026-08-01 00:08 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [22h51m](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445151) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [21h39m](https://github.com/iree-org/iree/actions/runs/30617667378/job/91122514612) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `fix/23345-custom-op-static-loop-ranges` | pull_request |
| [21h02m](https://github.com/iree-org/iree/actions/runs/30621832279/job/91129775249) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [14h15m](https://github.com/iree-org/iree/actions/runs/30646844543/job/91217330080) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `fix-stablehlo-scatter` | pull_request |
| [14h13m](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783698) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `fix-slo-composite` | pull_request |
| [12h26m](https://github.com/iree-org/iree/actions/runs/30655580496/job/91241055463) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [11h43m](https://github.com/iree-org/iree/actions/runs/30658571489/job/91250481355) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [11h41m](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001169) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `integrates/llvm-20260731-cleanup` | pull_request |
| [11h39m](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264223) | 2026-08-01 00:08 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 9 | 9 | [22h51m](https://github.com/iree-org/iree/actions/runs/30615166831/job/91108445151) | 2026-08-01 00:08 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639290) | [8s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639290) | [8s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639290) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334616614) | [4s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334616614) | [4s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334616614) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30607758195/job/91335039950) | [3s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91339200600) | [3s](https://github.com/iree-org/iree/actions/runs/30610564201/job/91339200600) | 2 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639281) | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639281) | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639281) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639276) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639276) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639276) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639284) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639284) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639284) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639287) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639287) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639287) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639283) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639283) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639283) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639274) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639274) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639274) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639271) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639271) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639271) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639296) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639296) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639296) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639303) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639303) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639303) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639302) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639302) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639302) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30686947433/job/91334541438) | [2s](https://github.com/iree-org/iree/actions/runs/30686947433/job/91334541438) | [2s](https://github.com/iree-org/iree/actions/runs/30686947433/job/91334541438) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 166 | 0% (0/166) |  | 10h39m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 118 | 1% (1/118) |  | 10h50m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 148 | 3% (4/148) |  | 10h52m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 123 | 1% (1/123) |  | 10h55m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 37 | 3% (1/37) |  | 11h09m ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 22h51m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
