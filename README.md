# iree-ci-monitor

_Updated: 2026-04-25 05:32 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | 0 | [45m12s](https://github.com/iree-org/iree/actions/runs/24923453747/job/72989537487) | [1h57m](https://github.com/iree-org/iree/actions/runs/24923453747/job/72989537462) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | 0 | [1h10m](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091803) | [1h43m](https://github.com/iree-org/iree/actions/runs/24923453747/job/72989537395) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | 0 | [1h02m](https://github.com/iree-org/iree/actions/runs/24923453747/job/72989537457) | [1h32m](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091880) | — | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 2 | 0 | — | 0 | [14m02s](https://github.com/iree-org/iree/actions/runs/24923453747/job/72989537481) | [1h04m](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091879) | — | `shark10-ci-2` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24923453747/job/72989537405) | [30m33s](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091897) | — | `shark10-ci-2` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091840) | [26m46s](https://github.com/iree-org/iree/actions/runs/24923453747/job/72989537454) | — | `shark01-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | 0 | [9m20s](https://github.com/iree-org/iree/actions/runs/24923453747/job/72989537476) | [25m46s](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091889) | — | `shark10-ci-2` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | 0 | [6m09s](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091914) | [24m35s](https://github.com/iree-org/iree/actions/runs/24923453747/job/72989537467) | — | `shark10-ci-2` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | 0 | [16m59s](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091874) | [23m08s](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091892) | — | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091893) | [22m13s](https://github.com/iree-org/iree/actions/runs/24923453747/job/72989537485) | — | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | 0 | [5m32s](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091793) | [18m37s](https://github.com/iree-org/iree/actions/runs/24923453747/job/72989537406) | — | `shark01-ci`, `shark10-ci-2` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | 0 | [4m18s](https://github.com/iree-org/iree/actions/runs/24923453747/job/72989537456) | [15m37s](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091886) | — | `shark10-ci-2` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | 0 | [19s](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091869) | [3m01s](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091898) | — | 8 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 2 | 0 | — | 0 | [2m19s](https://github.com/iree-org/iree/actions/runs/24921510131/job/72983829269) | [2m41s](https://github.com/iree-org/iree/actions/runs/24923453737/job/72989229732) | — | 2 |
| `azure-linux-scale` | ossci | 14 | 0 | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/24923453737/job/72989229752) | [2m32s](https://github.com/iree-org/iree/actions/runs/24921510131/job/72983829263) | — | 14 |
| `macos-14` | github-hosted | 10 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24923801476/job/72990117407) | [13s](https://github.com/iree-org/iree/actions/runs/24921510131/job/72983829268) | — | 10 |
| `ubuntu-24.04` | github-hosted | 70 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24921510131/job/72983829231) | [3s](https://github.com/iree-org/iree/actions/runs/24921510105/job/72983793911) | 38% (3/8) | 69 |
| `windows-2022` | github-hosted | 8 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24923453737/job/72989229746) | [3s](https://github.com/iree-org/iree/actions/runs/24921510131/job/72983829203) | — | 8 |
| `macos-15-intel` | github-hosted | 2 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/24921510131/job/72983829260) | [3s](https://github.com/iree-org/iree/actions/runs/24923453737/job/72989229772) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24921510131/job/72983829204) | [2s](https://github.com/iree-org/iree/actions/runs/24923801476/job/72990117406) | — | 9 |
| `ubuntu-latest` | github-hosted | 4 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24923452666/job/72989167262) | [2s](https://github.com/iree-org/iree/actions/runs/24923452666/job/72989167266) | — | 4 |
| `azure-windows-scale` | ossci | 2 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24921510131/job/72983829272) | [1s](https://github.com/iree-org/iree/actions/runs/24923453737/job/72989229765) | — | 2 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 2 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091800) | [1s](https://github.com/iree-org/iree/actions/runs/24923453747/job/72989537398) | — | 2 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24921510143/job/72984091885) | [1s](https://github.com/iree-org/iree/actions/runs/24923453747/job/72989537442) | — | `iree-mi308-1` |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 369 | 2% (6/365) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 397 | 14% (55/393) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 308 | 3% (8/303) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 293 | 0% (0/289) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 112 | 0% (0/109) | yes | running |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h57m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h43m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h04m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
