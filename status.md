# Status detail

_Updated: 2026-04-23T21:07Z_ — watching `iree-org/iree`, window = last 6h

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 2h46m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 3h57m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 3h09m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 3h09m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 3h25m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 2h16m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 3h57m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 3h57m (> 2h00m)
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

## Per-label metrics

| label | jobs | queued | oldest queued | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `self-hosted,persistent-cache,Linux,X64,threadripper` | 43 | 25 | 3h57m | 1 | 2h46m | 21m08s | 0s | 2h53m | 3h31m | 6% (1/17) | 0% (0/2) | 2 |  |
| `Linux,X64,iree-w7900` | 22 | 8 | 3h09m | 0 | — | 22m54s | 2s | 2h21m | 2h23m | 7% (1/14) | 0% (0/2) | 2 |  |
| `Linux,X64,iree-r9700` | 22 | 4 | 3h09m | 0 | — | 41m56s | 32m24s | 2h17m | 2h37m | 6% (1/18) | 0% (0/5) | 1 | yes |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | 22 | 5 | 2h16m | 0 | — | 41m04s | 15m34s | 2h03m | 2h09m | 0% (0/17) | 0% (0/4) | 1 | yes |
| `Linux,X64,gfx1100` | 44 | 5 | 46m21s | 1 | 2h07m | 34m42s | 25m39s | 1h51m | 2h27m | 3% (1/38) | 0% (0/8) | 3 |  |
| `Linux,X64,gfx1201` | 44 | 21 | 3h57m | 0 | — | 22m24s | 0s | 1h39m | 3h02m | 0% (0/23) | 0% (0/4) | 1 | yes |
| `Linux,X64,rdna3,shark10-ci` | 22 | 12 | 3h57m | 0 | — | 14m38s | 0s | 1h32m | 2h18m | 0% (0/10) | 0% (0/1) | 1 | yes |
| `Linux,X64,gfx1201,persistent-cache` | 22 | 6 | 2h46m | 1 | 2h07m | 29m26s | 17m22s | 1h31m | 1h55m | 0% (0/15) | 0% (0/3) | 1 | yes |
| `Linux,X64,iree-w7900x2,persistent-cache` | 22 | 6 | 3h25m | 0 | — | 24m13s | 5m00s | 1h27m | 1h56m | 56% (9/16) | 60% (3/5) | 2 |  |
| `Linux,X64,rdna3` | 22 | 2 | 18m32s | 0 | — | 32m54s | 29m52s | 1h26m | 2h21m | 5% (1/20) | 0% (0/5) | 3 |  |
| `self-hosted,persistent-cache,Linux,X64` | 45 | 3 | 18m32s | 1 | 18m32s | 20m48s | 13m37s | 1h17m | 1h26m | 0% (0/41) | 0% (0/10) | 4 |  |
| `Linux,X64,gfx1100,persistent-cache` | 22 | 2 | 18m32s | 0 | — | 27m32s | 20m47s | 1h04m | 1h46m | 0% (0/20) | 0% (0/5) | 3 |  |
| `nodai-amdgpu-mi308-x86-64` | 22 | 1 | 10m03s | 1 | 18m32s | 9m54s | 5m21s | 23m31s | 38m06s | 0% (0/20) | 0% (0/5) | 1 | yes |
| `linux-mi325-1gpu-ossci-iree-org` | 88 | 3 | 10m03s | 2 | 18m32s | 2m10s | 10s | 9m10s | 15m57s | 17% (14/83) | 15% (3/20) | 85 |  |
| `macos-14` | 87 | 1 | 16m12s | 3 | 2h21m | 1m54s | 47s | 7m23s | 10m41s | 0% (0/83) | 0% (0/15) | 84 |  |
| `ubuntu-24.04` | 429 | 9 | 10m03s | 6 | 2h21m | 55s | 3s | 4m47s | 16m10s | 7% (27/414) | 1% (1/78) | 412 |  |
| `windows-2022` | 84 | 0 | — | 3 | 16m12s | 1m07s | 24s | 4m06s | 5m38s | 0% (0/81) | 0% (0/15) | 84 |  |
| `ubuntu-24.04-arm` | 84 | 0 | — | 0 | — | 1m01s | 9s | 3m58s | 4m24s | 0% (0/84) | 0% (0/15) | 84 |  |
| `ah-ubuntu_22_04-c7g_4x-50` | 3 | 0 | — | 0 | — | 2m00s | 1m55s | 2m10s | 2m10s | 0% (0/3) | — | 3 |  |
| `macos-15-intel` | 3 | 0 | — | 2 | 2h21m | 41s | 14s | 1m47s | 1m47s | 0% (0/1) | — | 3 |  |
| `azure-linux-scale` | 152 | 0 | — | 5 | 33m35s | 16s | 10s | 52s | 2m48s | 4% (6/147) | 0% (0/30) | 152 |  |
| `azure-windows-scale` | 28 | 0 | — | 1 | 16m12s | 4s | 1s | 27s | 1m08s | 4% (1/27) | 0% (0/5) | 28 |  |
| `ubuntu-latest` | 31 | 0 | — | 0 | — | 15s | 3s | 5s | 3m33s | 6% (2/31) | 0% (0/8) | 31 |  |
| `linux-mi35x-1gpu-ossci-iree-org` | 22 | 0 | — | 1 | 10m03s | 1s | 2s | 2s | 7s | 24% (5/21) | 20% (1/5) | 22 |  |

## Methodology

- Window: last 6 hours of job records (created_at ≥ now-6h).
- Queue time: `started_at - created_at`. Skipped jobs excluded.
- Queued: jobs with `status == queued` or `waiting` (not yet assigned a runner).
- Running: jobs with `status == in_progress` (runner assigned, executing).
- Oldest queued: `now - created_at` for the oldest still-queued job. This is the actionable signal for runner starvation — a job that's been in_progress for hours is just slow, not starved.
- All-jobs fail rate: over every completed job (PR + push + schedule).
- Main-only fail rate: subset where `head_branch == main` and `event != pull_request` — post-merge, scheduled, and workflow_dispatch runs. PR noise excluded.
- SPOF: label has seen only one distinct `runner_name` in the last 7 days.
- Re-runs: `(job_id, run_attempt)` tuples are distinct; a re-run counts as a new job.

## Alert thresholds

- `queue-starved`: p95 queue > 1h00m
- `stale-queued`: oldest queued job (not yet started) > 2h00m
- `high-failure-main`: main-only failure rate > 20% with ≥ 10 completed main-only jobs
- `spof`: only one distinct runner in last 7d
