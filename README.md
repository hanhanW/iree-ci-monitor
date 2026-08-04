# iree-ci-monitor

_Updated: 2026-08-04 00:13 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/30855766296/job/91826294535) | [8s](https://github.com/iree-org/iree/actions/runs/30855766296/job/91826294535) | 0% (0/1) | 1 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [8s](https://github.com/iree-org/iree/actions/runs/30879814779/job/91898535543) | [8s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697634) | 0% (0/4) | 9 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697711) | [5s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697644) | — | 3 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697678) | [3s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697645) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697635) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697648) | — | 2 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 2 | 2 | [21h55m](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715262) | 2026-08-04 00:13 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [21h55m](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715262) | 2026-08-04 00:13 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `conv-dt-lower-to-ukernel` | pull_request |
| [18h10m](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209322) | 2026-08-04 00:13 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `integrates/llvm-20260731-cleanup` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 2 | [21h55m](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715262) | 2026-08-04 00:13 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697634) | [8s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697634) | [8s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697634) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906645173) | [8s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906645173) | [8s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906645173) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30879814779/job/91898535543) | [8s](https://github.com/iree-org/iree/actions/runs/30879814779/job/91898535543) | [8s](https://github.com/iree-org/iree/actions/runs/30879814779/job/91898535543) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30879814779/job/91899822700) | [8s](https://github.com/iree-org/iree/actions/runs/30879814779/job/91899822700) | [8s](https://github.com/iree-org/iree/actions/runs/30879814779/job/91899822700) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30882451212/job/91906498120) | [8s](https://github.com/iree-org/iree/actions/runs/30882451212/job/91906498120) | [8s](https://github.com/iree-org/iree/actions/runs/30882451212/job/91906498120) | 1 |
| `dynamic/dependabot/dependabot-updates` | Dependabot | `ubuntu-latest` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30855766296/job/91826294535) | [8s](https://github.com/iree-org/iree/actions/runs/30855766296/job/91826294535) | [8s](https://github.com/iree-org/iree/actions/runs/30855766296/job/91826294535) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697644) | [5s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697644) | [5s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697644) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697645) | [3s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697645) | [3s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697645) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697711) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697711) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697711) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697633) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697633) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697633) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697620) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697620) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697620) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697610) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697610) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697610) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697638) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697638) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697638) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697678) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697678) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697678) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697648) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697648) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697648) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697635) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697635) | [2s](https://github.com/iree-org/iree/actions/runs/30882500797/job/91906697635) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30879814779/job/91898535546) | [2s](https://github.com/iree-org/iree/actions/runs/30879814779/job/91898535546) | [2s](https://github.com/iree-org/iree/actions/runs/30879814779/job/91898535546) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 157 | 0% (0/157) |  | 17h37m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 111 | 0% (0/111) |  | 17h38m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 118 | 1% (1/118) |  | 17h40m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 139 | 2% (3/139) |  | 17h46m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 35 | 0% (0/35) |  | 17h59m ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 21h55m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
