# iree-ci-monitor

_Updated: 2026-07-18 11:36 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29648122758/job/88089706172) | [3s](https://github.com/iree-org/iree/actions/runs/29648122626/job/88089705809) | — | 12 |
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074634926) | [2s](https://github.com/iree-org/iree/actions/runs/29647947257/job/88089236098) | 0% (0/2) | 6 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29642447636/job/88075083613) | [3s](https://github.com/iree-org/iree/actions/runs/29648122758/job/88089706173) | [3s](https://github.com/iree-org/iree/actions/runs/29648122758/job/88089706173) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29648122758/job/88089706159) | [3s](https://github.com/iree-org/iree/actions/runs/29642447636/job/88075083603) | [3s](https://github.com/iree-org/iree/actions/runs/29642447636/job/88075083603) | 2 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29642447320/job/88075082911) | [3s](https://github.com/iree-org/iree/actions/runs/29648122626/job/88089705809) | [3s](https://github.com/iree-org/iree/actions/runs/29648122626/job/88089705809) | 2 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29648122626/job/88089720878) | [3s](https://github.com/iree-org/iree/actions/runs/29642447320/job/88075098537) | [3s](https://github.com/iree-org/iree/actions/runs/29642447320/job/88075098537) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29648122626/job/88089720859) | [3s](https://github.com/iree-org/iree/actions/runs/29642447320/job/88075098531) | [3s](https://github.com/iree-org/iree/actions/runs/29642447320/job/88075098531) | 2 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29642278730/job/88074641463) | [2s](https://github.com/iree-org/iree/actions/runs/29647947257/job/88089236098) | [2s](https://github.com/iree-org/iree/actions/runs/29647947257/job/88089236098) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29642447636/job/88075083598) | [2s](https://github.com/iree-org/iree/actions/runs/29648122758/job/88089706172) | [2s](https://github.com/iree-org/iree/actions/runs/29648122758/job/88089706172) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88074470123) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88074470123) | [2s](https://github.com/iree-org/iree/actions/runs/29632846960/job/88074470123) | 1 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29642912538/job/88076264915) | [2s](https://github.com/iree-org/iree/actions/runs/29642912538/job/88076264915) | [2s](https://github.com/iree-org/iree/actions/runs/29642912538/job/88076264915) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074634926) | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074634926) | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074634926) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074477306) | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074477306) | [2s](https://github.com/iree-org/iree/actions/runs/29642211846/job/88074477306) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 175 | 1% (1/175) |  | 19h46m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 141 | 9% (13/141) |  | 19h46m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 150 | 1% (2/150) |  | 19h52m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 137 | 0% (0/137) |  | 19h55m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 41 | 0% (0/41) |  | 20h06m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
