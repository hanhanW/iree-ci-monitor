# iree-ci-monitor

_Updated: 2026-04-28 19:24 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 36 | 1 | [12m05s](https://github.com/iree-org/iree/actions/runs/25087370054/job/73506252922) | 0 | [2h02m](https://github.com/iree-org/iree/actions/runs/25068496728/job/73443812782) | [4h11m](https://github.com/iree-org/iree/actions/runs/25074426402/job/73464132055) | 0% (0/10) | `shark01-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 34 | 1 | [12m05s](https://github.com/iree-org/iree/actions/runs/25087370054/job/73506252896) | 0 | [1h55m](https://github.com/iree-org/iree/actions/runs/25066373725/job/73436290717) | [4h06m](https://github.com/iree-org/iree/actions/runs/25070801494/job/73451698556) | 0% (0/10) | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 70 | 1 | [12m05s](https://github.com/iree-org/iree/actions/runs/25087370054/job/73506252967) | 1 | [2h12m](https://github.com/iree-org/iree/actions/runs/25069059840/job/73444069473) | [3h47m](https://github.com/iree-org/iree/actions/runs/25075545422/job/73469505087) | 0% (0/20) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 34 | 0 | — | 0 | [1h51m](https://github.com/iree-org/iree/actions/runs/25068038997/job/73441823269) | [3h01m](https://github.com/iree-org/iree/actions/runs/25069152880/job/73445937932) | 0% (0/10) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 34 | 1 | [12m05s](https://github.com/iree-org/iree/actions/runs/25087370054/job/73506252838) | 0 | [1h59m](https://github.com/iree-org/iree/actions/runs/25080899185/job/73486449497) | [3h00m](https://github.com/iree-org/iree/actions/runs/25077443208/job/73475103173) | 20% (2/10) | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 104 | 0 | — | 2 | [1h36m](https://github.com/iree-org/iree/actions/runs/25073902574/job/73462776836) | [2h54m](https://github.com/iree-org/iree/actions/runs/25078103342/job/73477137789) | 0% (0/30) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 70 | 0 | — | 1 | [1h40m](https://github.com/iree-org/iree/actions/runs/25074426402/job/73464132106) | [2h52m](https://github.com/iree-org/iree/actions/runs/25069152880/job/73445937998) | 5% (1/20) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 34 | 0 | — | 0 | [1h48m](https://github.com/iree-org/iree/actions/runs/25068038997/job/73441822894) | [2h48m](https://github.com/iree-org/iree/actions/runs/25079278088/job/73481188754) | 20% (2/10) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 34 | 0 | — | 0 | [1h29m](https://github.com/iree-org/iree/actions/runs/25068038997/job/73441823243) | [2h47m](https://github.com/iree-org/iree/actions/runs/25069152880/job/73445937995) | 0% (0/10) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 34 | 0 | — | 0 | [1h44m](https://github.com/iree-org/iree/actions/runs/25068038997/job/73441823197) | [2h41m](https://github.com/iree-org/iree/actions/runs/25075379724/job/73467653073) | 0% (0/10) | `shark01-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 34 | 0 | — | 1 | [3m55s](https://github.com/iree-org/iree/actions/runs/25067774560/job/73440728245) | [58m43s](https://github.com/iree-org/iree/actions/runs/25070641296/job/73450796936) | 0% (0/10) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 140 | 0 | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25077443208/job/73475103211) | [6m01s](https://github.com/iree-org/iree/actions/runs/25069152880/job/73445937968) | 5% (2/40) | 140 |
| `ubuntu-24.04` | github-hosted | 672 | 0 | — | 8 | [3s](https://github.com/iree-org/iree/actions/runs/25078103329/job/73476064842) | [5m18s](https://github.com/iree-org/iree/actions/runs/25075545448/job/73467690664) | 7% (11/161) | 658 |
| `ubuntu-latest` | github-hosted | 81 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25077441608/job/73473732390) | [4m32s](https://github.com/iree-org/iree/actions/runs/25068946169/job/73443665256) | 0% (0/21) | 81 |
| `macos-15-intel` | github-hosted | 4 | 0 | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/25087722646/job/73506889957) | [4m22s](https://github.com/iree-org/iree/actions/runs/25085978240/job/73501540005) | — | 4 |
| `macos-14` | github-hosted | 124 | 0 | — | 4 | [4s](https://github.com/iree-org/iree/actions/runs/25077443207/job/73473770897) | [3m07s](https://github.com/iree-org/iree/actions/runs/25065356481/job/73430891358) | 3% (1/30) | 121 |
| `windows-2022` | github-hosted | 120 | 0 | — | 3 | [9s](https://github.com/iree-org/iree/actions/runs/25070441619/job/73448994943) | [3m07s](https://github.com/iree-org/iree/actions/runs/25076248571/job/73469567383) | 3% (1/30) | 114 |
| `ubuntu-24.04-arm` | github-hosted | 120 | 0 | — | 3 | [4s](https://github.com/iree-org/iree/actions/runs/25077443207/job/73473771154) | [3m07s](https://github.com/iree-org/iree/actions/runs/25070801600/job/73450355436) | 0% (0/30) | 115 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 4 | 1 | [3m32s](https://github.com/iree-org/iree/actions/runs/25087722646/job/73506889916) | 0 | [1m35s](https://github.com/iree-org/iree/actions/runs/25085978240/job/73501539902) | [1m50s](https://github.com/iree-org/iree/actions/runs/25075379666/job/73466704577) | — | 3 |
| `azure-linux-scale` | ossci | 219 | 0 | — | 8 | [9s](https://github.com/iree-org/iree/actions/runs/25066373638/job/73434961878) | [46s](https://github.com/iree-org/iree/actions/runs/25075545448/job/73467690693) | 26% (16/61) | 219 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 34 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25066373725/job/73436290644) | [2s](https://github.com/iree-org/iree/actions/runs/25076879551/job/73472956373) | 20% (2/10) | 34 |
| `azure-windows-scale` | ossci | 40 | 0 | — | 2 | [1s](https://github.com/iree-org/iree/actions/runs/25076248571/job/73469567377) | [2s](https://github.com/iree-org/iree/actions/runs/25076879468/job/73471932494) | 40% (4/10) | 40 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 34 | 25 | [9h49m](https://github.com/iree-org/iree/actions/runs/25065007783/job/73430853160) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25070641296/job/73450796830) | [0s](https://github.com/iree-org/iree/actions/runs/25085978245/job/73502095752) | — | 0 |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 36 | 26 | [9h49m](https://github.com/iree-org/iree/actions/runs/25065007783/job/73430853080) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25070441542/job/73450148650) | [0s](https://github.com/iree-org/iree/actions/runs/25085978245/job/73502095865) | — | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 622 | 2% (10/617) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 736 | 4% (27/731) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 660 | 3% (22/654) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 199 | 1% (2/195) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 466 | 14% (63/462) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 9h49m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 9h49m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h47m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h52m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 3h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h47m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h48m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 3h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 4h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h41m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 4h11m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h54m (> 1h00m)
- **[high-failure-main]** `azure-linux-scale` main-branch failure rate 26% (16/61)
- **[high-failure-main]** `azure-windows-scale` main-branch failure rate 40% (4/10)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
