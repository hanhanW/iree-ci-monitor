# iree-ci-monitor

_Updated: 2026-06-27 11:43 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 5 | [7s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873394) | [1m44s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873372) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873136) | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873141) | — | 3 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28292217526/job/83826041223) | [3s](https://github.com/iree-org/iree/actions/runs/28292217526/job/83826041214) | — | 12 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873143) | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873146) | — | 3 |
| `ubuntu-24.04` | github-hosted | 13 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873097) | [2s](https://github.com/iree-org/iree/actions/runs/28298243961/job/83841858393) | 0% (0/1) | 13 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873140) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873145) | — | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873409) | [1s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873409) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [1m44s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873372) | [1m44s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873372) | [1m44s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873372) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [20s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873398) | [20s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873398) | [20s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873398) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873394) | [7s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873394) | [7s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873394) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873382) | [6s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873382) | [6s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873382) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873092) | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873092) | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873092) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873141) | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873141) | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873141) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873136) | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873136) | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873136) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28288606734/job/83816692575) | [4s](https://github.com/iree-org/iree/actions/runs/28292217241/job/83826052391) | [4s](https://github.com/iree-org/iree/actions/runs/28292217241/job/83826052391) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28288606832/job/83816683755) | [3s](https://github.com/iree-org/iree/actions/runs/28292217526/job/83826041198) | [3s](https://github.com/iree-org/iree/actions/runs/28292217526/job/83826041198) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28288606832/job/83816683747) | [3s](https://github.com/iree-org/iree/actions/runs/28292217526/job/83826041214) | [3s](https://github.com/iree-org/iree/actions/runs/28292217526/job/83826041214) | 2 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28288606734/job/83816683153) | [3s](https://github.com/iree-org/iree/actions/runs/28292217241/job/83826040933) | [3s](https://github.com/iree-org/iree/actions/runs/28292217241/job/83826040933) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83816303965) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83816303965) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83816303965) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873146) | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873146) | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873146) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873143) | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873143) | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873143) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28288489550/job/83816387516) | [2s](https://github.com/iree-org/iree/actions/runs/28292065298/job/83825632975) | [2s](https://github.com/iree-org/iree/actions/runs/28292065298/job/83825632975) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28288606832/job/83816683748) | [2s](https://github.com/iree-org/iree/actions/runs/28292217526/job/83826041223) | [2s](https://github.com/iree-org/iree/actions/runs/28292217526/job/83826041223) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28288606734/job/83816692581) | [2s](https://github.com/iree-org/iree/actions/runs/28292217241/job/83826052387) | [2s](https://github.com/iree-org/iree/actions/runs/28292217241/job/83826052387) | 2 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873088) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873088) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873088) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873097) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873097) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873097) | 1 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873093) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873093) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873093) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 119 | 0% (0/119) |  | 23h33m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 95 | 8% (8/95) |  | 23h43m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 91 | 0% (0/91) |  | 23h45m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 85 | 0% (0/85) |  | 23h46m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 26 | 0% (0/26) |  | 23h54m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
