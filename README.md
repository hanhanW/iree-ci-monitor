# iree-ci-monitor

_Updated: 2026-06-07 05:50 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715891) | [5s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715882) | — | 3 |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715894) | [3s](https://github.com/iree-org/iree/actions/runs/27091948133/job/79957004749) | 0% (0/1) | 10 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715930) | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715909) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715912) | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715926) | — | 2 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27092075999/job/79957356029) | [2s](https://github.com/iree-org/iree/actions/runs/27092075769/job/79957363883) | — | 6 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715882) | [5s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715882) | [5s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715882) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715883) | [4s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715883) | [4s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715883) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715891) | [4s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715891) | [4s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715891) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79956889167) | [3s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79956889167) | [3s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79956889167) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715920) | [3s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715920) | [3s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715920) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27091948133/job/79957004749) | [3s](https://github.com/iree-org/iree/actions/runs/27091948133/job/79957004749) | [3s](https://github.com/iree-org/iree/actions/runs/27091948133/job/79957004749) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715894) | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715894) | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715894) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715888) | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715888) | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715888) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715887) | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715887) | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715887) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715909) | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715909) | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715909) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937702438) | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937702438) | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937702438) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715912) | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715912) | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715912) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715926) | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715926) | [2s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715926) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27085015154/job/79937661860) | [2s](https://github.com/iree-org/iree/actions/runs/27085015154/job/79937661860) | [2s](https://github.com/iree-org/iree/actions/runs/27085015154/job/79937661860) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27091905853/job/79956997652) | [2s](https://github.com/iree-org/iree/actions/runs/27091905853/job/79956997652) | [2s](https://github.com/iree-org/iree/actions/runs/27091905853/job/79956997652) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27091905853/job/79956895377) | [2s](https://github.com/iree-org/iree/actions/runs/27091905853/job/79956895377) | [2s](https://github.com/iree-org/iree/actions/runs/27091905853/job/79956895377) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27092075769/job/79957355776) | [2s](https://github.com/iree-org/iree/actions/runs/27092075769/job/79957355776) | [2s](https://github.com/iree-org/iree/actions/runs/27092075769/job/79957355776) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27092075769/job/79957363883) | [2s](https://github.com/iree-org/iree/actions/runs/27092075769/job/79957363883) | [2s](https://github.com/iree-org/iree/actions/runs/27092075769/job/79957363883) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715930) | [1s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715930) | [1s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79937715930) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27092075999/job/79957356029) | [1s](https://github.com/iree-org/iree/actions/runs/27092075999/job/79957356029) | [1s](https://github.com/iree-org/iree/actions/runs/27092075999/job/79957356029) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 301 | 1% (2/301) |  | 1d13h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 256 | 3% (8/256) |  | 1d15h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 230 | 0% (1/230) |  | 1d15h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 215 | 0% (0/215) |  | 1d15h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 69 | 0% (0/69) |  | 1d16h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
