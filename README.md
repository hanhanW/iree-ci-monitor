# iree-ci-monitor

_Updated: 2026-04-30 18:18 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 40 | 18 | [8h40m](https://github.com/iree-org/iree/actions/runs/25177015220/job/73813311553) | 1 | [1h43m](https://github.com/iree-org/iree/actions/runs/25193803956/job/73870588477) | [6h36m](https://github.com/iree-org/iree/actions/runs/25181554794/job/73829168122) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 41 | 19 | [7h12m](https://github.com/iree-org/iree/actions/runs/25180977027/job/73827280187) | 0 | [49m09s](https://github.com/iree-org/iree/actions/runs/25193803956/job/73870588492) | [5h58m](https://github.com/iree-org/iree/actions/runs/25177015220/job/73813311523) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 81 | 28 | [7h00m](https://github.com/iree-org/iree/actions/runs/25181554794/job/73829168010) | 1 | [1h09m](https://github.com/iree-org/iree/actions/runs/25175016945/job/73805735183) | [5h32m](https://github.com/iree-org/iree/actions/runs/25185250008/job/73841971842) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 40 | 1 | [49m35s](https://github.com/iree-org/iree/actions/runs/25195977379/job/73877311974) | 0 | [57m51s](https://github.com/iree-org/iree/actions/runs/25186271144/job/73845573594) | [3h57m](https://github.com/iree-org/iree/actions/runs/25188878700/job/73854815467) | 0% (0/8) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 40 | 0 | — | 0 | [29m58s](https://github.com/iree-org/iree/actions/runs/25182050890/job/73831108945) | [3h10m](https://github.com/iree-org/iree/actions/runs/25187246783/job/73850396984) | 0% (0/9) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 40 | 0 | — | 0 | [1h01m](https://github.com/iree-org/iree/actions/runs/25178803390/job/73819498106) | [3h09m](https://github.com/iree-org/iree/actions/runs/25186904450/job/73851226925) | 11% (1/9) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 41 | 1 | [40m01s](https://github.com/iree-org/iree/actions/runs/25196262788/job/73878205569) | 1 | [1h18m](https://github.com/iree-org/iree/actions/runs/25175016945/job/73805735026) | [3h07m](https://github.com/iree-org/iree/actions/runs/25186904450/job/73851227112) | 0% (0/8) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 81 | 0 | — | 0 | [34m19s](https://github.com/iree-org/iree/actions/runs/25181157670/job/73827605169) | [2h40m](https://github.com/iree-org/iree/actions/runs/25186904450/job/73851227230) | 0% (0/18) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 112 | 0 | — | 0 | [40m17s](https://github.com/iree-org/iree/actions/runs/25193007052/job/73868033523) | [2h33m](https://github.com/iree-org/iree/actions/runs/25187246783/job/73850397166) | 0% (0/25) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 40 | 0 | — | 0 | [29m36s](https://github.com/iree-org/iree/actions/runs/25195139781/job/73874984478) | [2h19m](https://github.com/iree-org/iree/actions/runs/25187812990/job/73851113581) | 0% (0/9) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 40 | 0 | — | 0 | [17m00s](https://github.com/iree-org/iree/actions/runs/25186189594/job/73845357455) | [1h56m](https://github.com/iree-org/iree/actions/runs/25188872672/job/73854397096) | 0% (0/9) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 40 | 0 | — | 0 | [32m15s](https://github.com/iree-org/iree/actions/runs/25181924016/job/73830081780) | [1h53m](https://github.com/iree-org/iree/actions/runs/25188872672/job/73854397069) | 0% (0/9) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 40 | 0 | — | 0 | [3m22s](https://github.com/iree-org/iree/actions/runs/25184521011/job/73839329350) | [41m04s](https://github.com/iree-org/iree/actions/runs/25186449222/job/73847188118) | 0% (0/9) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 162 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25196262788/job/73878205620) | [7m20s](https://github.com/iree-org/iree/actions/runs/25187307476/job/73850267664) | 11% (4/36) | 161 |
| `macos-14` | github-hosted | 141 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25195139770/job/73873940479) | [4m37s](https://github.com/iree-org/iree/actions/runs/25186688311/job/73846450715) | 0% (0/27) | 141 |
| `ubuntu-24.04` | github-hosted | 773 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25182050890/job/73831109143) | [4m04s](https://github.com/iree-org/iree/actions/runs/25186449259/job/73845281044) | 1% (1/139) | 769 |
| `ubuntu-24.04-arm` | github-hosted | 141 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25193199915/job/73867820237) | [3m05s](https://github.com/iree-org/iree/actions/runs/25184527331/job/73838247357) | 0% (0/27) | 140 |
| `windows-2022` | github-hosted | 141 | 0 | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/25181157675/job/73826513534) | [2m25s](https://github.com/iree-org/iree/actions/runs/25186449259/job/73845281058) | 0% (0/27) | 139 |
| `ubuntu-latest` | github-hosted | 72 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25193747718/job/73869536964) | [2m16s](https://github.com/iree-org/iree/actions/runs/25184531516/job/73838237655) | 0% (0/18) | 72 |
| `azure-linux-scale` | ossci | 249 | 0 | — | 0 | [11s](https://github.com/iree-org/iree/actions/runs/25173730114/job/73800339294) | [51s](https://github.com/iree-org/iree/actions/runs/25188878678/job/73853440421) | 0% (0/55) | 244 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 40 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25178269937/job/73817386284) | [10s](https://github.com/iree-org/iree/actions/runs/25173730132/job/73801366463) | 22% (2/9) | 40 |
| `azure-windows-scale` | ossci | 47 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25193749565/job/73869563115) | [8s](https://github.com/iree-org/iree/actions/runs/25185250013/job/73841061899) | 11% (1/9) | 47 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 410 | 7% (28/409) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 931 | 3% (24/927) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1059 | 5% (55/1055) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 875 | 1% (10/874) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 266 | 2% (4/265) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 323 | 13% (42/321) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 7h00m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 8h40m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 7h12m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h53m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h40m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 5h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 3h10m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 3h57m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 6h36m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 5h58m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h56m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 3h07m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h33m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
