# iree-ci-monitor

_Updated: 2026-04-26 05:32 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24949550708/job/73057126256) | [3s](https://github.com/iree-org/iree/actions/runs/24954826040/job/73071154434) | 0% (0/1) | 10 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24949550708/job/73057126264) | [3s](https://github.com/iree-org/iree/actions/runs/24949550708/job/73057126271) | — | 3 |
| `macos-14` | github-hosted | 2 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24949550708/job/73057126263) | [3s](https://github.com/iree-org/iree/actions/runs/24949550708/job/73057126279) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24949550708/job/73057126259) | [2s](https://github.com/iree-org/iree/actions/runs/24949550708/job/73057126280) | — | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 376 | 2% (7/372) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 406 | 14% (56/402) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 114 | 0% (0/111) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 315 | 3% (9/310) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 298 | 0% (0/294) | yes | running |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
