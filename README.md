# iree-ci-monitor

_Updated: 2026-04-24 18:04 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 112 | 38 | [8h16m](https://github.com/iree-org/iree/actions/runs/24900544174/job/72918805196) | 0 | [21m14s](https://github.com/iree-org/iree/actions/runs/24903652880/job/72929418127) | [7h07m](https://github.com/iree-org/iree/actions/runs/24898023507/job/72913699892) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 56 | 5 | [2h25m](https://github.com/iree-org/iree/actions/runs/24914205009/job/72965265634) | 0 | [55m23s](https://github.com/iree-org/iree/actions/runs/24907741558/job/72943575420) | [5h45m](https://github.com/iree-org/iree/actions/runs/24905652922/job/72936028537) | 83% (5/6) | `shark01-ci`, `shark10-ci-2` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 56 | 17 | [6h50m](https://github.com/iree-org/iree/actions/runs/24904230921/job/72931391925) | 0 | [18m27s](https://github.com/iree-org/iree/actions/runs/24895263413/job/72903054063) | [5h19m](https://github.com/iree-org/iree/actions/runs/24905387938/job/72939332576) | 0% (0/3) | `shark10-ci-2` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 56 | 9 | [6h50m](https://github.com/iree-org/iree/actions/runs/24904230921/job/72931392083) | 0 | [55m41s](https://github.com/iree-org/iree/actions/runs/24907799862/job/72943134033) | [5h07m](https://github.com/iree-org/iree/actions/runs/24900544174/job/72918805225) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 56 | 13 | [5h27m](https://github.com/iree-org/iree/actions/runs/24907799862/job/72943134045) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24917576493/job/72973337729) | [4h09m](https://github.com/iree-org/iree/actions/runs/24910033503/job/72950566286) | 0% (0/5) | `shark10-ci-2` |
| `Linux,X64,iree-r9700` | self-hosted | 56 | 6 | [3h05m](https://github.com/iree-org/iree/actions/runs/24913503923/job/72961230182) | 0 | [29m12s](https://github.com/iree-org/iree/actions/runs/24895837737/job/72908733040) | [3h37m](https://github.com/iree-org/iree/actions/runs/24910033503/job/72950566117) | 0% (0/6) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 73 | 9 | [6h19m](https://github.com/iree-org/iree/actions/runs/24905652922/job/72936028577) | 1 | [34m25s](https://github.com/iree-org/iree/actions/runs/24895263413/job/72903054055) | [3h36m](https://github.com/iree-org/iree/actions/runs/24907744839/job/72944647859) | 0% (0/4) | `shark01-ci`, `shark10-ci-2` |
| `Linux,X64,iree-w7900` | self-hosted | 56 | 2 | [1h07m](https://github.com/iree-org/iree/actions/runs/24917071869/job/72971608398) | 0 | [1h05m](https://github.com/iree-org/iree/actions/runs/24916595314/job/72970329892) | [3h04m](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457771) | 0% (0/8) | `shark01-ci`, `shark10-ci-2` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 151 | 14 | [6h31m](https://github.com/iree-org/iree/actions/runs/24902742119/job/72934244440) | 3 | [46m23s](https://github.com/iree-org/iree/actions/runs/24898023507/job/72913699915) | [2h52m](https://github.com/iree-org/iree/actions/runs/24911179954/job/72955892266) | 0% (0/21) | `shark01-ci`, `shark10-ci-2`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 112 | 4 | [6h31m](https://github.com/iree-org/iree/actions/runs/24902742119/job/72934244439) | 0 | [36m57s](https://github.com/iree-org/iree/actions/runs/24902742119/job/72934244520) | [2h32m](https://github.com/iree-org/iree/actions/runs/24910031636/job/72956005693) | 0% (0/16) | `shark01-ci`, `shark10-ci-2`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 56 | 0 | — | 0 | [17m58s](https://github.com/iree-org/iree/actions/runs/24910033503/job/72950566337) | [1h56m](https://github.com/iree-org/iree/actions/runs/24913503923/job/72961230264) | 0% (0/9) | `shark01-ci`, `shark10-ci-2`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 56 | 2 | [1h07m](https://github.com/iree-org/iree/actions/runs/24917071869/job/72971608532) | 0 | [21m58s](https://github.com/iree-org/iree/actions/runs/24904230921/job/72931392073) | [1h52m](https://github.com/iree-org/iree/actions/runs/24910183738/job/72953295672) | 0% (0/9) | `shark01-ci`, `shark10-ci-2`, `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 224 | 0 | — | 0 | [6m19s](https://github.com/iree-org/iree/actions/runs/24905652922/job/72936028508) | [47m32s](https://github.com/iree-org/iree/actions/runs/24910032356/job/72953137476) | 6% (2/36) | 181 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 56 | 0 | — | 0 | [4m05s](https://github.com/iree-org/iree/actions/runs/24904441479/job/72936954172) | [31m04s](https://github.com/iree-org/iree/actions/runs/24900772096/job/72918793909) | 0% (0/9) | `iree-mi308-1` |
| `macos-14` | github-hosted | 231 | 0 | — | 0 | [1m07s](https://github.com/iree-org/iree/actions/runs/24901532289/job/72923977307) | [20m47s](https://github.com/iree-org/iree/actions/runs/24907799867/job/72941603527) | 0% (0/27) | 195 |
| `ubuntu-24.04` | github-hosted | 1231 | 1 | [7h29m](https://github.com/iree-org/iree/actions/runs/24902742119/job/72925775737) | 0 | [59s](https://github.com/iree-org/iree/actions/runs/24907920316/job/72941934404) | [18m13s](https://github.com/iree-org/iree/actions/runs/24901532289/job/72923977218) | 4% (6/141) | 1106 |
| `azure-linux-scale` | ossci | 401 | 0 | — | 0 | [36s](https://github.com/iree-org/iree/actions/runs/24902434764/job/72925341952) | [15m41s](https://github.com/iree-org/iree/actions/runs/24899310495/job/72912495498) | 16% (9/55) | 371 |
| `azure-windows-scale` | ossci | 74 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24900491452/job/72917083076) | [9m15s](https://github.com/iree-org/iree/actions/runs/24909029117/job/72946355087) | 0% (0/9) | 69 |
| `windows-2022` | github-hosted | 222 | 0 | — | 0 | [49s](https://github.com/iree-org/iree/actions/runs/24905968175/job/72936751168) | [7m48s](https://github.com/iree-org/iree/actions/runs/24900772084/job/72917685016) | 0% (0/27) | 204 |
| `ubuntu-24.04-arm` | github-hosted | 222 | 0 | — | 0 | [53s](https://github.com/iree-org/iree/actions/runs/24903116919/job/72926770421) | [7m46s](https://github.com/iree-org/iree/actions/runs/24907744859/job/72942795013) | 0% (0/27) | 200 |
| `ubuntu-latest` | github-hosted | 73 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/24897608606/job/72906567637) | [6m59s](https://github.com/iree-org/iree/actions/runs/24901530225/job/72920179274) | 0% (0/19) | 73 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 9 | 0 | — | 0 | [1m54s](https://github.com/iree-org/iree/actions/runs/24915202887/job/72965796684) | [2m16s](https://github.com/iree-org/iree/actions/runs/24917576485/job/72972580125) | — | 8 |
| `macos-15-intel` | github-hosted | 9 | 0 | — | 0 | [37s](https://github.com/iree-org/iree/actions/runs/24903652885/job/72928034842) | [1m00s](https://github.com/iree-org/iree/actions/runs/24902493133/job/72924342056) | — | 9 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 56 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24916482945/job/72970042641) | [22s](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457728) | 33% (3/9) | 56 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 344 | 14% (49/339) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 271 | 0% (0/266) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 283 | 1% (4/277) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 305 | 1% (4/300) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 108 | 0% (0/105) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 6h31m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 6h50m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 8h16m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 3h05m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 2h25m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 5h27m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 6h50m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 6h19m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 6h31m (> 2h00m)
- **[stale-queued]** `ubuntu-24.04` oldest queued job waiting 7h29m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h52m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 5h07m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 7h07m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h37m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 3h04m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 5h45m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 4h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 5h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h56m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 3h36m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h52m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
