# iree-ci-monitor

_Updated: 2026-04-25 23:58 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 1 | 0 | — | 0 | [11m23s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312700) | [11m23s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312700) | — | `shark10-ci-2` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | 0 | [9m27s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312695) | [9m27s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312695) | — | `shark10-ci-2` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | 0 | [8m01s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312666) | [8m01s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312666) | — | `shark01-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | 0 | [6m43s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312703) | [6m43s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312703) | — | `shark10-ci-2` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 3 | 0 | — | 1 | [5m42s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312685) | [6m34s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312711) | — | `shark55-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | 0 | [6m14s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312664) | [6m14s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312664) | — | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 1 | [5h56m](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312687) | 0 | [5m28s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312694) | [5m28s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312694) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312691) | [5m00s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312715) | — | `shark01-ci`, `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312686) | [2m19s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312717) | — | 4 |
| `azure-linux-scale` | ossci | 7 | 0 | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73043998096) | [2m03s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73043998078) | — | 7 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m40s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73043998090) | [1m40s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73043998090) | — | 1 |
| `ubuntu-latest` | github-hosted | 2 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24944671074/job/73043947727) | [4s](https://github.com/iree-org/iree/actions/runs/24944671074/job/73043947737) | — | 2 |
| `ubuntu-24.04` | github-hosted | 27 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73057801941) | [3s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312643) | 0% (0/1) | 27 |
| `macos-14` | github-hosted | 6 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73043998076) | [3s](https://github.com/iree-org/iree/actions/runs/24949550708/job/73057126279) | — | 6 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73043998091) | [3s](https://github.com/iree-org/iree/actions/runs/24949550708/job/73057126271) | — | 6 |
| `windows-2022` | github-hosted | 5 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73043998077) | [2s](https://github.com/iree-org/iree/actions/runs/24949550708/job/73057126280) | — | 5 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73043998130) | [2s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73043998130) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312592) | [2s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312592) | — | 1 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312594) | [2s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312594) | — | `shark75-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73043998102) | [1s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73043998102) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312617) | [1s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312617) | — | `shark01-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312699) | [1s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312699) | — | `iree-mi308-1` |
| `Linux,X64,rdna3` | self-hosted | 1 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312704) | [1s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312704) | — | `shark10-ci-2` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [5h56m](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312696) | 0 | 0s | 0s | — | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 406 | 14% (56/402) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 114 | 0% (0/111) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 315 | 3% (9/310) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 298 | 0% (0/294) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 374 | 2% (7/369) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 5h56m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 5h56m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
