# iree-ci-monitor

_Updated: 2026-04-23T21:08Z_ — `iree-org/iree`, last 6h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 2h47m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 3h58m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 3h11m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 3h11m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 3h26m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 2h17m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 3h58m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 3h58m (> 2h00m)
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
| `self-hosted,persistent-cache,Linux,X64,threadripper` | 43 | 25 | 3h58m | 1 | 0s | 2h53m | 0% (0/2) | 2 |
| `Linux,X64,iree-w7900` | 22 | 8 | 3h11m | 0 | 2s | 2h21m | 0% (0/2) | 2 |
| `Linux,X64,iree-r9700` | 22 | 4 | 3h11m | 0 | 32m24s | 2h17m | 0% (0/5) | 1 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | 22 | 5 | 2h17m | 0 | 15m34s | 2h03m | 0% (0/4) | 1 |
| `Linux,X64,gfx1100` | 44 | 5 | 47m57s | 1 | 25m39s | 1h51m | 0% (0/8) | 3 |
| `Linux,X64,gfx1201` | 44 | 21 | 3h58m | 0 | 0s | 1h39m | 0% (0/4) | 1 |
| `Linux,X64,rdna3,shark10-ci` | 22 | 12 | 3h58m | 0 | 0s | 1h32m | 0% (0/1) | 1 |
| `Linux,X64,gfx1201,persistent-cache` | 22 | 6 | 2h47m | 1 | 17m22s | 1h31m | 0% (0/3) | 1 |
| `Linux,X64,iree-w7900x2,persistent-cache` | 22 | 6 | 3h26m | 0 | 5m00s | 1h27m | 60% (3/5) | 2 |
| `Linux,X64,rdna3` | 22 | 2 | 20m08s | 0 | 29m52s | 1h26m | 0% (0/5) | 3 |
| `self-hosted,persistent-cache,Linux,X64` | 45 | 3 | 20m08s | 1 | 13m37s | 1h17m | 0% (0/10) | 4 |
| `Linux,X64,gfx1100,persistent-cache` | 22 | 2 | 20m08s | 0 | 20m47s | 1h04m | 0% (0/5) | 3 |
| `nodai-amdgpu-mi308-x86-64` | 22 | 1 | 11m39s | 1 | 5m21s | 23m31s | 0% (0/5) | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | 88 | 3 | 11m39s | 2 | 10s | 9m10s | 15% (3/20) | 85 |
| `macos-14` | 87 | 1 | 17m48s | 3 | 47s | 7m23s | 0% (0/15) | 84 |
| `ubuntu-24.04` | 428 | 9 | 11m39s | 6 | 3s | 4m47s | 1% (1/78) | 411 |
| `windows-2022` | 84 | 0 | — | 3 | 24s | 4m06s | 0% (0/15) | 84 |
| `ubuntu-24.04-arm` | 84 | 0 | — | 0 | 9s | 3m58s | 0% (0/15) | 84 |
| `ah-ubuntu_22_04-c7g_4x-50` | 3 | 0 | — | 0 | 1m55s | 2m10s | — | 3 |
| `macos-15-intel` | 3 | 0 | — | 2 | 14s | 1m47s | — | 3 |
| `azure-linux-scale` | 152 | 0 | — | 5 | 10s | 52s | 0% (0/30) | 152 |
| `azure-windows-scale` | 28 | 0 | — | 1 | 1s | 27s | 0% (0/5) | 28 |
| `ubuntu-latest` | 31 | 0 | — | 0 | 3s | 5s | 0% (0/8) | 31 |
| `linux-mi35x-1gpu-ossci-iree-org` | 22 | 0 | — | 1 | 2s | 2s | 20% (1/5) | 22 |

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds.
