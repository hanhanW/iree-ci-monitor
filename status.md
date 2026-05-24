# Status detail

_Updated: 2026-05-24 11:41 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | — | 1s | [2s](https://github.com/iree-org/iree/actions/runs/26360419115/job/77594729214) | [2s](https://github.com/iree-org/iree/actions/runs/26364018813/job/77604536498) | [3s](https://github.com/iree-org/iree/actions/runs/26360419115/job/77594740244) | 22% (4/18) | 0% (0/3) | 18 |  |
| `ubuntu-24.04` | github-hosted | 5 | 0 | — | — | 0 | — | 1s | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77594350012) | [2s](https://github.com/iree-org/iree/actions/runs/26360303396/job/77594422551) | [2s](https://github.com/iree-org/iree/actions/runs/26360303396/job/77594422551) | 0% (0/5) | 0% (0/1) | 5 |  |
| `azure-linux-scale` | ossci | 1 | 1 | [10m39s](https://github.com/iree-org/iree/actions/runs/26212319110/job/77181582238) | 2026-05-21 06:27 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | ossci | 1 | 1 | [10m39s](https://github.com/iree-org/iree/actions/runs/26212319110/job/77181582238) | 2026-05-21 06:27 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26364018553/job/77604545029) | [3s](https://github.com/iree-org/iree/actions/runs/26360419115/job/77594740244) | [3s](https://github.com/iree-org/iree/actions/runs/26360419115/job/77594740244) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 4 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26362659917/job/77600806136) | [2s](https://github.com/iree-org/iree/actions/runs/26364018813/job/77604536497) | [2s](https://github.com/iree-org/iree/actions/runs/26364018813/job/77604536497) | 4 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 4 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26362659917/job/77600806139) | [2s](https://github.com/iree-org/iree/actions/runs/26364018813/job/77604536496) | [2s](https://github.com/iree-org/iree/actions/runs/26364018813/job/77604536496) | 4 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 4 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26362659917/job/77600806148) | [2s](https://github.com/iree-org/iree/actions/runs/26364018813/job/77604536498) | [2s](https://github.com/iree-org/iree/actions/runs/26364018813/job/77604536498) | 4 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/26363904040/job/77604217278) | [2s](https://github.com/iree-org/iree/actions/runs/26360303396/job/77594422551) | [2s](https://github.com/iree-org/iree/actions/runs/26360303396/job/77594422551) | 2 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/26364018553/job/77604536253) | [2s](https://github.com/iree-org/iree/actions/runs/26360419115/job/77594729214) | [2s](https://github.com/iree-org/iree/actions/runs/26360419115/job/77594729214) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/26364018553/job/77604545008) | [2s](https://github.com/iree-org/iree/actions/runs/26360419115/job/77594740257) | [2s](https://github.com/iree-org/iree/actions/runs/26360419115/job/77594740257) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77594350012) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77594350012) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77594350012) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26360277848/job/77594414898) | [2s](https://github.com/iree-org/iree/actions/runs/26360277848/job/77594414898) | [2s](https://github.com/iree-org/iree/actions/runs/26360277848/job/77594414898) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/26360277848/job/77594355377) | [1s](https://github.com/iree-org/iree/actions/runs/26360277848/job/77594355377) | [1s](https://github.com/iree-org/iree/actions/runs/26360277848/job/77594355377) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 300 | 289 | 5 | 5 | 2% | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 270 | 244 | 20 | 5 | 7% | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 229 | 217 | 7 | 4 | 3% | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 224 | 214 | 2 | 7 | 1% | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 71 | 66 | 2 | 3 | 3% |  | 1d23h ago |

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
