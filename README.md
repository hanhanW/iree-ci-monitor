# iree-ci-monitor

_Updated: 2026-08-01 05:37 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 16 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30617667378/job/91353190084) | [9s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91356440816) | 75% (3/4) | 16 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860038) | [9s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366859375) | — | 9 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639296) | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639281) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639284) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639287) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639302) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639303) | — | 2 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 6 | 6 | [19h43m](https://github.com/iree-org/iree/actions/runs/30646844543/job/91217330080) | 2026-08-01 05:37 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [19h43m](https://github.com/iree-org/iree/actions/runs/30646844543/job/91217330080) | 2026-08-01 05:37 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `fix-stablehlo-scatter` | pull_request |
| [19h41m](https://github.com/iree-org/iree/actions/runs/30646568869/job/91217783698) | 2026-08-01 05:37 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `fix-slo-composite` | pull_request |
| [17h55m](https://github.com/iree-org/iree/actions/runs/30655580496/job/91241055463) | 2026-08-01 05:37 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [17h11m](https://github.com/iree-org/iree/actions/runs/30658571489/job/91250481355) | 2026-08-01 05:37 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [17h09m](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001169) | 2026-08-01 05:37 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `integrates/llvm-20260731-cleanup` | pull_request |
| [17h08m](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264223) | 2026-08-01 05:37 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 6 | 6 | [19h43m](https://github.com/iree-org/iree/actions/runs/30646844543/job/91217330080) | 2026-08-01 05:37 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 5 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30615166831/job/91346816450) | [9s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91356440816) | [9s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91356440816) | 5 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366187044) | [9s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366187044) | [9s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366187044) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366859375) | [9s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366859375) | [9s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366859375) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639290) | [8s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639290) | [8s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639290) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366883255) | [8s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366883255) | [8s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366883255) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366883254) | [8s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366883254) | [8s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366883254) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30698913070/job/91366348697) | [7s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860025) | [7s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860025) | 2 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334616614) | [4s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334616614) | [4s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334616614) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366275992) | [4s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366275992) | [4s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366275992) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30698913070/job/91366348677) | [3s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860038) | [3s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860038) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91366175468) | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91366175468) | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91366175468) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639281) | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639281) | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639281) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30698890796/job/91366289903) | [3s](https://github.com/iree-org/iree/actions/runs/30698890796/job/91366289903) | [3s](https://github.com/iree-org/iree/actions/runs/30698890796/job/91366289903) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30698913070/job/91366348709) | [2s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860062) | [2s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860062) | 2 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639276) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639276) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639276) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639284) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639284) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639284) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639287) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639287) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639287) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639283) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639283) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639283) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639274) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639274) | [2s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91334639274) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 166 | 0% (0/166) |  | 16h07m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 118 | 1% (1/118) |  | 16h19m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 148 | 3% (4/148) |  | 16h20m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 123 | 1% (1/123) |  | 16h23m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 37 | 3% (1/37) |  | 16h38m ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 19h43m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
