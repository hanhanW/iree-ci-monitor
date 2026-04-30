# iree-ci-monitor

_Updated: 2026-04-29 18:12 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 34 | 18 | [8h02m](https://github.com/iree-org/iree/actions/runs/25118751210/job/73628474615) | 1 | [1h29m](https://github.com/iree-org/iree/actions/runs/25122538292/job/73629812350) | [6h00m](https://github.com/iree-org/iree/actions/runs/25126054907/job/73640790632) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 68 | 24 | [8h34m](https://github.com/iree-org/iree/actions/runs/25117854274/job/73623111192) | 0 | [2h49m](https://github.com/iree-org/iree/actions/runs/25120992881/job/73628940983) | [5h59m](https://github.com/iree-org/iree/actions/runs/25128131882/job/73648013757) | 0% (0/7) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 34 | 15 | [7h59m](https://github.com/iree-org/iree/actions/runs/25120992881/job/73628940991) | 0 | [1h29m](https://github.com/iree-org/iree/actions/runs/25120714030/job/73629067405) | [5h40m](https://github.com/iree-org/iree/actions/runs/25115513541/job/73622803109) | 0% (0/2) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 34 | 11 | [7h15m](https://github.com/iree-org/iree/actions/runs/25124187219/job/73636176213) | 0 | [1h04m](https://github.com/iree-org/iree/actions/runs/25117388532/job/73622858148) | [5h03m](https://github.com/iree-org/iree/actions/runs/25122538292/job/73629812302) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 34 | 7 | [5h35m](https://github.com/iree-org/iree/actions/runs/25129081052/job/73652661542) | 1 | [1h48m](https://github.com/iree-org/iree/actions/runs/25124187219/job/73636175982) | [4h58m](https://github.com/iree-org/iree/actions/runs/25129099647/job/73652665000) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 34 | 8 | [6h47m](https://github.com/iree-org/iree/actions/runs/25126054907/job/73640790429) | 1 | [1h55m](https://github.com/iree-org/iree/actions/runs/25129056546/job/73652623992) | [4h32m](https://github.com/iree-org/iree/actions/runs/25117854274/job/73623111127) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 68 | 2 | [3h26m](https://github.com/iree-org/iree/actions/runs/25135228671/job/73672888410) | 1 | [2h09m](https://github.com/iree-org/iree/actions/runs/25124187219/job/73636176135) | [4h24m](https://github.com/iree-org/iree/actions/runs/25129099647/job/73652665079) | 0% (0/12) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 102 | 7 | [4h20m](https://github.com/iree-org/iree/actions/runs/25132845388/job/73664837961) | 0 | [2h31m](https://github.com/iree-org/iree/actions/runs/25128131882/job/73648013541) | [4h19m](https://github.com/iree-org/iree/actions/runs/25121696893/job/73628183068) | 6% (1/16) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 34 | 0 | — | 0 | [2h06m](https://github.com/iree-org/iree/actions/runs/25128131882/job/73648013542) | [4h09m](https://github.com/iree-org/iree/actions/runs/25120992881/job/73628940967) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 34 | 3 | [4h24m](https://github.com/iree-org/iree/actions/runs/25132303574/job/73664159112) | 0 | [1h45m](https://github.com/iree-org/iree/actions/runs/25124187219/job/73636176077) | [3h36m](https://github.com/iree-org/iree/actions/runs/25132456465/job/73665181604) | 67% (4/6) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 34 | 6 | [4h28m](https://github.com/iree-org/iree/actions/runs/25132043785/job/73663468455) | 0 | [1h35m](https://github.com/iree-org/iree/actions/runs/25116392084/job/73622630781) | [3h30m](https://github.com/iree-org/iree/actions/runs/25129099647/job/73652664835) | 33% (1/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 34 | 0 | — | 0 | [1h20m](https://github.com/iree-org/iree/actions/runs/25118280445/job/73623279184) | [3h17m](https://github.com/iree-org/iree/actions/runs/25135228671/job/73672888366) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 34 | 0 | — | 0 | [32m33s](https://github.com/iree-org/iree/actions/runs/25117854274/job/73623111256) | [1h21m](https://github.com/iree-org/iree/actions/runs/25123441598/job/73632905396) | 0% (0/6) | `iree-mi308-1` |
| `azure-linux-scale` | ossci | 189 | 0 | — | 0 | [14s](https://github.com/iree-org/iree/actions/runs/25132303560/job/73661525698) | [1h13m](https://github.com/iree-org/iree/actions/runs/25118751042/job/73613246649) | 0% (0/37) | 176 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 136 | 0 | — | 0 | [6m18s](https://github.com/iree-org/iree/actions/runs/25117388532/job/73622857847) | [26m46s](https://github.com/iree-org/iree/actions/runs/25117388532/job/73622858077) | 8% (2/24) | 136 |
| `azure-windows-scale` | ossci | 36 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25118280368/job/73611535442) | [13m25s](https://github.com/iree-org/iree/actions/runs/25129056558/job/73650418299) | 0% (0/6) | 35 |
| `ubuntu-24.04` | github-hosted | 624 | 0 | — | 0 | [25s](https://github.com/iree-org/iree/actions/runs/25115722337/job/73622811649) | [7m53s](https://github.com/iree-org/iree/actions/runs/25123441598/job/73630028656) | 3% (3/94) | 614 |
| `ubuntu-latest` | github-hosted | 47 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25132042774/job/73660582054) | [6m17s](https://github.com/iree-org/iree/actions/runs/25123440518/job/73630028813) | 0% (0/12) | 47 |
| `macos-14` | github-hosted | 109 | 0 | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25117199435/job/73607623501) | [4m48s](https://github.com/iree-org/iree/actions/runs/25123441609/job/73631729275) | 0% (0/18) | 106 |
| `ubuntu-24.04-arm` | github-hosted | 108 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25117199435/job/73607623616) | [4m39s](https://github.com/iree-org/iree/actions/runs/25123441609/job/73631729332) | 0% (0/18) | 105 |
| `windows-2022` | github-hosted | 108 | 0 | — | 0 | [29s](https://github.com/iree-org/iree/actions/runs/25117498585/job/73608669408) | [4m32s](https://github.com/iree-org/iree/actions/runs/25124187270/job/73632968893) | 0% (0/18) | 105 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 34 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25129056546/job/73652624021) | [2m37s](https://github.com/iree-org/iree/actions/runs/25117854274/job/73623111103) | 33% (2/6) | 34 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m27s](https://github.com/iree-org/iree/actions/runs/25118751042/job/73613246992) | [1m27s](https://github.com/iree-org/iree/actions/runs/25118751042/job/73613246992) | — | 1 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 0 | [15s](https://github.com/iree-org/iree/actions/runs/25118751042/job/73613246999) | [15s](https://github.com/iree-org/iree/actions/runs/25118751042/job/73613246999) | — | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 205 | 8% (17/204) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 914 | 6% (53/909) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 823 | 3% (25/817) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 775 | 1% (10/770) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 246 | 1% (2/243) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 459 | 14% (62/455) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 3h26m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 6h47m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 8h34m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 4h24m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 4h28m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 5h35m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 7h59m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 8h02m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 7h15m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 4h20m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 4h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 4h24m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 4h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 5h59m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h36m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 3h30m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 4h58m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 5h40m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 6h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 3h17m (> 1h00m)
- **[queue-starved]** `azure-linux-scale` p95 queue 1h13m (> 1h00m)
- **[queue-starved]** `nodai-amdgpu-mi308-x86-64` p95 queue 1h21m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 5h03m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 4h19m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
