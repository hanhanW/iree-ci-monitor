# Status detail

_Updated: 2026-10-03 09:26 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | — | 5s | [2s](https://github.com/iree-org/iree/actions/runs/37131310269/job/111226822511) | [37s](https://github.com/iree-org/iree/actions/runs/37118820192/job/111190745789) | [37s](https://github.com/iree-org/iree/actions/runs/37118820192/job/111190745789) | 22% (2/9) | — | 9 |  |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37114473273/job/111178474146) | [3s](https://github.com/iree-org/iree/actions/runs/37099241046/job/111190462734) | [3s](https://github.com/iree-org/iree/actions/runs/37099241046/job/111190462734) | 27% (3/11) | 33% (1/3) | 11 |  |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 3 | 3 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257364) | 2026-10-03 09:26 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 3 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257394) | 2026-10-03 09:26 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |
| `Linux,X64,rdna3` | self-hosted | 6 | 6 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257428) | 2026-10-03 09:26 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |
| `Linux,X64,gfx1100` | self-hosted | 6 | 6 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257509) | 2026-10-03 09:26 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257364) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257394) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257428) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257509) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257562) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257835) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [15h58m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943478) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [15h58m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943507) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [15h58m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943522) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [15h58m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943553) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [15h58m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943557) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [15h58m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943578) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [10h13m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173088) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `feat-python-async-parameter-files` | pull_request |
| [10h13m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173141) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `feat-python-async-parameter-files` | pull_request |
| [10h13m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173202) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `feat-python-async-parameter-files` | pull_request |
| [10h13m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173205) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `feat-python-async-parameter-files` | pull_request |
| [10h13m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173211) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `feat-python-async-parameter-files` | pull_request |
| [10h13m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173214) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `feat-python-async-parameter-files` | pull_request |

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 3 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257394) | 2026-10-03 09:26 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | self-hosted | 3 | 3 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257364) | 2026-10-03 09:26 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | self-hosted | 3 | 3 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257835) | 2026-10-03 09:26 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | self-hosted | 3 | 3 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257428) | 2026-10-03 09:26 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | self-hosted | 3 | 3 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257509) | 2026-10-03 09:26 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | self-hosted | 3 | 3 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257562) | 2026-10-03 09:26 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 19s | [2s](https://github.com/iree-org/iree/actions/runs/37131310269/job/111226822511) | [37s](https://github.com/iree-org/iree/actions/runs/37118820192/job/111190745789) | [37s](https://github.com/iree-org/iree/actions/runs/37118820192/job/111190745789) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/37099241046/job/111190462734) | [3s](https://github.com/iree-org/iree/actions/runs/37099241046/job/111190462734) | [3s](https://github.com/iree-org/iree/actions/runs/37099241046/job/111190462734) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226847576) | [3s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226847576) | [3s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226847576) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | github-hosted | 3 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37031842464/job/111241668141) | [2s](https://github.com/iree-org/iree/actions/runs/37031857001/job/111242297080) | [2s](https://github.com/iree-org/iree/actions/runs/37031857001/job/111242297080) | 3 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/37118783602/job/111190645881) | [2s](https://github.com/iree-org/iree/actions/runs/37130994553/job/111225902561) | [2s](https://github.com/iree-org/iree/actions/runs/37130994553/job/111225902561) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37118820192/job/111190745605) | [2s](https://github.com/iree-org/iree/actions/runs/37131310269/job/111226822556) | [2s](https://github.com/iree-org/iree/actions/runs/37131310269/job/111226822556) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/37118820192/job/111190745778) | [2s](https://github.com/iree-org/iree/actions/runs/37131310269/job/111226822544) | [2s](https://github.com/iree-org/iree/actions/runs/37131310269/job/111226822544) | 2 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111148940685) | [2s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111148940685) | [2s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111148940685) | 1 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37114473273/job/111178474146) | [2s](https://github.com/iree-org/iree/actions/runs/37114473273/job/111178474146) | [2s](https://github.com/iree-org/iree/actions/runs/37114473273/job/111178474146) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37135538489/job/111239206710) | [2s](https://github.com/iree-org/iree/actions/runs/37135538489/job/111239206710) | [2s](https://github.com/iree-org/iree/actions/runs/37135538489/job/111239206710) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37118726945/job/111190628501) | [2s](https://github.com/iree-org/iree/actions/runs/37118726945/job/111190628501) | [2s](https://github.com/iree-org/iree/actions/runs/37118726945/job/111190628501) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37118726945/job/111190485527) | [2s](https://github.com/iree-org/iree/actions/runs/37118726945/job/111190485527) | [2s](https://github.com/iree-org/iree/actions/runs/37118726945/job/111190485527) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226820308) | [2s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226820308) | [2s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226820308) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226847685) | [2s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226847685) | [2s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226847685) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 280 | 269 | 4 | 7 | 1% |  | 9h29m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 206 | 203 | 2 | 1 | 1% |  | 2d19h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 18h42m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 18h42m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 18h42m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 18h42m (> 2h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

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
