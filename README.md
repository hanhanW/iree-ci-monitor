# iree-ci-monitor

_Updated: 2026-04-23 16:32 PDT_ — `iree-org/iree`, last 6h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 6h)

| label | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-w7900` | 23 | 15 | 5h35m | 0 | 0s | 2h21m | 0% (0/1) | 2 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | 23 | 12 | 4h41m | 0 | 0s | 2h03m | 0% (0/3) | 1 |
| `Linux,X64,iree-r9700` | 23 | 10 | 5h35m | 0 | 0s | 1h53m | 0% (0/4) | 1 |
| `Linux,X64,gfx1100` | 46 | 14 | 3h12m | 3 | 14m27s | 1h51m | 0% (0/8) | 3 |
| `Linux,X64,gfx1201` | 46 | 34 | 5h50m | 0 | 0s | 1h38m | 0% (0/2) | 1 |
| `Linux,X64,gfx1201,persistent-cache` | 23 | 12 | 5h11m | 2 | 0s | 1h31m | 0% (0/2) | 1 |
| `Linux,X64,iree-w7900x2,persistent-cache` | 23 | 12 | 5h50m | 0 | 0s | 1h27m | 60% (3/5) | 2 |
| `Linux,X64,rdna3` | 23 | 7 | 2h44m | 0 | 12m40s | 1h26m | 0% (0/6) | 3 |
| `self-hosted,persistent-cache,Linux,X64` | 50 | 12 | 2h44m | 4 | 13m17s | 1h17m | 0% (0/11) | 4 |
| `Linux,X64,gfx1100,persistent-cache` | 23 | 4 | 2h44m | 0 | 7m55s | 1h04m | 0% (0/7) | 3 |
| `Linux,X64,rdna3,shark10-ci` | 23 | 18 | 5h50m | 0 | 0s | 57m37s | — | 1 |
| `nodai-amdgpu-mi308-x86-64` | 23 | 2 | 2h35m | 2 | 5m21s | 23m31s | 0% (0/7) | 1 |
| `macos-14` | 78 | 3 | 2h41m | 5 | 1m31s | 9m09s | 0% (0/23) | 73 |
| `linux-mi325-1gpu-ossci-iree-org` | 92 | 3 | 2h35m | 2 | 9s | 8m49s | 9% (3/32) | 89 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | 42 | 34 | 5h50m | 1 | 0s | 8m06s | — | 2 |
| `windows-2022` | 75 | 0 | — | 7 | 24s | 4m35s | 4% (1/23) | 75 |
| `macos-15-intel` | 4 | 0 | — | 4 | 1m47s | 4m30s | — | 4 |
| `ubuntu-24.04` | 411 | 9 | 2h35m | 11 | 3s | 4m19s | 2% (2/121) | 395 |
| `ubuntu-24.04-arm` | 75 | 0 | — | 2 | 9s | 4m02s | 0% (0/24) | 75 |
| `ah-ubuntu_22_04-c7g_4x-50` | 3 | 0 | — | 1 | 1m59s | 2m10s | — | 3 |
| `azure-windows-scale` | 25 | 0 | — | 5 | 2s | 2m05s | 0% (0/6) | 25 |
| `ubuntu-latest` | 33 | 0 | — | 0 | 3s | 56s | 0% (0/16) | 33 |
| `azure-linux-scale` | 141 | 0 | — | 23 | 9s | 52s | 0% (0/41) | 141 |
| `linux-mi35x-1gpu-ossci-iree-org` | 23 | 0 | — | 1 | 1s | 2s | 25% (2/8) | 23 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 44 | 0% (0/42) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +2 more | 109 | 0% (0/106) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +5 more | 125 | 2% (3/122) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, +2 more | 133 | 2% (2/131) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +7 more | 143 | 15% (21/141) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job waiting 2h44m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 3h12m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 5h11m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 5h50m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 5h35m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 5h35m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 5h50m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 4h41m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 5h50m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job waiting 2h44m (> 2h00m)
- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job waiting 2h35m (> 2h00m)
- **[stale-queued]** `macos-14` oldest queued job waiting 2h41m (> 2h00m)
- **[stale-queued]** `nodai-amdgpu-mi308-x86-64` oldest queued job waiting 2h35m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 5h50m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 2h44m (> 2h00m)
- **[stale-queued]** `ubuntu-24.04` oldest queued job waiting 2h35m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h04m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h51m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h31m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h38m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h53m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h21m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h03m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h26m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h17m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds.
