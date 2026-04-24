# iree-ci-monitor

_Updated: 2026-04-24 11:26 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 34 | 10 | [2h28m](https://github.com/iree-org/iree/actions/runs/24897841783/job/72911216701) | 0 | [6m46s](https://github.com/iree-org/iree/actions/runs/24894237547/job/72897652250) | [1h58m](https://github.com/iree-org/iree/actions/runs/24895465582/job/72906014663) | 0% (0/1) | 2 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 27 | 9 | [2h12m](https://github.com/iree-org/iree/actions/runs/24898023507/job/72913699878) | 0 | [18m36s](https://github.com/iree-org/iree/actions/runs/24895441888/job/72904295155) | [1h52m](https://github.com/iree-org/iree/actions/runs/24895652984/job/72908921626) | — | 1 |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 27 | 9 | [2h27m](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457881) | 0 | [18m27s](https://github.com/iree-org/iree/actions/runs/24895263413/job/72903054063) | [1h51m](https://github.com/iree-org/iree/actions/runs/24898023507/job/72913699899) | — | 1 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 27 | 8 | [2h12m](https://github.com/iree-org/iree/actions/runs/24898023507/job/72913699852) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24902493139/job/72925147720) | [1h41m](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457865) | 0% (0/2) | 1 |
| `Linux,X64,gfx1201` | self-hosted | 54 | 20 | [2h28m](https://github.com/iree-org/iree/actions/runs/24897841783/job/72911216728) | 1 | [25m03s](https://github.com/iree-org/iree/actions/runs/24895263413/job/72903054090) | [1h17m](https://github.com/iree-org/iree/actions/runs/24895263413/job/72903054009) | 0% (0/2) | 1 |
| `Linux,X64,gfx1100` | self-hosted | 54 | 9 | [2h12m](https://github.com/iree-org/iree/actions/runs/24898023507/job/72913699927) | 2 | [14m24s](https://github.com/iree-org/iree/actions/runs/24880836113/job/72849408897) | [1h11m](https://github.com/iree-org/iree/actions/runs/24900544174/job/72918805229) | 0% (0/3) | 3 |
| `Linux,X64,iree-r9700` | self-hosted | 27 | 4 | [1h56m](https://github.com/iree-org/iree/actions/runs/24899543804/job/72916224193) | 0 | [5m34s](https://github.com/iree-org/iree/actions/runs/24893856450/job/72894349985) | [1h10m](https://github.com/iree-org/iree/actions/runs/24897609790/job/72914155948) | 0% (0/1) | 1 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 74 | 16 | [1h56m](https://github.com/iree-org/iree/actions/runs/24899543804/job/72916224325) | 0 | [11m02s](https://github.com/iree-org/iree/actions/runs/24895214565/job/72899323176) | [1h06m](https://github.com/iree-org/iree/actions/runs/24900544174/job/72918805070) | 0% (0/6) | 4 |
| `Linux,X64,iree-w7900` | self-hosted | 27 | 9 | [2h27m](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457771) | 0 | [5m07s](https://github.com/iree-org/iree/actions/runs/24897841783/job/72911216599) | [1h00m](https://github.com/iree-org/iree/actions/runs/24900544174/job/72918805022) | 0% (0/1) | 2 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 27 | 8 | [2h27m](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457891) | 0 | [7m26s](https://github.com/iree-org/iree/actions/runs/24880836113/job/72849408921) | [1h00m](https://github.com/iree-org/iree/actions/runs/24900806704/job/72920875099) | 100% (1/1) | 2 |
| `Linux,X64,rdna3` | self-hosted | 27 | 3 | [28m47s](https://github.com/iree-org/iree/actions/runs/24903652239/job/72929142886) | 0 | [12m24s](https://github.com/iree-org/iree/actions/runs/24895652984/job/72908921761) | [54m20s](https://github.com/iree-org/iree/actions/runs/24897841783/job/72911216696) | 0% (0/3) | 3 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 27 | 3 | [1h39m](https://github.com/iree-org/iree/actions/runs/24900544174/job/72918805149) | 0 | [10m26s](https://github.com/iree-org/iree/actions/runs/24895263413/job/72903053966) | [53m48s](https://github.com/iree-org/iree/actions/runs/24900806704/job/72920875163) | 0% (0/3) | 3 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 27 | 0 | — | 1 | [8m38s](https://github.com/iree-org/iree/actions/runs/24904230921/job/72931392090) | [46m36s](https://github.com/iree-org/iree/actions/runs/24900806704/job/72920875153) | 0% (0/3) | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 108 | 5 | [26m51s](https://github.com/iree-org/iree/actions/runs/24903652880/job/72929418253) | 1 | [1m46s](https://github.com/iree-org/iree/actions/runs/24898023507/job/72913699906) | [38m39s](https://github.com/iree-org/iree/actions/runs/24900806704/job/72920875131) | 8% (1/12) | 99 |
| `azure-linux-scale` | ossci | 252 | 0 | — | 6 | [1m04s](https://github.com/iree-org/iree/actions/runs/24904260181/job/72929670962) | [32m59s](https://github.com/iree-org/iree/actions/runs/24895837721/job/72902181792) | 35% (9/26) | 232 |
| `ubuntu-24.04` | github-hosted | 688 | 23 | [51m54s](https://github.com/iree-org/iree/actions/runs/24902742119/job/72925775737) | 10 | [58s](https://github.com/iree-org/iree/actions/runs/24897905655/job/72915049638) | [17m37s](https://github.com/iree-org/iree/actions/runs/24900544174/job/72918805075) | 5% (3/55) | 642 |
| `macos-14` | github-hosted | 146 | 9 | [14m24s](https://github.com/iree-org/iree/actions/runs/24904497709/job/72931243309) | 3 | [59s](https://github.com/iree-org/iree/actions/runs/24895441885/job/72899037118) | [17m05s](https://github.com/iree-org/iree/actions/runs/24900544103/job/72917690518) | 0% (0/12) | 128 |
| `ubuntu-latest` | github-hosted | 45 | 2 | [8m24s](https://github.com/iree-org/iree/actions/runs/24905034603/job/72932118268) | 0 | [4s](https://github.com/iree-org/iree/actions/runs/24903650971/job/72927419176) | [6m59s](https://github.com/iree-org/iree/actions/runs/24901530225/job/72920179274) | 0% (0/8) | 43 |
| `ubuntu-24.04-arm` | github-hosted | 138 | 4 | [12m46s](https://github.com/iree-org/iree/actions/runs/24904356332/job/72931480444) | 1 | [58s](https://github.com/iree-org/iree/actions/runs/24898023514/job/72909126314) | [6m03s](https://github.com/iree-org/iree/actions/runs/24895914201/job/72900885459) | 0% (0/12) | 126 |
| `windows-2022` | github-hosted | 138 | 2 | [12m46s](https://github.com/iree-org/iree/actions/runs/24904356332/job/72931480405) | 4 | [1m14s](https://github.com/iree-org/iree/actions/runs/24895837721/job/72902181756) | [5m46s](https://github.com/iree-org/iree/actions/runs/24904230920/job/72930119785) | 0% (0/12) | 129 |
| `azure-windows-scale` | ossci | 46 | 1 | [12m46s](https://github.com/iree-org/iree/actions/runs/24904356332/job/72931480519) | 3 | [1s](https://github.com/iree-org/iree/actions/runs/24901532289/job/72923977438) | [3m20s](https://github.com/iree-org/iree/actions/runs/24904441481/job/72932192598) | 0% (0/3) | 44 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 8 | 0 | — | 2 | [1m51s](https://github.com/iree-org/iree/actions/runs/24900772084/job/72917685115) | [1m57s](https://github.com/iree-org/iree/actions/runs/24902493133/job/72924342051) | 0% (0/1) | 7 |
| `macos-15-intel` | github-hosted | 8 | 0 | — | 2 | [37s](https://github.com/iree-org/iree/actions/runs/24903652885/job/72928034842) | [1m06s](https://github.com/iree-org/iree/actions/runs/24895914201/job/72900885640) | 0% (0/1) | 8 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 27 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24893945295/job/72894658022) | [26s](https://github.com/iree-org/iree/actions/runs/24903652239/job/72929142809) | 25% (1/4) | 27 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +7 more | 241 | 14% (34/237) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 78 | 0% (0/74) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, +2 more | 223 | 1% (2/218) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +5 more | 206 | 2% (4/200) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +2 more | 190 | 0% (0/185) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 2h12m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 2h12m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 2h28m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 2h27m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 2h27m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 2h12m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 2h27m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 2h28m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h11m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h52m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h10m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h41m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h51m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h58m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h06m (> 1h00m)
- **[high-failure-main]** `azure-linux-scale` main-branch failure rate 35% (9/26)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
