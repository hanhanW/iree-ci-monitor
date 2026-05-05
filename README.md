# iree-ci-monitor

_Updated: 2026-05-05 11:50 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 15 | 1 | [5m29s](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481178928) | 0 | [14m10s](https://github.com/iree-org/iree/actions/runs/25382644326/job/74436329523) | [1h02m](https://github.com/iree-org/iree/actions/runs/25377325384/job/74416970433) | 33% (1/3) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 30 | 2 | [5m29s](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481179045) | 0 | [15m40s](https://github.com/iree-org/iree/actions/runs/25385358897/job/74448759697) | [52m47s](https://github.com/iree-org/iree/actions/runs/25388308899/job/74456846986) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 15 | 1 | [5m29s](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481178887) | 0 | [11m00s](https://github.com/iree-org/iree/actions/runs/25384048581/job/74441803438) | [50m19s](https://github.com/iree-org/iree/actions/runs/25373450592/job/74403622882) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 15 | 0 | — | 1 | [1m49s](https://github.com/iree-org/iree/actions/runs/25382644326/job/74436329292) | [44m57s](https://github.com/iree-org/iree/actions/runs/25380922129/job/74430454548) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 15 | 1 | [5m29s](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481178926) | 0 | [12m07s](https://github.com/iree-org/iree/actions/runs/25377325384/job/74416970306) | [32m04s](https://github.com/iree-org/iree/actions/runs/25371924407/job/74398729349) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 15 | 1 | [5m29s](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481178872) | 0 | [9m57s](https://github.com/iree-org/iree/actions/runs/25373450592/job/74403622789) | [29m21s](https://github.com/iree-org/iree/actions/runs/25389628161/job/74461689039) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 30 | 1 | [5m29s](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481178917) | 1 | [6m08s](https://github.com/iree-org/iree/actions/runs/25384048581/job/74441803402) | [19m59s](https://github.com/iree-org/iree/actions/runs/25388308899/job/74456846863) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 15 | 1 | [5m29s](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481178975) | 0 | [5m04s](https://github.com/iree-org/iree/actions/runs/25384048581/job/74441803729) | [19m53s](https://github.com/iree-org/iree/actions/runs/25388308899/job/74456846859) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 15 | 1 | [5m29s](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481179071) | 0 | [6m34s](https://github.com/iree-org/iree/actions/runs/25380922129/job/74430454768) | [17m33s](https://github.com/iree-org/iree/actions/runs/25370011042/job/74391984288) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 30 | 2 | [5m29s](https://github.com/iree-org/iree/actions/runs/25394229643/job/74481179062) | 0 | [4m59s](https://github.com/iree-org/iree/actions/runs/25373450592/job/74403626311) | [17m11s](https://github.com/iree-org/iree/actions/runs/25389628161/job/74461688920) | 33% (2/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 15 | 0 | — | 1 | [2m11s](https://github.com/iree-org/iree/actions/runs/25389628161/job/74461688851) | [15m39s](https://github.com/iree-org/iree/actions/runs/25370011042/job/74391984323) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 15 | 0 | — | 1 | [12s](https://github.com/iree-org/iree/actions/runs/25388308899/job/74456846643) | [13m00s](https://github.com/iree-org/iree/actions/runs/25382644326/job/74436329510) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 60 | 0 | — | 2 | [10s](https://github.com/iree-org/iree/actions/runs/25382644326/job/74436329410) | [6m09s](https://github.com/iree-org/iree/actions/runs/25388308899/job/74456846686) | 25% (3/12) | 60 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m52s](https://github.com/iree-org/iree/actions/runs/25369643681/job/74389509170) | [1m52s](https://github.com/iree-org/iree/actions/runs/25369643681/job/74389509170) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 129 | 0 | — | 14 | [11s](https://github.com/iree-org/iree/actions/runs/25393406921/job/74474108546) | [1m14s](https://github.com/iree-org/iree/actions/runs/25392158379/job/74469272973) | 0% (0/21) | 129 |
| `macos-14` | github-hosted | 73 | 2 | [2m23s](https://github.com/iree-org/iree/actions/runs/25395682280/job/74481711329) | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25395682280/job/74481711348) | [38s](https://github.com/iree-org/iree/actions/runs/25383121771/job/74437157146) | 0% (0/10) | 71 |
| `ubuntu-24.04-arm` | github-hosted | 72 | 1 | [2m23s](https://github.com/iree-org/iree/actions/runs/25395682280/job/74481711372) | 2 | [3s](https://github.com/iree-org/iree/actions/runs/25395491670/job/74481075140) | [28s](https://github.com/iree-org/iree/actions/runs/25395682280/job/74481711277) | 0% (0/9) | 71 |
| `ubuntu-latest` | github-hosted | 38 | 0 | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25373491749/job/74402743534) | [27s](https://github.com/iree-org/iree/actions/runs/25383458423/job/74437872953) | 0% (0/6) | 38 |
| `windows-2022` | github-hosted | 72 | 3 | [2m23s](https://github.com/iree-org/iree/actions/runs/25395682280/job/74481711193) | 3 | [4s](https://github.com/iree-org/iree/actions/runs/25383338376/job/74437729698) | [21s](https://github.com/iree-org/iree/actions/runs/25392383300/job/74470976798) | 0% (0/9) | 69 |
| `ubuntu-24.04` | github-hosted | 373 | 5 | [2m23s](https://github.com/iree-org/iree/actions/runs/25395682280/job/74481711063) | 14 | [8s](https://github.com/iree-org/iree/actions/runs/25394229643/job/74476635449) | [14s](https://github.com/iree-org/iree/actions/runs/25382771546/job/74435364116) | 5% (3/55) | 367 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 15 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25371924407/job/74398729260) | [3s](https://github.com/iree-org/iree/actions/runs/25382644326/job/74436329431) | 0% (0/3) | 15 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 15 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25371924407/job/74398729440) | [3s](https://github.com/iree-org/iree/actions/runs/25384048581/job/74441803363) | 0% (0/3) | `iree-mi308-1` |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25369622983/job/74389437589) | [3s](https://github.com/iree-org/iree/actions/runs/25369622983/job/74389437589) | 0% (0/1) | 1 |
| `azure-windows-scale` | ossci | 24 | 1 | [2m23s](https://github.com/iree-org/iree/actions/runs/25395682280/job/74481711522) | 2 | [1s](https://github.com/iree-org/iree/actions/runs/25395491670/job/74481075197) | [2s](https://github.com/iree-org/iree/actions/runs/25393406921/job/74474108585) | 33% (1/3) | 23 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 973 | 2% (21/971) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 858 | 7% (57/857) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1159 | 5% (54/1156) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 272 | 1% (4/271) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 876 | 1% (9/875) | yes | running |
| `shark10-ci-2` | `Linux,X64,iree-w7900`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64` | 5 | 0% (0/5) |  | 7d21h ago |

## Alerts

- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h02m (> 1h00m)
- **[high-failure-main]** `linux-mi325-1gpu-ossci-iree-org` main-branch failure rate 25% (3/12)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
