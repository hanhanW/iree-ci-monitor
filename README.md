# iree-ci-monitor

_Updated: 2026-04-23 16:54 PDT_ — `iree-org/iree`, last 6h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 6h)

| label | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | 42 | 14 | [3h34m](https://github.com/iree-org/iree/actions/runs/24856591127/job/72771964649) | 3 | 11m48s | 1h51m | 0% (0/6) | 3 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | 21 | 12 | [5h03m](https://github.com/iree-org/iree/actions/runs/24852668845/job/72758160871) | 0 | 0s | 1h39m | 0% (0/2) | 1 |
| `Linux,X64,gfx1201` | 42 | 33 | [5h57m](https://github.com/iree-org/iree/actions/runs/24850230442/job/72749565192) | 0 | 0s | 1h36m | — | 1 |
| `Linux,X64,iree-r9700` | 21 | 10 | [5h57m](https://github.com/iree-org/iree/actions/runs/24850230442/job/72749564658) | 0 | 0s | 1h29m | 0% (0/3) | 1 |
| `Linux,X64,iree-w7900x2,persistent-cache` | 21 | 11 | [5h33m](https://github.com/iree-org/iree/actions/runs/24851251242/job/72753263288) | 0 | 0s | 1h27m | 50% (2/4) | 2 |
| `Linux,X64,gfx1201,persistent-cache` | 21 | 12 | [5h33m](https://github.com/iree-org/iree/actions/runs/24851251242/job/72753263438) | 2 | 0s | 1h27m | 0% (0/1) | 1 |
| `Linux,X64,rdna3` | 21 | 7 | [3h06m](https://github.com/iree-org/iree/actions/runs/24857340131/job/72776289234) | 0 | 10m17s | 1h23m | 0% (0/5) | 3 |
| `self-hosted,persistent-cache,Linux,X64` | 46 | 12 | [3h06m](https://github.com/iree-org/iree/actions/runs/24857340131/job/72776289129) | 4 | 13m17s | 1h17m | 0% (0/9) | 4 |
| `Linux,X64,gfx1100,persistent-cache` | 21 | 4 | [3h06m](https://github.com/iree-org/iree/actions/runs/24857340131/job/72776289145) | 0 | 7m55s | 59m18s | 0% (0/6) | 3 |
| `Linux,X64,iree-w7900` | 21 | 15 | [5h57m](https://github.com/iree-org/iree/actions/runs/24850230442/job/72749564690) | 0 | 0s | 51m40s | — | 2 |
| `nodai-amdgpu-mi308-x86-64` | 21 | 2 | [2h57m](https://github.com/iree-org/iree/actions/runs/24857352018/job/72777570910) | 2 | 2s | 21m15s | 0% (0/6) | 1 |
| `Linux,X64,rdna3,shark10-ci` | 21 | 17 | [5h57m](https://github.com/iree-org/iree/actions/runs/24850230442/job/72749565034) | 0 | 0s | 13m16s | — | 1 |
| `macos-14` | 63 | 3 | [3h03m](https://github.com/iree-org/iree/actions/runs/24858194429/job/72776647073) | 5 | 1m27s | 8m13s | 0% (0/20) | 58 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | 38 | 30 | [5h57m](https://github.com/iree-org/iree/actions/runs/24850230442/job/72749565049) | 1 | 0s | 8m06s | — | 2 |
| `linux-mi325-1gpu-ossci-iree-org` | 84 | 3 | [2h57m](https://github.com/iree-org/iree/actions/runs/24857352018/job/72777570816) | 2 | 9s | 5m45s | 11% (3/28) | 81 |
| `macos-15-intel` | 4 | 0 | — | 4 | 1m47s | 4m30s | — | 4 |
| `ubuntu-24.04-arm` | 60 | 0 | — | 2 | 3s | 4m02s | 0% (0/21) | 60 |
| `windows-2022` | 60 | 0 | — | 7 | 28s | 3m54s | 5% (1/20) | 60 |
| `ubuntu-latest` | 27 | 0 | — | 0 | 3s | 3m04s | 0% (0/14) | 27 |
| `ubuntu-24.04` | 358 | 9 | [2h57m](https://github.com/iree-org/iree/actions/runs/24857352018/job/72777570689) | 11 | 3s | 2m37s | 2% (2/107) | 342 |
| `ah-ubuntu_22_04-c7g_4x-50` | 3 | 0 | — | 1 | 1m59s | 2m10s | — | 3 |
| `azure-windows-scale` | 20 | 0 | — | 5 | 1s | 2m05s | 0% (0/5) | 20 |
| `azure-linux-scale` | 115 | 0 | — | 23 | 9s | 36s | 0% (0/35) | 115 |
| `linux-mi35x-1gpu-ossci-iree-org` | 21 | 0 | — | 1 | 1s | 2s | 29% (2/7) | 21 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 44 | 0% (0/42) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +2 more | 109 | 0% (0/106) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +5 more | 125 | 2% (3/122) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, +2 more | 133 | 2% (2/131) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +7 more | 143 | 15% (21/141) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job waiting 3h06m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 3h34m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 5h33m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 5h57m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 5h57m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 5h57m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 5h33m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 5h03m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 5h57m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job waiting 3h06m (> 2h00m)
- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job waiting 2h57m (> 2h00m)
- **[stale-queued]** `macos-14` oldest queued job waiting 3h03m (> 2h00m)
- **[stale-queued]** `nodai-amdgpu-mi308-x86-64` oldest queued job waiting 2h57m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 5h57m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 3h06m (> 2h00m)
- **[stale-queued]** `ubuntu-24.04` oldest queued job waiting 2h57m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h51m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h36m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h29m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h39m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h23m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h17m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds.
