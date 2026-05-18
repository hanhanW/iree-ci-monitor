# iree-ci-monitor

_Updated: 2026-05-18 00:45 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426302) | [4s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426317) | — | 2 |
| `ubuntu-24.04` | github-hosted | 11 | 2 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470402410) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426323) | 50% (2/4) | 9 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426307) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426324) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426313) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426320) | — | 2 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | `users/keshavvinayak01/gpuvectoralloc-swizzle` | pull_request |
| [4h53m](https://github.com/iree-org/iree/actions/runs/25907295886/job/76143196900) | 2026-05-15 05:58 PDT | `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | `users/keshavvinayak01/gpuvectoralloc-swizzle` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | 1 | 1 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 1 | 1 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295886/job/76143196900) | 2026-05-15 05:58 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426317) | [4s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426317) | [4s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426317) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426302) | [3s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426302) | [3s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426302) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426307) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426307) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426307) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426324) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426324) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426324) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426291) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426291) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426291) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426312) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426312) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426312) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426299) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426299) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426299) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426305) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426305) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426305) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426323) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426323) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426323) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470402410) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470402410) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470402410) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426320) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426320) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426320) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426313) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426313) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426313) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76464514225) | [2s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76464514225) | [2s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76464514225) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76465397516) | [2s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76465397516) | [2s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76465397516) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26017347263/job/76470307584) | [2s](https://github.com/iree-org/iree/actions/runs/26017347263/job/76470307584) | [2s](https://github.com/iree-org/iree/actions/runs/26017347263/job/76470307584) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76464514259) | [1s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76464514259) | [1s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76464514259) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1095 | 2% (22/1093) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark55-ci`, `self-hosted,persistent-cache,Linux,X64` | 856 | 1% (11/856) |  | 1d06h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 972 | 6% (56/972) |  | 1d07h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark01-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 892 | 1% (11/892) |  | 1d07h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 299 | 2% (5/299) |  | 1d07h ago |

## Alerts

- **[stale-queued]** `ubuntu-24.04` oldest queued job observed waiting 4h53m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
