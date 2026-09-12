# iree-ci-monitor

_Updated: 2026-09-12 03:52 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103540747867) | [38s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503339755) | 0% (0/1) | 10 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427100) | [6s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427101) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427116) | [4s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427138) | — | 3 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34689056339/job/103541010101) | [3s](https://github.com/iree-org/iree/actions/runs/34689056339/job/103541010195) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427132) | [2s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427099) | — | 2 |
| `Linux,X64,gfx1201` | self-hosted | 1 | 1 | [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 1 | [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [38s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503339755) | [38s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503339755) | [38s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503339755) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [37s](https://github.com/iree-org/iree/actions/runs/34688958004/job/103540760526) | [37s](https://github.com/iree-org/iree/actions/runs/34688958004/job/103540760526) | [37s](https://github.com/iree-org/iree/actions/runs/34688958004/job/103540760526) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427100) | [6s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427100) | [6s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427100) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427101) | [6s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427101) | [6s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427101) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427138) | [4s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427138) | [4s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427138) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427116) | [3s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427116) | [3s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427116) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427112) | [3s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427112) | [3s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427112) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427097) | [3s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427097) | [3s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427097) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427093) | [3s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427093) | [3s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427093) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34689056339/job/103541010195) | [3s](https://github.com/iree-org/iree/actions/runs/34689056339/job/103541010195) | [3s](https://github.com/iree-org/iree/actions/runs/34689056339/job/103541010195) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103540747867) | [2s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103540747867) | [2s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103540747867) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427118) | [2s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427118) | [2s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427118) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427099) | [2s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427099) | [2s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427099) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34689032856/job/103540946636) | [2s](https://github.com/iree-org/iree/actions/runs/34689032856/job/103540946636) | [2s](https://github.com/iree-org/iree/actions/runs/34689032856/job/103540946636) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34675039758/job/103503271003) | [2s](https://github.com/iree-org/iree/actions/runs/34675039758/job/103503271003) | [2s](https://github.com/iree-org/iree/actions/runs/34675039758/job/103503271003) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34689056339/job/103541010101) | [2s](https://github.com/iree-org/iree/actions/runs/34689056339/job/103541010101) | [2s](https://github.com/iree-org/iree/actions/runs/34689056339/job/103541010101) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34689056339/job/103541010038) | [2s](https://github.com/iree-org/iree/actions/runs/34689056339/job/103541010038) | [2s](https://github.com/iree-org/iree/actions/runs/34689056339/job/103541010038) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427185) | [1s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427185) | [1s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427185) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427132) | [1s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427132) | [1s](https://github.com/iree-org/iree/actions/runs/34675062947/job/103503427132) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 254 | 8% (20/254) |  | 10h33m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 284 | 1% (4/284) |  | 10h47m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 214 | 1% (3/214) |  | 10h58m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 208 | 1% (2/208) |  | 11h05m ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 2h00m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
