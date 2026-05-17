# iree-ci-monitor

_Updated: 2026-05-17 05:38 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498082) | [3s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498086) | — | 3 |
| `ubuntu-24.04` | github-hosted | 12 | 2 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498088) | [2s](https://github.com/iree-org/iree/actions/runs/25989096907/job/76391874051) | 0% (0/1) | 10 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498084) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498102) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498095) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498100) | — | 2 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25989213859/job/76392201122) | [2s](https://github.com/iree-org/iree/actions/runs/25989213918/job/76392192544) | — | 6 |

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
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498086) | [3s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498086) | [3s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498086) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76391804889) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76391804889) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76391804889) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498078) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498078) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498078) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498082) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498082) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498082) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498076) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498076) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498076) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498080) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498080) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498080) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498091) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498091) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498091) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498088) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498088) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498088) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498095) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498095) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498095) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498100) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498100) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498100) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375488947) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375488947) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375488947) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498084) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498084) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498084) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498102) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498102) | [2s](https://github.com/iree-org/iree/actions/runs/25983134491/job/76375498102) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25989096907/job/76391874051) | [2s](https://github.com/iree-org/iree/actions/runs/25989096907/job/76391874051) | [2s](https://github.com/iree-org/iree/actions/runs/25989096907/job/76391874051) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25983123506/job/76375453635) | [2s](https://github.com/iree-org/iree/actions/runs/25983123506/job/76375453635) | [2s](https://github.com/iree-org/iree/actions/runs/25983123506/job/76375453635) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25989074428/job/76391860976) | [2s](https://github.com/iree-org/iree/actions/runs/25989074428/job/76391860976) | [2s](https://github.com/iree-org/iree/actions/runs/25989074428/job/76391860976) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25989074428/job/76391810483) | [2s](https://github.com/iree-org/iree/actions/runs/25989074428/job/76391810483) | [2s](https://github.com/iree-org/iree/actions/runs/25989074428/job/76391810483) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/25989213918/job/76392192544) | [2s](https://github.com/iree-org/iree/actions/runs/25989213918/job/76392192544) | [2s](https://github.com/iree-org/iree/actions/runs/25989213918/job/76392192544) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1099 | 2% (22/1097) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark55-ci`, `self-hosted,persistent-cache,Linux,X64` | 859 | 1% (11/859) |  | 11h51m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 977 | 6% (56/977) |  | 11h55m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark01-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 895 | 1% (11/895) |  | 11h57m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 300 | 2% (5/300) |  | 12h12m ago |

## Alerts

- **[stale-queued]** `ubuntu-24.04` oldest queued job observed waiting 4h53m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
