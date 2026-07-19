# iree-ci-monitor

_Updated: 2026-07-19 11:36 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29684894228/job/88187371832) | [4s](https://github.com/iree-org/iree/actions/runs/29684852401/job/88187361738) | 0% (0/1) | 5 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29689132605/job/88198627897) | [3s](https://github.com/iree-org/iree/actions/runs/29685046849/job/88187788978) | 0% (0/3) | 15 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/29684852401/job/88187361738) | [4s](https://github.com/iree-org/iree/actions/runs/29684852401/job/88187361738) | [4s](https://github.com/iree-org/iree/actions/runs/29684852401/job/88187361738) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29689132605/job/88198627878) | [3s](https://github.com/iree-org/iree/actions/runs/29691025681/job/88203657327) | [3s](https://github.com/iree-org/iree/actions/runs/29691025681/job/88203657327) | 3 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29691025428/job/88203671906) | [3s](https://github.com/iree-org/iree/actions/runs/29685046849/job/88187788978) | [3s](https://github.com/iree-org/iree/actions/runs/29685046849/job/88187788978) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29689132605/job/88198627897) | [2s](https://github.com/iree-org/iree/actions/runs/29691025681/job/88203657315) | [2s](https://github.com/iree-org/iree/actions/runs/29691025681/job/88203657315) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29689132605/job/88198627880) | [2s](https://github.com/iree-org/iree/actions/runs/29691025681/job/88203657304) | [2s](https://github.com/iree-org/iree/actions/runs/29691025681/job/88203657304) | 3 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29684894228/job/88187371832) | [2s](https://github.com/iree-org/iree/actions/runs/29690830730/job/88203126053) | [2s](https://github.com/iree-org/iree/actions/runs/29690830730/job/88203126053) | 2 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29685046849/job/88187776010) | [2s](https://github.com/iree-org/iree/actions/runs/29691025428/job/88203656754) | [2s](https://github.com/iree-org/iree/actions/runs/29691025428/job/88203656754) | 2 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29685046849/job/88187788995) | [2s](https://github.com/iree-org/iree/actions/runs/29691025428/job/88203671901) | [2s](https://github.com/iree-org/iree/actions/runs/29691025428/job/88203671901) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88187254987) | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88187254987) | [2s](https://github.com/iree-org/iree/actions/runs/29675791124/job/88187254987) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29684852401/job/88187263166) | [2s](https://github.com/iree-org/iree/actions/runs/29684852401/job/88187263166) | [2s](https://github.com/iree-org/iree/actions/runs/29684852401/job/88187263166) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 175 | 1% (1/175) |  | 1d19h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 141 | 9% (13/141) |  | 1d19h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 150 | 1% (2/150) |  | 1d19h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 137 | 0% (0/137) |  | 1d19h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 41 | 0% (0/41) |  | 1d20h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
