# Daily report — 2026-09-20 (Sunday)

_Updated: 2026-09-21 05:55 PDT_ — `iree-org/iree`, covering `2026-09-20 00:00 PDT` → `2026-09-21 00:00 PDT` (Pacific calendar day **2026-09-20 (Sunday)**)

Snapshot of the most recently completed Pacific calendar day. Larger window than the rolling [`status.md`](status.md) — better percentile stability and small-volume labels can reach the failure-rate threshold. Refreshed each tick; content only changes when crossing midnight Pacific time, so most ticks produce no diff.

## Per-label metrics

| label | type | jobs | completed | p50 queue | p95 queue | max queue | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04` | github-hosted | 11 | 10 | [2s](https://github.com/iree-org/iree/actions/runs/35510074988/job/106076328551) | [3s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106055323466) | [3s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106055323466) | 10% (1/10) | 0% (0/4) | 10 |  |
| `ubuntu-latest` | github-hosted | 9 | 9 | [2s](https://github.com/iree-org/iree/actions/runs/35515594893/job/106090887366) | [3s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090909005) | [3s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090909005) | 22% (2/9) | 0% (0/3) | 9 |  |

## Workflow/job waiting time

| workflow | job | labels | jobs | completed | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 2 | [2s](https://github.com/iree-org/iree/actions/runs/35515594893/job/106090887406) | [3s](https://github.com/iree-org/iree/actions/runs/35513885621/job/106086431666) | [3s](https://github.com/iree-org/iree/actions/runs/35513885621/job/106086431666) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 1 | [3s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106055323466) | [3s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106055323466) | [3s](https://github.com/iree-org/iree/actions/runs/35491175698/job/106055323466) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 1 | [3s](https://github.com/iree-org/iree/actions/runs/35444212759/job/106094721639) | [3s](https://github.com/iree-org/iree/actions/runs/35444212759/job/106094721639) | [3s](https://github.com/iree-org/iree/actions/runs/35444212759/job/106094721639) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 1 | [3s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090908972) | [3s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090908972) | [3s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090908972) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 1 | [3s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090909005) | [3s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090909005) | [3s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090909005) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 2 | [2s](https://github.com/iree-org/iree/actions/runs/35502073745/job/106055496041) | [2s](https://github.com/iree-org/iree/actions/runs/35515299901/job/106090107955) | [2s](https://github.com/iree-org/iree/actions/runs/35515299901/job/106090107955) | 2 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 2 | 2 | [2s](https://github.com/iree-org/iree/actions/runs/35510074988/job/106076328551) | [2s](https://github.com/iree-org/iree/actions/runs/35510074988/job/106076328551) | [2s](https://github.com/iree-org/iree/actions/runs/35510074988/job/106076328551) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 2 | [2s](https://github.com/iree-org/iree/actions/runs/35513885621/job/106086431509) | [2s](https://github.com/iree-org/iree/actions/runs/35515594893/job/106090887170) | [2s](https://github.com/iree-org/iree/actions/runs/35515594893/job/106090887170) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 2 | [2s](https://github.com/iree-org/iree/actions/runs/35513885621/job/106086431329) | [2s](https://github.com/iree-org/iree/actions/runs/35515594893/job/106090887366) | [2s](https://github.com/iree-org/iree/actions/runs/35515594893/job/106090887366) | 2 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/35560968379/job/106213637027) | [2s](https://github.com/iree-org/iree/actions/runs/35560968379/job/106213637027) | [2s](https://github.com/iree-org/iree/actions/runs/35560968379/job/106213637027) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/35560968379/job/106213637253) | [2s](https://github.com/iree-org/iree/actions/runs/35560968379/job/106213637253) | [2s](https://github.com/iree-org/iree/actions/runs/35560968379/job/106213637253) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055481141) | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055481141) | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055481141) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055339751) | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055339751) | [2s](https://github.com/iree-org/iree/actions/runs/35502017021/job/106055339751) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090887014) | [2s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090887014) | [2s](https://github.com/iree-org/iree/actions/runs/35515594267/job/106090887014) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 1 | [1s](https://github.com/iree-org/iree/actions/runs/35560968379/job/106215336028) | [1s](https://github.com/iree-org/iree/actions/runs/35560968379/job/106215336028) | [1s](https://github.com/iree-org/iree/actions/runs/35560968379/job/106215336028) | 1 |

## Methodology

- Window: jobs with `created_at` in the previous `America/Los_Angeles` calendar day (24h, midnight to midnight local). Bounds shift at midnight PT regardless of DST.
- Live state (queued/running counts and oldest-queued/oldest-running ages) is omitted: this is a historical view, those signals only make sense in the rolling window.
- Workflow/job waiting time is grouped by workflow file/name, job name, and exact `runs-on` label set.
- See [`status.md`](status.md) for full methodology, runner table, and alert thresholds.
