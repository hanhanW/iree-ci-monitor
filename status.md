# Status detail

_Updated: 2026-10-31 05:40 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124519918097) | [5s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087933) | [5s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087933) | 0% (0/10) | 0% (0/1) | 10 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 4s | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087906) | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087962) | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087962) | 33% (1/3) | — | 3 |  |
| `macos-15` | github-hosted | 2 | 0 | — | — | 0 | — | 3s | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087894) | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087932) | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087932) | 0% (0/2) | — | 2 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087914) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087936) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087936) | 0% (0/2) | — | 2 |  |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/41195383688/job/124520394428) | [2s](https://github.com/iree-org/iree/actions/runs/41195383688/job/124520394473) | [2s](https://github.com/iree-org/iree/actions/runs/41195383688/job/124520394473) | 0% (0/3) | — | 3 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087933) | [5s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087933) | [5s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087933) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087906) | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087906) | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087906) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087962) | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087962) | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087962) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087877) | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087877) | [4s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087877) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087894) | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087894) | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087894) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087932) | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087932) | [3s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087932) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/41171390063/job/124449897128) | [3s](https://github.com/iree-org/iree/actions/runs/41171390063/job/124449897128) | [3s](https://github.com/iree-org/iree/actions/runs/41171390063/job/124449897128) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124519918097) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124519918097) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124519918097) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087882) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087882) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087882) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087943) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087943) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087943) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087874) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087874) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087874) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450050929) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450050929) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450050929) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087936) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087936) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087936) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087914) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087914) | [2s](https://github.com/iree-org/iree/actions/runs/41171437933/job/124450087914) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/41195338177/job/124520263126) | [2s](https://github.com/iree-org/iree/actions/runs/41195338177/job/124520263126) | [2s](https://github.com/iree-org/iree/actions/runs/41195338177/job/124520263126) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/41195227268/job/124520234804) | [2s](https://github.com/iree-org/iree/actions/runs/41195227268/job/124520234804) | [2s](https://github.com/iree-org/iree/actions/runs/41195227268/job/124520234804) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/41195227268/job/124519943524) | [2s](https://github.com/iree-org/iree/actions/runs/41195227268/job/124519943524) | [2s](https://github.com/iree-org/iree/actions/runs/41195227268/job/124519943524) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/41195383688/job/124520394428) | [2s](https://github.com/iree-org/iree/actions/runs/41195383688/job/124520394428) | [2s](https://github.com/iree-org/iree/actions/runs/41195383688/job/124520394428) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/41195383688/job/124520394280) | [2s](https://github.com/iree-org/iree/actions/runs/41195383688/job/124520394280) | [2s](https://github.com/iree-org/iree/actions/runs/41195383688/job/124520394280) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/41195383688/job/124520394473) | [2s](https://github.com/iree-org/iree/actions/runs/41195383688/job/124520394473) | [2s](https://github.com/iree-org/iree/actions/runs/41195383688/job/124520394473) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 265 | 256 | 8 | 1 | 3% |  | 1d00h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 222 | 212 | 7 | 3 | 3% |  | 1d00h ago |

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
