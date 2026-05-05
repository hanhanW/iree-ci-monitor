# iree-ci-monitor

_Updated: 2026-05-05 00:06 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 32 | 2 | [14m13s](https://github.com/iree-org/iree/actions/runs/25361915751/job/74364110260) | 0 | [14m28s](https://github.com/iree-org/iree/actions/runs/25354816778/job/74342405774) | [2h34m](https://github.com/iree-org/iree/actions/runs/25343205335/job/74306876760) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 16 | 0 | — | 0 | [2m43s](https://github.com/iree-org/iree/actions/runs/25352771855/job/74336341150) | [1h02m](https://github.com/iree-org/iree/actions/runs/25345874964/job/74315535706) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 16 | 0 | — | 1 | [5m39s](https://github.com/iree-org/iree/actions/runs/25359682065/job/74357349052) | [55m57s](https://github.com/iree-org/iree/actions/runs/25343349132/job/74307441387) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 16 | 0 | — | 0 | [8m21s](https://github.com/iree-org/iree/actions/runs/25352771855/job/74336341136) | [46m59s](https://github.com/iree-org/iree/actions/runs/25354816778/job/74342405812) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 16 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/25361915751/job/74364110234) | 0 | [20m21s](https://github.com/iree-org/iree/actions/runs/25354325697/job/74340810674) | [42m36s](https://github.com/iree-org/iree/actions/runs/25354816778/job/74342405784) | 0% (0/2) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 16 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/25361915751/job/74364110296) | 0 | [15m01s](https://github.com/iree-org/iree/actions/runs/25359682065/job/74357349124) | [35m31s](https://github.com/iree-org/iree/actions/runs/25345874964/job/74315535650) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 32 | 0 | — | 0 | [10m38s](https://github.com/iree-org/iree/actions/runs/25354325697/job/74340810668) | [23m59s](https://github.com/iree-org/iree/actions/runs/25343349132/job/74307441671) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 16 | 0 | — | 1 | [4m08s](https://github.com/iree-org/iree/actions/runs/25354816778/job/74342405725) | [20m22s](https://github.com/iree-org/iree/actions/runs/25346316029/job/74317075024) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 16 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/25361915751/job/74364110220) | 0 | [6m57s](https://github.com/iree-org/iree/actions/runs/25355717889/job/74345145619) | [18m39s](https://github.com/iree-org/iree/actions/runs/25346316029/job/74317075239) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 32 | 0 | — | 1 | [5m41s](https://github.com/iree-org/iree/actions/runs/25346316029/job/74317075224) | [17m39s](https://github.com/iree-org/iree/actions/runs/25343349132/job/74307441567) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 16 | 0 | — | 1 | [6m02s](https://github.com/iree-org/iree/actions/runs/25359682065/job/74357349178) | [11m30s](https://github.com/iree-org/iree/actions/runs/25343349132/job/74307441683) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 16 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25359682065/job/74357349128) | [6m50s](https://github.com/iree-org/iree/actions/runs/25343349132/job/74307441447) | 0% (0/2) | `iree-mi308-1` |
| `Linux,X64,rdna3` | self-hosted | 16 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/25361915751/job/74364110261) | 0 | [43s](https://github.com/iree-org/iree/actions/runs/25345874964/job/74315535729) | [6m29s](https://github.com/iree-org/iree/actions/runs/25350866726/job/74331036761) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 64 | 0 | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/25360275330/job/74358946919) | [2m32s](https://github.com/iree-org/iree/actions/runs/25346316029/job/74317075231) | 0% (0/8) | 64 |
| `azure-windows-scale` | ossci | 18 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25354325695/job/74340339094) | [2m26s](https://github.com/iree-org/iree/actions/runs/25361915793/job/74363313664) | 0% (0/1) | 18 |
| `azure-linux-scale` | ossci | 92 | 0 | — | 1 | [11s](https://github.com/iree-org/iree/actions/runs/25359833075/job/74356849375) | [1m53s](https://github.com/iree-org/iree/actions/runs/25361915793/job/74363313370) | 0% (0/6) | 89 |
| `windows-2022` | github-hosted | 56 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25356187309/job/74346072596) | [42s](https://github.com/iree-org/iree/actions/runs/25345874992/job/74314604525) | 0% (0/3) | 56 |
| `ubuntu-24.04-arm` | github-hosted | 57 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25359682070/job/74356376649) | [40s](https://github.com/iree-org/iree/actions/runs/25345874992/job/74314604492) | 0% (0/3) | 57 |
| `ubuntu-24.04` | github-hosted | 348 | 0 | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/25359682065/job/74357349054) | [38s](https://github.com/iree-org/iree/actions/runs/25359833075/job/74356849321) | 0% (0/35) | 345 |
| `macos-14` | github-hosted | 56 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25360275331/job/74358236483) | [18s](https://github.com/iree-org/iree/actions/runs/25361915793/job/74363313388) | 0% (0/3) | 56 |
| `ubuntu-latest` | github-hosted | 17 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25352608330/job/74335282908) | [9s](https://github.com/iree-org/iree/actions/runs/25361777858/job/74362799513) | 0% (0/3) | 17 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25343349132/job/74307441334) | [2s](https://github.com/iree-org/iree/actions/runs/25359682065/job/74357349045) | 0% (0/2) | 16 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1092 | 5% (53/1089) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 833 | 1% (9/832) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 920 | 2% (21/918) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 797 | 6% (49/796) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 256 | 2% (4/256) |  | 3m48s ago |
| `shark10-ci-2` | `Linux,X64,iree-w7900`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64` | 5 | 0% (0/5) |  | 7d09h ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h34m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
