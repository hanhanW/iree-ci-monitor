# Status detail

_Updated: 2026-06-28 05:47 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463969) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463979) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463979) | 0% (0/3) | — | 3 |  |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463965) | [3s](https://github.com/iree-org/iree/actions/runs/28321109256/job/83903093822) | [3s](https://github.com/iree-org/iree/actions/runs/28321109256/job/83903093822) | 0% (0/10) | 0% (0/1) | 10 |  |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903596417) | [3s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584491) | [3s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584491) | 33% (2/6) | — | 6 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | — | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463972) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463975) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463975) | 0% (0/2) | — | 2 |  |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463977) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463988) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463988) | 0% (0/2) | — | 2 |  |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 6 | [17h43m](https://github.com/iree-org/iree/actions/runs/28298636190/job/83843455562) | 2026-06-28 05:47 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [17h43m](https://github.com/iree-org/iree/actions/runs/28298636190/job/83843455562) | 2026-06-28 05:47 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/fill-buffer-1byte-edge` | pull_request |
| [17h25m](https://github.com/iree-org/iree/actions/runs/28299106146/job/83844610658) | 2026-06-28 05:47 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/copy-buffer-1byte-grid` | pull_request |
| [17h22m](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820560) | 2026-06-28 05:47 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/indirect-dispatch-stack-garbage` | pull_request |
| [17h19m](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978281) | 2026-06-28 05:47 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/staging-buffer-overflow` | pull_request |
| [17h18m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041346) | 2026-06-28 05:47 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/export-name-lookup` | pull_request |
| [17h17m](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077655) | 2026-06-28 05:47 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/indirect-dispatch-offset` | pull_request |

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 6 | [17h43m](https://github.com/iree-org/iree/actions/runs/28298636190/job/83843455562) | 2026-06-28 05:47 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463967) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463967) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463967) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463969) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463969) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463969) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463979) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463979) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463979) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463974) | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463974) | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463974) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883450588) | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883450588) | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883450588) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28313880526/job/83883403723) | [3s](https://github.com/iree-org/iree/actions/runs/28313880526/job/83883403723) | [3s](https://github.com/iree-org/iree/actions/runs/28313880526/job/83883403723) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28321109256/job/83903093822) | [3s](https://github.com/iree-org/iree/actions/runs/28321109256/job/83903093822) | [3s](https://github.com/iree-org/iree/actions/runs/28321109256/job/83903093822) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584491) | [3s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584491) | [3s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584491) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463965) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463965) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463965) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463988) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463988) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463988) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463977) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463977) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463977) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463975) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463975) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463975) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28321153273/job/83903205799) | [2s](https://github.com/iree-org/iree/actions/runs/28321153273/job/83903205799) | [2s](https://github.com/iree-org/iree/actions/runs/28321153273/job/83903205799) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584460) | [2s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584460) | [2s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584460) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584462) | [2s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584462) | [2s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584462) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903584185) | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903584185) | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903584185) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903596417) | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903596417) | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903596417) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903596411) | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903596411) | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903596411) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83903087528) | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83903087528) | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83903087528) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463964) | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463964) | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463964) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463985) | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463985) | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463985) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463972) | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463972) | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463972) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28321109256/job/83903198206) | [1s](https://github.com/iree-org/iree/actions/runs/28321109256/job/83903198206) | [1s](https://github.com/iree-org/iree/actions/runs/28321109256/job/83903198206) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 149 | 148 | 0 | 1 | 0% |  | 13h55m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 122 | 112 | 9 | 1 | 7% |  | 15h04m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 110 | 109 | 0 | 1 | 0% |  | 15h10m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 106 | 105 | 0 | 1 | 0% |  | 15h18m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 33 | 32 | 0 | 1 | 0% |  | 16h33m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 17h43m (> 2h00m)

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
