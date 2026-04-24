# iree-ci-monitor

_Updated: 2026-04-24 14:09 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 45 | 15 | [4h25m](https://github.com/iree-org/iree/actions/runs/24900491423/job/72918388734) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24909029111/job/72949018937) | [3h58m](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457881) | 0% (0/2) | 1 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 63 | 17 | [3h12m](https://github.com/iree-org/iree/actions/runs/24903652239/job/72929142868) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24909029111/job/72949018899) | [3h34m](https://github.com/iree-org/iree/actions/runs/24897841783/job/72911216701) | 0% (0/3) | 2 |
| `Linux,X64,gfx1201` | self-hosted | 90 | 31 | [5h10m](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457854) | 2 | [0s](https://github.com/iree-org/iree/actions/runs/24909030962/job/72948373786) | [3h30m](https://github.com/iree-org/iree/actions/runs/24900491423/job/72918388548) | 0% (0/3) | 1 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 45 | 13 | [4h25m](https://github.com/iree-org/iree/actions/runs/24900491423/job/72918388468) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24909029111/job/72949018903) | [3h06m](https://github.com/iree-org/iree/actions/runs/24900828535/job/72920651656) | 0% (0/4) | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 45 | 7 | [2h24m](https://github.com/iree-org/iree/actions/runs/24905652922/job/72936028512) | 1 | [8m38s](https://github.com/iree-org/iree/actions/runs/24895441888/job/72904294887) | [3h04m](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457771) | 0% (0/4) | 2 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 117 | 27 | [4h10m](https://github.com/iree-org/iree/actions/runs/24900828535/job/72920651584) | 1 | [10m46s](https://github.com/iree-org/iree/actions/runs/24897609790/job/72914156186) | [2h29m](https://github.com/iree-org/iree/actions/runs/24903652239/job/72929142852) | 0% (0/10) | 4 |
| `Linux,X64,gfx1100` | self-hosted | 90 | 12 | [2h37m](https://github.com/iree-org/iree/actions/runs/24902742119/job/72934244439) | 1 | [14m45s](https://github.com/iree-org/iree/actions/runs/24895465582/job/72906014777) | [2h27m](https://github.com/iree-org/iree/actions/runs/24900806704/job/72920875094) | 0% (0/10) | 3 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 45 | 12 | [4h39m](https://github.com/iree-org/iree/actions/runs/24899543804/job/72916224273) | 0 | [6m49s](https://github.com/iree-org/iree/actions/runs/24895214565/job/72899323087) | [2h06m](https://github.com/iree-org/iree/actions/runs/24903652239/job/72929142841) | 100% (1/1) | 2 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 45 | 13 | [4h39m](https://github.com/iree-org/iree/actions/runs/24899543804/job/72916224395) | 0 | [18m36s](https://github.com/iree-org/iree/actions/runs/24895441888/job/72904295155) | [1h58m](https://github.com/iree-org/iree/actions/runs/24895263413/job/72903054165) | 0% (0/1) | 1 |
| `Linux,X64,iree-r9700` | self-hosted | 45 | 8 | [2h56m](https://github.com/iree-org/iree/actions/runs/24904230921/job/72931391793) | 0 | [5m34s](https://github.com/iree-org/iree/actions/runs/24893856450/job/72894349985) | [1h52m](https://github.com/iree-org/iree/actions/runs/24897905655/job/72915049677) | 0% (0/3) | 1 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 45 | 5 | [1h06m](https://github.com/iree-org/iree/actions/runs/24908508697/job/72946866390) | 0 | [13m53s](https://github.com/iree-org/iree/actions/runs/24897609790/job/72914155933) | [1h18m](https://github.com/iree-org/iree/actions/runs/24905652922/job/72936028517) | 0% (0/5) | 3 |
| `Linux,X64,rdna3` | self-hosted | 45 | 4 | [1h06m](https://github.com/iree-org/iree/actions/runs/24908508697/job/72946866456) | 0 | [15m48s](https://github.com/iree-org/iree/actions/runs/24900491423/job/72918388547) | [49m41s](https://github.com/iree-org/iree/actions/runs/24907744839/job/72944647766) | 0% (0/5) | 3 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 180 | 12 | [41m21s](https://github.com/iree-org/iree/actions/runs/24909699051/job/72950211597) | 2 | [2m31s](https://github.com/iree-org/iree/actions/runs/24895263413/job/72903053930) | [39m04s](https://github.com/iree-org/iree/actions/runs/24907744839/job/72944647819) | 5% (1/20) | 132 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 45 | 0 | — | 1 | [4m35s](https://github.com/iree-org/iree/actions/runs/24907744839/job/72944647737) | [32m54s](https://github.com/iree-org/iree/actions/runs/24900544174/job/72918805095) | 0% (0/5) | 1 |
| `azure-linux-scale` | ossci | 381 | 0 | — | 8 | [1m13s](https://github.com/iree-org/iree/actions/runs/24904497703/job/72932848742) | [29m29s](https://github.com/iree-org/iree/actions/runs/24897905651/job/72907721621) | 30% (9/30) | 343 |
| `macos-14` | github-hosted | 223 | 0 | — | 2 | [1m45s](https://github.com/iree-org/iree/actions/runs/24894237407/job/72894549073) | [21m00s](https://github.com/iree-org/iree/actions/runs/24901252984/job/72920391332) | 0% (0/15) | 188 |
| `ubuntu-24.04` | github-hosted | 1115 | 1 | [3h35m](https://github.com/iree-org/iree/actions/runs/24902742119/job/72925775737) | 7 | [2m00s](https://github.com/iree-org/iree/actions/runs/24895263329/job/72898257676) | [18m37s](https://github.com/iree-org/iree/actions/runs/24909699017/job/72949190212) | 6% (5/78) | 985 |
| `azure-windows-scale` | ossci | 72 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/24900491452/job/72917083076) | [9m15s](https://github.com/iree-org/iree/actions/runs/24909029117/job/72946355087) | 0% (0/5) | 68 |
| `windows-2022` | github-hosted | 216 | 0 | — | 0 | [1m20s](https://github.com/iree-org/iree/actions/runs/24907153474/job/72940114835) | [7m48s](https://github.com/iree-org/iree/actions/runs/24900772084/job/72917685016) | 0% (0/15) | 198 |
| `ubuntu-24.04-arm` | github-hosted | 216 | 0 | — | 0 | [1m27s](https://github.com/iree-org/iree/actions/runs/24895095257/job/72897619448) | [7m46s](https://github.com/iree-org/iree/actions/runs/24907744859/job/72942795013) | 0% (0/15) | 195 |
| `ubuntu-latest` | github-hosted | 55 | 0 | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/24895911776/job/72900544541) | [7m05s](https://github.com/iree-org/iree/actions/runs/24901530225/job/72920179258) | 0% (0/10) | 55 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 7 | 0 | — | 0 | [1m43s](https://github.com/iree-org/iree/actions/runs/24895914201/job/72900885556) | [1m57s](https://github.com/iree-org/iree/actions/runs/24902493133/job/72924342051) | — | 6 |
| `macos-15-intel` | github-hosted | 7 | 0 | — | 2 | [37s](https://github.com/iree-org/iree/actions/runs/24903652885/job/72928034842) | [1m06s](https://github.com/iree-org/iree/actions/runs/24895914201/job/72900885640) | — | 7 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 45 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24893945295/job/72894658022) | [26s](https://github.com/iree-org/iree/actions/runs/24903652239/job/72929142809) | 20% (1/5) | 45 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, +2 more | 250 | 2% (4/244) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +2 more | 218 | 0% (0/213) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +5 more | 231 | 2% (4/225) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 92 | 0% (0/88) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +7 more | 281 | 14% (39/276) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 2h37m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 4h39m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 5h10m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 2h56m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 2h24m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 4h39m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 4h25m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 4h25m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 3h12m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 4h10m (> 2h00m)
- **[stale-queued]** `ubuntu-24.04` oldest queued job waiting 3h35m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h18m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h58m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h30m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h52m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 3h04m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 2h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 3h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 3h58m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 3h34m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h29m (> 1h00m)
- **[high-failure-main]** `azure-linux-scale` main-branch failure rate 30% (9/30)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
