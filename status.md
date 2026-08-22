# Status detail

_Updated: 2026-08-22 06:02 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 5s | [6s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259625) | [7s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259518) | [7s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259518) | 33% (1/3) | — | 3 |  |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/97022593147) | [4s](https://github.com/iree-org/iree/actions/runs/32569405589/job/97022606638) | [4s](https://github.com/iree-org/iree/actions/runs/32569405589/job/97022606638) | 0% (0/10) | 0% (0/1) | 10 |  |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259570) | [3s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259567) | [3s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259567) | 0% (0/2) | — | 2 |  |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32569720185/job/97023379707) | [3s](https://github.com/iree-org/iree/actions/runs/32569491194/job/97022816137) | [3s](https://github.com/iree-org/iree/actions/runs/32569491194/job/97022816137) | 22% (2/9) | — | 9 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259542) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259574) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259574) | 0% (0/2) | — | 2 |  |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759524) | 2026-08-19 00:07 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |
| `Linux,X64,rdna3` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759599) | 2026-08-19 00:07 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759660) | 2026-08-19 00:07 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |
| `Linux,X64,gfx1100` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759688) | 2026-08-19 00:07 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759971) | 2026-08-19 00:07 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759524) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759660) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759599) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759971) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759688) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 7s | [7s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259518) | [7s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259518) | [7s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259518) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 6s | [6s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259625) | [6s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259625) | [6s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259625) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259533) | [4s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259533) | [4s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259533) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984237827) | [4s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984237827) | [4s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984237827) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/32569405589/job/97022606638) | [4s](https://github.com/iree-org/iree/actions/runs/32569405589/job/97022606638) | [4s](https://github.com/iree-org/iree/actions/runs/32569405589/job/97022606638) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32569720887/job/97023367806) | [3s](https://github.com/iree-org/iree/actions/runs/32569491194/job/97022816137) | [3s](https://github.com/iree-org/iree/actions/runs/32569491194/job/97022816137) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [1s](https://github.com/iree-org/iree/actions/runs/32569720887/job/97023367837) | [3s](https://github.com/iree-org/iree/actions/runs/32569491194/job/97022815980) | [3s](https://github.com/iree-org/iree/actions/runs/32569491194/job/97022815980) | 2 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259566) | [3s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259566) | [3s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259566) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259567) | [3s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259567) | [3s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259567) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/32569468667/job/97022758871) | [3s](https://github.com/iree-org/iree/actions/runs/32569468667/job/97022758871) | [3s](https://github.com/iree-org/iree/actions/runs/32569468667/job/97022758871) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32569491194/job/97022816159) | [2s](https://github.com/iree-org/iree/actions/runs/32569720887/job/97023367720) | [2s](https://github.com/iree-org/iree/actions/runs/32569720887/job/97023367720) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/97022593147) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/97022593147) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/97022593147) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259520) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259520) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259520) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259549) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259549) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259549) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259511) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259511) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259511) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259570) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259570) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259570) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259542) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259542) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259542) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259574) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259574) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259574) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32553589096/job/96984164875) | [2s](https://github.com/iree-org/iree/actions/runs/32553589096/job/96984164875) | [2s](https://github.com/iree-org/iree/actions/runs/32553589096/job/96984164875) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32569405589/job/97022743997) | [2s](https://github.com/iree-org/iree/actions/runs/32569405589/job/97022743997) | [2s](https://github.com/iree-org/iree/actions/runs/32569405589/job/97022743997) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32569720185/job/97023379707) | [2s](https://github.com/iree-org/iree/actions/runs/32569720185/job/97023379707) | [2s](https://github.com/iree-org/iree/actions/runs/32569720185/job/97023379707) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/32569720185/job/97023379600) | [2s](https://github.com/iree-org/iree/actions/runs/32569720185/job/97023379600) | [2s](https://github.com/iree-org/iree/actions/runs/32569720185/job/97023379600) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/32569720185/job/97023365805) | [1s](https://github.com/iree-org/iree/actions/runs/32569720185/job/97023365805) | [1s](https://github.com/iree-org/iree/actions/runs/32569720185/job/97023365805) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 196 | 186 | 5 | 4 | 3% | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 208 | 199 | 3 | 5 | 1% | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 145 | 136 | 0 | 8 | 0% | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 150 | 144 | 0 | 5 | 0% | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d

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
