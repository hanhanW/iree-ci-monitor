# iree-ci-monitor

_Updated: 2026-05-01 05:39 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 8 | 0 | — | 0 | [56m47s](https://github.com/iree-org/iree/actions/runs/25204484740/job/73902719816) | [1h56m](https://github.com/iree-org/iree/actions/runs/25203443657/job/73899688274) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 16 | 0 | — | 0 | [31m13s](https://github.com/iree-org/iree/actions/runs/25206915265/job/73915579759) | [1h43m](https://github.com/iree-org/iree/actions/runs/25202926956/job/73898161595) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 8 | 0 | — | 0 | [29m35s](https://github.com/iree-org/iree/actions/runs/25206830378/job/73911950115) | [1h20m](https://github.com/iree-org/iree/actions/runs/25204705621/job/73903705065) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 8 | 0 | — | 0 | [20m58s](https://github.com/iree-org/iree/actions/runs/25206915265/job/73915579774) | [58m28s](https://github.com/iree-org/iree/actions/runs/25204705621/job/73903705162) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 8 | 0 | — | 0 | [18m47s](https://github.com/iree-org/iree/actions/runs/25203443657/job/73899688325) | [53m13s](https://github.com/iree-org/iree/actions/runs/25204705621/job/73903705169) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 8 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25202926956/job/73898161538) | [49m30s](https://github.com/iree-org/iree/actions/runs/25204484740/job/73902719682) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 8 | 0 | — | 0 | [9m01s](https://github.com/iree-org/iree/actions/runs/25206830378/job/73911950034) | [47m07s](https://github.com/iree-org/iree/actions/runs/25204705621/job/73903705104) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 35 | 0 | — | 0 | [34s](https://github.com/iree-org/iree/actions/runs/25204705635/job/73902907305) | [29m50s](https://github.com/iree-org/iree/actions/runs/25206915287/job/73909182977) | 0% (0/8) | 35 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 8 | 0 | — | 0 | [13m26s](https://github.com/iree-org/iree/actions/runs/25206915265/job/73915579752) | [22m29s](https://github.com/iree-org/iree/actions/runs/25204484740/job/73902719722) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 16 | 0 | — | 0 | [10m33s](https://github.com/iree-org/iree/actions/runs/25206915265/job/73915579764) | [21m50s](https://github.com/iree-org/iree/actions/runs/25204705621/job/73903705167) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 8 | 0 | — | 0 | [6m33s](https://github.com/iree-org/iree/actions/runs/25206915265/job/73915579730) | [19m17s](https://github.com/iree-org/iree/actions/runs/25202926956/job/73898161548) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | 0 | [5m42s](https://github.com/iree-org/iree/actions/runs/25206915265/job/73915579750) | [17m38s](https://github.com/iree-org/iree/actions/runs/25206830378/job/73911950110) | 0% (0/1) | `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 17 | 0 | — | 0 | [1m45s](https://github.com/iree-org/iree/actions/runs/25204705621/job/73903705155) | [15m57s](https://github.com/iree-org/iree/actions/runs/25204484740/job/73902719720) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `windows-2022` | github-hosted | 20 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25204546331/job/73902372753) | [3m19s](https://github.com/iree-org/iree/actions/runs/25204705635/job/73902907236) | 0% (0/3) | 20 |
| `macos-14` | github-hosted | 21 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25204484749/job/73902184264) | [2m58s](https://github.com/iree-org/iree/actions/runs/25206915287/job/73909182907) | 0% (0/3) | 21 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m44s](https://github.com/iree-org/iree/actions/runs/25210238746/job/73919140136) | [1m44s](https://github.com/iree-org/iree/actions/runs/25210238746/job/73919140136) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25206830383/job/73908949698) | [1m30s](https://github.com/iree-org/iree/actions/runs/25206915287/job/73909182938) | 0% (0/3) | 21 |
| `ubuntu-24.04` | github-hosted | 165 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25206915265/job/73915579638) | [1m20s](https://github.com/iree-org/iree/actions/runs/25206830383/job/73908949757) | 3% (1/30) | 165 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 32 | 0 | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/25206830378/job/73911950152) | [19s](https://github.com/iree-org/iree/actions/runs/25206915265/job/73915579769) | 25% (1/4) | 32 |
| `ubuntu-latest` | github-hosted | 11 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25212796670/job/73926755131) | [10s](https://github.com/iree-org/iree/actions/runs/25212905687/job/73927072648) | 0% (0/2) | 11 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25206830378/job/73911950069) | [2s](https://github.com/iree-org/iree/actions/runs/25206915265/job/73915579608) | 100% (1/1) | 8 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 8 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25206915265/job/73915579701) | [2s](https://github.com/iree-org/iree/actions/runs/25206830378/job/73911950168) | 0% (0/1) | `iree-mi308-1` |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25210218261/job/73919079681) | [2s](https://github.com/iree-org/iree/actions/runs/25210218261/job/73919079681) | — | 1 |
| `azure-windows-scale` | ossci | 6 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25204484749/job/73902184261) | [1s](https://github.com/iree-org/iree/actions/runs/25206915287/job/73909183011) | 0% (0/1) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1126 | 5% (57/1123) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 966 | 3% (26/963) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 907 | 1% (11/906) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 276 | 2% (5/275) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 323 | 13% (42/321) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 486 | 7% (32/486) |  | 3h02m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h56m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h43m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h20m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
