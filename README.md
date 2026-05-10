# iree-ci-monitor

_Updated: 2026-05-10 00:13 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `azure-linux-scale` | ossci | 5 | 0 | — | 0 | [6m25s](https://github.com/iree-org/iree/actions/runs/25612674106/job/75185413467) | [7m39s](https://github.com/iree-org/iree/actions/runs/25612674106/job/75185413488) | — | 5 |
| `windows-2022` | github-hosted | 5 | 0 | — | 1 | [1m04s](https://github.com/iree-org/iree/actions/runs/25612674106/job/75185413456) | [1m37s](https://github.com/iree-org/iree/actions/runs/25612674106/job/75185413425) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25621413539/job/75208691462) | [1m30s](https://github.com/iree-org/iree/actions/runs/25612674106/job/75185413446) | — | 6 |
| `macos-14` | github-hosted | 5 | 0 | — | 1 | [12s](https://github.com/iree-org/iree/actions/runs/25612674106/job/75185413442) | [1m18s](https://github.com/iree-org/iree/actions/runs/25612674106/job/75185413441) | — | 5 |
| `ubuntu-24.04` | github-hosted | 29 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25621413539/job/75208691464) | [1m06s](https://github.com/iree-org/iree/actions/runs/25612674106/job/75185413448) | 0% (0/2) | 29 |
| `ubuntu-latest` | github-hosted | 2 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25612673216/job/75185398130) | [4s](https://github.com/iree-org/iree/actions/runs/25612673216/job/75185398131) | — | 2 |
| `azure-windows-scale` | ossci | 1 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25612674106/job/75185413472) | [1s](https://github.com/iree-org/iree/actions/runs/25612674106/job/75185413472) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25612674104/job/75189017470) | [1s](https://github.com/iree-org/iree/actions/runs/25612674104/job/75189017470) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25612674104/job/75189017475) | [1s](https://github.com/iree-org/iree/actions/runs/25612674104/job/75189017475) | — | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25612674104/job/75189017523) | [1s](https://github.com/iree-org/iree/actions/runs/25612674104/job/75189017523) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 1 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25612674104/job/75189017592) | [1s](https://github.com/iree-org/iree/actions/runs/25612674104/job/75189017592) | — | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | 0 | 0s | 0s | — | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | 0 | 0s | 0s | — | `shark01-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | 0 | 0s | 0s | — | 4 |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | 0 | 0s | 0s | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 1 | 0 | — | 0 | 0s | 0s | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | 0 | 0s | 0s | — | `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | 0 | 0s | 0s | — | `iree-mi308-1` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | 0 | 0s | 0s | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | 0 | 0s | 0s | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | 0 | 0s | 0s | — | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | 0 | 0s | 0s | — | `shark75-ci` |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 651 | 2% (12/649) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 756 | 3% (24/754) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 909 | 8% (77/906) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 965 | 5% (48/963) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 248 | 2% (5/247) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
