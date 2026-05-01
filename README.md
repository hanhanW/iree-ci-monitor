# iree-ci-monitor

_Updated: 2026-05-01 00:14 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 34 | 5 | [7h11m](https://github.com/iree-org/iree/actions/runs/25195139781/job/73874984521) | 0 | [1h33m](https://github.com/iree-org/iree/actions/runs/25203443657/job/73899688398) | [6h27m](https://github.com/iree-org/iree/actions/runs/25193199667/job/73868542401) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 17 | 2 | [7h11m](https://github.com/iree-org/iree/actions/runs/25195139781/job/73874984467) | 0 | [1h39m](https://github.com/iree-org/iree/actions/runs/25197755860/job/73882571538) | [4h21m](https://github.com/iree-org/iree/actions/runs/25191741191/job/73864054593) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 17 | 2 | [7h11m](https://github.com/iree-org/iree/actions/runs/25195139781/job/73874984608) | 0 | [1h09m](https://github.com/iree-org/iree/actions/runs/25198150944/job/73884010877) | [4h09m](https://github.com/iree-org/iree/actions/runs/25195977379/job/73877312019) | 0% (0/3) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 17 | 0 | — | 0 | [19m17s](https://github.com/iree-org/iree/actions/runs/25202926956/job/73898161548) | [1h41m](https://github.com/iree-org/iree/actions/runs/25191741191/job/73864054594) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 17 | 2 | [1h44m](https://github.com/iree-org/iree/actions/runs/25203443657/job/73899688274) | 1 | [29m36s](https://github.com/iree-org/iree/actions/runs/25195139781/job/73874984478) | [1h17m](https://github.com/iree-org/iree/actions/runs/25193199667/job/73868542493) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 17 | 0 | — | 1 | [11m32s](https://github.com/iree-org/iree/actions/runs/25203443657/job/73899688227) | [1h16m](https://github.com/iree-org/iree/actions/runs/25191741191/job/73864054554) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 34 | 0 | — | 0 | [14m16s](https://github.com/iree-org/iree/actions/runs/25198150944/job/73884010881) | [1h12m](https://github.com/iree-org/iree/actions/runs/25193007052/job/73868033549) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 17 | 2 | [1h03m](https://github.com/iree-org/iree/actions/runs/25204484740/job/73902719702) | 0 | [20m49s](https://github.com/iree-org/iree/actions/runs/25203443657/job/73899688174) | [1h10m](https://github.com/iree-org/iree/actions/runs/25193199667/job/73868542305) | 33% (1/3) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 39 | 0 | — | 0 | [11m24s](https://github.com/iree-org/iree/actions/runs/25203443657/job/73899688316) | [1h07m](https://github.com/iree-org/iree/actions/runs/25191741191/job/73864054575) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 17 | 0 | — | 0 | [27m42s](https://github.com/iree-org/iree/actions/runs/25196262788/job/73878205603) | [1h00m](https://github.com/iree-org/iree/actions/runs/25191741191/job/73864054650) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 17 | 0 | — | 0 | [8m38s](https://github.com/iree-org/iree/actions/runs/25197755860/job/73882571532) | [45m29s](https://github.com/iree-org/iree/actions/runs/25193199667/job/73868542459) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 17 | 0 | — | 0 | [7m28s](https://github.com/iree-org/iree/actions/runs/25195139781/job/73874984533) | [40m21s](https://github.com/iree-org/iree/actions/runs/25193803956/job/73870588469) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 98 | 0 | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/25193749565/job/73869563062) | [2m07s](https://github.com/iree-org/iree/actions/runs/25198150944/job/73883287685) | 0% (0/18) | 92 |
| `windows-2022` | github-hosted | 56 | 0 | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/25193803967/job/73869823957) | [1m19s](https://github.com/iree-org/iree/actions/runs/25204705635/job/73902907230) | 0% (0/9) | 54 |
| `macos-14` | github-hosted | 56 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25191599281/job/73863013731) | [1m11s](https://github.com/iree-org/iree/actions/runs/25196262792/job/73877464170) | 0% (0/9) | 56 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 68 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25191741191/job/73864054753) | [1m02s](https://github.com/iree-org/iree/actions/runs/25193199667/job/73868542333) | 8% (1/12) | 63 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 17 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25192541274/job/73866770203) | [53s](https://github.com/iree-org/iree/actions/runs/25196262788/job/73878205653) | 0% (0/3) | `iree-mi308-1` |
| `ubuntu-24.04-arm` | github-hosted | 57 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25204546331/job/73902372705) | [13s](https://github.com/iree-org/iree/actions/runs/25204705635/job/73902907241) | 0% (0/9) | 56 |
| `ubuntu-24.04` | github-hosted | 361 | 0 | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/25203443664/job/73898970033) | [9s](https://github.com/iree-org/iree/actions/runs/25204546331/job/73902372727) | 3% (2/64) | 349 |
| `ubuntu-latest` | github-hosted | 27 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25204484054/job/73902168895) | [8s](https://github.com/iree-org/iree/actions/runs/25196261587/job/73877432636) | 0% (0/6) | 27 |
| `azure-windows-scale` | ossci | 18 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25197755841/job/73882096525) | [2s](https://github.com/iree-org/iree/actions/runs/25196262792/job/73877464260) | 33% (1/3) | 18 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 17 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25192541274/job/73866770109) | [2s](https://github.com/iree-org/iree/actions/runs/25204705621/job/73903705049) | 33% (1/3) | 17 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 960 | 3% (25/957) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 474 | 7% (32/473) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1110 | 5% (55/1106) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 902 | 1% (11/901) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 274 | 1% (4/273) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 323 | 13% (42/321) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 7h11m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 7h11m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 7h11m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h12m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 6h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h10m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h16m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 4h21m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 4h09m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h41m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h07m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
