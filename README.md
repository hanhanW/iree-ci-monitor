# iree-ci-monitor

_Updated: 2026-04-27 18:12 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 30 | 14 | [6h19m](https://github.com/iree-org/iree/actions/runs/25013235171/job/73255418958) | 0 | [2h20m](https://github.com/iree-org/iree/actions/runs/25015534965/job/73265248083) | [4h40m](https://github.com/iree-org/iree/actions/runs/25014018450/job/73258080349) | 0% (0/1) | `shark01-ci`, `shark10-ci-2` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 26 | 8 | [6h19m](https://github.com/iree-org/iree/actions/runs/25013235171/job/73255418847) | 0 | [2h23m](https://github.com/iree-org/iree/actions/runs/25018080083/job/73272808048) | [4h35m](https://github.com/iree-org/iree/actions/runs/25016293529/job/73265967404) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 53 | 29 | [6h19m](https://github.com/iree-org/iree/actions/runs/25013235171/job/73255418827) | 0 | [1h46m](https://github.com/iree-org/iree/actions/runs/25016293529/job/73265967469) | [4h29m](https://github.com/iree-org/iree/actions/runs/25015534965/job/73265248336) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 26 | 5 | [2h39m](https://github.com/iree-org/iree/actions/runs/25022814186/job/73288074455) | 0 | [1h37m](https://github.com/iree-org/iree/actions/runs/25016384733/job/73266788583) | [3h45m](https://github.com/iree-org/iree/actions/runs/25014018450/job/73258080041) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 26 | 10 | [6h45m](https://github.com/iree-org/iree/actions/runs/25012051815/job/73251250886) | 0 | [2h07m](https://github.com/iree-org/iree/actions/runs/25018003113/job/73271994882) | [3h20m](https://github.com/iree-org/iree/actions/runs/25013510002/job/73259548419) | — | `shark01-ci` |
| `Linux,X64,gfx1100` | self-hosted | 53 | 8 | [2h27m](https://github.com/iree-org/iree/actions/runs/25023134490/job/73289495852) | 0 | [1h39m](https://github.com/iree-org/iree/actions/runs/25022814186/job/73288074530) | [2h55m](https://github.com/iree-org/iree/actions/runs/25016293529/job/73265967524) | 0% (0/10) | `shark01-ci`, `shark10-ci-2`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 76 | 10 | [2h27m](https://github.com/iree-org/iree/actions/runs/25023134490/job/73289495865) | 1 | [1h25m](https://github.com/iree-org/iree/actions/runs/25013235171/job/73255418843) | [2h38m](https://github.com/iree-org/iree/actions/runs/25013510002/job/73259548767) | 0% (0/15) | `shark01-ci`, `shark10-ci-2`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 26 | 5 | [2h30m](https://github.com/iree-org/iree/actions/runs/25023118334/job/73289097189) | 1 | [1h25m](https://github.com/iree-org/iree/actions/runs/25013825927/job/73260314107) | [2h35m](https://github.com/iree-org/iree/actions/runs/25016384733/job/73266788547) | 0% (0/4) | `shark01-ci`, `shark10-ci-2` |
| `Linux,X64,rdna3` | self-hosted | 26 | 4 | [2h27m](https://github.com/iree-org/iree/actions/runs/25023134490/job/73289495884) | 0 | [40m07s](https://github.com/iree-org/iree/actions/runs/25015534965/job/73265248332) | [2h08m](https://github.com/iree-org/iree/actions/runs/25023118334/job/73289097246) | 0% (0/5) | `shark01-ci`, `shark10-ci-2`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 26 | 19 | [6h45m](https://github.com/iree-org/iree/actions/runs/25012051815/job/73251251025) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25018296091/job/73273067956) | [2h00m](https://github.com/iree-org/iree/actions/runs/25014018450/job/73258080198) | — | `shark10-ci-2` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 26 | 5 | [2h39m](https://github.com/iree-org/iree/actions/runs/25022814186/job/73288074549) | 1 | [34m11s](https://github.com/iree-org/iree/actions/runs/25015534965/job/73265248127) | [1h54m](https://github.com/iree-org/iree/actions/runs/25018080083/job/73272808021) | 0% (0/4) | `shark01-ci`, `shark10-ci-2`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 26 | 0 | — | 0 | [8m25s](https://github.com/iree-org/iree/actions/runs/25013235171/job/73255418869) | [33m10s](https://github.com/iree-org/iree/actions/runs/25018080083/job/73272808103) | 0% (0/7) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 106 | 0 | — | 0 | [17s](https://github.com/iree-org/iree/actions/runs/25013510002/job/73259548486) | [7m01s](https://github.com/iree-org/iree/actions/runs/25023134490/job/73289495816) | 7% (2/28) | 106 |
| `ubuntu-24.04` | github-hosted | 450 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25019281507/job/73276245218) | [4m12s](https://github.com/iree-org/iree/actions/runs/25016384733/job/73266788594) | 2% (2/105) | 441 |
| `windows-2022` | github-hosted | 81 | 0 | — | 0 | [1m18s](https://github.com/iree-org/iree/actions/runs/25014990466/job/73260466821) | [4m05s](https://github.com/iree-org/iree/actions/runs/25023118330/job/73288417025) | 0% (0/21) | 81 |
| `macos-14` | github-hosted | 82 | 0 | — | 0 | [20s](https://github.com/iree-org/iree/actions/runs/25014990466/job/73260466731) | [3m32s](https://github.com/iree-org/iree/actions/runs/25012003396/job/73250298062) | 0% (0/21) | 82 |
| `ubuntu-24.04-arm` | github-hosted | 81 | 0 | — | 0 | [30s](https://github.com/iree-org/iree/actions/runs/25022814198/job/73287169740) | [3m31s](https://github.com/iree-org/iree/actions/runs/25016464750/job/73265608121) | 0% (0/21) | 81 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m52s](https://github.com/iree-org/iree/actions/runs/25012003396/job/73250298239) | [1m52s](https://github.com/iree-org/iree/actions/runs/25012003396/job/73250298239) | — | 1 |
| `azure-linux-scale` | ossci | 147 | 0 | — | 4 | [8s](https://github.com/iree-org/iree/actions/runs/25022814198/job/73287169819) | [1m48s](https://github.com/iree-org/iree/actions/runs/25012003396/job/73250298276) | 5% (2/43) | 147 |
| `azure-windows-scale` | ossci | 27 | 0 | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/25023118330/job/73288417220) | [1m41s](https://github.com/iree-org/iree/actions/runs/25014018465/job/73256992337) | 0% (0/7) | 27 |
| `ubuntu-latest` | github-hosted | 37 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25018293703/job/73271875301) | [51s](https://github.com/iree-org/iree/actions/runs/25012002223/job/73249892500) | 0% (0/15) | 37 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/25012003396/job/73250298274) | [6s](https://github.com/iree-org/iree/actions/runs/25012003396/job/73250298274) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 26 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25016384733/job/73266788531) | [2s](https://github.com/iree-org/iree/actions/runs/25026229088/job/73298600637) | 43% (3/7) | 26 |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 27 | 23 | [6h45m](https://github.com/iree-org/iree/actions/runs/25012051815/job/73251251024) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25017068473/job/73273477403) | [0s](https://github.com/iree-org/iree/actions/runs/25018296091/job/73273068026) | — | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 386 | 1% (4/381) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 145 | 1% (1/142) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 467 | 2% (8/462) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 405 | 3% (13/399) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 461 | 14% (63/457) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job waiting 2h39m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 2h27m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 6h19m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 6h19m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 2h39m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 2h30m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 6h45m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 6h45m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 6h45m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job waiting 2h27m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 6h19m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 2h27m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h54m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h55m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 4h35m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 4h29m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h45m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h35m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 3h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h08m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 4h40m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h38m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
