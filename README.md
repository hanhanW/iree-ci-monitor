# iree-ci-monitor

_Updated: 2026-04-23 18:58 PDT_ — `iree-org/iree`, last 6h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 6h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 30 | 16 | [5h37m](https://github.com/iree-org/iree/actions/runs/24856591127/job/72771964649) | 2 | 0s | 22m11s | 0% (0/5) | 3 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 15 | 12 | [5h37m](https://github.com/iree-org/iree/actions/runs/24856591127/job/72771964531) | 1 | 0s | 16m49s | — | 1 |
| `Linux,X64,gfx1201` | self-hosted | 30 | 26 | [5h37m](https://github.com/iree-org/iree/actions/runs/24856591127/job/72771964507) | 0 | 0s | 16m41s | — | 1 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 37 | 14 | [5h09m](https://github.com/iree-org/iree/actions/runs/24857340131/job/72776289129) | 5 | 2s | 16m28s | 0% (0/8) | 4 |
| `Linux,X64,rdna3` | self-hosted | 15 | 8 | [5h09m](https://github.com/iree-org/iree/actions/runs/24857340131/job/72776289234) | 0 | 0s | 12m40s | 0% (0/4) | 3 |
| `Linux,X64,iree-r9700` | self-hosted | 15 | 9 | [5h09m](https://github.com/iree-org/iree/actions/runs/24857340131/job/72776288962) | 1 | 0s | 12m36s | 0% (0/1) | 1 |
| `macos-14` | github-hosted | 51 | 3 | [5h07m](https://github.com/iree-org/iree/actions/runs/24858194429/job/72776647073) | 6 | 1m31s | 10m41s | 0% (0/17) | 46 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 15 | 4 | [5h09m](https://github.com/iree-org/iree/actions/runs/24857340131/job/72776289145) | 1 | 2s | 7m55s | 0% (0/5) | 3 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 15 | 3 | [5h01m](https://github.com/iree-org/iree/actions/runs/24857352018/job/72777570910) | 3 | 1s | 7m48s | 0% (0/5) | 1 |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 15 | 12 | [5h37m](https://github.com/iree-org/iree/actions/runs/24856591127/job/72771964585) | 0 | 0s | 7m25s | 0% (0/1) | 1 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 15 | 9 | [5h09m](https://github.com/iree-org/iree/actions/runs/24857340131/job/72776289041) | 0 | 0s | 5m36s | 67% (2/3) | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 15 | 11 | [5h37m](https://github.com/iree-org/iree/actions/runs/24856591127/job/72771964563) | 0 | 0s | 4m57s | 0% (0/1) | 2 |
| `macos-15-intel` | github-hosted | 4 | 0 | — | 4 | 3m13s | 4m30s | — | 4 |
| `ubuntu-24.04-arm` | github-hosted | 48 | 0 | — | 2 | 3s | 4m02s | 0% (0/18) | 48 |
| `windows-2022` | github-hosted | 48 | 0 | — | 10 | 24s | 3m54s | 6% (1/17) | 48 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 60 | 3 | [5h01m](https://github.com/iree-org/iree/actions/runs/24857352018/job/72777570816) | 6 | 8s | 3m39s | 8% (2/24) | 57 |
| `ubuntu-24.04` | github-hosted | 284 | 9 | [5h01m](https://github.com/iree-org/iree/actions/runs/24857352018/job/72777570689) | 20 | 2s | 2m33s | 3% (3/94) | 268 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 23 | 17 | [5h37m](https://github.com/iree-org/iree/actions/runs/24856591127/job/72771964356) | 1 | 0s | 2m29s | 0% (0/1) | 2 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 3 | 0 | — | 3 | 1m59s | 2m06s | — | 3 |
| `azure-windows-scale` | ossci | 16 | 0 | — | 6 | 1s | 2m05s | 0% (0/4) | 16 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 15 | 12 | [5h37m](https://github.com/iree-org/iree/actions/runs/24856591127/job/72771964674) | 0 | 0s | 1m13s | 0% (0/1) | 1 |
| `ubuntu-latest` | github-hosted | 32 | 0 | — | 0 | 2s | 56s | 0% (0/12) | 32 |
| `azure-linux-scale` | ossci | 93 | 0 | — | 28 | 8s | 32s | 0% (0/29) | 93 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 15 | 0 | — | 2 | 1s | 1s | 17% (1/6) | 15 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, +2 more | 142 | 1% (2/139) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 47 | 0% (0/44) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +2 more | 118 | 0% (0/114) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +5 more | 139 | 2% (3/135) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +7 more | 154 | 16% (24/151) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job waiting 5h09m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 5h37m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 5h37m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 5h37m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 5h09m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 5h37m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 5h09m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 5h37m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 5h37m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job waiting 5h09m (> 2h00m)
- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job waiting 5h01m (> 2h00m)
- **[stale-queued]** `macos-14` oldest queued job waiting 5h07m (> 2h00m)
- **[stale-queued]** `nodai-amdgpu-mi308-x86-64` oldest queued job waiting 5h01m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 5h37m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 5h09m (> 2h00m)
- **[stale-queued]** `ubuntu-24.04` oldest queued job waiting 5h01m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds.
