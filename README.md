# iree-ci-monitor

_Updated: 2026-05-10 05:38 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 7 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25627683215/job/75225632775) | [8s](https://github.com/iree-org/iree/actions/runs/25627683215/job/75225632781) | — | 7 |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25621413539/job/75208691478) | [4s](https://github.com/iree-org/iree/actions/runs/25621413539/job/75208691476) | 0% (0/1) | 10 |
| `macos-14` | github-hosted | 2 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25621413539/job/75208691470) | [3s](https://github.com/iree-org/iree/actions/runs/25621413539/job/75208691463) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25621413539/job/75208691469) | [3s](https://github.com/iree-org/iree/actions/runs/25621413539/job/75208691479) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25621413539/job/75208691458) | [2s](https://github.com/iree-org/iree/actions/runs/25621413539/job/75208691462) | — | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 651 | 2% (12/649) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 756 | 3% (24/754) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 909 | 8% (77/906) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 965 | 5% (48/963) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 248 | 2% (5/247) | yes | running |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
