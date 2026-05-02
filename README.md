# iree-ci-monitor

_Updated: 2026-05-01 18:09 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 50 | 4 | [8h42m](https://github.com/iree-org/iree/actions/runs/25222174334/job/73958116155) | 1 | [4h40m](https://github.com/iree-org/iree/actions/runs/25223228674/job/73962225113) | [7h04m](https://github.com/iree-org/iree/actions/runs/25222502218/job/73960658309) | 0% (0/17) | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 25 | 0 | — | 0 | [4h05m](https://github.com/iree-org/iree/actions/runs/25219713733/job/73949635450) | [6h09m](https://github.com/iree-org/iree/actions/runs/25219918076/job/73950951666) | 0% (0/10) | `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 25 | 1 | [8h42m](https://github.com/iree-org/iree/actions/runs/25222174334/job/73958116059) | 0 | [3h04m](https://github.com/iree-org/iree/actions/runs/25219461262/job/73948748069) | [5h23m](https://github.com/iree-org/iree/actions/runs/25221679391/job/73956141814) | 0% (0/10) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 25 | 0 | — | 0 | [1h32m](https://github.com/iree-org/iree/actions/runs/25219713733/job/73949635483) | [5h10m](https://github.com/iree-org/iree/actions/runs/25228125118/job/73978067256) | 0% (0/10) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 25 | 0 | — | 0 | [2h21m](https://github.com/iree-org/iree/actions/runs/25220729478/job/73953067670) | [4h48m](https://github.com/iree-org/iree/actions/runs/25222502218/job/73960658161) | 0% (0/10) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 25 | 0 | — | 0 | [2h10m](https://github.com/iree-org/iree/actions/runs/25219713733/job/73949635373) | [4h36m](https://github.com/iree-org/iree/actions/runs/25222502218/job/73960658260) | 0% (0/10) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 25 | 0 | — | 0 | [1h37m](https://github.com/iree-org/iree/actions/runs/25219012438/job/73948755107) | [4h08m](https://github.com/iree-org/iree/actions/runs/25223791601/job/73963630062) | 0% (0/10) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 50 | 0 | — | 0 | [1h12m](https://github.com/iree-org/iree/actions/runs/25219918076/job/73950951548) | [3h39m](https://github.com/iree-org/iree/actions/runs/25220983125/job/73953960254) | 10% (2/20) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 50 | 0 | — | 0 | [59m50s](https://github.com/iree-org/iree/actions/runs/25222174334/job/73958116102) | [2h14m](https://github.com/iree-org/iree/actions/runs/25219713733/job/73949635437) | 0% (0/20) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 25 | 0 | — | 0 | [39m23s](https://github.com/iree-org/iree/actions/runs/25221679391/job/73956141613) | [1h36m](https://github.com/iree-org/iree/actions/runs/25222154447/job/73957861096) | 0% (0/10) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 25 | 0 | — | 0 | [42m48s](https://github.com/iree-org/iree/actions/runs/25219713733/job/73949635432) | [1h22m](https://github.com/iree-org/iree/actions/runs/25223791601/job/73963630232) | 0% (0/10) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 25 | 0 | — | 0 | [35m20s](https://github.com/iree-org/iree/actions/runs/25220729478/job/73953067848) | [1h06m](https://github.com/iree-org/iree/actions/runs/25220478946/job/73952149373) | 0% (0/10) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 25 | 0 | — | 0 | [7m41s](https://github.com/iree-org/iree/actions/runs/25225063841/job/73967595422) | [45m33s](https://github.com/iree-org/iree/actions/runs/25219012438/job/73948755167) | 0% (0/10) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 100 | 0 | — | 0 | [17s](https://github.com/iree-org/iree/actions/runs/25221679391/job/73956141651) | [7m05s](https://github.com/iree-org/iree/actions/runs/25222174334/job/73958116142) | 8% (3/40) | 96 |
| `ubuntu-24.04` | github-hosted | 436 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25222154447/job/73957861222) | [2m49s](https://github.com/iree-org/iree/actions/runs/25219574262/job/73949208128) | 3% (5/177) | 426 |
| `windows-2022` | github-hosted | 66 | 0 | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/25234638886/job/73998007060) | [2m23s](https://github.com/iree-org/iree/actions/runs/25219918057/job/73949658349) | 0% (0/30) | 66 |
| `ubuntu-24.04-arm` | github-hosted | 66 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25221679406/job/73955195198) | [2m16s](https://github.com/iree-org/iree/actions/runs/25222502488/job/73957968741) | 0% (0/30) | 66 |
| `macos-14` | github-hosted | 66 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25225063839/job/73966503892) | [2m10s](https://github.com/iree-org/iree/actions/runs/25220502760/job/73951535010) | 0% (0/30) | 66 |
| `azure-windows-scale` | ossci | 22 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25228125116/job/73976706860) | [2m07s](https://github.com/iree-org/iree/actions/runs/25220729477/job/73952252488) | 10% (1/10) | 22 |
| `azure-linux-scale` | ossci | 122 | 0 | — | 0 | [12s](https://github.com/iree-org/iree/actions/runs/25219713757/job/73948653019) | [46s](https://github.com/iree-org/iree/actions/runs/25235327560/job/74000154226) | 0% (0/61) | 121 |
| `ubuntu-latest` | github-hosted | 52 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25219713033/job/73948633415) | [9s](https://github.com/iree-org/iree/actions/runs/25223995480/job/73962907729) | 0% (0/20) | 52 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 25 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25220983125/job/73953960241) | [2s](https://github.com/iree-org/iree/actions/runs/25237508696/job/74007461071) | 0% (0/10) | 24 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1037 | 5% (56/1035) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 902 | 3% (28/901) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 819 | 1% (11/819) |  | 1h20m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 605 | 6% (37/605) |  | 1h20m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 244 | 2% (5/244) |  | 1h23m ago |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 94 | 14% (13/94) |  | 4d03h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 8h42m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 8h42m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h14m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 5h10m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 7h04m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 4h48m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 4h08m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 4h36m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 5h23m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 6h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h22m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h36m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 3h39m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
