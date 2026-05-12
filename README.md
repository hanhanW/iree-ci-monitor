# iree-ci-monitor

_Updated: 2026-05-12 12:00 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 26 | 11 | [3h55m](https://github.com/iree-org/iree/actions/runs/25742691185/job/75599029409) | 0 | [37m05s](https://github.com/iree-org/iree/actions/runs/25726159309/job/75540890071) | [2h55m](https://github.com/iree-org/iree/actions/runs/25742301702/job/75598103634) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 26 | 8 | [2h46m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151971) | 1 | [21m25s](https://github.com/iree-org/iree/actions/runs/25742663953/job/75601214435) | [2h35m](https://github.com/iree-org/iree/actions/runs/25741726937/job/75596051934) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 52 | 17 | [2h46m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613152005) | 0 | [24m34s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602871113) | [1h59m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151870) | 0% (0/5) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 26 | 3 | [34m54s](https://github.com/iree-org/iree/actions/runs/25753418567/job/75637474930) | 0 | [32m34s](https://github.com/iree-org/iree/actions/runs/25746463459/job/75616179781) | [1h56m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458139) | 67% (4/6) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 25 | 6 | [2h46m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151844) | 0 | [20m54s](https://github.com/iree-org/iree/actions/runs/25742301702/job/75598103669) | [1h48m](https://github.com/iree-org/iree/actions/runs/25742723361/job/75599901190) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 26 | 6 | [2h34m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458328) | 0 | [48m56s](https://github.com/iree-org/iree/actions/runs/25726607433/job/75544392912) | [1h44m](https://github.com/iree-org/iree/actions/runs/25742691185/job/75599029620) | 0% (0/5) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 26 | 3 | [34m53s](https://github.com/iree-org/iree/actions/runs/25753418567/job/75637475501) | 0 | [9m12s](https://github.com/iree-org/iree/actions/runs/25741726937/job/75596051930) | [1h30m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614252973) | 0% (0/6) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 26 | 4 | [38m16s](https://github.com/iree-org/iree/actions/runs/25753177037/job/75636848383) | 0 | [15m38s](https://github.com/iree-org/iree/actions/runs/25741726937/job/75596052363) | [1h18m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458058) | 0% (0/6) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 26 | 1 | [24m54s](https://github.com/iree-org/iree/actions/runs/25754050386/job/75639336268) | 0 | [12m11s](https://github.com/iree-org/iree/actions/runs/25726168960/job/75540753918) | [1h13m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614253006) | 0% (0/7) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 52 | 2 | [38m16s](https://github.com/iree-org/iree/actions/runs/25753177037/job/75636848572) | 2 | [7m29s](https://github.com/iree-org/iree/actions/runs/25741726937/job/75596052381) | [1h11m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458269) | 8% (1/13) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 52 | 3 | [31m32s](https://github.com/iree-org/iree/actions/runs/25753534872/job/75638096167) | 1 | [11m29s](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151876) | [1h00m](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328122) | 0% (0/14) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 27 | 4 | [38m16s](https://github.com/iree-org/iree/actions/runs/25753177037/job/75636848529) | 0 | [11m38s](https://github.com/iree-org/iree/actions/runs/25744170015/job/75610721675) | [53m42s](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328144) | 0% (0/7) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 26 | 0 | — | 1 | [3m07s](https://github.com/iree-org/iree/actions/runs/25742723361/job/75599900693) | [21m37s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602871081) | 0% (0/7) | `iree-mi308-1` |
| `ubuntu-24.04` | github-hosted | 592 | 0 | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/25749978296/job/75625010411) | [8m34s](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614252944) | 37% (59/158) | 584 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [7m08s](https://github.com/iree-org/iree/actions/runs/25727680023/job/75544582497) | [7m08s](https://github.com/iree-org/iree/actions/runs/25727680023/job/75544582497) | 0% (0/1) | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 104 | 0 | — | 0 | [56s](https://github.com/iree-org/iree/actions/runs/25733921709/job/75567054228) | [6m46s](https://github.com/iree-org/iree/actions/runs/25726607433/job/75544392895) | 25% (7/28) | 104 |
| `macos-14` | github-hosted | 112 | 0 | — | 0 | [12s](https://github.com/iree-org/iree/actions/runs/25726168924/job/75539766946) | [6m41s](https://github.com/iree-org/iree/actions/runs/25746922409/job/75616560049) | 73% (27/37) | 112 |
| `windows-2022` | github-hosted | 111 | 0 | — | 0 | [21s](https://github.com/iree-org/iree/actions/runs/25743657367/job/75600891241) | [6m21s](https://github.com/iree-org/iree/actions/runs/25746922409/job/75616559884) | 75% (27/36) | 111 |
| `ubuntu-24.04-arm` | github-hosted | 111 | 0 | — | 0 | [23s](https://github.com/iree-org/iree/actions/runs/25751058313/job/75627332433) | [5m30s](https://github.com/iree-org/iree/actions/runs/25747011862/job/75616891463) | 75% (27/36) | 111 |
| `azure-windows-scale` | ossci | 37 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25746700519/job/75611941234) | [4m37s](https://github.com/iree-org/iree/actions/runs/25749978264/job/75623984819) | 75% (9/12) | 37 |
| `ubuntu-latest` | github-hosted | 57 | 0 | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/25746606852/job/75611444868) | [4m22s](https://github.com/iree-org/iree/actions/runs/25748502308/job/75618204056) | 0% (0/24) | 57 |
| `azure-linux-scale` | ossci | 201 | 0 | — | 1 | [16s](https://github.com/iree-org/iree/actions/runs/25746840561/job/75616508580) | [2m50s](https://github.com/iree-org/iree/actions/runs/25746734624/job/75612310076) | 68% (50/74) | 201 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/25727633237/job/75544419803) | [6s](https://github.com/iree-org/iree/actions/runs/25727633237/job/75544419803) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 26 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151803) | [4s](https://github.com/iree-org/iree/actions/runs/25742723361/job/75599901632) | 57% (4/7) | 26 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,shark55-ci`, `self-hosted,persistent-cache,Linux,X64` | 788 | 2% (12/785) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,shark01-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 905 | 3% (26/902) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 1070 | 9% (92/1066) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 298 | 3% (8/296) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1138 | 4% (49/1135) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 2h34m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 2h46m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 2h46m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 3h55m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 2h46m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h13m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h44m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h59m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h35m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h56m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h30m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h55m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h48m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h18m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h11m (> 1h00m)
- **[high-failure-main]** `azure-linux-scale` main-branch failure rate 68% (50/74)
- **[high-failure-main]** `azure-windows-scale` main-branch failure rate 75% (9/12)
- **[high-failure-main]** `linux-mi325-1gpu-ossci-iree-org` main-branch failure rate 25% (7/28)
- **[high-failure-main]** `macos-14` main-branch failure rate 73% (27/37)
- **[high-failure-main]** `ubuntu-24.04-arm` main-branch failure rate 75% (27/36)
- **[high-failure-main]** `ubuntu-24.04` main-branch failure rate 37% (59/158)
- **[high-failure-main]** `windows-2022` main-branch failure rate 75% (27/36)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
