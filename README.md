# iree-ci-monitor

_Updated: 2026-05-06 11:55 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 20 | 1 | [35m25s](https://github.com/iree-org/iree/actions/runs/25452862026/job/74675568323) | 0 | [41m36s](https://github.com/iree-org/iree/actions/runs/25435309899/job/74612856373) | [2h20m](https://github.com/iree-org/iree/actions/runs/25444324780/job/74646531732) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 20 | 2 | [35m25s](https://github.com/iree-org/iree/actions/runs/25452862026/job/74675568389) | 0 | [31m56s](https://github.com/iree-org/iree/actions/runs/25437773775/job/74621668283) | [1h39m](https://github.com/iree-org/iree/actions/runs/25448249077/job/74659571847) | 25% (1/4) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 40 | 2 | [12m15s](https://github.com/iree-org/iree/actions/runs/25453930468/job/74679486300) | 1 | [36m15s](https://github.com/iree-org/iree/actions/runs/25435309899/job/74612856688) | [1h36m](https://github.com/iree-org/iree/actions/runs/25448249077/job/74659571881) | 0% (0/8) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 20 | 0 | — | 0 | [39m43s](https://github.com/iree-org/iree/actions/runs/25450051546/job/74665818567) | [1h09m](https://github.com/iree-org/iree/actions/runs/25448786506/job/74661336699) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 20 | 0 | — | 0 | [33m20s](https://github.com/iree-org/iree/actions/runs/25444324780/job/74646532108) | [57m44s](https://github.com/iree-org/iree/actions/runs/25448786506/job/74661336794) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 20 | 0 | — | 1 | [13m25s](https://github.com/iree-org/iree/actions/runs/25452862026/job/74675568267) | [54m18s](https://github.com/iree-org/iree/actions/runs/25444824291/job/74647419684) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 40 | 0 | — | 0 | [11m15s](https://github.com/iree-org/iree/actions/runs/25452862026/job/74675568160) | [52m59s](https://github.com/iree-org/iree/actions/runs/25444824291/job/74647420085) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 20 | 2 | [2h02m](https://github.com/iree-org/iree/actions/runs/25448473550/job/74660987369) | 0 | [25m38s](https://github.com/iree-org/iree/actions/runs/25426615835/job/74589390371) | [47m49s](https://github.com/iree-org/iree/actions/runs/25444824291/job/74647419853) | 0% (0/4) | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 20 | 0 | — | 1 | [8m47s](https://github.com/iree-org/iree/actions/runs/25426615835/job/74589390425) | [44m29s](https://github.com/iree-org/iree/actions/runs/25448786506/job/74661336737) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 40 | 0 | — | 0 | [10m07s](https://github.com/iree-org/iree/actions/runs/25433015907/job/74604898253) | [43m56s](https://github.com/iree-org/iree/actions/runs/25444824291/job/74647419857) | 12% (1/8) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 20 | 0 | — | 1 | [8m07s](https://github.com/iree-org/iree/actions/runs/25449821789/job/74665152513) | [35m32s](https://github.com/iree-org/iree/actions/runs/25444324780/job/74646532074) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 20 | 1 | [12m15s](https://github.com/iree-org/iree/actions/runs/25453930468/job/74679486118) | 0 | [17m39s](https://github.com/iree-org/iree/actions/runs/25435872002/job/74614892056) | [32m34s](https://github.com/iree-org/iree/actions/runs/25449821789/job/74665152505) | 0% (0/4) | `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 20 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25453930468/job/74679486340) | [13m44s](https://github.com/iree-org/iree/actions/runs/25448473550/job/74660987674) | 0% (0/4) | `iree-mi308-1` |
| `azure-linux-scale` | ossci | 101 | 0 | — | 3 | [12s](https://github.com/iree-org/iree/actions/runs/25452852706/job/74674481619) | [10m43s](https://github.com/iree-org/iree/actions/runs/25444257686/job/74643894224) | 0% (0/26) | 101 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 80 | 0 | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25450051546/job/74665818587) | [5m32s](https://github.com/iree-org/iree/actions/runs/25437773775/job/74621668261) | 12% (2/16) | 80 |
| `azure-windows-scale` | ossci | 18 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25448425387/job/74658831278) | [5m31s](https://github.com/iree-org/iree/actions/runs/25443967256/job/74642850876) | 0% (0/4) | 18 |
| `macos-14` | github-hosted | 55 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25450051544/job/74664511988) | [1m46s](https://github.com/iree-org/iree/actions/runs/25444823902/job/74645967944) | 0% (0/13) | 55 |
| `windows-2022` | github-hosted | 54 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25453930458/job/74678230977) | [1m39s](https://github.com/iree-org/iree/actions/runs/25448473576/job/74659143028) | 0% (0/12) | 54 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m32s](https://github.com/iree-org/iree/actions/runs/25428734466/job/74589028159) | [1m32s](https://github.com/iree-org/iree/actions/runs/25428734466/job/74589028159) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 54 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25452852706/job/74674481442) | [1m27s](https://github.com/iree-org/iree/actions/runs/25448786453/job/74660139477) | 0% (0/12) | 54 |
| `ubuntu-24.04` | github-hosted | 360 | 0 | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/25449821789/job/74665152405) | [59s](https://github.com/iree-org/iree/actions/runs/25426615835/job/74581672712) | 4% (3/72) | 360 |
| `ubuntu-latest` | github-hosted | 37 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25452843045/job/74674418004) | [10s](https://github.com/iree-org/iree/actions/runs/25444669010/job/74645343335) | 0% (0/8) | 37 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25428720443/job/74588980113) | [3s](https://github.com/iree-org/iree/actions/runs/25428720443/job/74588980113) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 20 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25433015907/job/74604898339) | [2s](https://github.com/iree-org/iree/actions/runs/25453930468/job/74679486048) | 25% (1/4) | 20 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 261 | 1% (3/260) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 891 | 2% (14/888) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 776 | 1% (6/774) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 957 | 6% (62/955) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1111 | 4% (42/1107) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 2h02m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h36m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h39m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h09m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
