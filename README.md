# iree-ci-monitor

_Updated: 2026-04-28 18:14 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 38 | 0 | — | 0 | [1h51m](https://github.com/iree-org/iree/actions/runs/25065529495/job/73432983706) | [4h11m](https://github.com/iree-org/iree/actions/runs/25074426402/job/73464132055) | 0% (0/11) | `shark01-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 36 | 1 | [9m06s](https://github.com/iree-org/iree/actions/runs/25085590895/job/73500942497) | 0 | [1h55m](https://github.com/iree-org/iree/actions/runs/25066373725/job/73436290717) | [4h06m](https://github.com/iree-org/iree/actions/runs/25070801494/job/73451698556) | 0% (0/10) | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 74 | 1 | [9m06s](https://github.com/iree-org/iree/actions/runs/25085590895/job/73500942544) | 1 | [2h04m](https://github.com/iree-org/iree/actions/runs/25068170987/job/73442784665) | [3h46m](https://github.com/iree-org/iree/actions/runs/25075177788/job/73466745248) | 0% (0/20) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 36 | 1 | [9m06s](https://github.com/iree-org/iree/actions/runs/25085590895/job/73500942619) | 0 | [1h51m](https://github.com/iree-org/iree/actions/runs/25068038997/job/73441823269) | [3h01m](https://github.com/iree-org/iree/actions/runs/25069152880/job/73445937932) | 0% (0/10) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 36 | 0 | — | 0 | [1h58m](https://github.com/iree-org/iree/actions/runs/25067774560/job/73440728201) | [3h00m](https://github.com/iree-org/iree/actions/runs/25077443208/job/73475103173) | 18% (2/11) | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 110 | 2 | [9m06s](https://github.com/iree-org/iree/actions/runs/25085590895/job/73500942606) | 0 | [1h35m](https://github.com/iree-org/iree/actions/runs/25075177788/job/73466745144) | [2h54m](https://github.com/iree-org/iree/actions/runs/25078103342/job/73477137789) | 0% (0/31) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 74 | 1 | [9m06s](https://github.com/iree-org/iree/actions/runs/25085590895/job/73500942591) | 1 | [1h40m](https://github.com/iree-org/iree/actions/runs/25073902574/job/73462776834) | [2h51m](https://github.com/iree-org/iree/actions/runs/25075545422/job/73469505121) | 5% (1/20) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 36 | 1 | [9m06s](https://github.com/iree-org/iree/actions/runs/25085590895/job/73500942425) | 0 | [1h48m](https://github.com/iree-org/iree/actions/runs/25068038997/job/73441822894) | [2h48m](https://github.com/iree-org/iree/actions/runs/25079278088/job/73481188754) | 20% (2/10) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 36 | 0 | — | 1 | [1h29m](https://github.com/iree-org/iree/actions/runs/25068038997/job/73441823243) | [2h47m](https://github.com/iree-org/iree/actions/runs/25069152880/job/73445937995) | 0% (0/10) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 36 | 1 | [9m06s](https://github.com/iree-org/iree/actions/runs/25085590895/job/73500942590) | 0 | [1h44m](https://github.com/iree-org/iree/actions/runs/25068038997/job/73441823197) | [2h41m](https://github.com/iree-org/iree/actions/runs/25075379724/job/73467653073) | 0% (0/10) | `shark01-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 36 | 0 | — | 1 | [7m09s](https://github.com/iree-org/iree/actions/runs/25059642220/job/73417592526) | [58m43s](https://github.com/iree-org/iree/actions/runs/25070641296/job/73450796936) | 0% (0/10) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 148 | 0 | — | 2 | [10s](https://github.com/iree-org/iree/actions/runs/25070441542/job/73450148634) | [6m01s](https://github.com/iree-org/iree/actions/runs/25069152880/job/73445937968) | 5% (2/42) | 148 |
| `ubuntu-24.04` | github-hosted | 646 | 0 | — | 3 | [4s](https://github.com/iree-org/iree/actions/runs/25063327979/job/73424951676) | [5m28s](https://github.com/iree-org/iree/actions/runs/25075177788/job/73466745279) | 6% (11/174) | 632 |
| `ubuntu-latest` | github-hosted | 73 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25070437715/job/73448955368) | [4m32s](https://github.com/iree-org/iree/actions/runs/25068946169/job/73443665256) | 0% (0/23) | 73 |
| `ubuntu-24.04-arm` | github-hosted | 108 | 0 | — | 0 | [24s](https://github.com/iree-org/iree/actions/runs/25065529541/job/73431600434) | [3m29s](https://github.com/iree-org/iree/actions/runs/25065841372/job/73432836790) | 0% (0/33) | 103 |
| `macos-14` | github-hosted | 110 | 0 | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/25063327925/job/73423458865) | [3m10s](https://github.com/iree-org/iree/actions/runs/25065356481/job/73430891299) | 3% (1/33) | 107 |
| `windows-2022` | github-hosted | 108 | 0 | — | 0 | [12s](https://github.com/iree-org/iree/actions/runs/25065356481/job/73430891317) | [3m09s](https://github.com/iree-org/iree/actions/runs/25069035476/job/73445612315) | 3% (1/33) | 102 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 2 | 0 | — | 0 | [1m25s](https://github.com/iree-org/iree/actions/runs/25070441619/job/73448995260) | [1m50s](https://github.com/iree-org/iree/actions/runs/25075379666/job/73466704577) | — | 2 |
| `azure-linux-scale` | ossci | 197 | 0 | — | 2 | [9s](https://github.com/iree-org/iree/actions/runs/25066373638/job/73434961878) | [53s](https://github.com/iree-org/iree/actions/runs/25068038972/job/73440448895) | 25% (16/65) | 197 |
| `macos-15-intel` | github-hosted | 2 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25075379666/job/73466704564) | [4s](https://github.com/iree-org/iree/actions/runs/25070441619/job/73448995184) | — | 2 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 36 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25066557925/job/73439328311) | [2s](https://github.com/iree-org/iree/actions/runs/25077443208/job/73475103063) | 18% (2/11) | 36 |
| `azure-windows-scale` | ossci | 36 | 0 | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/25075379666/job/73466704500) | [2s](https://github.com/iree-org/iree/actions/runs/25076879468/job/73471932494) | 40% (4/10) | 36 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 36 | 29 | [9h55m](https://github.com/iree-org/iree/actions/runs/25061098491/job/73416789752) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25070441542/job/73450148452) | [0s](https://github.com/iree-org/iree/actions/runs/25076879551/job/73472956429) | — | 0 |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 38 | 30 | [9h55m](https://github.com/iree-org/iree/actions/runs/25061098491/job/73416789855) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25070441542/job/73450148650) | [0s](https://github.com/iree-org/iree/actions/runs/25076879551/job/73472956455) | — | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 613 | 1% (9/608) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 651 | 3% (22/645) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 724 | 3% (25/719) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 197 | 1% (2/193) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 466 | 14% (63/462) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 9h55m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 9h55m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h47m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h51m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 3h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h46m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h48m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 3h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 4h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h41m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 4h11m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h54m (> 1h00m)
- **[high-failure-main]** `azure-linux-scale` main-branch failure rate 25% (16/65)
- **[high-failure-main]** `azure-windows-scale` main-branch failure rate 40% (4/10)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
