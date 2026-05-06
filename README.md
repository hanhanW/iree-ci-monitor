# iree-ci-monitor

_Updated: 2026-05-05 18:08 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 21 | 1 | [6h23m](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481178926) | 0 | [24m43s](https://github.com/iree-org/iree/actions/runs/25409390616/job/74528060634) | [1h40m](https://github.com/iree-org/iree/actions/runs/25396049629/job/74487009468) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 42 | 2 | [6h23m](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481179045) | 0 | [32m45s](https://github.com/iree-org/iree/actions/runs/25406956552/job/74520847627) | [1h40m](https://github.com/iree-org/iree/actions/runs/25399796321/job/74497560820) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 21 | 1 | [6h23m](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481178928) | 0 | [25m16s](https://github.com/iree-org/iree/actions/runs/25409390616/job/74528060762) | [1h34m](https://github.com/iree-org/iree/actions/runs/25396046742/job/74487539738) | 50% (1/2) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 21 | 0 | — | 1 | [11m02s](https://github.com/iree-org/iree/actions/runs/25403224533/job/74508965274) | [1h30m](https://github.com/iree-org/iree/actions/runs/25396049629/job/74487009409) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 21 | 1 | [6h23m](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481178887) | 0 | [11m12s](https://github.com/iree-org/iree/actions/runs/25406956552/job/74520847663) | [1h23m](https://github.com/iree-org/iree/actions/runs/25396049629/job/74487009412) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 21 | 0 | — | 1 | [3m54s](https://github.com/iree-org/iree/actions/runs/25406956552/job/74520847618) | [37m22s](https://github.com/iree-org/iree/actions/runs/25398878971/job/74494182122) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 21 | 0 | — | 1 | [4m17s](https://github.com/iree-org/iree/actions/runs/25385358897/job/74448759782) | [35m18s](https://github.com/iree-org/iree/actions/runs/25396046742/job/74487539626) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 21 | 1 | [6h23m](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481178975) | 0 | [6m06s](https://github.com/iree-org/iree/actions/runs/25396046742/job/74487539740) | [32m29s](https://github.com/iree-org/iree/actions/runs/25399796321/job/74497560624) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 21 | 1 | [6h23m](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481178872) | 0 | [8m55s](https://github.com/iree-org/iree/actions/runs/25402877605/job/74507951516) | [32m24s](https://github.com/iree-org/iree/actions/runs/25396049629/job/74487009364) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 42 | 1 | [6h23m](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481178917) | 1 | [8m13s](https://github.com/iree-org/iree/actions/runs/25389628161/job/74461688921) | [31m57s](https://github.com/iree-org/iree/actions/runs/25396049629/job/74487009408) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 21 | 1 | [6h23m](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481179071) | 0 | [7m14s](https://github.com/iree-org/iree/actions/runs/25409390616/job/74528060712) | [27m11s](https://github.com/iree-org/iree/actions/runs/25404683548/job/74514032860) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 42 | 2 | [6h23m](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481179062) | 0 | [5m17s](https://github.com/iree-org/iree/actions/runs/25399796321/job/74497560828) | [24m34s](https://github.com/iree-org/iree/actions/runs/25402877605/job/74507951590) | 25% (1/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 21 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25389628161/job/74461688996) | [5m25s](https://github.com/iree-org/iree/actions/runs/25404961935/job/74514687193) | 0% (0/2) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 84 | 0 | — | 2 | [9s](https://github.com/iree-org/iree/actions/runs/25385358897/job/74448759753) | [4m54s](https://github.com/iree-org/iree/actions/runs/25396046742/job/74487539777) | 25% (2/8) | 80 |
| `macos-14` | github-hosted | 84 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25399796429/job/74496071055) | [1m51s](https://github.com/iree-org/iree/actions/runs/25395682280/job/74481711484) | 0% (0/6) | 81 |
| `windows-2022` | github-hosted | 84 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25404961938/job/74513647488) | [1m36s](https://github.com/iree-org/iree/actions/runs/25395682280/job/74481711399) | 0% (0/6) | 81 |
| `ubuntu-24.04` | github-hosted | 463 | 0 | — | 6 | [8s](https://github.com/iree-org/iree/actions/runs/25399796321/job/74497560800) | [1m24s](https://github.com/iree-org/iree/actions/runs/25395491735/job/74482354257) | 6% (2/35) | 447 |
| `ubuntu-24.04-arm` | github-hosted | 84 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25399796429/job/74496071125) | [1m07s](https://github.com/iree-org/iree/actions/runs/25395682280/job/74481711372) | 0% (0/6) | 81 |
| `azure-linux-scale` | ossci | 146 | 0 | — | 1 | [10s](https://github.com/iree-org/iree/actions/runs/25395694697/job/74481974808) | [27s](https://github.com/iree-org/iree/actions/runs/25391318139/job/74466325020) | 0% (0/13) | 142 |
| `ubuntu-latest` | github-hosted | 35 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25391316897/job/74466274414) | [12s](https://github.com/iree-org/iree/actions/runs/25384822662/job/74442868384) | 0% (0/4) | 35 |
| `azure-windows-scale` | ossci | 28 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25404683549/job/74512762631) | [8s](https://github.com/iree-org/iree/actions/runs/25396046506/job/74483428753) | 50% (1/2) | 26 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 21 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25385358897/job/74448759507) | [2s](https://github.com/iree-org/iree/actions/runs/25406956552/job/74520847523) | 0% (0/2) | 20 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 839 | 6% (53/838) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 992 | 4% (41/989) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 793 | 2% (14/791) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 699 | 1% (6/698) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 233 | 1% (3/232) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 6h23m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 6h23m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 6h23m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 6h23m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 6h23m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 6h23m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job waiting 6h23m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 6h23m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 6h23m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h40m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h40m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h30m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h23m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h34m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
