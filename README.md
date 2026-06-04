# iree-ci-monitor

_Updated: 2026-06-04 06:28 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m25s](https://github.com/iree-org/iree/actions/runs/26946175694/job/79499591877) | [1m25s](https://github.com/iree-org/iree/actions/runs/26946175694/job/79499591877) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277161) | [7s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277202) | — | 3 |
| `ubuntu-24.04` | github-hosted | 15 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277145) | [3s](https://github.com/iree-org/iree/actions/runs/26949639584/job/79511321449) | 50% (2/4) | 15 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26946162366/job/79499547725) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277165) | 0% (0/1) | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277185) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277188) | — | 2 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415263) | [3s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415249) | — | 3 |
| `azure-linux-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26946170748/job/79499576084) | [2s](https://github.com/iree-org/iree/actions/runs/26946148701/job/79499500413) | 0% (0/2) | 2 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26946159967/job/79499538990) | [2s](https://github.com/iree-org/iree/actions/runs/26946159967/job/79499538990) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m25s](https://github.com/iree-org/iree/actions/runs/26946175694/job/79499591877) | [1m25s](https://github.com/iree-org/iree/actions/runs/26946175694/job/79499591877) | [1m25s](https://github.com/iree-org/iree/actions/runs/26946175694/job/79499591877) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277202) | [7s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277202) | [7s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277202) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277161) | [6s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277161) | [6s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277161) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277226) | [5s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277226) | [5s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277226) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277291) | [4s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277291) | [4s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277291) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277206) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277206) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277206) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277180) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277180) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277180) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277165) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277165) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277165) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277188) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277188) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277188) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277185) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277185) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277185) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26949639584/job/79511321449) | [3s](https://github.com/iree-org/iree/actions/runs/26949639584/job/79511321449) | [3s](https://github.com/iree-org/iree/actions/runs/26949639584/job/79511321449) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26949544597/job/79511005394) | [3s](https://github.com/iree-org/iree/actions/runs/26949544597/job/79511005394) | [3s](https://github.com/iree-org/iree/actions/runs/26949544597/job/79511005394) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415249) | [3s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415249) | [3s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415249) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79510982547) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79510982547) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79510982547) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277145) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277145) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277145) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277144) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277144) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277144) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463251509) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463251509) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463251509) | 1 |
| `.github/workflows/ci_linux_x64_clang_debug.yml` | linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26946148701/job/79499500413) | [2s](https://github.com/iree-org/iree/actions/runs/26946148701/job/79499500413) | [2s](https://github.com/iree-org/iree/actions/runs/26946148701/job/79499500413) | 1 |
| `.github/workflows/ci_macos_arm64_clang.yml` | macos_arm64_clang | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26946162366/job/79499547725) | [2s](https://github.com/iree-org/iree/actions/runs/26946162366/job/79499547725) | [2s](https://github.com/iree-org/iree/actions/runs/26946162366/job/79499547725) | 1 |
| `.github/workflows/ci_macos_x64_clang.yml` | macos_x64_clang | `macos-15-intel` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26946159967/job/79499538990) | [2s](https://github.com/iree-org/iree/actions/runs/26946159967/job/79499538990) | [2s](https://github.com/iree-org/iree/actions/runs/26946159967/job/79499538990) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 274 | 4% (11/273) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 301 | 0% (1/301) |  | 16h42m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 208 | 1% (2/208) |  | 16h47m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 212 | 0% (0/212) |  | 16h56m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 68 | 1% (1/68) |  | 16h59m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
