# iree-ci-monitor

_Updated: 2026-04-29 00:10 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 13 | 5 | [6h05m](https://github.com/iree-org/iree/actions/runs/25085590895/job/73500942592) | 0 | [1h35m](https://github.com/iree-org/iree/actions/runs/25090083229/job/73514611500) | [6h01m](https://github.com/iree-org/iree/actions/runs/25079278088/job/73481188879) | — | `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 13 | 3 | [6h05m](https://github.com/iree-org/iree/actions/runs/25085590895/job/73500942550) | 1 | [34m03s](https://github.com/iree-org/iree/actions/runs/25094079135/job/73527431035) | [5h05m](https://github.com/iree-org/iree/actions/runs/25079278088/job/73481188904) | — | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 13 | 2 | [39m55s](https://github.com/iree-org/iree/actions/runs/25094079135/job/73527431048) | 0 | [28m19s](https://github.com/iree-org/iree/actions/runs/25085978245/job/73502095789) | [3h06m](https://github.com/iree-org/iree/actions/runs/25078103342/job/73477137689) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 26 | 1 | [21m26s](https://github.com/iree-org/iree/actions/runs/25094689645/job/73529356046) | 0 | [17m07s](https://github.com/iree-org/iree/actions/runs/25087370054/job/73506252967) | [2h53m](https://github.com/iree-org/iree/actions/runs/25079278088/job/73481188933) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 39 | 0 | — | 1 | [8m59s](https://github.com/iree-org/iree/actions/runs/25085590895/job/73500943171) | [2h51m](https://github.com/iree-org/iree/actions/runs/25078103342/job/73477137795) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 26 | 0 | — | 0 | [11m22s](https://github.com/iree-org/iree/actions/runs/25090083229/job/73514611543) | [2h44m](https://github.com/iree-org/iree/actions/runs/25078103342/job/73477137736) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 13 | 0 | — | 0 | [29m09s](https://github.com/iree-org/iree/actions/runs/25093569755/job/73525928465) | [2h36m](https://github.com/iree-org/iree/actions/runs/25079278088/job/73481188747) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 13 | 0 | — | 0 | [11m27s](https://github.com/iree-org/iree/actions/runs/25087722639/job/73507422837) | [2h31m](https://github.com/iree-org/iree/actions/runs/25079278088/job/73481188905) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 13 | 0 | — | 1 | [10m20s](https://github.com/iree-org/iree/actions/runs/25091459647/job/73518748130) | [2h30m](https://github.com/iree-org/iree/actions/runs/25079278088/job/73481188900) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 13 | 0 | — | 0 | [10m54s](https://github.com/iree-org/iree/actions/runs/25087370054/job/73506252896) | [2h30m](https://github.com/iree-org/iree/actions/runs/25079278088/job/73481188826) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 13 | 0 | — | 0 | [13m48s](https://github.com/iree-org/iree/actions/runs/25087370054/job/73506252922) | [2h27m](https://github.com/iree-org/iree/actions/runs/25079278088/job/73481188857) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 13 | 1 | [21m26s](https://github.com/iree-org/iree/actions/runs/25094689645/job/73529355957) | 1 | [10m50s](https://github.com/iree-org/iree/actions/runs/25087722639/job/73507422784) | [2h22m](https://github.com/iree-org/iree/actions/runs/25078103342/job/73477137577) | 0% (0/1) | `shark75-ci` |
| `macos-15-intel` | github-hosted | 3 | 0 | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/25087722646/job/73506889957) | [4m22s](https://github.com/iree-org/iree/actions/runs/25085978240/job/73501540005) | — | 3 |
| `ubuntu-latest` | github-hosted | 30 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25087368729/job/73505769326) | [2m24s](https://github.com/iree-org/iree/actions/runs/25093917124/job/73526100622) | 0% (0/3) | 30 |
| `macos-14` | github-hosted | 56 | 0 | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/25087370027/job/73505945348) | [2m14s](https://github.com/iree-org/iree/actions/runs/25094079131/job/73526753477) | 0% (0/3) | 54 |
| `azure-linux-scale` | ossci | 92 | 0 | — | 9 | [9s](https://github.com/iree-org/iree/actions/runs/25080899203/job/73485518028) | [1m51s](https://github.com/iree-org/iree/actions/runs/25090083219/job/73514160508) | 0% (0/6) | 88 |
| `windows-2022` | github-hosted | 53 | 0 | — | 4 | [3s](https://github.com/iree-org/iree/actions/runs/25087112807/job/73505203152) | [1m42s](https://github.com/iree-org/iree/actions/runs/25093569744/job/73525146906) | 0% (0/3) | 50 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 3 | 0 | — | 0 | [1m35s](https://github.com/iree-org/iree/actions/runs/25085978240/job/73501539902) | [1m42s](https://github.com/iree-org/iree/actions/runs/25087722646/job/73506889916) | — | 3 |
| `ubuntu-24.04-arm` | github-hosted | 54 | 0 | — | 4 | [2s](https://github.com/iree-org/iree/actions/runs/25093480375/job/73524743064) | [1m33s](https://github.com/iree-org/iree/actions/runs/25095516710/job/73531297354) | 0% (0/3) | 51 |
| `ubuntu-24.04` | github-hosted | 316 | 0 | — | 6 | [2s](https://github.com/iree-org/iree/actions/runs/25090083229/job/73514611422) | [1m28s](https://github.com/iree-org/iree/actions/runs/25094079131/job/73526753433) | 27% (8/30) | 314 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 52 | 0 | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/25093569755/job/73525928462) | [16s](https://github.com/iree-org/iree/actions/runs/25085978245/job/73502095818) | 25% (1/4) | 52 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 13 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25091459647/job/73518748022) | [2s](https://github.com/iree-org/iree/actions/runs/25094079135/job/73527430890) | 100% (1/1) | 13 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 13 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25094079135/job/73527431103) | [2s](https://github.com/iree-org/iree/actions/runs/25091459647/job/73518748100) | 0% (0/1) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 17 | 1 | [4m32s](https://github.com/iree-org/iree/actions/runs/25095516710/job/73531297511) | 1 | [1s](https://github.com/iree-org/iree/actions/runs/25087722646/job/73506889946) | [1s](https://github.com/iree-org/iree/actions/runs/25094689647/job/73528562871) | 0% (0/1) | 16 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 764 | 4% (30/759) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 646 | 2% (10/641) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 75 | 9% (7/74) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 689 | 3% (22/683) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 206 | 1% (2/203) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 466 | 14% (63/462) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 6h05m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 6h05m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h30m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h44m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 3h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h53m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h22m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h36m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 2h30m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 6h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 5h05m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h31m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h27m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h51m (> 1h00m)
- **[high-failure-main]** `ubuntu-24.04` main-branch failure rate 27% (8/30)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
