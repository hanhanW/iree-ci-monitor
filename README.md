# iree-ci-monitor

_Updated: 2026-05-07 11:56 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 34 | 10 | [2h06m](https://github.com/iree-org/iree/actions/runs/25509285996/job/74865071881) | 0 | [9m17s](https://github.com/iree-org/iree/actions/runs/25497024643/job/74820791269) | [1h09m](https://github.com/iree-org/iree/actions/runs/25510068890/job/74867611927) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 34 | 6 | [56m15s](https://github.com/iree-org/iree/actions/runs/25512800403/job/74877117673) | 1 | [5m12s](https://github.com/iree-org/iree/actions/runs/25495012547/job/74813441570) | [58m36s](https://github.com/iree-org/iree/actions/runs/25511153714/job/74871222128) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 17 | 1 | [2m13s](https://github.com/iree-org/iree/actions/runs/25515374712/job/74886451083) | 0 | [4m07s](https://github.com/iree-org/iree/actions/runs/25509285996/job/74865071628) | [49m40s](https://github.com/iree-org/iree/actions/runs/25511153714/job/74871222033) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 17 | 4 | [1h27m](https://github.com/iree-org/iree/actions/runs/25510413063/job/74871735300) | 0 | [10m00s](https://github.com/iree-org/iree/actions/runs/25497024643/job/74820791344) | [45m17s](https://github.com/iree-org/iree/actions/runs/25511153714/job/74871222053) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 17 | 5 | [1h30m](https://github.com/iree-org/iree/actions/runs/25511153714/job/74871222149) | 0 | [11m28s](https://github.com/iree-org/iree/actions/runs/25509285996/job/74865071803) | [43m57s](https://github.com/iree-org/iree/actions/runs/25510068890/job/74867611730) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 17 | 2 | [56m15s](https://github.com/iree-org/iree/actions/runs/25512800403/job/74877117648) | 0 | [8m55s](https://github.com/iree-org/iree/actions/runs/25495012547/job/74813441574) | [41m38s](https://github.com/iree-org/iree/actions/runs/25494600410/job/74812568456) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 17 | 2 | [39m34s](https://github.com/iree-org/iree/actions/runs/25513473692/job/74880066348) | 1 | [12m32s](https://github.com/iree-org/iree/actions/runs/25511400083/job/74872580492) | [34m33s](https://github.com/iree-org/iree/actions/runs/25494600410/job/74812568369) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 34 | 5 | [1h30m](https://github.com/iree-org/iree/actions/runs/25511153714/job/74871222214) | 2 | [8m50s](https://github.com/iree-org/iree/actions/runs/25510413063/job/74871735326) | [34m10s](https://github.com/iree-org/iree/actions/runs/25510068890/job/74867611970) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 17 | 2 | [1h51m](https://github.com/iree-org/iree/actions/runs/25510068890/job/74867611899) | 0 | [6m06s](https://github.com/iree-org/iree/actions/runs/25502862216/job/74841875084) | [29m45s](https://github.com/iree-org/iree/actions/runs/25494600410/job/74812568587) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 17 | 1 | [2m13s](https://github.com/iree-org/iree/actions/runs/25515374712/job/74886451362) | 0 | [8m04s](https://github.com/iree-org/iree/actions/runs/25497024643/job/74820791584) | [23m41s](https://github.com/iree-org/iree/actions/runs/25510413063/job/74871735293) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 17 | 2 | [56m15s](https://github.com/iree-org/iree/actions/runs/25512800403/job/74877117681) | 0 | [4m17s](https://github.com/iree-org/iree/actions/runs/25495012547/job/74813441193) | [18m06s](https://github.com/iree-org/iree/actions/runs/25497024643/job/74820791332) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 17 | 1 | [2m13s](https://github.com/iree-org/iree/actions/runs/25515374712/job/74886451339) | 0 | [1m35s](https://github.com/iree-org/iree/actions/runs/25510068890/job/74867612069) | [17m37s](https://github.com/iree-org/iree/actions/runs/25497024643/job/74820791294) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 68 | 0 | — | 4 | [19s](https://github.com/iree-org/iree/actions/runs/25494600410/job/74812568542) | [15m46s](https://github.com/iree-org/iree/actions/runs/25510413063/job/74871735349) | 38% (3/8) | 64 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 17 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25513473692/job/74880066420) | [4m59s](https://github.com/iree-org/iree/actions/runs/25495012547/job/74813441678) | 0% (0/2) | `iree-mi308-1` |
| `azure-linux-scale` | ossci | 126 | 0 | — | 8 | [9s](https://github.com/iree-org/iree/actions/runs/25515119921/job/74884117563) | [2m47s](https://github.com/iree-org/iree/actions/runs/25513473692/job/74878211045) | 0% (0/14) | 126 |
| `macos-14` | github-hosted | 73 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25515576602/job/74886054704) | [1m48s](https://github.com/iree-org/iree/actions/runs/25511153702/job/74870359584) | 0% (0/7) | 73 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m42s](https://github.com/iree-org/iree/actions/runs/25489252129/job/74792730081) | [1m42s](https://github.com/iree-org/iree/actions/runs/25489252129/job/74792730081) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 72 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25515576602/job/74886054873) | [1m39s](https://github.com/iree-org/iree/actions/runs/25494769773/job/74811561422) | 0% (0/6) | 72 |
| `windows-2022` | github-hosted | 72 | 0 | — | 6 | [3s](https://github.com/iree-org/iree/actions/runs/25513473708/job/74878208612) | [1m36s](https://github.com/iree-org/iree/actions/runs/25495012563/job/74812627996) | 0% (0/6) | 72 |
| `ubuntu-24.04` | github-hosted | 387 | 0 | — | 12 | [9s](https://github.com/iree-org/iree/actions/runs/25487837827/job/74787935120) | [1m32s](https://github.com/iree-org/iree/actions/runs/25510413063/job/74871735209) | 0% (0/36) | 385 |
| `azure-windows-scale` | ossci | 24 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25490669675/job/74797774234) | [13s](https://github.com/iree-org/iree/actions/runs/25510413097/job/74867402527) | 0% (0/2) | 24 |
| `ubuntu-latest` | github-hosted | 26 | 0 | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25493124825/job/74805931473) | [10s](https://github.com/iree-org/iree/actions/runs/25515371864/job/74884958642) | 0% (0/4) | 26 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 17 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25509285996/job/74865071688) | [3s](https://github.com/iree-org/iree/actions/runs/25502862216/job/74841874720) | 50% (1/2) | 17 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25489233190/job/74792665775) | [3s](https://github.com/iree-org/iree/actions/runs/25489233190/job/74792665775) | 0% (0/1) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 247 | 2% (4/245) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 698 | 1% (6/695) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1017 | 2% (16/1013) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 793 | 2% (12/790) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 927 | 6% (56/924) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 2h06m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h09m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
