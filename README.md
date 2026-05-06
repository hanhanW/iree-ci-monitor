# iree-ci-monitor

_Updated: 2026-05-06 00:15 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 28 | 0 | — | 0 | [24m57s](https://github.com/iree-org/iree/actions/runs/25417850768/job/74553696760) | [1h27m](https://github.com/iree-org/iree/actions/runs/25402877605/job/74507951654) | 0% (0/12) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 14 | 0 | — | 0 | [18m18s](https://github.com/iree-org/iree/actions/runs/25417850768/job/74553696701) | [43m07s](https://github.com/iree-org/iree/actions/runs/25406956552/job/74520847611) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 28 | 0 | — | 0 | [12m20s](https://github.com/iree-org/iree/actions/runs/25414453644/job/74543495093) | [31m23s](https://github.com/iree-org/iree/actions/runs/25419265247/job/74558231104) | 0% (0/12) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 14 | 0 | — | 0 | [18m46s](https://github.com/iree-org/iree/actions/runs/25403224533/job/74508965467) | [31m13s](https://github.com/iree-org/iree/actions/runs/25402877605/job/74507951653) | 17% (1/6) | `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 14 | 0 | — | 0 | [10m35s](https://github.com/iree-org/iree/actions/runs/25414480014/job/74543695050) | [27m35s](https://github.com/iree-org/iree/actions/runs/25419800066/job/74560010082) | 0% (0/6) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 14 | 0 | — | 0 | [11m02s](https://github.com/iree-org/iree/actions/runs/25403224533/job/74508965274) | [27m22s](https://github.com/iree-org/iree/actions/runs/25415140705/job/74545545294) | 0% (0/6) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 28 | 0 | — | 0 | [4m12s](https://github.com/iree-org/iree/actions/runs/25414480014/job/74543695099) | [24m34s](https://github.com/iree-org/iree/actions/runs/25402877605/job/74507951590) | 0% (0/12) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 14 | 0 | — | 0 | [8m55s](https://github.com/iree-org/iree/actions/runs/25402877605/job/74507951516) | [23m54s](https://github.com/iree-org/iree/actions/runs/25414453644/job/74543495076) | 0% (0/6) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 14 | 0 | — | 0 | [19m52s](https://github.com/iree-org/iree/actions/runs/25417850768/job/74553696800) | [23m01s](https://github.com/iree-org/iree/actions/runs/25419800066/job/74560010090) | 0% (0/6) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 14 | 0 | — | 0 | [7m44s](https://github.com/iree-org/iree/actions/runs/25414480014/job/74543695059) | [16m46s](https://github.com/iree-org/iree/actions/runs/25415140705/job/74545545464) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 14 | 0 | — | 0 | [7m14s](https://github.com/iree-org/iree/actions/runs/25409390616/job/74528060712) | [14m58s](https://github.com/iree-org/iree/actions/runs/25414453644/job/74543495151) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 14 | 0 | — | 0 | [4m13s](https://github.com/iree-org/iree/actions/runs/25402877605/job/74507951509) | [8m47s](https://github.com/iree-org/iree/actions/runs/25415140705/job/74545545303) | 0% (0/6) | `shark01-ci`, `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 14 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25402877605/job/74507951542) | [5m25s](https://github.com/iree-org/iree/actions/runs/25404961935/job/74514687193) | 0% (0/6) | `iree-mi308-1` |
| `macos-14` | github-hosted | 44 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25416826753/job/74549942013) | [2m51s](https://github.com/iree-org/iree/actions/runs/25419265250/job/74557457176) | 0% (0/18) | 44 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 56 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25402877605/job/74507951644) | [2m18s](https://github.com/iree-org/iree/actions/runs/25403224533/job/74508965489) | 17% (4/24) | 56 |
| `azure-linux-scale` | ossci | 76 | 0 | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/25406956546/job/74520275672) | [2m09s](https://github.com/iree-org/iree/actions/runs/25414453634/job/74542897828) | 0% (0/36) | 76 |
| `windows-2022` | github-hosted | 44 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25403224570/job/74507909285) | [1m41s](https://github.com/iree-org/iree/actions/runs/25419265250/job/74557457246) | 0% (0/18) | 44 |
| `ubuntu-24.04-arm` | github-hosted | 45 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25417850565/job/74552973657) | [1m21s](https://github.com/iree-org/iree/actions/runs/25419265250/job/74557457151) | 0% (0/18) | 45 |
| `ubuntu-24.04` | github-hosted | 269 | 0 | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/25419800066/job/74560010099) | [1m07s](https://github.com/iree-org/iree/actions/runs/25402877605/job/74507951642) | 1% (1/107) | 269 |
| `ubuntu-latest` | github-hosted | 23 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25419264548/job/74557422627) | [10s](https://github.com/iree-org/iree/actions/runs/25404900222/job/74513426377) | 0% (0/12) | 23 |
| `azure-windows-scale` | ossci | 14 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25409390622/job/74527481843) | [2s](https://github.com/iree-org/iree/actions/runs/25402877532/job/74507018982) | 0% (0/6) | 14 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 14 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25416826758/job/74554757118) | [2s](https://github.com/iree-org/iree/actions/runs/25419800066/job/74560010020) | 0% (0/6) | 14 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1023 | 4% (41/1020) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 815 | 2% (14/813) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 718 | 1% (6/717) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 872 | 6% (54/871) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 240 | 1% (3/239) | yes | running |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h27m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
