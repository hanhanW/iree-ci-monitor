# iree-ci-monitor

_Updated: 2026-09-07 05:40 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m31s](https://github.com/iree-org/iree/actions/runs/34106670660/job/101693165399) | [1m31s](https://github.com/iree-org/iree/actions/runs/34106670660/job/101693165399) | 0% (0/1) | 1 |
| `macos-14` | github-hosted | 1 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/34106658240/job/101693126531) | [8s](https://github.com/iree-org/iree/actions/runs/34106658240/job/101693126531) | — | 1 |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/34092747062/job/101649538002) | [3s](https://github.com/iree-org/iree/actions/runs/34111910863/job/101709857430) | 50% (3/6) | 11 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711812476) | [3s](https://github.com/iree-org/iree/actions/runs/34112523409/job/101711773910) | 0% (0/3) | 12 |
| `azure-linux-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/34106590769/job/101692912456) | [1s](https://github.com/iree-org/iree/actions/runs/34106662954/job/101693140736) | 0% (0/2) | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m31s](https://github.com/iree-org/iree/actions/runs/34106670660/job/101693165399) | [1m31s](https://github.com/iree-org/iree/actions/runs/34106670660/job/101693165399) | [1m31s](https://github.com/iree-org/iree/actions/runs/34106670660/job/101693165399) | 1 |
| `.github/workflows/ci_macos_arm64_clang.yml` | macos_arm64_clang | `macos-14` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/34106658240/job/101693126531) | [8s](https://github.com/iree-org/iree/actions/runs/34106658240/job/101693126531) | [8s](https://github.com/iree-org/iree/actions/runs/34106658240/job/101693126531) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34111972445/job/101710056265) | [4s](https://github.com/iree-org/iree/actions/runs/34112523409/job/101711773762) | [4s](https://github.com/iree-org/iree/actions/runs/34112523409/job/101711773762) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34087813321/job/101635134204) | [3s](https://github.com/iree-org/iree/actions/runs/34112523409/job/101711773910) | [3s](https://github.com/iree-org/iree/actions/runs/34112523409/job/101711773910) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34111972445/job/101710056512) | [3s](https://github.com/iree-org/iree/actions/runs/34112523409/job/101711773640) | [3s](https://github.com/iree-org/iree/actions/runs/34112523409/job/101711773640) | 3 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34092747062/job/101649538002) | [3s](https://github.com/iree-org/iree/actions/runs/34088666173/job/101637554084) | [3s](https://github.com/iree-org/iree/actions/runs/34088666173/job/101637554084) | 2 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34111910863/job/101709857430) | [3s](https://github.com/iree-org/iree/actions/runs/34111910863/job/101709857430) | [3s](https://github.com/iree-org/iree/actions/runs/34111910863/job/101709857430) | 1 |
| `.github/workflows/ci_linux_x64_clang_byollvm.yml` | linux_x64_clang_byollvm | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34106675608/job/101693181063) | [2s](https://github.com/iree-org/iree/actions/runs/34106675608/job/101693181063) | [2s](https://github.com/iree-org/iree/actions/runs/34106675608/job/101693181063) | 1 |
| `.github/workflows/ci_linux_x64_gcc.yml` | linux_x64_gcc | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34106680563/job/101693196548) | [2s](https://github.com/iree-org/iree/actions/runs/34106680563/job/101693196548) | [2s](https://github.com/iree-org/iree/actions/runs/34106680563/job/101693196548) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101621747818) | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101621747818) | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101621747818) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101621747903) | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101621747903) | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101621747903) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101623366660) | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101623366660) | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101623366660) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34111819315/job/101709821986) | [2s](https://github.com/iree-org/iree/actions/runs/34111819315/job/101709821986) | [2s](https://github.com/iree-org/iree/actions/runs/34111819315/job/101709821986) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711770644) | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711770644) | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711770644) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711812476) | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711812476) | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711812476) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711812655) | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711812655) | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711812655) | 1 |
| `.github/workflows/ci_linux_x64_clang_debug.yml` | linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/34106590769/job/101692912456) | [1s](https://github.com/iree-org/iree/actions/runs/34106590769/job/101692912456) | [1s](https://github.com/iree-org/iree/actions/runs/34106590769/job/101692912456) | 1 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/34106662954/job/101693140736) | [1s](https://github.com/iree-org/iree/actions/runs/34106662954/job/101693140736) | [1s](https://github.com/iree-org/iree/actions/runs/34106662954/job/101693140736) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/34107484925/job/101695733703) | [1s](https://github.com/iree-org/iree/actions/runs/34107484925/job/101695733703) | [1s](https://github.com/iree-org/iree/actions/runs/34107484925/job/101695733703) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/34111819315/job/101709574559) | [1s](https://github.com/iree-org/iree/actions/runs/34111819315/job/101709574559) | [1s](https://github.com/iree-org/iree/actions/runs/34111819315/job/101709574559) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 129 | 2% (2/129) |  | 15h54m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 86 | 0% (0/86) |  | 16h30m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 107 | 5% (5/107) |  | 16h37m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 97 | 0% (0/97) |  | 16h38m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
