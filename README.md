# iree-ci-monitor

_Updated: 2026-05-07 18:15 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 82 | 26 | [6h17m](https://github.com/iree-org/iree/actions/runs/25515576646/job/74887000302) | 1 | [0s](https://github.com/iree-org/iree/actions/runs/25525875632/job/74922116755) | [4h57m](https://github.com/iree-org/iree/actions/runs/25519062199/job/74899400671) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 82 | 7 | [1h23m](https://github.com/iree-org/iree/actions/runs/25528190121/job/74929278348) | 2 | [13m07s](https://github.com/iree-org/iree/actions/runs/25509285996/job/74865071831) | [3h29m](https://github.com/iree-org/iree/actions/runs/25523405349/job/74914231738) | 0% (0/10) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 41 | 5 | [3h31m](https://github.com/iree-org/iree/actions/runs/25523405349/job/74914231619) | 0 | [8m07s](https://github.com/iree-org/iree/actions/runs/25509285996/job/74865071698) | [3h16m](https://github.com/iree-org/iree/actions/runs/25513473692/job/74880066348) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 41 | 13 | [7h45m](https://github.com/iree-org/iree/actions/runs/25510413063/job/74871735300) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25525875632/job/74922116736) | [3h10m](https://github.com/iree-org/iree/actions/runs/25513473692/job/74880066747) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 41 | 7 | [5h03m](https://github.com/iree-org/iree/actions/runs/25519062199/job/74899400682) | 0 | [5m36s](https://github.com/iree-org/iree/actions/runs/25512800403/job/74877117593) | [2h49m](https://github.com/iree-org/iree/actions/runs/25515576646/job/74886999999) | 0% (0/5) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 41 | 9 | [4h38m](https://github.com/iree-org/iree/actions/runs/25520299281/job/74903648182) | 0 | [27s](https://github.com/iree-org/iree/actions/runs/25510569869/job/74869599839) | [2h33m](https://github.com/iree-org/iree/actions/runs/25519062199/job/74899400587) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 41 | 3 | [1h16m](https://github.com/iree-org/iree/actions/runs/25528463019/job/74929932753) | 1 | [6m43s](https://github.com/iree-org/iree/actions/runs/25509285996/job/74865071781) | [2h27m](https://github.com/iree-org/iree/actions/runs/25523405349/job/74914231913) | 0% (0/6) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 82 | 4 | [27m39s](https://github.com/iree-org/iree/actions/runs/25529982572/job/74934647567) | 2 | [17m24s](https://github.com/iree-org/iree/actions/runs/25528463019/job/74929932760) | [2h06m](https://github.com/iree-org/iree/actions/runs/25518745717/job/74900076138) | 7% (1/14) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 41 | 4 | [1h23m](https://github.com/iree-org/iree/actions/runs/25528190121/job/74929278315) | 0 | [5m15s](https://github.com/iree-org/iree/actions/runs/25510569869/job/74869599717) | [1h34m](https://github.com/iree-org/iree/actions/runs/25521304092/job/74907082895) | 0% (0/5) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 41 | 9 | [5h03m](https://github.com/iree-org/iree/actions/runs/25519062199/job/74899400605) | 0 | [4m43s](https://github.com/iree-org/iree/actions/runs/25510569869/job/74869599780) | [1h23m](https://github.com/iree-org/iree/actions/runs/25512800403/job/74877117648) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 41 | 2 | [23m37s](https://github.com/iree-org/iree/actions/runs/25530086833/job/74935020419) | 0 | [11m54s](https://github.com/iree-org/iree/actions/runs/25528190121/job/74929278353) | [1h10m](https://github.com/iree-org/iree/actions/runs/25525875632/job/74922116741) | 0% (0/7) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 41 | 18 | [7h45m](https://github.com/iree-org/iree/actions/runs/25510413063/job/74871735351) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25523663200/job/74915052018) | [43m57s](https://github.com/iree-org/iree/actions/runs/25510068890/job/74867611730) | — | `shark10-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 164 | 0 | — | 2 | [9s](https://github.com/iree-org/iree/actions/runs/25516615546/job/74890547642) | [8m36s](https://github.com/iree-org/iree/actions/runs/25511400083/job/74872580467) | 32% (9/28) | 157 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 41 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25527815290/job/74928103916) | [6m27s](https://github.com/iree-org/iree/actions/runs/25530086833/job/74935020386) | 0% (0/7) | `iree-mi308-1` |
| `macos-14` | github-hosted | 150 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25526891503/job/74924467765) | [2m33s](https://github.com/iree-org/iree/actions/runs/25517002736/job/74890785812) | 0% (0/21) | 150 |
| `azure-linux-scale` | ossci | 263 | 0 | — | 8 | [9s](https://github.com/iree-org/iree/actions/runs/25517731535/job/74893963794) | [2m18s](https://github.com/iree-org/iree/actions/runs/25510569869/job/74867976715) | 0% (0/43) | 259 |
| `ubuntu-24.04` | github-hosted | 841 | 0 | — | 3 | [8s](https://github.com/iree-org/iree/actions/runs/25529157742/job/74932310247) | [2m14s](https://github.com/iree-org/iree/actions/runs/25523865862/job/74915850649) | 2% (2/114) | 827 |
| `ubuntu-24.04-arm` | github-hosted | 150 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25526891503/job/74924467710) | [2m04s](https://github.com/iree-org/iree/actions/runs/25510668846/job/74868333983) | 0% (0/21) | 150 |
| `ubuntu-latest` | github-hosted | 59 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25516611644/job/74889340220) | [2m04s](https://github.com/iree-org/iree/actions/runs/25517167850/job/74891315389) | 0% (0/14) | 59 |
| `windows-2022` | github-hosted | 150 | 0 | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/25521304114/job/74905774232) | [1m37s](https://github.com/iree-org/iree/actions/runs/25518745600/job/74896888393) | 5% (1/21) | 150 |
| `azure-windows-scale` | ossci | 50 | 0 | — | 2 | [1s](https://github.com/iree-org/iree/actions/runs/25525242274/job/74919260737) | [22s](https://github.com/iree-org/iree/actions/runs/25509286041/job/74863458079) | 14% (1/7) | 50 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 41 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25510668756/job/74869828450) | [2s](https://github.com/iree-org/iree/actions/runs/25527815290/job/74928103854) | 29% (2/7) | 40 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 564 | 2% (10/560) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 771 | 7% (53/767) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 828 | 2% (17/825) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 660 | 2% (12/657) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 216 | 2% (4/214) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 5h03m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 6h17m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 3h31m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 5h03m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 4h38m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 7h45m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 7h45m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h34m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 3h29m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h23m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 4h57m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h16m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h49m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 2h33m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 3h10m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h10m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h27m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h06m (> 1h00m)
- **[high-failure-main]** `linux-mi325-1gpu-ossci-iree-org` main-branch failure rate 32% (9/28)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
