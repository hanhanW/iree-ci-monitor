# iree-ci-monitor

_Updated: 2026-05-08 11:51 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 36 | 7 | [2h01m](https://github.com/iree-org/iree/actions/runs/25567513058/job/75056109735) | 0 | [10m54s](https://github.com/iree-org/iree/actions/runs/25570335810/job/75065264205) | [2h03m](https://github.com/iree-org/iree/actions/runs/25566048207/job/75050952242) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 36 | 6 | [1h28m](https://github.com/iree-org/iree/actions/runs/25569081688/job/75061158759) | 1 | [13m34s](https://github.com/iree-org/iree/actions/runs/25565320897/job/75048881059) | [1h54m](https://github.com/iree-org/iree/actions/runs/25566005727/job/75050777990) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 36 | 5 | [48m40s](https://github.com/iree-org/iree/actions/runs/25570931809/job/75067389908) | 0 | [14m07s](https://github.com/iree-org/iree/actions/runs/25566048207/job/75050952296) | [1h52m](https://github.com/iree-org/iree/actions/runs/25566005619/job/75050735540) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 36 | 11 | [2h35m](https://github.com/iree-org/iree/actions/runs/25566005619/job/75050735571) | 0 | [11m44s](https://github.com/iree-org/iree/actions/runs/25565320897/job/75048881164) | [1h48m](https://github.com/iree-org/iree/actions/runs/25555373579/job/75014044629) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 72 | 26 | [2h47m](https://github.com/iree-org/iree/actions/runs/25565320897/job/75048881161) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25571178567/job/75068226979) | [1h37m](https://github.com/iree-org/iree/actions/runs/25555373579/job/75014044650) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 36 | 10 | [2h35m](https://github.com/iree-org/iree/actions/runs/25566005619/job/75050735488) | 1 | [15m59s](https://github.com/iree-org/iree/actions/runs/25555107126/job/75013230218) | [1h20m](https://github.com/iree-org/iree/actions/runs/25555125920/job/75013299416) | 0% (0/3) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 36 | 3 | [15m19s](https://github.com/iree-org/iree/actions/runs/25572402482/job/75072548203) | 1 | [8m21s](https://github.com/iree-org/iree/actions/runs/25566806595/job/75055726092) | [1h03m](https://github.com/iree-org/iree/actions/runs/25567513058/job/75056109803) | 0% (0/5) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 72 | 11 | [1h28m](https://github.com/iree-org/iree/actions/runs/25569081688/job/75061158898) | 0 | [10m56s](https://github.com/iree-org/iree/actions/runs/25564563421/job/75046012550) | [1h01m](https://github.com/iree-org/iree/actions/runs/25555125920/job/75013299448) | 0% (0/7) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 36 | 6 | [2h01m](https://github.com/iree-org/iree/actions/runs/25567513058/job/75056109822) | 0 | [15m37s](https://github.com/iree-org/iree/actions/runs/25566576835/job/75053253020) | [49m28s](https://github.com/iree-org/iree/actions/runs/25560451465/job/75031729109) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 72 | 3 | [15m19s](https://github.com/iree-org/iree/actions/runs/25572402482/job/75072548309) | 1 | [7m39s](https://github.com/iree-org/iree/actions/runs/25564563421/job/75046012398) | [46m18s](https://github.com/iree-org/iree/actions/runs/25555373579/job/75014044649) | 0% (0/11) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 36 | 3 | [15m19s](https://github.com/iree-org/iree/actions/runs/25572402482/job/75072548189) | 0 | [13m08s](https://github.com/iree-org/iree/actions/runs/25569376504/job/75062226502) | [30m39s](https://github.com/iree-org/iree/actions/runs/25555107126/job/75013230289) | 0% (0/5) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 36 | 1 | [12m21s](https://github.com/iree-org/iree/actions/runs/25572626442/job/75073016062) | 1 | [1m58s](https://github.com/iree-org/iree/actions/runs/25570931809/job/75067389830) | [30m09s](https://github.com/iree-org/iree/actions/runs/25566434848/job/75052852560) | 0% (0/5) | `iree-mi308-1` |
| `Linux,X64,rdna3` | self-hosted | 36 | 3 | [15m19s](https://github.com/iree-org/iree/actions/runs/25572402482/job/75072548235) | 0 | [10m52s](https://github.com/iree-org/iree/actions/runs/25566434848/job/75052852661) | [25m57s](https://github.com/iree-org/iree/actions/runs/25560451465/job/75031729139) | 0% (0/5) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 144 | 0 | — | 4 | [11s](https://github.com/iree-org/iree/actions/runs/25572402482/job/75072548220) | [8m48s](https://github.com/iree-org/iree/actions/runs/25566576835/job/75053253146) | 27% (6/22) | 139 |
| `ubuntu-24.04` | github-hosted | 698 | 2 | [3m17s](https://github.com/iree-org/iree/actions/runs/25573374511/job/75074452577) | 11 | [9s](https://github.com/iree-org/iree/actions/runs/25572402482/job/75071269938) | [7m39s](https://github.com/iree-org/iree/actions/runs/25566806640/job/75053262168) | 1% (1/103) | 685 |
| `windows-2022` | github-hosted | 117 | 3 | [3m17s](https://github.com/iree-org/iree/actions/runs/25573374511/job/75074452691) | 3 | [4s](https://github.com/iree-org/iree/actions/runs/25560451431/job/75030386160) | [4m49s](https://github.com/iree-org/iree/actions/runs/25566576780/job/75053236951) | 0% (0/18) | 114 |
| `macos-14` | github-hosted | 118 | 0 | — | 3 | [4s](https://github.com/iree-org/iree/actions/runs/25563855246/job/75042147230) | [4m32s](https://github.com/iree-org/iree/actions/runs/25566005699/job/75050009218) | 0% (0/19) | 118 |
| `ubuntu-24.04-arm` | github-hosted | 117 | 2 | [3m17s](https://github.com/iree-org/iree/actions/runs/25573374511/job/75074452682) | 1 | [7s](https://github.com/iree-org/iree/actions/runs/25561576494/job/75034294361) | [3m36s](https://github.com/iree-org/iree/actions/runs/25566385266/job/75052329277) | 0% (0/18) | 115 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m30s](https://github.com/iree-org/iree/actions/runs/25548944272/job/74991875074) | [1m30s](https://github.com/iree-org/iree/actions/runs/25548944272/job/74991875074) | 0% (0/1) | 1 |
| `ubuntu-latest` | github-hosted | 55 | 0 | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25560747631/job/75031386187) | [1m29s](https://github.com/iree-org/iree/actions/runs/25572641866/job/75071914422) | 0% (0/12) | 55 |
| `azure-linux-scale` | ossci | 205 | 4 | [3m17s](https://github.com/iree-org/iree/actions/runs/25573374511/job/75074452777) | 11 | [9s](https://github.com/iree-org/iree/actions/runs/25564563840/job/75044988877) | [1m27s](https://github.com/iree-org/iree/actions/runs/25563861730/job/75042190132) | 0% (0/35) | 201 |
| `azure-windows-scale` | ossci | 39 | 0 | — | 4 | [2s](https://github.com/iree-org/iree/actions/runs/25563861730/job/75042190234) | [22s](https://github.com/iree-org/iree/actions/runs/25565320867/job/75047853033) | 0% (0/5) | 39 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 36 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25564563264/job/75046117057) | [11s](https://github.com/iree-org/iree/actions/runs/25571178567/job/75068226737) | 0% (0/6) | 36 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25548931396/job/74991832237) | [4s](https://github.com/iree-org/iree/actions/runs/25548931396/job/74991832237) | 0% (0/1) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 255 | 2% (6/253) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 928 | 7% (67/924) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 781 | 2% (18/778) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 993 | 3% (31/990) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 673 | 2% (12/670) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 2h47m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 2h01m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 2h01m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 2h35m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 2h35m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h54m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h37m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h03m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h52m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h48m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h03m (> 1h00m)
- **[high-failure-main]** `linux-mi325-1gpu-ossci-iree-org` main-branch failure rate 27% (6/22)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
