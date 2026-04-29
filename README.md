# iree-ci-monitor

_Updated: 2026-04-29 11:52 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 24 | 15 | [2h16m](https://github.com/iree-org/iree/actions/runs/25116392084/job/73622630894) | 1 | [25m02s](https://github.com/iree-org/iree/actions/runs/25104202023/job/73562224350) | [1h52m](https://github.com/iree-org/iree/actions/runs/25115513541/job/73622803188) | 0% (0/1) | `shark10-ci` |
| `azure-linux-scale` | ossci | 164 | 0 | — | 1 | [2m52s](https://github.com/iree-org/iree/actions/runs/25123441609/job/73631729461) | [1h43m](https://github.com/iree-org/iree/actions/runs/25115722346/job/73602085941) | 0% (0/20) | 139 |
| `Linux,X64,gfx1100` | self-hosted | 48 | 18 | [2h13m](https://github.com/iree-org/iree/actions/runs/25117854274/job/73623111198) | 1 | [24m10s](https://github.com/iree-org/iree/actions/runs/25116392084/job/73622630886) | [1h40m](https://github.com/iree-org/iree/actions/runs/25121696893/job/73628183147) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 24 | 15 | [2h16m](https://github.com/iree-org/iree/actions/runs/25116392084/job/73622630836) | 0 | [30m40s](https://github.com/iree-org/iree/actions/runs/25103620998/job/73560244945) | [1h29m](https://github.com/iree-org/iree/actions/runs/25120714030/job/73629067405) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 24 | 12 | [2h16m](https://github.com/iree-org/iree/actions/runs/25116392084/job/73622630868) | 0 | [21m19s](https://github.com/iree-org/iree/actions/runs/25102296074/job/73555784676) | [1h25m](https://github.com/iree-org/iree/actions/runs/25120992881/job/73628940966) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 72 | 30 | [2h15m](https://github.com/iree-org/iree/actions/runs/25117388532/job/73622857860) | 1 | [16m56s](https://github.com/iree-org/iree/actions/runs/25115513541/job/73622803063) | [1h24m](https://github.com/iree-org/iree/actions/runs/25122538292/job/73629812215) | 33% (1/3) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 48 | 26 | [2h15m](https://github.com/iree-org/iree/actions/runs/25115513541/job/73622803211) | 0 | [9m29s](https://github.com/iree-org/iree/actions/runs/25107515648/job/73573766201) | [1h22m](https://github.com/iree-org/iree/actions/runs/25115513541/job/73622803097) | 0% (0/3) | `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 24 | 4 | [1h14m](https://github.com/iree-org/iree/actions/runs/25123441598/job/73632905396) | 1 | [20m51s](https://github.com/iree-org/iree/actions/runs/25115513541/job/73622803192) | [1h18m](https://github.com/iree-org/iree/actions/runs/25122538292/job/73629812232) | 0% (0/2) | `iree-mi308-1` |
| `Linux,X64,rdna3` | self-hosted | 24 | 9 | [1h41m](https://github.com/iree-org/iree/actions/runs/25118751210/job/73628474598) | 0 | [13m01s](https://github.com/iree-org/iree/actions/runs/25104202023/job/73562224255) | [1h11m](https://github.com/iree-org/iree/actions/runs/25120992881/job/73628941036) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 24 | 11 | [2h15m](https://github.com/iree-org/iree/actions/runs/25115513541/job/73622803127) | 0 | [21m10s](https://github.com/iree-org/iree/actions/runs/25103620998/job/73560244821) | [1h06m](https://github.com/iree-org/iree/actions/runs/25120992881/job/73628940915) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 24 | 10 | [1h43m](https://github.com/iree-org/iree/actions/runs/25121179061/job/73628235661) | 0 | [9m00s](https://github.com/iree-org/iree/actions/runs/25107515648/job/73573766047) | [1h06m](https://github.com/iree-org/iree/actions/runs/25120992881/job/73628940930) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 24 | 13 | [2h15m](https://github.com/iree-org/iree/actions/runs/25115722337/job/73622811744) | 0 | [13m25s](https://github.com/iree-org/iree/actions/runs/25103620998/job/73560245049) | [55m08s](https://github.com/iree-org/iree/actions/runs/25115513541/job/73622803180) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 24 | 12 | [2h13m](https://github.com/iree-org/iree/actions/runs/25117854274/job/73623111130) | 0 | [9m50s](https://github.com/iree-org/iree/actions/runs/25104202023/job/73562224213) | [43m08s](https://github.com/iree-org/iree/actions/runs/25118751210/job/73628474517) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 24 | 8 | [1h41m](https://github.com/iree-org/iree/actions/runs/25118751210/job/73628474410) | 1 | [16m35s](https://github.com/iree-org/iree/actions/runs/25117388532/job/73622857757) | [28m47s](https://github.com/iree-org/iree/actions/runs/25117854274/job/73623111444) | 50% (1/2) | `shark75-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 96 | 0 | — | 0 | [10m38s](https://github.com/iree-org/iree/actions/runs/25118751210/job/73628474546) | [26m59s](https://github.com/iree-org/iree/actions/runs/25116392084/job/73622630888) | 0% (0/12) | 96 |
| `ubuntu-24.04` | github-hosted | 520 | 0 | — | 2 | [9s](https://github.com/iree-org/iree/actions/runs/25125731229/job/73638126006) | [7m40s](https://github.com/iree-org/iree/actions/runs/25119213325/job/73629883851) | 9% (6/65) | 515 |
| `ubuntu-latest` | github-hosted | 48 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25122535247/job/73626800399) | [6m17s](https://github.com/iree-org/iree/actions/runs/25123440518/job/73630028813) | 0% (0/6) | 48 |
| `azure-windows-scale` | ossci | 31 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25123772865/job/73631269469) | [4m56s](https://github.com/iree-org/iree/actions/runs/25116511423/job/73605112454) | 0% (0/3) | 31 |
| `ubuntu-24.04-arm` | github-hosted | 93 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25117199435/job/73607623616) | [4m39s](https://github.com/iree-org/iree/actions/runs/25123441609/job/73631729332) | 0% (0/9) | 93 |
| `macos-14` | github-hosted | 95 | 0 | — | 1 | [11s](https://github.com/iree-org/iree/actions/runs/25116305882/job/73604268951) | [4m38s](https://github.com/iree-org/iree/actions/runs/25116511423/job/73605112125) | 0% (0/10) | 95 |
| `windows-2022` | github-hosted | 93 | 0 | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25116392009/job/73604620913) | [4m06s](https://github.com/iree-org/iree/actions/runs/25118750475/job/73613285883) | 0% (0/9) | 93 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 24 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25121696893/job/73628182842) | [2m37s](https://github.com/iree-org/iree/actions/runs/25117854274/job/73623111103) | 33% (1/3) | 24 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 2 | 0 | — | 0 | [1m27s](https://github.com/iree-org/iree/actions/runs/25118751042/job/73613246992) | [1m37s](https://github.com/iree-org/iree/actions/runs/25102369230/job/73554686741) | 0% (0/1) | 2 |
| `macos-15-intel` | github-hosted | 2 | 0 | — | 1 | [15s](https://github.com/iree-org/iree/actions/runs/25118751042/job/73613246999) | [41s](https://github.com/iree-org/iree/actions/runs/25102342238/job/73554593901) | 0% (0/1) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 851 | 5% (40/846) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 765 | 3% (22/759) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 157 | 8% (13/156) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 230 | 1% (2/226) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 709 | 1% (10/704) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 466 | 14% (63/462) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job waiting 2h13m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 2h13m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 2h16m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 2h15m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 2h15m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 2h15m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 2h16m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 2h16m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 2h15m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h40m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h25m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h22m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h29m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h52m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h11m (> 1h00m)
- **[queue-starved]** `azure-linux-scale` p95 queue 1h43m (> 1h00m)
- **[queue-starved]** `nodai-amdgpu-mi308-x86-64` p95 queue 1h18m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h06m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h24m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
