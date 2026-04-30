# iree-ci-monitor

_Updated: 2026-04-30 00:13 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 10 | 1 | [9h27m](https://github.com/iree-org/iree/actions/runs/25135228671/job/73672888468) | 0 | [11m43s](https://github.com/iree-org/iree/actions/runs/25144674733/job/73702428537) | [4h26m](https://github.com/iree-org/iree/actions/runs/25135122040/job/73672525358) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 10 | 1 | [9h27m](https://github.com/iree-org/iree/actions/runs/25135228671/job/73672888433) | 0 | [6m42s](https://github.com/iree-org/iree/actions/runs/25149748717/job/73719652529) | [4h09m](https://github.com/iree-org/iree/actions/runs/25135122040/job/73672525213) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 10 | 0 | — | 1 | [19m02s](https://github.com/iree-org/iree/actions/runs/25149748717/job/73719652619) | [3h54m](https://github.com/iree-org/iree/actions/runs/25135122040/job/73672525308) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 10 | 1 | [9h27m](https://github.com/iree-org/iree/actions/runs/25135228671/job/73672888315) | 0 | [17m16s](https://github.com/iree-org/iree/actions/runs/25148831047/job/73715160468) | [3h34m](https://github.com/iree-org/iree/actions/runs/25135122040/job/73672525181) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 10 | 1 | [9h27m](https://github.com/iree-org/iree/actions/runs/25135228671/job/73672888355) | 0 | [18m09s](https://github.com/iree-org/iree/actions/runs/25150066715/job/73722186145) | [3h26m](https://github.com/iree-org/iree/actions/runs/25135122040/job/73672525330) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 0 | — | 0 | [19m39s](https://github.com/iree-org/iree/actions/runs/25150066715/job/73722186141) | [3h22m](https://github.com/iree-org/iree/actions/runs/25135122040/job/73672525322) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 10 | 0 | — | 0 | [9m26s](https://github.com/iree-org/iree/actions/runs/25148831047/job/73715160644) | [3h17m](https://github.com/iree-org/iree/actions/runs/25135228671/job/73672888366) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 30 | 3 | [9h27m](https://github.com/iree-org/iree/actions/runs/25135228671/job/73672888382) | 0 | [9m42s](https://github.com/iree-org/iree/actions/runs/25149748717/job/73719652750) | [3h17m](https://github.com/iree-org/iree/actions/runs/25135122040/job/73672525340) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 20 | 2 | [9h27m](https://github.com/iree-org/iree/actions/runs/25135228671/job/73672888410) | 0 | [8m22s](https://github.com/iree-org/iree/actions/runs/25149748717/job/73719652788) | [3h07m](https://github.com/iree-org/iree/actions/runs/25135122040/job/73672525324) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 10 | 1 | [9h27m](https://github.com/iree-org/iree/actions/runs/25135228671/job/73672888339) | 0 | [21m24s](https://github.com/iree-org/iree/actions/runs/25150066715/job/73722186219) | [2h00m](https://github.com/iree-org/iree/actions/runs/25135228671/job/73701455253) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 10 | 1 | [9h27m](https://github.com/iree-org/iree/actions/runs/25135228671/job/73672888478) | 1 | [22m19s](https://github.com/iree-org/iree/actions/runs/25149748717/job/73719652760) | [1h51m](https://github.com/iree-org/iree/actions/runs/25135228671/job/73701455379) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 20 | 2 | [9h27m](https://github.com/iree-org/iree/actions/runs/25135228671/job/73672888371) | 1 | [24m33s](https://github.com/iree-org/iree/actions/runs/25150066715/job/73722186161) | [46m07s](https://github.com/iree-org/iree/actions/runs/25144674733/job/73702428564) | 0% (0/4) | `shark75-ci` |
| `azure-linux-scale` | ossci | 48 | 0 | — | 0 | [16s](https://github.com/iree-org/iree/actions/runs/25135122079/job/73671841462) | [29m08s](https://github.com/iree-org/iree/actions/runs/25150066713/job/73718428287) | 0% (0/12) | 47 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 10 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25149748717/job/73719652632) | [10m21s](https://github.com/iree-org/iree/actions/runs/25135228671/job/73672888434) | 0% (0/2) | `iree-mi308-1` |
| `windows-2022` | github-hosted | 29 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25148429599/job/73713191807) | [2m26s](https://github.com/iree-org/iree/actions/runs/25135122079/job/73671841352) | 0% (0/6) | 29 |
| `macos-14` | github-hosted | 29 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25144674738/job/73701821149) | [1m36s](https://github.com/iree-org/iree/actions/runs/25135122079/job/73671841336) | 0% (0/6) | 29 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 40 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25135122040/job/73672525306) | [19s](https://github.com/iree-org/iree/actions/runs/25134610450/job/73670708546) | 0% (0/8) | 38 |
| `ubuntu-24.04` | github-hosted | 194 | 0 | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/25148831047/job/73715160567) | [9s](https://github.com/iree-org/iree/actions/runs/25149748732/job/73721451689) | 12% (5/43) | 185 |
| `ubuntu-latest` | github-hosted | 8 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25150064340/job/73718405837) | [8s](https://github.com/iree-org/iree/actions/runs/25150064340/job/73718405847) | 0% (0/4) | 8 |
| `ubuntu-24.04-arm` | github-hosted | 30 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25149748732/job/73717422439) | [5s](https://github.com/iree-org/iree/actions/runs/25135122079/job/73671841268) | 0% (0/6) | 30 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 10 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25120992881/job/73721338067) | [3s](https://github.com/iree-org/iree/actions/runs/25149748717/job/73719652524) | 50% (1/2) | 9 |
| `azure-windows-scale` | ossci | 9 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25149748732/job/73717422479) | [2s](https://github.com/iree-org/iree/actions/runs/25135122079/job/73671841461) | 0% (0/2) | 9 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 266 | 7% (19/265) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 975 | 6% (54/970) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 869 | 3% (25/863) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 801 | 1% (10/797) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 253 | 1% (2/250) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 459 | 14% (62/455) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 9h27m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 9h27m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 9h27m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 9h27m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 9h27m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 9h27m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 9h27m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 9h27m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 9h27m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 3h22m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 3h07m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 3h26m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 4h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 3h34m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 3h54m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h51m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 3h17m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 4h26m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 3h17m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
