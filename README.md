# iree-ci-monitor

_Updated: 2026-04-23 16:07 PDT_ — `iree-org/iree`, last 6h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 6h)

| label | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64,threadripper` | 48 | 36 | 5h57m | 1 | 0s | 2h53m | — | 2 |
| `Linux,X64,iree-w7900` | 26 | 15 | 5h10m | 0 | 0s | 2h21m | 0% (0/1) | 2 |
| `Linux,X64,iree-r9700` | 26 | 10 | 5h10m | 0 | 0s | 2h17m | 0% (0/4) | 1 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | 26 | 12 | 4h16m | 0 | 0s | 2h03m | 0% (0/3) | 1 |
| `Linux,X64,gfx1100` | 52 | 14 | 2h47m | 3 | 17m11s | 1h51m | 0% (0/8) | 3 |
| `Linux,X64,gfx1201` | 52 | 35 | 5h57m | 0 | 0s | 1h38m | 0% (0/2) | 1 |
| `Linux,X64,rdna3,shark10-ci` | 26 | 19 | 5h57m | 0 | 0s | 1h32m | — | 1 |
| `Linux,X64,gfx1201,persistent-cache` | 26 | 12 | 4h47m | 2 | 0s | 1h31m | 0% (0/2) | 1 |
| `Linux,X64,iree-w7900x2,persistent-cache` | 26 | 12 | 5h26m | 0 | 0s | 1h27m | 60% (3/5) | 2 |
| `Linux,X64,rdna3` | 26 | 7 | 2h19m | 0 | 10m17s | 1h26m | 0% (0/6) | 3 |
| `self-hosted,persistent-cache,Linux,X64` | 56 | 12 | 2h19m | 4 | 13m17s | 1h14m | 0% (0/11) | 4 |
| `Linux,X64,gfx1100,persistent-cache` | 26 | 4 | 2h19m | 0 | 13m46s | 1h04m | 0% (0/7) | 3 |
| `nodai-amdgpu-mi308-x86-64` | 26 | 2 | 2h10m | 2 | 5m21s | 23m31s | 0% (0/7) | 1 |
| `macos-14` | 81 | 3 | 2h17m | 5 | 1m09s | 9m09s | 0% (0/23) | 76 |
| `linux-mi325-1gpu-ossci-iree-org` | 104 | 3 | 2h10m | 2 | 10s | 8m49s | 9% (3/32) | 101 |
| `ubuntu-24.04` | 440 | 9 | 2h10m | 11 | 3s | 4m47s | 2% (2/121) | 423 |
| `windows-2022` | 78 | 0 | — | 7 | 23s | 4m35s | 4% (1/23) | 78 |
| `macos-15-intel` | 4 | 0 | — | 4 | 1m47s | 4m30s | — | 4 |
| `ubuntu-24.04-arm` | 78 | 0 | — | 2 | 4s | 4m02s | 0% (0/24) | 78 |
| `ah-ubuntu_22_04-c7g_4x-50` | 3 | 0 | — | 1 | 1m59s | 2m10s | — | 3 |
| `azure-windows-scale` | 26 | 0 | — | 5 | 2s | 2m05s | 0% (0/6) | 26 |
| `ubuntu-latest` | 35 | 0 | — | 0 | 3s | 56s | 0% (0/16) | 35 |
| `azure-linux-scale` | 147 | 0 | — | 23 | 9s | 52s | 0% (0/41) | 147 |
| `linux-mi35x-1gpu-ossci-iree-org` | 26 | 0 | — | 1 | 1s | 2s | 25% (2/8) | 26 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 44 | 0% (0/42) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +2 more | 109 | 0% (0/106) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +5 more | 125 | 2% (3/122) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, +2 more | 133 | 2% (2/131) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +7 more | 143 | 15% (21/141) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job waiting 2h19m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 2h47m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 4h47m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 5h57m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 5h10m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 5h10m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 5h26m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 4h16m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 5h57m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job waiting 2h19m (> 2h00m)
- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job waiting 2h10m (> 2h00m)
- **[stale-queued]** `macos-14` oldest queued job waiting 2h17m (> 2h00m)
- **[stale-queued]** `nodai-amdgpu-mi308-x86-64` oldest queued job waiting 2h10m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 5h57m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 2h19m (> 2h00m)
- **[stale-queued]** `ubuntu-24.04` oldest queued job waiting 2h10m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h04m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h51m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h31m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h38m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h21m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h03m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h26m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h53m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h14m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds.
