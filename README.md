# iree-ci-monitor

_Updated: 2026-04-29 05:55 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 16 | 0 | — | 0 | [1h35m](https://github.com/iree-org/iree/actions/runs/25090083229/job/73514611500) | [3h57m](https://github.com/iree-org/iree/actions/runs/25093569755/job/73525928596) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 16 | 0 | — | 0 | [48m43s](https://github.com/iree-org/iree/actions/runs/25088691479/job/73529948924) | [3h25m](https://github.com/iree-org/iree/actions/runs/25098891486/job/73543456900) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 16 | 0 | — | 0 | [21m19s](https://github.com/iree-org/iree/actions/runs/25102296074/job/73555784676) | [2h05m](https://github.com/iree-org/iree/actions/runs/25094689645/job/73529356049) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 32 | 0 | — | 0 | [16m38s](https://github.com/iree-org/iree/actions/runs/25104202023/job/73562224222) | [1h53m](https://github.com/iree-org/iree/actions/runs/25097410230/job/73538651944) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 16 | 0 | — | 0 | [19m52s](https://github.com/iree-org/iree/actions/runs/25095516714/job/73561237423) | [1h20m](https://github.com/iree-org/iree/actions/runs/25094689645/job/73529355957) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 16 | 0 | — | 0 | [9m45s](https://github.com/iree-org/iree/actions/runs/25094689645/job/73529356059) | [1h18m](https://github.com/iree-org/iree/actions/runs/25098247886/job/73541687742) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 16 | 0 | — | 0 | [4m04s](https://github.com/iree-org/iree/actions/runs/25094689645/job/73529356080) | [1h01m](https://github.com/iree-org/iree/actions/runs/25098891486/job/73543456962) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 48 | 0 | — | 0 | [8m22s](https://github.com/iree-org/iree/actions/runs/25096285982/job/73534841653) | [48m20s](https://github.com/iree-org/iree/actions/runs/25098891486/job/73543456916) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 32 | 0 | — | 0 | [7m34s](https://github.com/iree-org/iree/actions/runs/25091459647/job/73518748115) | [44m22s](https://github.com/iree-org/iree/actions/runs/25098891486/job/73543456891) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 16 | 0 | — | 0 | [9m00s](https://github.com/iree-org/iree/actions/runs/25107515648/job/73573766047) | [33m52s](https://github.com/iree-org/iree/actions/runs/25098247886/job/73541687845) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 16 | 0 | — | 0 | [9m13s](https://github.com/iree-org/iree/actions/runs/25098891486/job/73543456831) | [27m54s](https://github.com/iree-org/iree/actions/runs/25098247886/job/73541687892) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 16 | 0 | — | 0 | [6m34s](https://github.com/iree-org/iree/actions/runs/25098247886/job/73541687901) | [16m52s](https://github.com/iree-org/iree/actions/runs/25098891486/job/73543456877) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `macos-14` | github-hosted | 62 | 0 | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/25097410178/job/73538238355) | [5m26s](https://github.com/iree-org/iree/actions/runs/25097410178/job/73538238288) | 0% (0/7) | 57 |
| `ubuntu-24.04` | github-hosted | 369 | 0 | — | 5 | [3s](https://github.com/iree-org/iree/actions/runs/25097209700/job/73537017803) | [4m49s](https://github.com/iree-org/iree/actions/runs/25093569755/job/73525928489) | 15% (8/53) | 361 |
| `windows-2022` | github-hosted | 59 | 0 | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/25107388191/job/73572052627) | [3m30s](https://github.com/iree-org/iree/actions/runs/25097410178/job/73538238291) | 0% (0/6) | 53 |
| `ubuntu-latest` | github-hosted | 28 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25105793293/job/73566581067) | [2m24s](https://github.com/iree-org/iree/actions/runs/25093917124/job/73526100622) | 0% (0/4) | 28 |
| `ubuntu-24.04-arm` | github-hosted | 60 | 0 | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/25103621044/job/73559092500) | [2m12s](https://github.com/iree-org/iree/actions/runs/25097410178/job/73538238367) | 0% (0/6) | 54 |
| `azure-linux-scale` | ossci | 103 | 0 | — | 5 | [14s](https://github.com/iree-org/iree/actions/runs/25104202032/job/73561110495) | [1m51s](https://github.com/iree-org/iree/actions/runs/25090083219/job/73514160508) | 7% (1/14) | 95 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 3 | 0 | — | 0 | [1m37s](https://github.com/iree-org/iree/actions/runs/25102369230/job/73554686741) | [1m43s](https://github.com/iree-org/iree/actions/runs/25097209700/job/73537017882) | 0% (0/1) | 3 |
| `macos-15-intel` | github-hosted | 3 | 0 | — | 2 | [7s](https://github.com/iree-org/iree/actions/runs/25097209700/job/73537017934) | [41s](https://github.com/iree-org/iree/actions/runs/25102342238/job/73554593901) | — | 3 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 64 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25093569755/job/73525928576) | [20s](https://github.com/iree-org/iree/actions/runs/25107515648/job/73573766218) | 0% (0/8) | 64 |
| `azure-windows-scale` | ossci | 19 | 1 | [5h49m](https://github.com/iree-org/iree/actions/runs/25095516710/job/73531297511) | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25102296161/job/73554467262) | [12s](https://github.com/iree-org/iree/actions/runs/25098247902/job/73540417806) | 0% (0/2) | 18 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25104202023/job/73562224002) | [2s](https://github.com/iree-org/iree/actions/runs/25102296074/job/73555784627) | 0% (0/2) | 16 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 16 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25094689645/job/73529356070) | [2s](https://github.com/iree-org/iree/actions/runs/25107515648/job/73573766202) | 0% (0/2) | `iree-mi308-1` |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 816 | 4% (35/812) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 678 | 1% (10/674) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 732 | 3% (22/727) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 216 | 1% (2/213) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 466 | 14% (63/462) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 141 | 8% (11/141) |  | 25m09s ago |

## Alerts

- **[stale-queued]** `azure-windows-scale` oldest queued job waiting 5h49m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h05m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h53m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h18m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 3h57m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 3h25m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
