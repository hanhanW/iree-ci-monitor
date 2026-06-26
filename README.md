# iree-ci-monitor

_Updated: 2026-06-26 00:37 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051276) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | — | 3 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051325) | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | — | 2 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603031487) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051332) | 50% (2/4) | 9 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051295) | — | 2 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 4 | [21h43m](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332845) | 2026-06-26 00:36 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [21h43m](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332845) | 2026-06-26 00:36 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `fuse_multiple-slice` | pull_request |
| [21h30m](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683033) | 2026-06-26 00:36 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [19h32m](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161012) | 2026-06-26 00:36 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `integrates/llvm-20260625` | pull_request |
| [17h59m](https://github.com/iree-org/iree/actions/runs/28172319267/job/83446011596) | 2026-06-26 00:36 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 4 | 4 | [21h43m](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332845) | 2026-06-26 00:36 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051276) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051276) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051276) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051279) | [4s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051279) | [4s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051279) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051300) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051300) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051300) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051304) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051304) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051304) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051305) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051305) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051305) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051332) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051332) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051332) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051325) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051325) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051325) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603031487) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603031487) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603031487) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051295) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051295) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051295) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228962) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228962) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228962) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228950) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228950) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228950) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83598184239) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83598184239) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83598184239) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221278784/job/83602925806) | [2s](https://github.com/iree-org/iree/actions/runs/28221278784/job/83602925806) | [2s](https://github.com/iree-org/iree/actions/runs/28221278784/job/83602925806) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 123 | 0% (0/123) |  | 17h29m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 94 | 0% (0/94) |  | 17h33m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 6% (6/102) |  | 17h34m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 86 | 0% (0/86) |  | 17h34m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 27 | 0% (0/27) |  | 17h46m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 21h43m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
