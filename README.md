# iree-ci-monitor

_Updated: 2026-08-01 11:37 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91366175468) | [9s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366187044) | 50% (1/2) | 10 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860038) | [8s](https://github.com/iree-org/iree/actions/runs/30704032983/job/91379944127) | — | 15 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 4 | [23h55m](https://github.com/iree-org/iree/actions/runs/30655580496/job/91241055463) | 2026-08-01 11:37 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [23h55m](https://github.com/iree-org/iree/actions/runs/30655580496/job/91241055463) | 2026-08-01 11:37 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [23h12m](https://github.com/iree-org/iree/actions/runs/30658571489/job/91250481355) | 2026-08-01 11:37 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [23h09m](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001169) | 2026-08-01 11:37 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `integrates/llvm-20260731-cleanup` | pull_request |
| [23h08m](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264223) | 2026-08-01 11:37 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 4 | [23h55m](https://github.com/iree-org/iree/actions/runs/30655580496/job/91241055463) | 2026-08-01 11:37 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30646844543/job/91393372227) | [9s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91356440816) | [9s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91356440816) | 4 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30704032983/job/91379920356) | [9s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366859375) | [9s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366859375) | 2 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366187044) | [9s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366187044) | [9s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366187044) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30698890796/job/91366289903) | [8s](https://github.com/iree-org/iree/actions/runs/30703843054/job/91379396846) | [8s](https://github.com/iree-org/iree/actions/runs/30703843054/job/91379396846) | 2 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366883255) | [8s](https://github.com/iree-org/iree/actions/runs/30704032983/job/91379944115) | [8s](https://github.com/iree-org/iree/actions/runs/30704032983/job/91379944115) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366883254) | [8s](https://github.com/iree-org/iree/actions/runs/30704032983/job/91379944127) | [8s](https://github.com/iree-org/iree/actions/runs/30704032983/job/91379944127) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30698913070/job/91366348697) | [7s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860025) | [7s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860025) | 3 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366275992) | [4s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366275992) | [4s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366275992) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30704033068/job/91379920594) | [3s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860038) | [3s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860038) | 3 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91366175468) | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91366175468) | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91366175468) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860062) | [2s](https://github.com/iree-org/iree/actions/runs/30704033068/job/91379920623) | [2s](https://github.com/iree-org/iree/actions/runs/30704033068/job/91379920623) | 3 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30697447328/job/91362619593) | [2s](https://github.com/iree-org/iree/actions/runs/30697447328/job/91362619593) | [2s](https://github.com/iree-org/iree/actions/runs/30697447328/job/91362619593) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 166 | 0% (0/166) |  | 22h07m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 118 | 1% (1/118) |  | 22h19m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 148 | 3% (4/148) |  | 22h20m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 123 | 1% (1/123) |  | 22h23m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 37 | 3% (1/37) |  | 22h38m ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 23h55m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
