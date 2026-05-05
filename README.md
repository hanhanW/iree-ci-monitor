# iree-ci-monitor

_Updated: 2026-05-05 05:46 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 9 | 0 | — | 0 | [27m05s](https://github.com/iree-org/iree/actions/runs/25359682065/job/74357349158) | [1h15m](https://github.com/iree-org/iree/actions/runs/25371924407/job/74398729411) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 9 | 0 | — | 0 | [25m41s](https://github.com/iree-org/iree/actions/runs/25364929954/job/74375118193) | [50m19s](https://github.com/iree-org/iree/actions/runs/25373450592/job/74403622882) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 18 | 0 | — | 0 | [25m02s](https://github.com/iree-org/iree/actions/runs/25370011042/job/74391984342) | [44m37s](https://github.com/iree-org/iree/actions/runs/25360275330/job/74358946911) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 9 | 0 | — | 0 | [5m39s](https://github.com/iree-org/iree/actions/runs/25359682065/job/74357349052) | [35m32s](https://github.com/iree-org/iree/actions/runs/25373450592/job/74403622761) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 9 | 0 | — | 0 | [7m15s](https://github.com/iree-org/iree/actions/runs/25364929954/job/74375118242) | [32m04s](https://github.com/iree-org/iree/actions/runs/25371924407/job/74398729349) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 9 | 0 | — | 0 | [9m57s](https://github.com/iree-org/iree/actions/runs/25373450592/job/74403622789) | [28m41s](https://github.com/iree-org/iree/actions/runs/25361915751/job/74364110220) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 9 | 0 | — | 0 | [15m01s](https://github.com/iree-org/iree/actions/runs/25359682065/job/74357349124) | [24m15s](https://github.com/iree-org/iree/actions/runs/25360275330/job/74358946902) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 9 | 0 | — | 0 | [6m30s](https://github.com/iree-org/iree/actions/runs/25364929954/job/74375118226) | [17m33s](https://github.com/iree-org/iree/actions/runs/25370011042/job/74391984288) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 9 | 0 | — | 0 | [9m46s](https://github.com/iree-org/iree/actions/runs/25361915751/job/74364110230) | [15m39s](https://github.com/iree-org/iree/actions/runs/25370011042/job/74391984323) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 18 | 0 | — | 0 | [11m04s](https://github.com/iree-org/iree/actions/runs/25359682065/job/74357349095) | [15m03s](https://github.com/iree-org/iree/actions/runs/25370011042/job/74391984361) | 25% (1/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 18 | 0 | — | 0 | [5m58s](https://github.com/iree-org/iree/actions/runs/25355717889/job/74345145738) | [13m42s](https://github.com/iree-org/iree/actions/runs/25373450592/job/74403622798) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 9 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25373450592/job/74403622723) | [5m59s](https://github.com/iree-org/iree/actions/runs/25364929954/job/74375118115) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 64 | 0 | — | 0 | [13s](https://github.com/iree-org/iree/actions/runs/25371924420/job/74397368133) | [2m45s](https://github.com/iree-org/iree/actions/runs/25361915793/job/74363313442) | 0% (0/14) | 61 |
| `azure-windows-scale` | ossci | 12 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25364929962/job/74373290309) | [2m26s](https://github.com/iree-org/iree/actions/runs/25361915793/job/74363313664) | 0% (0/2) | 12 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m52s](https://github.com/iree-org/iree/actions/runs/25369643681/job/74389509170) | [1m52s](https://github.com/iree-org/iree/actions/runs/25369643681/job/74389509170) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 39 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25371924420/job/74397368095) | [1m04s](https://github.com/iree-org/iree/actions/runs/25361779370/job/74362821056) | 0% (0/6) | 39 |
| `macos-14` | github-hosted | 39 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25373450620/job/74402499024) | [18s](https://github.com/iree-org/iree/actions/runs/25361915793/job/74363313388) | 0% (0/6) | 39 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 36 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25359682065/job/74357349026) | [11s](https://github.com/iree-org/iree/actions/runs/25361915751/job/74364110353) | 0% (0/8) | 36 |
| `ubuntu-24.04` | github-hosted | 218 | 0 | — | 2 | [8s](https://github.com/iree-org/iree/actions/runs/25355717889/job/74345886992) | [10s](https://github.com/iree-org/iree/actions/runs/25360174992/job/74358073923) | 2% (1/42) | 218 |
| `ubuntu-latest` | github-hosted | 31 | 0 | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25360173925/job/74357867561) | [10s](https://github.com/iree-org/iree/actions/runs/25371924365/job/74397332427) | 0% (0/4) | 31 |
| `windows-2022` | github-hosted | 38 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25360275331/job/74358236437) | [7s](https://github.com/iree-org/iree/actions/runs/25370011048/job/74390839776) | 0% (0/6) | 38 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25369622983/job/74389437589) | [3s](https://github.com/iree-org/iree/actions/runs/25369622983/job/74389437589) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 9 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25360275330/job/74358946800) | [2s](https://github.com/iree-org/iree/actions/runs/25373450592/job/74403622754) | 0% (0/2) | 9 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 9 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25364929954/job/74375118205) | [2s](https://github.com/iree-org/iree/actions/runs/25373450592/job/74403622806) | 0% (0/2) | `iree-mi308-1` |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1113 | 5% (53/1111) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 935 | 2% (21/934) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 817 | 6% (52/817) |  | 20m08s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 843 | 1% (9/843) |  | 54m53s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 260 | 2% (4/260) |  | 1h04m ago |
| `shark10-ci-2` | `Linux,X64,iree-w7900`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64` | 5 | 0% (0/5) |  | 7d15h ago |

## Alerts

- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h15m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
