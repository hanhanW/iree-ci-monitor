# iree-ci-monitor

_Updated: 2026-05-08 18:13 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 52 | 11 | [6h34m](https://github.com/iree-org/iree/actions/runs/25572626442/job/75073016090) | 2 | [24m29s](https://github.com/iree-org/iree/actions/runs/25574189224/job/75078404099) | [4h43m](https://github.com/iree-org/iree/actions/runs/25577031874/job/75087664237) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 52 | 9 | [7h51m](https://github.com/iree-org/iree/actions/runs/25569081688/job/75061158759) | 1 | [26m46s](https://github.com/iree-org/iree/actions/runs/25574326102/job/75078970808) | [3h57m](https://github.com/iree-org/iree/actions/runs/25577031854/job/75089880086) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 50 | 9 | [4h57m](https://github.com/iree-org/iree/actions/runs/25577031840/job/75087773162) | 0 | [13m04s](https://github.com/iree-org/iree/actions/runs/25574326102/job/75078970882) | [3h48m](https://github.com/iree-org/iree/actions/runs/25572644639/job/75073537062) | 0% (0/4) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 104 | 29 | [7h51m](https://github.com/iree-org/iree/actions/runs/25569081688/job/75061158893) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25575894724/job/75083999882) | [3h44m](https://github.com/iree-org/iree/actions/runs/25577031874/job/75087664125) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 52 | 0 | — | 1 | [22m36s](https://github.com/iree-org/iree/actions/runs/25566576835/job/75053252799) | [2h45m](https://github.com/iree-org/iree/actions/runs/25577032507/job/75087772976) | 33% (2/6) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 104 | 1 | [7h51m](https://github.com/iree-org/iree/actions/runs/25569081688/job/75061158898) | 1 | [28m25s](https://github.com/iree-org/iree/actions/runs/25566048207/job/75050952463) | [2h35m](https://github.com/iree-org/iree/actions/runs/25577031874/job/75087664279) | 0% (0/13) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 52 | 1 | [2h21m](https://github.com/iree-org/iree/actions/runs/25583203487/job/75107094302) | 0 | [24m48s](https://github.com/iree-org/iree/actions/runs/25574325766/job/75079119023) | [2h27m](https://github.com/iree-org/iree/actions/runs/25581695300/job/75104651033) | 0% (0/7) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 52 | 4 | [2h45m](https://github.com/iree-org/iree/actions/runs/25581695300/job/75104651027) | 0 | [14m43s](https://github.com/iree-org/iree/actions/runs/25566005727/job/75050777996) | [2h25m](https://github.com/iree-org/iree/actions/runs/25577031840/job/75087772880) | 20% (1/5) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 52 | 0 | — | 0 | [9m56s](https://github.com/iree-org/iree/actions/runs/25565320897/job/75048881051) | [2h07m](https://github.com/iree-org/iree/actions/runs/25572644639/job/75073537015) | 0% (0/7) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 104 | 0 | — | 0 | [13m45s](https://github.com/iree-org/iree/actions/runs/25577031840/job/75087772924) | [1h39m](https://github.com/iree-org/iree/actions/runs/25581029007/job/75103295857) | 0% (0/14) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 52 | 0 | — | 0 | [12m32s](https://github.com/iree-org/iree/actions/runs/25571178567/job/75068226747) | [56m05s](https://github.com/iree-org/iree/actions/runs/25573374530/job/75075554213) | 0% (0/7) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 54 | 1 | [1h04m](https://github.com/iree-org/iree/actions/runs/25585445125/job/75113742361) | 0 | [15m37s](https://github.com/iree-org/iree/actions/runs/25566005619/job/75050735544) | [41m08s](https://github.com/iree-org/iree/actions/runs/25574326102/job/75078970811) | 0% (0/7) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 52 | 0 | — | 0 | [6m18s](https://github.com/iree-org/iree/actions/runs/25574189224/job/75078404184) | [33m53s](https://github.com/iree-org/iree/actions/runs/25566806595/job/75055726057) | 0% (0/7) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 208 | 0 | — | 0 | [1m23s](https://github.com/iree-org/iree/actions/runs/25566806595/job/75055726101) | [14m07s](https://github.com/iree-org/iree/actions/runs/25577031854/job/75089880521) | 18% (5/28) | 200 |
| `ubuntu-24.04` | github-hosted | 1075 | 1 | [3m31s](https://github.com/iree-org/iree/actions/runs/25586349099/job/75118399368) | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25582806110/job/75105271407) | [8m04s](https://github.com/iree-org/iree/actions/runs/25564563843/job/75045985153) | 0% (0/123) | 1016 |
| `macos-14` | github-hosted | 183 | 0 | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/25577031806/job/75086699880) | [5m15s](https://github.com/iree-org/iree/actions/runs/25564563458/job/75045332336) | 0% (0/24) | 169 |
| `windows-2022` | github-hosted | 183 | 0 | — | 3 | [9s](https://github.com/iree-org/iree/actions/runs/25564661041/job/75044941942) | [4m49s](https://github.com/iree-org/iree/actions/runs/25566576780/job/75053236951) | 0% (0/24) | 171 |
| `ubuntu-24.04-arm` | github-hosted | 183 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25576917763/job/75086260244) | [4m16s](https://github.com/iree-org/iree/actions/runs/25577032456/job/75086707547) | 0% (0/24) | 170 |
| `azure-linux-scale` | ossci | 315 | 1 | [40m51s](https://github.com/iree-org/iree/actions/runs/25586349104/job/75115582138) | 2 | [10s](https://github.com/iree-org/iree/actions/runs/25572001110/job/75069833780) | [2m43s](https://github.com/iree-org/iree/actions/runs/25579494456/job/75094758003) | 0% (0/48) | 300 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 52 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25564563264/job/75046117057) | [2m24s](https://github.com/iree-org/iree/actions/runs/25566048207/job/75050952401) | 57% (4/7) | 52 |
| `ubuntu-latest` | github-hosted | 66 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25586348577/job/75115561488) | [1m10s](https://github.com/iree-org/iree/actions/runs/25580017910/job/75096478329) | 0% (0/16) | 66 |
| `azure-windows-scale` | ossci | 61 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25563861730/job/75042190234) | [22s](https://github.com/iree-org/iree/actions/runs/25565320867/job/75047853033) | 0% (0/8) | 59 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 851 | 8% (68/846) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 887 | 4% (38/884) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 723 | 3% (21/720) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 627 | 2% (11/624) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 239 | 2% (5/238) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 7h51m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 7h51m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 7h51m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 2h45m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 2h21m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 6h34m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 4h57m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h35m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 3h57m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h44m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h25m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h45m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 2h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 4h43m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 3h48m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h07m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h39m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
