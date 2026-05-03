# iree-ci-monitor

_Updated: 2026-05-03 00:09 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664148) | [8s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664150) | 0% (0/1) | 6 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664145) | [3s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664147) | — | 3 |
| `macos-14` | github-hosted | 2 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664151) | [3s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664168) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664165) | [2s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664170) | — | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1024 | 5% (54/1023) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 885 | 3% (24/884) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 799 | 1% (11/799) |  | 1d01h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 610 | 6% (38/610) |  | 1d01h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 237 | 2% (5/237) |  | 1d02h ago |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 64 | 11% (7/64) |  | 5d09h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
