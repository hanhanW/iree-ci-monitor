# iree-ci-monitor

_Updated: 2026-05-07 23:58 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 42 | 0 | — | 1 | [1h29m](https://github.com/iree-org/iree/actions/runs/25536256872/job/74959512181) | [7h09m](https://github.com/iree-org/iree/actions/runs/25523405349/job/74914231716) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 21 | 0 | — | 0 | [21m01s](https://github.com/iree-org/iree/actions/runs/25526891462/job/74925199837) | [6h35m](https://github.com/iree-org/iree/actions/runs/25525242265/job/74920104198) | 0% (0/4) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 21 | 0 | — | 0 | [54m11s](https://github.com/iree-org/iree/actions/runs/25527815290/job/74928103875) | [6h21m](https://github.com/iree-org/iree/actions/runs/25528463019/job/74929932819) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 21 | 0 | — | 0 | [1h25m](https://github.com/iree-org/iree/actions/runs/25530525047/job/74936409326) | [4h56m](https://github.com/iree-org/iree/actions/runs/25528463019/job/74929932795) | 0% (0/4) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 21 | 0 | — | 0 | [59m30s](https://github.com/iree-org/iree/actions/runs/25523663200/job/74915051704) | [4h01m](https://github.com/iree-org/iree/actions/runs/25523405349/job/74914231619) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 21 | 0 | — | 0 | [12m28s](https://github.com/iree-org/iree/actions/runs/25530776586/job/74937387101) | [3h44m](https://github.com/iree-org/iree/actions/runs/25528190121/job/74929278297) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 21 | 0 | — | 0 | [30m20s](https://github.com/iree-org/iree/actions/runs/25525875632/job/74922116563) | [2h40m](https://github.com/iree-org/iree/actions/runs/25523405349/job/74914231653) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 42 | 0 | — | 0 | [45m56s](https://github.com/iree-org/iree/actions/runs/25530525047/job/74936409312) | [2h13m](https://github.com/iree-org/iree/actions/runs/25528463019/job/74929932804) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 21 | 0 | — | 0 | [35m32s](https://github.com/iree-org/iree/actions/runs/25532313521/job/74942195416) | [2h06m](https://github.com/iree-org/iree/actions/runs/25528463019/job/74929932753) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 21 | 0 | — | 0 | [20m34s](https://github.com/iree-org/iree/actions/runs/25530776586/job/74937387150) | [1h42m](https://github.com/iree-org/iree/actions/runs/25528190121/job/74929278315) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 21 | 0 | — | 0 | [25m34s](https://github.com/iree-org/iree/actions/runs/25526891462/job/74925199917) | [1h31m](https://github.com/iree-org/iree/actions/runs/25523405349/job/74914231721) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 42 | 0 | — | 0 | [11m04s](https://github.com/iree-org/iree/actions/runs/25528190121/job/74929278307) | [1h15m](https://github.com/iree-org/iree/actions/runs/25525875632/job/74922116729) | 12% (1/8) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 21 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25524917780/job/74919175834) | [8m54s](https://github.com/iree-org/iree/actions/runs/25530980013/job/74937723454) | 0% (0/4) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 84 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25527815290/job/74928103868) | [4m21s](https://github.com/iree-org/iree/actions/runs/25530086833/job/74935020343) | 31% (5/16) | 84 |
| `ubuntu-24.04` | github-hosted | 454 | 0 | — | 3 | [8s](https://github.com/iree-org/iree/actions/runs/25525242265/job/74920104174) | [2m14s](https://github.com/iree-org/iree/actions/runs/25523865862/job/74915850649) | 8% (7/85) | 454 |
| `ubuntu-24.04-arm` | github-hosted | 78 | 0 | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/25525242274/job/74919260733) | [1m44s](https://github.com/iree-org/iree/actions/runs/25528463026/job/74929333667) | 0% (0/15) | 78 |
| `azure-windows-scale` | ossci | 25 | 0 | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/25529157672/job/74931420575) | [1m35s](https://github.com/iree-org/iree/actions/runs/25530086843/job/74934307804) | 25% (1/4) | 25 |
| `windows-2022` | github-hosted | 77 | 0 | — | 4 | [3s](https://github.com/iree-org/iree/actions/runs/25522427210/job/74909734002) | [1m23s](https://github.com/iree-org/iree/actions/runs/25530776617/job/74936440132) | 0% (0/12) | 77 |
| `azure-linux-scale` | ossci | 131 | 5 | [7m35s](https://github.com/iree-org/iree/actions/runs/25541570366/job/74968454389) | 1 | [8s](https://github.com/iree-org/iree/actions/runs/25530980056/job/74937254730) | [1m05s](https://github.com/iree-org/iree/actions/runs/25532313513/job/74941014070) | 0% (0/24) | 123 |
| `macos-14` | github-hosted | 77 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25526891503/job/74924467750) | [53s](https://github.com/iree-org/iree/actions/runs/25530776617/job/74936440139) | 0% (0/15) | 77 |
| `ubuntu-latest` | github-hosted | 44 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25541787411/job/74969074846) | [12s](https://github.com/iree-org/iree/actions/runs/25523404348/job/74913069257) | 0% (0/10) | 44 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 21 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25530980013/job/74937723360) | [2s](https://github.com/iree-org/iree/actions/runs/25530086833/job/74935020352) | 25% (1/4) | 21 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 889 | 2% (20/886) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 692 | 2% (12/690) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 826 | 7% (57/823) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 585 | 2% (10/583) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 221 | 2% (4/220) | yes | running |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h42m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h13m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 6h21m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 7h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 4h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h40m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 3h44m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 6h35m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 4h56m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h31m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h06m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h15m (> 1h00m)
- **[high-failure-main]** `linux-mi325-1gpu-ossci-iree-org` main-branch failure rate 31% (5/16)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
