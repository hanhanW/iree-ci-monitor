# iree-ci-monitor

_Updated: 2026-08-31 22:15 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 4 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33469915714/job/99737403236) | [4s](https://github.com/iree-org/iree/actions/runs/33442733891/job/99654566591) | 0% (0/4) | 4 |
| `ubuntu-24.04` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33469674032/job/99738472413) | [3s](https://github.com/iree-org/iree/actions/runs/33469674032/job/99736701619) | 0% (0/3) | 3 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/dependabot/dependabot-updates` | Dependabot | `ubuntu-latest` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/33442733891/job/99654566591) | [4s](https://github.com/iree-org/iree/actions/runs/33442733891/job/99654566591) | [4s](https://github.com/iree-org/iree/actions/runs/33442733891/job/99654566591) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33469674032/job/99736701619) | [3s](https://github.com/iree-org/iree/actions/runs/33469674032/job/99736701619) | [3s](https://github.com/iree-org/iree/actions/runs/33469674032/job/99736701619) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33469915714/job/99737403236) | [3s](https://github.com/iree-org/iree/actions/runs/33469915714/job/99737403236) | [3s](https://github.com/iree-org/iree/actions/runs/33469915714/job/99737403236) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33469674032/job/99736701416) | [2s](https://github.com/iree-org/iree/actions/runs/33469674032/job/99736701416) | [2s](https://github.com/iree-org/iree/actions/runs/33469674032/job/99736701416) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33469674032/job/99738472413) | [2s](https://github.com/iree-org/iree/actions/runs/33469674032/job/99738472413) | [2s](https://github.com/iree-org/iree/actions/runs/33469674032/job/99738472413) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33469915714/job/99737403393) | [2s](https://github.com/iree-org/iree/actions/runs/33469915714/job/99737403393) | [2s](https://github.com/iree-org/iree/actions/runs/33469915714/job/99737403393) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33469915714/job/99737403430) | [2s](https://github.com/iree-org/iree/actions/runs/33469915714/job/99737403430) | [2s](https://github.com/iree-org/iree/actions/runs/33469915714/job/99737403430) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 265 | 0% (1/265) |  | 13h59m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 191 | 1% (1/191) |  | 14h49m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 185 | 0% (0/185) |  | 14h51m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 222 | 4% (9/222) |  | 14h54m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
