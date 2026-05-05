# iree-ci-monitor

_Updated: 2026-05-04 18:07 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 64 | 0 | — | 0 | [32m04s](https://github.com/iree-org/iree/actions/runs/25330573484/job/74264065957) | [3h29m](https://github.com/iree-org/iree/actions/runs/25339888327/job/74295395794) | 0% (0/12) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 32 | 0 | — | 0 | [28m14s](https://github.com/iree-org/iree/actions/runs/25330573484/job/74264066027) | [2h32m](https://github.com/iree-org/iree/actions/runs/25332338190/job/74270444893) | 0% (0/6) | `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 32 | 0 | — | 0 | [35m14s](https://github.com/iree-org/iree/actions/runs/25340435516/job/74297304731) | [2h13m](https://github.com/iree-org/iree/actions/runs/25341534382/job/74301140989) | 0% (0/6) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 32 | 0 | — | 0 | [15m19s](https://github.com/iree-org/iree/actions/runs/25329322746/job/74259712260) | [2h02m](https://github.com/iree-org/iree/actions/runs/25342702473/job/74305161219) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 32 | 0 | — | 0 | [23m18s](https://github.com/iree-org/iree/actions/runs/25350866726/job/74331036457) | [1h38m](https://github.com/iree-org/iree/actions/runs/25340435516/job/74297304630) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 32 | 0 | — | 0 | [9m27s](https://github.com/iree-org/iree/actions/runs/25350866726/job/74331036539) | [1h17m](https://github.com/iree-org/iree/actions/runs/25329744694/job/74261550904) | 0% (0/6) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 32 | 0 | — | 0 | [15m14s](https://github.com/iree-org/iree/actions/runs/25341534382/job/74301140952) | [1h01m](https://github.com/iree-org/iree/actions/runs/25332690900/job/74273124119) | 0% (0/6) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 32 | 0 | — | 0 | [18m48s](https://github.com/iree-org/iree/actions/runs/25346257007/job/74316744153) | [1h00m](https://github.com/iree-org/iree/actions/runs/25343205335/job/74306876765) | 0% (0/6) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 64 | 0 | — | 0 | [11m35s](https://github.com/iree-org/iree/actions/runs/25333663639/job/74274844029) | [59m24s](https://github.com/iree-org/iree/actions/runs/25332690900/job/74273124208) | 0% (0/12) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 64 | 0 | — | 0 | [9m02s](https://github.com/iree-org/iree/actions/runs/25332690900/job/74273124172) | [46m58s](https://github.com/iree-org/iree/actions/runs/25340435516/job/74297304775) | 8% (1/12) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 32 | 0 | — | 0 | [3m56s](https://github.com/iree-org/iree/actions/runs/25330573484/job/74264066020) | [18m44s](https://github.com/iree-org/iree/actions/runs/25342702473/job/74305161168) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 32 | 0 | — | 0 | [3m45s](https://github.com/iree-org/iree/actions/runs/25333663639/job/74274843970) | [16m41s](https://github.com/iree-org/iree/actions/runs/25341534382/job/74301141109) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 32 | 0 | — | 0 | [25s](https://github.com/iree-org/iree/actions/runs/25332950994/job/74272032925) | [9m57s](https://github.com/iree-org/iree/actions/runs/25329744694/job/74261551107) | 0% (0/6) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 128 | 0 | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25328279637/job/74256207242) | [3m54s](https://github.com/iree-org/iree/actions/runs/25331363304/job/74267052010) | 8% (2/24) | 124 |
| `ubuntu-latest` | github-hosted | 26 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25341106947/job/74298309328) | [3m04s](https://github.com/iree-org/iree/actions/runs/25341531810/job/74299738694) | 0% (0/12) | 26 |
| `windows-2022` | github-hosted | 108 | 0 | — | 3 | [4s](https://github.com/iree-org/iree/actions/runs/25331150353/job/74264938020) | [1m51s](https://github.com/iree-org/iree/actions/runs/25334108804/job/74274881949) | 0% (0/18) | 105 |
| `macos-14` | github-hosted | 108 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25337116026/job/74285368149) | [1m38s](https://github.com/iree-org/iree/actions/runs/25329322736/job/74258591138) | 0% (0/18) | 105 |
| `ubuntu-24.04-arm` | github-hosted | 108 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25337116026/job/74285367798) | [1m29s](https://github.com/iree-org/iree/actions/runs/25334108804/job/74274882009) | 0% (0/18) | 105 |
| `ubuntu-24.04` | github-hosted | 639 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25328279637/job/74256207293) | [1m10s](https://github.com/iree-org/iree/actions/runs/25346316029/job/74317075063) | 2% (2/102) | 629 |
| `azure-linux-scale` | ossci | 187 | 0 | — | 4 | [13s](https://github.com/iree-org/iree/actions/runs/25341367018/job/74299219434) | [1m08s](https://github.com/iree-org/iree/actions/runs/25339388787/job/74292788465) | 0% (0/37) | 184 |
| `azure-windows-scale` | ossci | 36 | 0 | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/25350496445/job/74328824084) | [51s](https://github.com/iree-org/iree/actions/runs/25341534324/job/74299950385) | 17% (1/6) | 35 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 32 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25328279637/job/74256228424) | [2s](https://github.com/iree-org/iree/actions/runs/25345874964/job/74315535647) | 67% (4/6) | 32 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1062 | 5% (53/1060) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 895 | 2% (21/894) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 766 | 6% (48/766) |  | 11m52s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 812 | 1% (9/812) |  | 13m08s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 248 | 2% (4/248) |  | 27m06s ago |
| `shark10-ci-2` | `Linux,X64,iree-w7900`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64` | 5 | 0% (0/5) |  | 7d03h ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h29m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h38m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 2h13m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h00m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
