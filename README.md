# iree-ci-monitor

_Updated: 2026-04-28 11:55 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 55 | 27 | [1h29m](https://github.com/iree-org/iree/actions/runs/25066557925/job/73439328419) | 1 | [1h00m](https://github.com/iree-org/iree/actions/runs/25061206090/job/73420571606) | [2h01m](https://github.com/iree-org/iree/actions/runs/25065529495/job/73432983818) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 26 | 13 | [1h47m](https://github.com/iree-org/iree/actions/runs/25066373725/job/73436290717) | 0 | [1h20m](https://github.com/iree-org/iree/actions/runs/25066557925/job/73439328367) | [1h55m](https://github.com/iree-org/iree/actions/runs/25059642220/job/73417592555) | 0% (0/5) | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 29 | 14 | [1h29m](https://github.com/iree-org/iree/actions/runs/25066557925/job/73439328413) | 0 | [57m19s](https://github.com/iree-org/iree/actions/runs/25059794993/job/73412014075) | [1h50m](https://github.com/iree-org/iree/actions/runs/25065356772/job/73432108027) | 0% (0/4) | `shark01-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 26 | 13 | [1h29m](https://github.com/iree-org/iree/actions/runs/25066557925/job/73439328372) | 0 | [1h00m](https://github.com/iree-org/iree/actions/runs/25065356772/job/73432107815) | [1h33m](https://github.com/iree-org/iree/actions/runs/25061206090/job/73420571563) | 0% (0/4) | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 26 | 14 | [1h47m](https://github.com/iree-org/iree/actions/runs/25066373725/job/73436290762) | 0 | [1h00m](https://github.com/iree-org/iree/actions/runs/25063327979/job/73424951796) | [1h28m](https://github.com/iree-org/iree/actions/runs/25065840917/job/73434370049) | 0% (0/4) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 81 | 36 | [1h21m](https://github.com/iree-org/iree/actions/runs/25067774560/job/73440728188) | 1 | [53m21s](https://github.com/iree-org/iree/actions/runs/25065356772/job/73432107991) | [1h25m](https://github.com/iree-org/iree/actions/runs/25066373725/job/73436290761) | 0% (0/15) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 26 | 12 | [1h21m](https://github.com/iree-org/iree/actions/runs/25067774560/job/73440728323) | 0 | [51m33s](https://github.com/iree-org/iree/actions/runs/25059642220/job/73417592427) | [1h22m](https://github.com/iree-org/iree/actions/runs/25065840917/job/73434370056) | 0% (0/5) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 55 | 25 | [1h21m](https://github.com/iree-org/iree/actions/runs/25067774560/job/73440728190) | 1 | [47m02s](https://github.com/iree-org/iree/actions/runs/25059688262/job/73411724584) | [1h21m](https://github.com/iree-org/iree/actions/runs/25066557925/job/73439328505) | 0% (0/9) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 26 | 12 | [1h47m](https://github.com/iree-org/iree/actions/runs/25066373725/job/73436290656) | 0 | [41m06s](https://github.com/iree-org/iree/actions/runs/25067774560/job/73440728244) | [1h21m](https://github.com/iree-org/iree/actions/runs/25065529495/job/73432983531) | 20% (1/5) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 26 | 12 | [1h21m](https://github.com/iree-org/iree/actions/runs/25067774560/job/73440728375) | 0 | [45m44s](https://github.com/iree-org/iree/actions/runs/25065007783/job/73430853516) | [1h19m](https://github.com/iree-org/iree/actions/runs/25066557925/job/73439328384) | 0% (0/5) | `shark01-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 26 | 5 | [49m12s](https://github.com/iree-org/iree/actions/runs/25069152880/job/73445937914) | 1 | [7m09s](https://github.com/iree-org/iree/actions/runs/25059642220/job/73417592526) | [33m41s](https://github.com/iree-org/iree/actions/runs/25068679996/job/73444430638) | 0% (0/7) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 110 | 0 | — | 1 | [20s](https://github.com/iree-org/iree/actions/runs/25059688262/job/73411724752) | [7m23s](https://github.com/iree-org/iree/actions/runs/25059794993/job/73412013983) | 0% (0/40) | 110 |
| `ubuntu-24.04` | github-hosted | 465 | 0 | — | 4 | [10s](https://github.com/iree-org/iree/actions/runs/25063327979/job/73424951745) | [6m00s](https://github.com/iree-org/iree/actions/runs/25069152880/job/73445937926) | 3% (5/158) | 457 |
| `ubuntu-latest` | github-hosted | 73 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25070437715/job/73448955368) | [4m32s](https://github.com/iree-org/iree/actions/runs/25068946169/job/73443665256) | 0% (0/20) | 73 |
| `macos-14` | github-hosted | 86 | 0 | — | 1 | [9s](https://github.com/iree-org/iree/actions/runs/25061098434/job/73415187934) | [3m16s](https://github.com/iree-org/iree/actions/runs/25069035476/job/73445612324) | 3% (1/31) | 83 |
| `ubuntu-24.04-arm` | github-hosted | 84 | 0 | — | 0 | [27s](https://github.com/iree-org/iree/actions/runs/25068038972/job/73440448740) | [3m07s](https://github.com/iree-org/iree/actions/runs/25070801600/job/73450355436) | 0% (0/30) | 79 |
| `windows-2022` | github-hosted | 84 | 0 | — | 0 | [20s](https://github.com/iree-org/iree/actions/runs/25065529541/job/73431600318) | [2m54s](https://github.com/iree-org/iree/actions/runs/25068170751/job/73441572432) | 3% (1/30) | 78 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 2 | 0 | — | 1 | [1m25s](https://github.com/iree-org/iree/actions/runs/25070441619/job/73448995260) | [1m41s](https://github.com/iree-org/iree/actions/runs/25046449719/job/73362674548) | 0% (0/1) | 2 |
| `azure-linux-scale` | ossci | 157 | 0 | — | 3 | [9s](https://github.com/iree-org/iree/actions/runs/25067774504/job/73439514539) | [1m27s](https://github.com/iree-org/iree/actions/runs/25068038972/job/73440448932) | 24% (15/62) | 157 |
| `azure-windows-scale` | ossci | 28 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25054099963/job/73389514564) | [1m24s](https://github.com/iree-org/iree/actions/runs/25059794862/job/73410518952) | 40% (4/10) | 28 |
| `macos-15-intel` | github-hosted | 2 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25046431930/job/73362613190) | [4s](https://github.com/iree-org/iree/actions/runs/25070441619/job/73448995184) | 0% (0/1) | 2 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 26 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25065007783/job/73430853205) | [2s](https://github.com/iree-org/iree/actions/runs/25070801494/job/73451698271) | 10% (1/10) | 26 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 26 | 25 | [5h48m](https://github.com/iree-org/iree/actions/runs/25054099930/job/73391238519) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25065491548/job/73433099189) | [0s](https://github.com/iree-org/iree/actions/runs/25065491548/job/73433099189) | — | 0 |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 29 | 26 | [5h48m](https://github.com/iree-org/iree/actions/runs/25054099930/job/73391238540) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25054878408/job/73392268628) | [0s](https://github.com/iree-org/iree/actions/runs/25065491548/job/73433099487) | — | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 521 | 1% (7/516) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 626 | 2% (15/621) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 555 | 3% (16/549) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 180 | 1% (1/176) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 466 | 14% (63/462) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 5h48m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 5h48m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h22m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h21m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h28m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h21m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h33m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h55m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h19m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h50m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h25m (> 1h00m)
- **[high-failure-main]** `azure-linux-scale` main-branch failure rate 24% (15/62)
- **[high-failure-main]** `azure-windows-scale` main-branch failure rate 40% (4/10)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
