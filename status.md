# Status detail

_Updated: 2026-06-26 00:37 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [1h09m](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051279) | 4s | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051276) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | 0% (0/1) | — | 3 |  |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [1h09m](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051325) | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | 0% (0/1) | — | 2 |  |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [1h09m](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051300) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603031487) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051332) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051332) | 29% (2/7) | 50% (2/4) | 9 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [1h09m](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051295) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051295) | 0% (0/1) | — | 2 |  |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 4 | [21h43m](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332845) | 2026-06-26 00:36 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [21h43m](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332845) | 2026-06-26 00:36 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `fuse_multiple-slice` | pull_request |
| [21h30m](https://github.com/iree-org/iree/actions/runs/28162167887/job/83406683033) | 2026-06-26 00:36 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [19h32m](https://github.com/iree-org/iree/actions/runs/28167098275/job/83427161012) | 2026-06-26 00:36 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `integrates/llvm-20260625` | pull_request |
| [17h59m](https://github.com/iree-org/iree/actions/runs/28172319267/job/83446011596) | 2026-06-26 00:36 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 4 | [21h43m](https://github.com/iree-org/iree/actions/runs/28156378002/job/83404332845) | 2026-06-26 00:36 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051276) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051276) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051276) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051279) | [4s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051279) | [4s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051279) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051300) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051300) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051300) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051304) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051304) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051304) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051305) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051305) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051305) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051332) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051332) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051332) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051325) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051325) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051325) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603031487) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603031487) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603031487) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051295) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051295) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051295) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228962) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228962) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228962) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228950) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228950) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228950) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83598184239) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83598184239) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83598184239) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221278784/job/83602925806) | [2s](https://github.com/iree-org/iree/actions/runs/28221278784/job/83602925806) | [2s](https://github.com/iree-org/iree/actions/runs/28221278784/job/83602925806) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 123 | 122 | 0 | 1 | 0% |  | 17h29m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 94 | 93 | 0 | 1 | 0% |  | 17h33m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 96 | 6 | 0 | 6% |  | 17h34m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 86 | 86 | 0 | 0 | 0% |  | 17h34m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 27 | 27 | 0 | 0 | 0% |  | 17h46m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 21h43m (> 2h00m)

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
