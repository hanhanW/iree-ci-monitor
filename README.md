# iree-ci-monitor

_Updated: 2026-04-24 11:35 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 35 | 11 | [2h37m](https://github.com/iree-org/iree/actions/runs/24897841783/job/72911216701) | 0 | [6m46s](https://github.com/iree-org/iree/actions/runs/24894237547/job/72897652250) | [1h58m](https://github.com/iree-org/iree/actions/runs/24895465582/job/72906014663) | 0% (0/1) | 2 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 28 | 9 | [2h21m](https://github.com/iree-org/iree/actions/runs/24898023507/job/72913699878) | 1 | [18m36s](https://github.com/iree-org/iree/actions/runs/24895441888/job/72904295155) | [1h52m](https://github.com/iree-org/iree/actions/runs/24895652984/job/72908921626) | — | 1 |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 28 | 10 | [2h35m](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457881) | 0 | [18m27s](https://github.com/iree-org/iree/actions/runs/24895263413/job/72903054063) | [1h51m](https://github.com/iree-org/iree/actions/runs/24898023507/job/72913699899) | — | 1 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 28 | 9 | [2h21m](https://github.com/iree-org/iree/actions/runs/24898023507/job/72913699852) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24902493139/job/72925147720) | [1h41m](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457865) | 0% (0/2) | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 28 | 9 | [2h35m](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457771) | 1 | [5m07s](https://github.com/iree-org/iree/actions/runs/24897841783/job/72911216599) | [1h26m](https://github.com/iree-org/iree/actions/runs/24895652984/job/72908921521) | 0% (0/1) | 2 |
| `Linux,X64,gfx1201` | self-hosted | 56 | 22 | [2h37m](https://github.com/iree-org/iree/actions/runs/24897841783/job/72911216728) | 0 | [25m03s](https://github.com/iree-org/iree/actions/runs/24895263413/job/72903054090) | [1h17m](https://github.com/iree-org/iree/actions/runs/24895263413/job/72903054009) | 0% (0/2) | 1 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 28 | 8 | [2h35m](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457891) | 0 | [7m44s](https://github.com/iree-org/iree/actions/runs/24895837737/job/72908733093) | [1h15m](https://github.com/iree-org/iree/actions/runs/24897905655/job/72915049742) | 100% (1/1) | 2 |
| `Linux,X64,gfx1100` | self-hosted | 56 | 10 | [2h21m](https://github.com/iree-org/iree/actions/runs/24898023507/job/72913699927) | 1 | [14m45s](https://github.com/iree-org/iree/actions/runs/24895465582/job/72906014777) | [1h11m](https://github.com/iree-org/iree/actions/runs/24900544174/job/72918805229) | 0% (0/4) | 3 |
| `Linux,X64,iree-r9700` | self-hosted | 28 | 5 | [2h05m](https://github.com/iree-org/iree/actions/runs/24899543804/job/72916224193) | 0 | [5m34s](https://github.com/iree-org/iree/actions/runs/24893856450/job/72894349985) | [1h10m](https://github.com/iree-org/iree/actions/runs/24897609790/job/72914155948) | 0% (0/1) | 1 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 77 | 18 | [2h05m](https://github.com/iree-org/iree/actions/runs/24899543804/job/72916224325) | 0 | [11m57s](https://github.com/iree-org/iree/actions/runs/24895263413/job/72903053920) | [1h09m](https://github.com/iree-org/iree/actions/runs/24900806704/job/72920875230) | 0% (0/6) | 4 |
| `Linux,X64,rdna3` | self-hosted | 28 | 3 | [37m21s](https://github.com/iree-org/iree/actions/runs/24903652239/job/72929142886) | 1 | [15m48s](https://github.com/iree-org/iree/actions/runs/24900491423/job/72918388547) | [54m20s](https://github.com/iree-org/iree/actions/runs/24897841783/job/72911216696) | 0% (0/3) | 3 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 28 | 4 | [1h47m](https://github.com/iree-org/iree/actions/runs/24900544174/job/72918805149) | 0 | [10m26s](https://github.com/iree-org/iree/actions/runs/24895263413/job/72903053966) | [53m48s](https://github.com/iree-org/iree/actions/runs/24900806704/job/72920875163) | 0% (0/3) | 3 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 28 | 0 | — | 1 | [8m38s](https://github.com/iree-org/iree/actions/runs/24904230921/job/72931392090) | [46m36s](https://github.com/iree-org/iree/actions/runs/24900806704/job/72920875153) | 0% (0/4) | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 112 | 4 | [2m39s](https://github.com/iree-org/iree/actions/runs/24902742119/job/72934244343) | 3 | [2m12s](https://github.com/iree-org/iree/actions/runs/24895441888/job/72904295090) | [38m39s](https://github.com/iree-org/iree/actions/runs/24900806704/job/72920875131) | 7% (1/14) | 104 |
| `azure-linux-scale` | ossci | 254 | 0 | — | 4 | [1m04s](https://github.com/iree-org/iree/actions/runs/24904230921/job/72930129346) | [32m17s](https://github.com/iree-org/iree/actions/runs/24895837721/job/72902181862) | 35% (9/26) | 234 |
| `ubuntu-24.04` | github-hosted | 704 | 16 | [1h00m](https://github.com/iree-org/iree/actions/runs/24902742119/job/72925775737) | 11 | [1m03s](https://github.com/iree-org/iree/actions/runs/24900491452/job/72917082802) | [17m37s](https://github.com/iree-org/iree/actions/runs/24900544174/job/72918805075) | 6% (4/64) | 663 |
| `macos-14` | github-hosted | 146 | 5 | [21m20s](https://github.com/iree-org/iree/actions/runs/24904356332/job/72931480367) | 3 | [1m11s](https://github.com/iree-org/iree/actions/runs/24895214557/job/72898282733) | [17m37s](https://github.com/iree-org/iree/actions/runs/24904497709/job/72931243552) | 0% (0/13) | 132 |
| `ubuntu-latest` | github-hosted | 49 | 1 | [2m45s](https://github.com/iree-org/iree/actions/runs/24905651472/job/72934229742) | 1 | [8s](https://github.com/iree-org/iree/actions/runs/24897608606/job/72906567637) | [10m40s](https://github.com/iree-org/iree/actions/runs/24900827207/job/72917774486) | 0% (0/8) | 48 |
| `ubuntu-24.04-arm` | github-hosted | 138 | 0 | — | 0 | [1m02s](https://github.com/iree-org/iree/actions/runs/24901532289/job/72923977189) | [10m23s](https://github.com/iree-org/iree/actions/runs/24900544103/job/72917690480) | 0% (0/12) | 130 |
| `windows-2022` | github-hosted | 138 | 0 | — | 2 | [1m14s](https://github.com/iree-org/iree/actions/runs/24895837721/job/72902181756) | [7m48s](https://github.com/iree-org/iree/actions/runs/24900772084/job/72917685016) | 0% (0/12) | 131 |
| `azure-windows-scale` | ossci | 46 | 0 | — | 2 | [1s](https://github.com/iree-org/iree/actions/runs/24901532289/job/72923977438) | [4m46s](https://github.com/iree-org/iree/actions/runs/24902742096/job/72925659402) | 0% (0/4) | 45 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 8 | 0 | — | 2 | [1m51s](https://github.com/iree-org/iree/actions/runs/24900772084/job/72917685115) | [1m57s](https://github.com/iree-org/iree/actions/runs/24902493133/job/72924342051) | 0% (0/1) | 7 |
| `macos-15-intel` | github-hosted | 8 | 0 | — | 2 | [37s](https://github.com/iree-org/iree/actions/runs/24903652885/job/72928034842) | [1m06s](https://github.com/iree-org/iree/actions/runs/24895914201/job/72900885640) | 0% (0/1) | 8 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 28 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/24894237547/job/72897652087) | [26s](https://github.com/iree-org/iree/actions/runs/24903652239/job/72929142809) | 25% (1/4) | 28 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 79 | 0% (0/75) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, +2 more | 224 | 1% (2/219) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +7 more | 243 | 14% (34/238) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +5 more | 208 | 2% (4/202) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +2 more | 191 | 0% (0/186) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 2h21m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 2h21m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 2h37m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 2h05m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 2h35m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 2h35m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 2h21m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 2h35m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 2h37m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 2h05m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h11m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h52m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h10m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h26m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h15m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h41m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h51m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h58m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h09m (> 1h00m)
- **[high-failure-main]** `azure-linux-scale` main-branch failure rate 35% (9/26)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
