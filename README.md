# iree-ci-monitor

_Updated: 2026-08-15 06:00 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694209) | [5s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694178) | — | 3 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31878809038/job/94998366504) | [4s](https://github.com/iree-org/iree/actions/runs/31878566175/job/94997760982) | — | 9 |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694174) | [3s](https://github.com/iree-org/iree/actions/runs/31878538415/job/94997692413) | 0% (0/1) | 11 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694213) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694186) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694207) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694235) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694178) | [5s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694178) | [5s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694178) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31878809038/job/94998366423) | [4s](https://github.com/iree-org/iree/actions/runs/31878566175/job/94997760982) | [4s](https://github.com/iree-org/iree/actions/runs/31878566175/job/94997760982) | 2 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694176) | [4s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694176) | [4s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694176) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694209) | [4s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694209) | [4s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694209) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31878809038/job/94998366504) | [3s](https://github.com/iree-org/iree/actions/runs/31878566175/job/94997760987) | [3s](https://github.com/iree-org/iree/actions/runs/31878566175/job/94997760987) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31878566175/job/94997761028) | [3s](https://github.com/iree-org/iree/actions/runs/31878809038/job/94998366486) | [3s](https://github.com/iree-org/iree/actions/runs/31878809038/job/94998366486) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94997467406) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94997467406) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94997467406) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694194) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694194) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694194) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694215) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694215) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694215) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694174) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694174) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694174) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694235) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694235) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694235) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967669963) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967669963) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967669963) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694186) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694186) | [3s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694186) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31878538415/job/94997692413) | [3s](https://github.com/iree-org/iree/actions/runs/31878538415/job/94997692413) | [3s](https://github.com/iree-org/iree/actions/runs/31878538415/job/94997692413) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31866199228/job/94967579852) | [3s](https://github.com/iree-org/iree/actions/runs/31866199228/job/94967579852) | [3s](https://github.com/iree-org/iree/actions/runs/31866199228/job/94967579852) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31878449394/job/94997679596) | [3s](https://github.com/iree-org/iree/actions/runs/31878449394/job/94997679596) | [3s](https://github.com/iree-org/iree/actions/runs/31878449394/job/94997679596) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694216) | [2s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694216) | [2s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694216) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694207) | [2s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694207) | [2s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694207) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694213) | [2s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694213) | [2s](https://github.com/iree-org/iree/actions/runs/31866233104/job/94967694213) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31877596421/job/94995512376) | [2s](https://github.com/iree-org/iree/actions/runs/31877596421/job/94995512376) | [2s](https://github.com/iree-org/iree/actions/runs/31877596421/job/94995512376) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 203 | 0% (0/203) |  | 17h33m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 167 | 7% (12/167) |  | 17h34m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 167 | 4% (6/167) |  | 17h39m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 138 | 9% (12/138) |  | 17h40m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
