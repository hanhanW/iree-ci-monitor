# iree-ci-monitor

_Updated: 2026-04-23T22:30Z_ — `iree-org/iree`, last 6h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 2h09m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 4h09m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 5h20m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 4h33m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 4h33m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 4h48m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 3h39m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 5h20m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 5h20m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h04m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h51m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h31m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h39m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h21m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h03m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h26m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h53m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h17m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

## Top of queue (sorted by p95, last 6h)

| label | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64,threadripper` | 43 | 31 | 5h20m | 1 | 0s | 2h53m | — | 2 |
| `Linux,X64,iree-w7900` | 22 | 11 | 4h33m | 0 | 0s | 2h21m | 0% (0/1) | 2 |
| `Linux,X64,iree-r9700` | 22 | 7 | 4h33m | 0 | 12m36s | 2h17m | 0% (0/4) | 1 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | 22 | 8 | 3h39m | 0 | 0s | 2h03m | 0% (0/3) | 1 |
| `Linux,X64,gfx1100` | 44 | 9 | 2h09m | 2 | 22m33s | 1h51m | 0% (0/7) | 3 |
| `Linux,X64,gfx1201` | 44 | 27 | 5h20m | 0 | 0s | 1h39m | 0% (0/2) | 1 |
| `Linux,X64,rdna3,shark10-ci` | 22 | 15 | 5h20m | 0 | 0s | 1h32m | — | 1 |
| `Linux,X64,gfx1201,persistent-cache` | 22 | 9 | 4h09m | 1 | 0s | 1h31m | 0% (0/2) | 1 |
| `Linux,X64,iree-w7900x2,persistent-cache` | 22 | 8 | 4h48m | 0 | 5m00s | 1h27m | 60% (3/5) | 2 |
| `Linux,X64,rdna3` | 22 | 3 | 1h42m | 0 | 15m20s | 1h26m | 0% (0/6) | 3 |
| `self-hosted,persistent-cache,Linux,X64` | 45 | 6 | 1h42m | 3 | 16m28s | 1h17m | 0% (0/9) | 4 |
| `Linux,X64,gfx1100,persistent-cache` | 22 | 2 | 1h42m | 0 | 20m33s | 1h04m | 0% (0/6) | 3 |
| `nodai-amdgpu-mi308-x86-64` | 22 | 1 | 1h33m | 1 | 5m21s | 23m31s | 0% (0/6) | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | 88 | 3 | 1h33m | 2 | 9s | 9m10s | 12% (3/24) | 85 |
| `macos-14` | 91 | 3 | 1h39m | 5 | 1m08s | 9m09s | 0% (0/23) | 86 |
| `windows-2022` | 87 | 0 | — | 7 | 30s | 4m35s | 4% (1/23) | 87 |
| `ubuntu-24.04` | 436 | 9 | 1h33m | 9 | 3s | 4m34s | 1% (1/104) | 419 |
| `macos-15-intel` | 5 | 0 | — | 4 | 14s | 4m30s | — | 5 |
| `ubuntu-24.04-arm` | 87 | 0 | — | 2 | 9s | 3m59s | 0% (0/24) | 87 |
| `ah-ubuntu_22_04-c7g_4x-50` | 4 | 0 | — | 1 | 1m59s | 2m10s | — | 4 |
| `azure-windows-scale` | 29 | 0 | — | 4 | 2s | 2m05s | 0% (0/6) | 29 |
| `ubuntu-latest` | 39 | 0 | — | 0 | 3s | 56s | 0% (0/16) | 39 |
| `azure-linux-scale` | 164 | 0 | — | 19 | 9s | 52s | 0% (0/41) | 164 |
| `linux-mi35x-1gpu-ossci-iree-org` | 22 | 0 | — | 1 | 2s | 2s | 33% (2/6) | 22 |

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds.
