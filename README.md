# iree-ci-monitor

_Updated: 2026-04-24 10:56 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 27 | 9 | [2h13m](https://github.com/iree-org/iree/actions/runs/24895837737/job/72908733237) | 1 | [22m26s](https://github.com/iree-org/iree/actions/runs/24895465582/job/72906014787) | [1h52m](https://github.com/iree-org/iree/actions/runs/24895652984/job/72908921626) | — | 1 |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 27 | 11 | [2h13m](https://github.com/iree-org/iree/actions/runs/24895837737/job/72908733297) | 0 | [20m04s](https://github.com/iree-org/iree/actions/runs/24879287212/job/72844568481) | [1h51m](https://github.com/iree-org/iree/actions/runs/24895465582/job/72906014661) | — | 1 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 34 | 15 | [3h10m](https://github.com/iree-org/iree/actions/runs/24895214565/job/72899323042) | 0 | [6m46s](https://github.com/iree-org/iree/actions/runs/24894237547/job/72897652250) | [1h48m](https://github.com/iree-org/iree/actions/runs/24895652984/job/72908921871) | — | 2 |
| `Linux,X64,gfx1201` | self-hosted | 54 | 23 | [2h40m](https://github.com/iree-org/iree/actions/runs/24895441888/job/72904295149) | 0 | [19m22s](https://github.com/iree-org/iree/actions/runs/24879277085/job/72844226667) | [1h17m](https://github.com/iree-org/iree/actions/runs/24895263413/job/72903054009) | 0% (0/1) | 1 |
| `Linux,X64,gfx1100` | self-hosted | 54 | 12 | [1h42m](https://github.com/iree-org/iree/actions/runs/24898023507/job/72913699927) | 2 | [13m52s](https://github.com/iree-org/iree/actions/runs/24893945295/job/72894658305) | [1h01m](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457846) | 0% (0/2) | 3 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 74 | 13 | [1h25m](https://github.com/iree-org/iree/actions/runs/24899543804/job/72916224325) | 1 | [10m46s](https://github.com/iree-org/iree/actions/runs/24897609790/job/72914156186) | [55m07s](https://github.com/iree-org/iree/actions/runs/24899543804/job/72916224269) | 0% (0/5) | 4 |
| `Linux,X64,iree-r9700` | self-hosted | 27 | 8 | [2h12m](https://github.com/iree-org/iree/actions/runs/24895652984/job/72908921494) | 0 | [1m57s](https://github.com/iree-org/iree/actions/runs/24895441888/job/72904294953) | [54m29s](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457692) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 27 | 9 | [1h56m](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457771) | 0 | [8m10s](https://github.com/iree-org/iree/actions/runs/24895465582/job/72906014545) | [51m07s](https://github.com/iree-org/iree/actions/runs/24897905655/job/72915049628) | 0% (0/1) | 2 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 27 | 15 | [2h40m](https://github.com/iree-org/iree/actions/runs/24895441888/job/72904295169) | 0 | [4m16s](https://github.com/iree-org/iree/actions/runs/24880836113/job/72849408783) | [47m23s](https://github.com/iree-org/iree/actions/runs/24893945295/job/72894658106) | — | 1 |
| `Linux,X64,rdna3` | self-hosted | 27 | 3 | [56m05s](https://github.com/iree-org/iree/actions/runs/24900828535/job/72920651675) | 0 | [11m03s](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457837) | [38m07s](https://github.com/iree-org/iree/actions/runs/24897609790/job/72914155994) | 0% (0/2) | 3 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 27 | 5 | [1h11m](https://github.com/iree-org/iree/actions/runs/24900491423/job/72918388529) | 0 | [9m20s](https://github.com/iree-org/iree/actions/runs/24895652984/job/72908921682) | [37m01s](https://github.com/iree-org/iree/actions/runs/24897841783/job/72911216706) | 0% (0/2) | 3 |
| `azure-linux-scale` | ossci | 222 | 0 | — | 10 | [41s](https://github.com/iree-org/iree/actions/runs/24900772096/job/72917648604) | [33m02s](https://github.com/iree-org/iree/actions/runs/24895837737/job/72902120620) | 30% (6/20) | 202 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 27 | 2 | [54m40s](https://github.com/iree-org/iree/actions/runs/24900806704/job/72920875153) | 1 | [4m38s](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457855) | [32m54s](https://github.com/iree-org/iree/actions/runs/24900544174/job/72918805095) | 0% (0/2) | 1 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 27 | 9 | [1h56m](https://github.com/iree-org/iree/actions/runs/24897794914/job/72911457891) | 1 | [7m44s](https://github.com/iree-org/iree/actions/runs/24895837737/job/72908733093) | [32m45s](https://github.com/iree-org/iree/actions/runs/24879277085/job/72844226712) | — | 2 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 108 | 11 | [1h08m](https://github.com/iree-org/iree/actions/runs/24900544174/job/72918805241) | 1 | [26s](https://github.com/iree-org/iree/actions/runs/24893945295/job/72894658286) | [26m29s](https://github.com/iree-org/iree/actions/runs/24900828535/job/72920651548) | 10% (1/10) | 95 |
| `ubuntu-24.04` | github-hosted | 629 | 16 | [33m34s](https://github.com/iree-org/iree/actions/runs/24901532289/job/72923977218) | 8 | [25s](https://github.com/iree-org/iree/actions/runs/24895837721/job/72902088891) | [17m48s](https://github.com/iree-org/iree/actions/runs/24900806704/job/72920874989) | 6% (3/49) | 592 |
| `macos-14` | github-hosted | 129 | 2 | [22m06s](https://github.com/iree-org/iree/actions/runs/24902742096/job/72925659258) | 3 | [49s](https://github.com/iree-org/iree/actions/runs/24897841769/job/72907697970) | [17m05s](https://github.com/iree-org/iree/actions/runs/24900544103/job/72917690518) | 0% (0/10) | 118 |
| `windows-2022` | github-hosted | 123 | 2 | [22m06s](https://github.com/iree-org/iree/actions/runs/24902742096/job/72925659248) | 4 | [49s](https://github.com/iree-org/iree/actions/runs/24900828451/job/72919403548) | [7m19s](https://github.com/iree-org/iree/actions/runs/24901252984/job/72920391315) | 0% (0/9) | 114 |
| `ubuntu-latest` | github-hosted | 39 | 1 | [22m20s](https://github.com/iree-org/iree/actions/runs/24903115373/job/72925624212) | 0 | [4s](https://github.com/iree-org/iree/actions/runs/24895092264/job/72897575870) | [6m59s](https://github.com/iree-org/iree/actions/runs/24901530225/job/72920179274) | 0% (0/6) | 38 |
| `ubuntu-24.04-arm` | github-hosted | 123 | 1 | [22m06s](https://github.com/iree-org/iree/actions/runs/24902742096/job/72925659255) | 2 | [47s](https://github.com/iree-org/iree/actions/runs/24897559417/job/72906409973) | [6m01s](https://github.com/iree-org/iree/actions/runs/24900544103/job/72917690451) | 0% (0/9) | 114 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 6 | 0 | — | 1 | [1m43s](https://github.com/iree-org/iree/actions/runs/24895914201/job/72900885556) | [1m57s](https://github.com/iree-org/iree/actions/runs/24902493133/job/72924342051) | 0% (0/1) | 5 |
| `azure-windows-scale` | ossci | 41 | 1 | [22m06s](https://github.com/iree-org/iree/actions/runs/24902742096/job/72925659402) | 2 | [1s](https://github.com/iree-org/iree/actions/runs/24900057812/job/72915273758) | [1m08s](https://github.com/iree-org/iree/actions/runs/24900544103/job/72917690614) | 0% (0/3) | 39 |
| `macos-15-intel` | github-hosted | 6 | 0 | — | 2 | [35s](https://github.com/iree-org/iree/actions/runs/24900772084/job/72917685153) | [1m06s](https://github.com/iree-org/iree/actions/runs/24895914201/job/72900885640) | 0% (0/1) | 6 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 27 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/24879287212/job/72844568304) | [4s](https://github.com/iree-org/iree/actions/runs/24895214565/job/72899322946) | 33% (1/3) | 27 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, +2 more | 215 | 1% (2/209) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +2 more | 183 | 0% (0/178) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +5 more | 199 | 2% (4/193) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 73 | 0% (0/69) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +7 more | 229 | 15% (33/224) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 2h13m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 2h40m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 2h12m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 2h40m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 2h13m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 3h10m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h52m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h51m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h48m (> 1h00m)
- **[high-failure-main]** `azure-linux-scale` main-branch failure rate 30% (6/20)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
