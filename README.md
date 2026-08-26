# iree-ci-monitor

_Updated: 2026-08-26 00:10 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 3 | [8s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465596) | [3m58s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98087468667) | — | 6 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368595) | [1m22s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465318) | — | 6 |
| `ubuntu-24.04` | github-hosted | 17 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368556) | [41s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465184) | 0% (0/4) | 17 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465237) | [5s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465355) | — | 5 |
| `ubuntu-cca-77785908-7ef3-498a-9ae0-bbebb95125d3` | github-hosted | 1 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/32914766325/job/98016071579) | [4s](https://github.com/iree-org/iree/actions/runs/32914766325/job/98016071579) | — | 1 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32936394713/job/98078311215) | [4s](https://github.com/iree-org/iree/actions/runs/32939514772/job/98087420915) | 0% (0/3) | 6 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465345) | [3s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368555) | — | 5 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465659) | [1s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465659) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [3m58s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98087468667) | [3m58s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98087468667) | [3m58s](https://github.com/iree-org/iree/actions/runs/32939517212/job/98087468667) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [1m38s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465360) | [1m38s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465360) | [1m38s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465360) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [1m31s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465515) | [1m31s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465515) | [1m31s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465515) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1m22s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465318) | [1m22s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465318) | [1m22s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465318) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 1 | 0 | — | — | [50s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465271) | [50s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465271) | [50s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465271) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 1 | 0 | — | — | [41s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465184) | [41s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465184) | [41s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465184) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 1 | 0 | — | — | [38s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465298) | [38s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465298) | [38s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465298) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465489) | [8s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465489) | [8s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465489) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465596) | [8s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465596) | [8s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465596) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465297) | [5s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465297) | [5s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465297) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465355) | [5s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465355) | [5s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465355) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32936394713/job/98078311135) | [4s](https://github.com/iree-org/iree/actions/runs/32939514772/job/98087420915) | [4s](https://github.com/iree-org/iree/actions/runs/32939514772/job/98087420915) | 2 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368566) | [4s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368566) | [4s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368566) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368595) | [4s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368595) | [4s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368595) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368574) | [4s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368574) | [4s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368574) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465144) | [4s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465144) | [4s](https://github.com/iree-org/iree/actions/runs/32939517158/job/98087465144) | 1 |
| `dynamic/copilot-swe-agent/copilot` | copilot | `ubuntu-cca-77785908-7ef3-498a-9ae0-bbebb95125d3` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32914766325/job/98016071579) | [4s](https://github.com/iree-org/iree/actions/runs/32914766325/job/98016071579) | [4s](https://github.com/iree-org/iree/actions/runs/32914766325/job/98016071579) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368555) | [3s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368555) | [3s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368555) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368545) | [3s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368545) | [3s](https://github.com/iree-org/iree/actions/runs/32933213459/job/98069368545) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32936394713/job/98078311045) | [2s](https://github.com/iree-org/iree/actions/runs/32939514772/job/98087420922) | [2s](https://github.com/iree-org/iree/actions/runs/32939514772/job/98087420922) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 276 | 1% (4/275) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 193 | 0% (0/192) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 203 | 0% (0/202) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 244 | 3% (7/243) | yes | running |

## Alerts

- **[spof]** `ubuntu-cca-77785908-7ef3-498a-9ae0-bbebb95125d3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
