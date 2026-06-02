# iree-ci-monitor

_Updated: 2026-06-01 18:27 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26766665391/job/78894816659) | [4s](https://github.com/iree-org/iree/actions/runs/26766664674/job/78894850368) | — | 6 |
| `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26766333978/job/78893604565) | [2s](https://github.com/iree-org/iree/actions/runs/26766333978/job/78893604565) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/26766664674/job/78894850368) | [4s](https://github.com/iree-org/iree/actions/runs/26766664674/job/78894850368) | [4s](https://github.com/iree-org/iree/actions/runs/26766664674/job/78894850368) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26766664674/job/78894821043) | [3s](https://github.com/iree-org/iree/actions/runs/26766664674/job/78894821043) | [3s](https://github.com/iree-org/iree/actions/runs/26766664674/job/78894821043) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26766664674/job/78894850355) | [3s](https://github.com/iree-org/iree/actions/runs/26766664674/job/78894850355) | [3s](https://github.com/iree-org/iree/actions/runs/26766664674/job/78894850355) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26766333978/job/78893604565) | [2s](https://github.com/iree-org/iree/actions/runs/26766333978/job/78893604565) | [2s](https://github.com/iree-org/iree/actions/runs/26766333978/job/78893604565) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26766665391/job/78894816354) | [2s](https://github.com/iree-org/iree/actions/runs/26766665391/job/78894816354) | [2s](https://github.com/iree-org/iree/actions/runs/26766665391/job/78894816354) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26766665391/job/78894816659) | [2s](https://github.com/iree-org/iree/actions/runs/26766665391/job/78894816659) | [2s](https://github.com/iree-org/iree/actions/runs/26766665391/job/78894816659) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26766665391/job/78894816243) | [2s](https://github.com/iree-org/iree/actions/runs/26766665391/job/78894816243) | [2s](https://github.com/iree-org/iree/actions/runs/26766665391/job/78894816243) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 230 | 5% (11/229) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 256 | 0% (1/256) |  | 12h47m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 172 | 1% (1/172) |  | 12h52m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 180 | 0% (0/180) |  | 12h54m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 57 | 2% (1/57) |  | 13h08m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
