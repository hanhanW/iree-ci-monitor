# Status detail

_Updated: 2026-07-25 11:37 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30161906811/job/89688501514) | [3s](https://github.com/iree-org/iree/actions/runs/30161906816/job/89688488586) | [4s](https://github.com/iree-org/iree/actions/runs/30156418353/job/89674994274) | 27% (4/15) | — | 15 |  |
| `ubuntu-24.04` | github-hosted | 5 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30156399834/job/89674947661) | [3s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89674810918) | [3s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89674810918) | 0% (0/5) | 0% (0/1) | 5 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | 2s | [3s](https://github.com/iree-org/iree/actions/runs/30161906816/job/89688488586) | [4s](https://github.com/iree-org/iree/actions/runs/30156418353/job/89674994274) | [4s](https://github.com/iree-org/iree/actions/runs/30156418353/job/89674994274) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30156418353/job/89674994275) | [3s](https://github.com/iree-org/iree/actions/runs/30161906816/job/89688488568) | [3s](https://github.com/iree-org/iree/actions/runs/30161906816/job/89688488568) | 3 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30161906811/job/89688501529) | [3s](https://github.com/iree-org/iree/actions/runs/30156562912/job/89675362953) | [3s](https://github.com/iree-org/iree/actions/runs/30156562912/job/89675362953) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30161906811/job/89688501514) | [3s](https://github.com/iree-org/iree/actions/runs/30156562912/job/89675362964) | [3s](https://github.com/iree-org/iree/actions/runs/30156562912/job/89675362964) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89674810918) | [3s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89674810918) | [3s](https://github.com/iree-org/iree/actions/runs/30146602410/job/89674810918) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30156563140/job/89675353643) | [2s](https://github.com/iree-org/iree/actions/runs/30161906816/job/89688488541) | [2s](https://github.com/iree-org/iree/actions/runs/30161906816/job/89688488541) | 3 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30156399834/job/89674947661) | [2s](https://github.com/iree-org/iree/actions/runs/30161739158/job/89688046578) | [2s](https://github.com/iree-org/iree/actions/runs/30161739158/job/89688046578) | 2 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30156562912/job/89675352927) | [2s](https://github.com/iree-org/iree/actions/runs/30161906811/job/89688488415) | [2s](https://github.com/iree-org/iree/actions/runs/30161906811/job/89688488415) | 2 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30156349799/job/89674940871) | [2s](https://github.com/iree-org/iree/actions/runs/30156349799/job/89674940871) | [2s](https://github.com/iree-org/iree/actions/runs/30156349799/job/89674940871) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30156349799/job/89674821579) | [2s](https://github.com/iree-org/iree/actions/runs/30156349799/job/89674821579) | [2s](https://github.com/iree-org/iree/actions/runs/30156349799/job/89674821579) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 269 | 263 | 3 | 3 | 1% |  | 1d02h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 368 | 360 | 5 | 3 | 1% |  | 1d02h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 300 | 283 | 14 | 3 | 5% |  | 1d02h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 281 | 274 | 2 | 5 | 1% |  | 1d02h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 84 | 82 | 1 | 1 | 1% |  | 1d02h ago |

## Alerts

_No active alerts._

## Methodology

- Window: last 10 hours of job records for queue-time percentiles and failure metrics; queued observations are scanned for 3 days; last 7 days for runner metrics and SPOF.
- Timestamps rendered in `America/Los_Angeles` local time; underlying records are UTC.
- Queue time: `started_at - created_at`. Skipped jobs excluded.
- Queued: jobs with `status == queued` or `waiting` (not yet assigned a runner).
- Running: jobs with `status == in_progress` (runner assigned, executing).
- Oldest queued: `collected_at - created_at` for the oldest job observed with `status == queued` or `waiting`. This is only updated by collection; rerunning the reporter does not inflate stale queued snapshots.
- Workflow/job waiting time: same queue-time definition, grouped by stable workflow id/name + job name + exact label set. Older records collected before `workflow_path` was stored fall back to `workflow_name`.
- All-jobs fail rate: over every completed job (PR + push + schedule).
- Main-only fail rate: subset where `head_branch == main` and `event != pull_request` — post-merge, scheduled, and workflow_dispatch runs. PR noise excluded.
- Runner type:
  - `self-hosted`: persistent physical hosts managed by the IREE infra team (shark fleet, `iree-mi308-1`, etc.). The `runners` count is the number of physical boxes.
  - `github-hosted`: GitHub's standard runner pool (`ubuntu-*`, `macos-*`, `windows-*`) and Actions Hosting partners (`ah-*`). Ephemeral — one worker per job.
  - `ossci`: org-managed autoscaler pools (`azure-*`, `*-ossci-iree-org`). Ephemeral — one worker per job, so the `runners` count here is really "pod spawns in the window" not physical capacity.
- SPOF: label has seen only one distinct `runner_name` in the last 7 days.
- Persistent runner: ran ≥ 5 jobs in the lookback window AND served at least one label with ≤ 15 distinct runners. Ephemeral auto-scaler worker names (which appear once per spawn) are excluded.
- Re-runs: `(job_id, run_attempt)` tuples are distinct; a re-run counts as a new job.

## Alert thresholds

- `queue-starved`: p95 queue > 1h00m
- `stale-queued`: oldest observed queued job (not yet started) > 2h00m
- `high-failure-main`: main-only failure rate > 20% with ≥ 10 completed main-only jobs
- `spof`: only one distinct runner in last 7d
