# iree-ci-monitor

_Updated: 2026-05-09 00:02 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 30 | 0 | — | 0 | [3h41m](https://github.com/iree-org/iree/actions/runs/25586349104/job/75121119248) | [6h42m](https://github.com/iree-org/iree/actions/runs/25581695300/job/75104651084) | 0% (0/10) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 15 | 0 | — | 0 | [3h08m](https://github.com/iree-org/iree/actions/runs/25582228510/job/75105530893) | [6h20m](https://github.com/iree-org/iree/actions/runs/25583911816/job/75110594826) | 0% (0/5) | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 13 | 0 | — | 0 | [1h27m](https://github.com/iree-org/iree/actions/runs/25581029007/job/75103295839) | [4h36m](https://github.com/iree-org/iree/actions/runs/25581695300/job/75104651087) | 20% (1/5) | `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 15 | 0 | — | 0 | [2h23m](https://github.com/iree-org/iree/actions/runs/25583203487/job/75107094191) | [3h41m](https://github.com/iree-org/iree/actions/runs/25581695300/job/75104651051) | 0% (0/5) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 15 | 0 | — | 0 | [1h08m](https://github.com/iree-org/iree/actions/runs/25579494456/job/75096405179) | [2h56m](https://github.com/iree-org/iree/actions/runs/25583203487/job/75107094160) | 80% (4/5) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 30 | 0 | — | 0 | [34m52s](https://github.com/iree-org/iree/actions/runs/25579494456/job/75096405282) | [2h29m](https://github.com/iree-org/iree/actions/runs/25580147932/job/75098136025) | 0% (0/10) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 15 | 0 | — | 0 | [43m01s](https://github.com/iree-org/iree/actions/runs/25581029007/job/75103295776) | [2h27m](https://github.com/iree-org/iree/actions/runs/25581695300/job/75104651033) | 0% (0/5) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 15 | 0 | — | 0 | [1h35m](https://github.com/iree-org/iree/actions/runs/25583911816/job/75110594781) | [2h20m](https://github.com/iree-org/iree/actions/runs/25579494456/job/75096405084) | 80% (4/5) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 15 | 0 | — | 0 | [39m59s](https://github.com/iree-org/iree/actions/runs/25580020835/job/75097780108) | [1h51m](https://github.com/iree-org/iree/actions/runs/25581695300/job/75104651110) | 0% (0/5) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 30 | 0 | — | 0 | [19m31s](https://github.com/iree-org/iree/actions/runs/25588230197/job/75121533365) | [1h42m](https://github.com/iree-org/iree/actions/runs/25580147932/job/75098135780) | 0% (0/10) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 17 | 0 | — | 0 | [18m09s](https://github.com/iree-org/iree/actions/runs/25583911816/job/75110594810) | [45m40s](https://github.com/iree-org/iree/actions/runs/25585445125/job/75113742349) | 0% (0/5) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 15 | 0 | — | 0 | [7m13s](https://github.com/iree-org/iree/actions/runs/25583911816/job/75110594817) | [36m41s](https://github.com/iree-org/iree/actions/runs/25583203487/job/75107094195) | 0% (0/5) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 105 | 0 | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/25585445153/job/75113127517) | [11m53s](https://github.com/iree-org/iree/actions/runs/25582228510/job/75103537666) | 0% (0/31) | 98 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 15 | 0 | — | 0 | [3m55s](https://github.com/iree-org/iree/actions/runs/25588230197/job/75121533377) | [10m34s](https://github.com/iree-org/iree/actions/runs/25580147932/job/75098135779) | 0% (0/5) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 60 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25586349104/job/75121119165) | [9m37s](https://github.com/iree-org/iree/actions/runs/25580147932/job/75098136032) | 20% (4/20) | 60 |
| `azure-windows-scale` | ossci | 20 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25584377758/job/75109926594) | [1m23s](https://github.com/iree-org/iree/actions/runs/25580147921/job/75097163167) | 0% (0/5) | 20 |
| `windows-2022` | github-hosted | 62 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25580147921/job/75097163067) | [55s](https://github.com/iree-org/iree/actions/runs/25580020808/job/75096726693) | 0% (0/15) | 62 |
| `ubuntu-24.04` | github-hosted | 345 | 0 | — | 2 | [8s](https://github.com/iree-org/iree/actions/runs/25579494468/job/75109955612) | [48s](https://github.com/iree-org/iree/actions/runs/25580020808/job/75096726583) | 4% (4/90) | 344 |
| `macos-14` | github-hosted | 62 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25582806173/job/75105413715) | [44s](https://github.com/iree-org/iree/actions/runs/25581695297/job/75101859704) | 0% (0/15) | 62 |
| `ubuntu-24.04-arm` | github-hosted | 63 | 0 | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/25580147921/job/75097163085) | [29s](https://github.com/iree-org/iree/actions/runs/25581695297/job/75101859715) | 0% (0/15) | 63 |
| `ubuntu-latest` | github-hosted | 33 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25581659063/job/75101716315) | [24s](https://github.com/iree-org/iree/actions/runs/25580017910/job/75096478321) | 0% (0/10) | 33 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 15 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25583911816/job/75110594707) | [2s](https://github.com/iree-org/iree/actions/runs/25584377810/job/75111209240) | 100% (5/5) | 15 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 939 | 5% (45/937) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 882 | 8% (71/879) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 736 | 3% (24/734) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 636 | 2% (12/634) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 242 | 2% (5/241) | yes | running |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h29m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 6h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 6h42m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h56m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 2h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 3h41m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 4h36m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h51m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h42m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
