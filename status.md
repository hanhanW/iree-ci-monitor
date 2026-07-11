# Status detail

_Updated: 2026-07-11 00:01 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [1h07m](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674783) | 5s | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674785) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674791) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674791) | 0% (0/1) | — | 3 |  |
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 2 | [1h07m](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674776) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674788) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674776) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674776) | 0% (0/4) | 0% (0/1) | 6 |  |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [1h07m](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674804) | 2s | [1s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674795) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674804) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674804) | 0% (0/1) | — | 2 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [1h07m](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674797) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674793) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674797) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674797) | 0% (0/1) | — | 2 |  |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 8 | [21h16m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510684) | 2026-07-11 00:01 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [21h16m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510684) | 2026-07-11 00:01 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `dependabot/github_actions/github-actions-bda1fe1b4d` | pull_request |
| [21h16m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510732) | 2026-07-11 00:01 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | `dependabot/github_actions/github-actions-bda1fe1b4d` | pull_request |
| [21h16m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510802) | 2026-07-11 00:01 PDT | `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | `dependabot/github_actions/github-actions-bda1fe1b4d` | pull_request |
| [21h16m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510822) | 2026-07-11 00:01 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | `dependabot/github_actions/github-actions-bda1fe1b4d` | pull_request |
| [19h28m](https://github.com/iree-org/iree/actions/runs/29089345918/job/86352075842) | 2026-07-11 00:01 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [19h28m](https://github.com/iree-org/iree/actions/runs/29089345918/job/86352075870) | 2026-07-11 00:01 PDT | `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [19h28m](https://github.com/iree-org/iree/actions/runs/29089345918/job/86352075886) | 2026-07-11 00:01 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [19h28m](https://github.com/iree-org/iree/actions/runs/29089345918/job/86352075970) | 2026-07-11 00:01 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | ossci | 2 | 2 | [21h16m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510684) | 2026-07-11 00:01 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | ossci | 2 | 2 | [21h16m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510732) | 2026-07-11 00:01 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | ossci | 2 | 2 | [21h16m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510822) | 2026-07-11 00:01 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | ossci | 2 | 2 | [21h16m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510802) | 2026-07-11 00:01 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674791) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674791) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674791) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674783) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674783) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674783) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674785) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674785) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674785) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674776) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674776) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674776) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674774) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674774) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674774) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674804) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674804) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674804) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674792) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674792) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674792) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674788) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674788) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674788) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516660522) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516660522) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516660522) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674797) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674797) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674797) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674793) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674793) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674793) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29141922849/job/86516605989) | [2s](https://github.com/iree-org/iree/actions/runs/29141922849/job/86516605989) | [2s](https://github.com/iree-org/iree/actions/runs/29141922849/job/86516605989) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674795) | [1s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674795) | [1s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674795) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 159 | 146 | 11 | 1 | 7% | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 202 | 196 | 3 | 2 | 1% | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 162 | 158 | 1 | 2 | 1% | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 150 | 148 | 1 | 0 | 1% | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 47 | 41 | 5 | 1 | 11% |  | 19h17m ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 21h16m (> 2h00m)

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
