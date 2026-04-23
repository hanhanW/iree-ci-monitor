# Status detail

_Updated: 2026-04-23T22:30Z_ — watching `iree-org/iree`, window = last 6h

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

## Per-label metrics

| label | jobs | queued | oldest queued | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `self-hosted,persistent-cache,Linux,X64,threadripper` | 43 | 31 | 5h20m | 1 | 4h09m | 19m35s | 0s | 2h53m | 3h31m | 9% (1/11) | — | 2 |  |
| `Linux,X64,iree-w7900` | 22 | 11 | 4h33m | 0 | — | 21m26s | 0s | 2h21m | 2h23m | 9% (1/11) | 0% (0/1) | 2 |  |
| `Linux,X64,iree-r9700` | 22 | 7 | 4h33m | 0 | — | 39m21s | 12m36s | 2h17m | 2h37m | 7% (1/15) | 0% (0/4) | 1 | yes |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | 22 | 8 | 3h39m | 0 | — | 39m06s | 0s | 2h03m | 2h09m | 0% (0/14) | 0% (0/3) | 1 | yes |
| `Linux,X64,gfx1100` | 44 | 9 | 2h09m | 2 | 3h30m | 33m32s | 22m33s | 1h51m | 2h27m | 3% (1/33) | 0% (0/7) | 3 |  |
| `Linux,X64,gfx1201` | 44 | 27 | 5h20m | 0 | — | 20m58s | 0s | 1h39m | 3h02m | 0% (0/17) | 0% (0/2) | 1 | yes |
| `Linux,X64,rdna3,shark10-ci` | 22 | 15 | 5h20m | 0 | — | 13m43s | 0s | 1h32m | 2h18m | 0% (0/7) | — | 1 | yes |
| `Linux,X64,gfx1201,persistent-cache` | 22 | 9 | 4h09m | 1 | 3h30m | 26m40s | 0s | 1h31m | 1h55m | 0% (0/12) | 0% (0/2) | 1 | yes |
| `Linux,X64,iree-w7900x2,persistent-cache` | 22 | 8 | 4h48m | 0 | — | 23m12s | 5m00s | 1h27m | 1h56m | 57% (8/14) | 60% (3/5) | 2 |  |
| `Linux,X64,rdna3` | 22 | 3 | 1h42m | 0 | — | 32m29s | 15m20s | 1h26m | 2h21m | 5% (1/19) | 0% (0/6) | 3 |  |
| `self-hosted,persistent-cache,Linux,X64` | 45 | 6 | 1h42m | 3 | 1h42m | 20m57s | 16m28s | 1h17m | 1h26m | 0% (0/36) | 0% (0/9) | 4 |  |
| `Linux,X64,gfx1100,persistent-cache` | 22 | 2 | 1h42m | 0 | — | 26m56s | 20m33s | 1h04m | 1h46m | 0% (0/20) | 0% (0/6) | 3 |  |
| `nodai-amdgpu-mi308-x86-64` | 22 | 1 | 1h33m | 1 | 1h42m | 9m24s | 5m21s | 23m31s | 38m06s | 0% (0/20) | 0% (0/6) | 1 | yes |
| `linux-mi325-1gpu-ossci-iree-org` | 88 | 3 | 1h33m | 2 | 1h42m | 2m03s | 9s | 9m10s | 15m57s | 17% (14/83) | 12% (3/24) | 85 |  |
| `macos-14` | 91 | 3 | 1h39m | 5 | 3h45m | 2m17s | 1m08s | 9m09s | 12m21s | 0% (0/83) | 0% (0/23) | 86 |  |
| `windows-2022` | 87 | 0 | — | 7 | 1h39m | 1m09s | 30s | 4m35s | 5m38s | 1% (1/80) | 4% (1/23) | 87 |  |
| `ubuntu-24.04` | 436 | 9 | 1h33m | 9 | 3h45m | 54s | 3s | 4m34s | 16m10s | 6% (23/418) | 1% (1/104) | 419 |  |
| `macos-15-intel` | 5 | 0 | — | 4 | 3h45m | 1m19s | 14s | 4m30s | 4m30s | 0% (0/1) | — | 5 |  |
| `ubuntu-24.04-arm` | 87 | 0 | — | 2 | 8m20s | 1m01s | 9s | 3m59s | 5m22s | 0% (0/85) | 0% (0/24) | 87 |  |
| `ah-ubuntu_22_04-c7g_4x-50` | 4 | 0 | — | 1 | 8m20s | 1m59s | 1m59s | 2m10s | 2m10s | 0% (0/3) | — | 4 |  |
| `azure-windows-scale` | 29 | 0 | — | 4 | 1h39m | 21s | 2s | 2m05s | 3m58s | 4% (1/25) | 0% (0/6) | 29 |  |
| `ubuntu-latest` | 39 | 0 | — | 0 | — | 16s | 3s | 56s | 3m33s | 5% (2/39) | 0% (0/16) | 39 |  |
| `azure-linux-scale` | 164 | 0 | — | 19 | 1h57m | 14s | 9s | 52s | 2m48s | 3% (4/145) | 0% (0/41) | 164 |  |
| `linux-mi35x-1gpu-ossci-iree-org` | 22 | 0 | — | 1 | 1h33m | 1s | 2s | 2s | 7s | 19% (4/21) | 33% (2/6) | 22 |  |

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
