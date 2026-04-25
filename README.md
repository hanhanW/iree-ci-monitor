# iree-ci-monitor

_Updated: 2026-04-24 23:49 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 22 | 0 | — | 0 | [2h03m](https://github.com/iree-org/iree/actions/runs/24910031636/job/72956005655) | [7h34m](https://github.com/iree-org/iree/actions/runs/24910032356/job/72953137411) | 0% (0/4) | `shark10-ci-2` |
| `Linux,X64,gfx1201` | self-hosted | 44 | 13 | [9h58m](https://github.com/iree-org/iree/actions/runs/24910032356/job/72953137470) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091871) | [7h24m](https://github.com/iree-org/iree/actions/runs/24913503923/job/72961230361) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 22 | 0 | — | 0 | [1h32m](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091880) | [5h53m](https://github.com/iree-org/iree/actions/runs/24914205009/job/72965265595) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 22 | 0 | — | 0 | [2h54m](https://github.com/iree-org/iree/actions/runs/24911179954/job/72955892254) | [5h14m](https://github.com/iree-org/iree/actions/runs/24913399955/job/72960739348) | 0% (0/4) | `shark10-ci-2` |
| `Linux,X64,iree-r9700` | self-hosted | 22 | 1 | [1h22m](https://github.com/iree-org/iree/actions/runs/24923453747/job/72989537395) | 0 | [2h03m](https://github.com/iree-org/iree/actions/runs/24910031636/job/72956005492) | [4h37m](https://github.com/iree-org/iree/actions/runs/24914205009/job/72965265543) | 0% (0/4) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 25 | 0 | — | 0 | [1h59m](https://github.com/iree-org/iree/actions/runs/24910032356/job/72953137463) | [4h31m](https://github.com/iree-org/iree/actions/runs/24911179954/job/72955892205) | 0% (0/4) | `shark01-ci`, `shark10-ci-2` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 22 | 0 | — | 0 | [59m41s](https://github.com/iree-org/iree/actions/runs/24902742119/job/72968972690) | [3h36m](https://github.com/iree-org/iree/actions/runs/24910032356/job/72953137420) | 25% (1/4) | `shark01-ci`, `shark10-ci-2` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 63 | 0 | — | 0 | [1h05m](https://github.com/iree-org/iree/actions/runs/24917071869/job/72971608460) | [2h49m](https://github.com/iree-org/iree/actions/runs/24916595314/job/72970329964) | 0% (0/12) | `shark01-ci`, `shark10-ci-2`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 22 | 0 | — | 0 | [1h05m](https://github.com/iree-org/iree/actions/runs/24916595314/job/72970329892) | [2h44m](https://github.com/iree-org/iree/actions/runs/24910183738/job/72953295568) | 0% (0/4) | `shark01-ci`, `shark10-ci-2` |
| `Linux,X64,gfx1100` | self-hosted | 44 | 0 | — | 0 | [45m21s](https://github.com/iree-org/iree/actions/runs/24917391141/job/72972530158) | [2h13m](https://github.com/iree-org/iree/actions/runs/24910183738/job/72953295587) | 0% (0/8) | `shark01-ci`, `shark10-ci-2`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 22 | 0 | — | 0 | [25m42s](https://github.com/iree-org/iree/actions/runs/24917391141/job/72972530128) | [2h07m](https://github.com/iree-org/iree/actions/runs/24910031636/job/72956005709) | 0% (0/4) | `shark01-ci`, `shark10-ci-2`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 22 | 0 | — | 0 | [53m20s](https://github.com/iree-org/iree/actions/runs/24917391141/job/72972530107) | [1h57m](https://github.com/iree-org/iree/actions/runs/24911179954/job/72955892237) | 0% (0/4) | `shark01-ci`, `shark10-ci-2`, `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 88 | 0 | — | 0 | [4m45s](https://github.com/iree-org/iree/actions/runs/24917391141/job/72972530160) | [44m07s](https://github.com/iree-org/iree/actions/runs/24910031636/job/72956005490) | 6% (1/16) | 84 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 22 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24920075927/job/72980115067) | [9m31s](https://github.com/iree-org/iree/actions/runs/24910031636/job/72956005680) | 0% (0/4) | `iree-mi308-1` |
| `ubuntu-24.04` | github-hosted | 438 | 0 | — | 4 | [2s](https://github.com/iree-org/iree/actions/runs/24917576493/job/72973337776) | [3m54s](https://github.com/iree-org/iree/actions/runs/24917605066/job/72972649710) | 3% (2/67) | 434 |
| `macos-14` | github-hosted | 78 | 0 | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/24916985170/job/72971020804) | [3m49s](https://github.com/iree-org/iree/actions/runs/24917576485/job/72972580177) | 0% (0/12) | 74 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 7 | 0 | — | 0 | [2m08s](https://github.com/iree-org/iree/actions/runs/24919295494/job/72977607625) | [2m41s](https://github.com/iree-org/iree/actions/runs/24923453737/job/72989229732) | — | 7 |
| `azure-linux-scale` | ossci | 135 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/24913697165/job/72961126973) | [2m17s](https://github.com/iree-org/iree/actions/runs/24911179929/job/72952998999) | 0% (0/25) | 132 |
| `ubuntu-24.04-arm` | github-hosted | 72 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/24923453737/job/72989229741) | [2m11s](https://github.com/iree-org/iree/actions/runs/24913503900/job/72960449722) | 0% (0/12) | 68 |
| `windows-2022` | github-hosted | 71 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/24921510131/job/72983829202) | [2m05s](https://github.com/iree-org/iree/actions/runs/24911179929/job/72952999033) | 0% (0/12) | 68 |
| `ubuntu-latest` | github-hosted | 44 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/24913400759/job/72960099288) | [1m14s](https://github.com/iree-org/iree/actions/runs/24917754112/job/72973111670) | 0% (0/9) | 44 |
| `macos-15-intel` | github-hosted | 7 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/24923453737/job/72989229772) | [50s](https://github.com/iree-org/iree/actions/runs/24913697165/job/72961127099) | — | 7 |
| `azure-windows-scale` | ossci | 23 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24916985170/job/72971020839) | [29s](https://github.com/iree-org/iree/actions/runs/24917071877/job/72971149053) | 0% (0/4) | 21 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 22 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24917391141/job/72972529963) | [2s](https://github.com/iree-org/iree/actions/runs/24917576493/job/72973337774) | 50% (2/4) | 22 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 353 | 1% (5/348) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 397 | 14% (55/393) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 308 | 3% (8/303) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 293 | 0% (0/289) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 112 | 0% (0/109) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 9h58m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h57m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h13m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 5h53m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 7h24m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 4h37m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h44m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 3h36m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 7h34m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 5h14m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h07m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 4h31m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h49m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
