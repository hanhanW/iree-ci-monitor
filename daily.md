# Daily report — 2026-09-13 (Sunday)

_Updated: 2026-09-14 14:52 PDT_ — `iree-org/iree`, covering `2026-09-13 00:00 PDT` → `2026-09-14 00:00 PDT` (Pacific calendar day **2026-09-13 (Sunday)**)

Snapshot of the most recently completed Pacific calendar day. Larger window than the rolling [`status.md`](status.md) — better percentile stability and small-volume labels can reach the failure-rate threshold. Refreshed each tick; content only changes when crossing midnight Pacific time, so most ticks produce no diff.

## Per-label metrics

| label | type | jobs | completed | p50 queue | p95 queue | max queue | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-latest` | github-hosted | 9 | 9 | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735931895) | [3s](https://github.com/iree-org/iree/actions/runs/34761829563/job/103735908124) | [3s](https://github.com/iree-org/iree/actions/runs/34761829563/job/103735908124) | 22% (2/9) | 0% (0/3) | 9 |  |
| `ubuntu-24.04` | github-hosted | 6 | 5 | [2s](https://github.com/iree-org/iree/actions/runs/34806020074/job/103857950499) | [2s](https://github.com/iree-org/iree/actions/runs/34806020074/job/103859657516) | [2s](https://github.com/iree-org/iree/actions/runs/34806020074/job/103859657516) | 0% (0/5) | 0% (0/5) | 5 |  |

## Workflow/job waiting time

| workflow | job | labels | jobs | completed | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 2 | [2s](https://github.com/iree-org/iree/actions/runs/34760657622/job/103732802833) | [3s](https://github.com/iree-org/iree/actions/runs/34761829563/job/103735908124) | [3s](https://github.com/iree-org/iree/actions/runs/34761829563/job/103735908124) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 2 | [2s](https://github.com/iree-org/iree/actions/runs/34760657622/job/103732802919) | [2s](https://github.com/iree-org/iree/actions/runs/34761829563/job/103735907933) | [2s](https://github.com/iree-org/iree/actions/runs/34761829563/job/103735907933) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 2 | [2s](https://github.com/iree-org/iree/actions/runs/34760657622/job/103732802905) | [2s](https://github.com/iree-org/iree/actions/runs/34761829563/job/103735908098) | [2s](https://github.com/iree-org/iree/actions/runs/34761829563/job/103735908098) | 2 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/34777397818/job/103777904018) | [2s](https://github.com/iree-org/iree/actions/runs/34777397818/job/103777904018) | [2s](https://github.com/iree-org/iree/actions/runs/34777397818/job/103777904018) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/34761556655/job/103735181276) | [2s](https://github.com/iree-org/iree/actions/runs/34761556655/job/103735181276) | [2s](https://github.com/iree-org/iree/actions/runs/34761556655/job/103735181276) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/34806020074/job/103857950767) | [2s](https://github.com/iree-org/iree/actions/runs/34806020074/job/103857950767) | [2s](https://github.com/iree-org/iree/actions/runs/34806020074/job/103857950767) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/34806020074/job/103857950499) | [2s](https://github.com/iree-org/iree/actions/runs/34806020074/job/103857950499) | [2s](https://github.com/iree-org/iree/actions/runs/34806020074/job/103857950499) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/34806020074/job/103859657516) | [2s](https://github.com/iree-org/iree/actions/runs/34806020074/job/103859657516) | [2s](https://github.com/iree-org/iree/actions/runs/34806020074/job/103859657516) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735908426) | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735908426) | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735908426) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735931895) | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735931895) | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735931895) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735931978) | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735931978) | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735931978) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 1 | 0s | 0s | 0s | 0 |

## Methodology

- Window: jobs with `created_at` in the previous `America/Los_Angeles` calendar day (24h, midnight to midnight local). Bounds shift at midnight PT regardless of DST.
- Live state (queued/running counts and oldest-queued/oldest-running ages) is omitted: this is a historical view, those signals only make sense in the rolling window.
- Workflow/job waiting time is grouped by workflow file/name, job name, and exact `runs-on` label set.
- See [`status.md`](status.md) for full methodology, runner table, and alert thresholds.
