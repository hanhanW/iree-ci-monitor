# Daily report — 2026-10-25 (Sunday)

_Updated: 2026-10-26 22:11 PDT_ — `iree-org/iree`, covering `2026-10-25 00:00 PDT` → `2026-10-26 00:00 PDT` (Pacific calendar day **2026-10-25 (Sunday)**)

Snapshot of the most recently completed Pacific calendar day. Larger window than the rolling [`status.md`](status.md) — better percentile stability and small-volume labels can reach the failure-rate threshold. Refreshed each tick; content only changes when crossing midnight Pacific time, so most ticks produce no diff.

## Per-label metrics

| label | type | jobs | completed | p50 queue | p95 queue | max queue | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04` | github-hosted | 7 | 5 | [2s](https://github.com/iree-org/iree/actions/runs/40269016889/job/121397579247) | [3s](https://github.com/iree-org/iree/actions/runs/40269016889/job/121397579449) | [3s](https://github.com/iree-org/iree/actions/runs/40269016889/job/121397579449) | 0% (0/5) | 0% (0/4) | 5 |  |
| `ubuntu-latest` | github-hosted | 9 | 9 | [2s](https://github.com/iree-org/iree/actions/runs/40200871044/job/121191591022) | [3s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191625564) | [3s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191625564) | 22% (2/9) | 0% (0/3) | 9 |  |

## Workflow/job waiting time

| workflow | job | labels | jobs | completed | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 1 | [3s](https://github.com/iree-org/iree/actions/runs/40269016889/job/121397579449) | [3s](https://github.com/iree-org/iree/actions/runs/40269016889/job/121397579449) | [3s](https://github.com/iree-org/iree/actions/runs/40269016889/job/121397579449) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 1 | [3s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191625564) | [3s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191625564) | [3s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191625564) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 2 | [2s](https://github.com/iree-org/iree/actions/runs/40198120915/job/121183294019) | [2s](https://github.com/iree-org/iree/actions/runs/40200871044/job/121191591135) | [2s](https://github.com/iree-org/iree/actions/runs/40200871044/job/121191591135) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 2 | [2s](https://github.com/iree-org/iree/actions/runs/40198120915/job/121183294169) | [2s](https://github.com/iree-org/iree/actions/runs/40200871044/job/121191590940) | [2s](https://github.com/iree-org/iree/actions/runs/40200871044/job/121191590940) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 2 | [2s](https://github.com/iree-org/iree/actions/runs/40198120915/job/121183294159) | [2s](https://github.com/iree-org/iree/actions/runs/40200871044/job/121191591022) | [2s](https://github.com/iree-org/iree/actions/runs/40200871044/job/121191591022) | 2 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/40200444630/job/121190298131) | [2s](https://github.com/iree-org/iree/actions/runs/40200444630/job/121190298131) | [2s](https://github.com/iree-org/iree/actions/runs/40200444630/job/121190298131) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/40230273951/job/121280303351) | [2s](https://github.com/iree-org/iree/actions/runs/40230273951/job/121280303351) | [2s](https://github.com/iree-org/iree/actions/runs/40230273951/job/121280303351) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/40269016889/job/121397579247) | [2s](https://github.com/iree-org/iree/actions/runs/40269016889/job/121397579247) | [2s](https://github.com/iree-org/iree/actions/runs/40269016889/job/121397579247) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/40269016889/job/121400189843) | [2s](https://github.com/iree-org/iree/actions/runs/40269016889/job/121400189843) | [2s](https://github.com/iree-org/iree/actions/runs/40269016889/job/121400189843) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191590276) | [2s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191590276) | [2s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191590276) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 1 | [2s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191625591) | [2s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191625591) | [2s](https://github.com/iree-org/iree/actions/runs/40200871121/job/121191625591) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 1 | 0s | 0s | 0s | 0 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | 1 | 1 | 0s | 0s | 0s | 0 |

## Methodology

- Window: jobs with `created_at` in the previous `America/Los_Angeles` calendar day (24h, midnight to midnight local). Bounds shift at midnight PT regardless of DST.
- Live state (queued/running counts and oldest-queued/oldest-running ages) is omitted: this is a historical view, those signals only make sense in the rolling window.
- Workflow/job waiting time is grouped by workflow file/name, job name, and exact `runs-on` label set.
- See [`status.md`](status.md) for full methodology, runner table, and alert thresholds.
