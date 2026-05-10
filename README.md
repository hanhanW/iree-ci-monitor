# iree-ci-monitor

_Updated: 2026-05-09 18:17 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | 0 | [41m19s](https://github.com/iree-org/iree/actions/runs/25610397679/job/75182635033) | [1h48m](https://github.com/iree-org/iree/actions/runs/25609761497/job/75178282385) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | 0 | [53m36s](https://github.com/iree-org/iree/actions/runs/25610307198/job/75179616269) | [1h05m](https://github.com/iree-org/iree/actions/runs/25609600925/job/75178599501) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | 0 | [3m22s](https://github.com/iree-org/iree/actions/runs/25610397679/job/75182635091) | [1h01m](https://github.com/iree-org/iree/actions/runs/25609761497/job/75178282386) | 0% (0/2) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 0 | — | 0 | [18m22s](https://github.com/iree-org/iree/actions/runs/25608596565/job/75175258837) | [1h01m](https://github.com/iree-org/iree/actions/runs/25609600925/job/75178599494) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 6 | 0 | — | 0 | [12m57s](https://github.com/iree-org/iree/actions/runs/25609761497/job/75178282394) | [50m15s](https://github.com/iree-org/iree/actions/runs/25610307198/job/75179616303) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | 0 | [16m19s](https://github.com/iree-org/iree/actions/runs/25610397679/job/75182635077) | [48m17s](https://github.com/iree-org/iree/actions/runs/25609600925/job/75178599506) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | 0 | [8m55s](https://github.com/iree-org/iree/actions/runs/25609761497/job/75178282346) | [45m11s](https://github.com/iree-org/iree/actions/runs/25610307198/job/75179616274) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 0 | — | 0 | [20m16s](https://github.com/iree-org/iree/actions/runs/25610397679/job/75182635063) | [44m04s](https://github.com/iree-org/iree/actions/runs/25609600925/job/75178599507) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | 0 | [16m58s](https://github.com/iree-org/iree/actions/runs/25610397679/job/75182635001) | [35m39s](https://github.com/iree-org/iree/actions/runs/25609600925/job/75178599484) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | 0 | [13m50s](https://github.com/iree-org/iree/actions/runs/25610397679/job/75182635064) | [21m19s](https://github.com/iree-org/iree/actions/runs/25609600925/job/75178599505) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 0 | — | 0 | [2m11s](https://github.com/iree-org/iree/actions/runs/25610397679/job/75182635014) | [13m54s](https://github.com/iree-org/iree/actions/runs/25608596565/job/75175258829) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | 0 | [5m17s](https://github.com/iree-org/iree/actions/runs/25610307198/job/75179616218) | [13m50s](https://github.com/iree-org/iree/actions/runs/25608596565/job/75175258771) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 31 | 0 | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25609761486/job/75177835806) | [6m25s](https://github.com/iree-org/iree/actions/runs/25612674106/job/75185413467) | 0% (0/6) | 31 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 6 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25610397679/job/75182635034) | [5m35s](https://github.com/iree-org/iree/actions/runs/25610307198/job/75179616264) | 0% (0/1) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 24 | 0 | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/25610397679/job/75182635013) | [2m03s](https://github.com/iree-org/iree/actions/runs/25609600925/job/75178599526) | 0% (0/4) | 24 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25610307209/job/75179252118) | [1m30s](https://github.com/iree-org/iree/actions/runs/25612674106/job/75185413446) | 0% (0/3) | 18 |
| `windows-2022` | github-hosted | 18 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25610397689/job/75182249243) | [1m23s](https://github.com/iree-org/iree/actions/runs/25612674106/job/75185413419) | 0% (0/3) | 18 |
| `ubuntu-24.04` | github-hosted | 113 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25609761497/job/75184368187) | [54s](https://github.com/iree-org/iree/actions/runs/25612674106/job/75185413390) | 0% (0/18) | 113 |
| `macos-14` | github-hosted | 18 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25609761486/job/75177835759) | [39s](https://github.com/iree-org/iree/actions/runs/25612674106/job/75185413433) | 0% (0/3) | 18 |
| `ubuntu-latest` | github-hosted | 13 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25610404648/job/75179507932) | [8s](https://github.com/iree-org/iree/actions/runs/25610404648/job/75179495817) | 0% (0/2) | 13 |
| `azure-windows-scale` | ossci | 6 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25609761486/job/75177835823) | [1s](https://github.com/iree-org/iree/actions/runs/25612674106/job/75185413472) | 0% (0/1) | 6 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25609761497/job/75178282297) | [1s](https://github.com/iree-org/iree/actions/runs/25612674104/job/75189017470) | 100% (1/1) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 651 | 2% (12/649) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 756 | 3% (24/754) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 909 | 8% (77/906) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 965 | 5% (48/963) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 248 | 2% (5/247) | yes | running |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h05m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h48m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h01m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h01m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
