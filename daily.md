# Daily report — 2026-05-02 (Saturday)

_Updated: 2026-05-03 05:35 PDT_ — `iree-org/iree`, covering `2026-05-02 00:00 PDT` → `2026-05-03 00:00 PDT` (Pacific calendar day **2026-05-02 (Saturday)**)

Snapshot of the most recently completed Pacific calendar day. Larger window than the rolling [`status.md`](status.md) — better percentile stability and small-volume labels can reach the failure-rate threshold. Refreshed each tick; content only changes when crossing midnight Pacific time, so most ticks produce no diff.

## Per-label metrics

| label | type | jobs | completed | p50 queue | p95 queue | max queue | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04` | github-hosted | 11 | 11 | [2s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664148) | [8s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664150) | [8s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664150) | 0% (0/11) | 0% (0/2) | 11 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 3 | [3s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664145) | [3s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664147) | [3s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664147) | 0% (0/3) | — | 3 |  |
| `macos-14` | github-hosted | 2 | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664151) | [3s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664168) | [3s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664168) | 0% (0/2) | — | 2 |  |
| `ubuntu-latest` | github-hosted | 12 | 12 | [2s](https://github.com/iree-org/iree/actions/runs/25250831639/job/74042554051) | [2s](https://github.com/iree-org/iree/actions/runs/25254016387/job/74050394520) | [8s](https://github.com/iree-org/iree/actions/runs/25250755438/job/74042367080) | 33% (4/12) | — | 12 |  |
| `windows-2022` | github-hosted | 2 | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664165) | [2s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664170) | [2s](https://github.com/iree-org/iree/actions/runs/25271522649/job/74094664170) | 0% (0/2) | — | 2 |  |

## Methodology

- Window: jobs with `created_at` in the previous `America/Los_Angeles` calendar day (24h, midnight to midnight local). Bounds shift at midnight PT regardless of DST.
- Live state (queued/running counts and oldest-queued/oldest-running ages) is omitted: this is a historical view, those signals only make sense in the rolling window.
- See [`status.md`](status.md) for full methodology, runner table, and alert thresholds.
