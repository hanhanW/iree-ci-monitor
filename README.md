# iree-ci-monitor

_Updated: 2026-04-23 18:07 PDT_ — `iree-org/iree`, last 6h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 6h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 32 | 16 | [4h46m](https://github.com/iree-org/iree/actions/runs/24856591127/job/72771964649) | 2 | 0s | 38m48s | 0% (0/3) | 3 |
| `Linux,X64,iree-r9700` | self-hosted | 16 | 9 | [5h21m](https://github.com/iree-org/iree/actions/runs/24847371366/job/72766667331) | 1 | 0s | 33m26s | 0% (0/1) | 1 |
| `Linux,X64,rdna3` | self-hosted | 16 | 8 | [4h18m](https://github.com/iree-org/iree/actions/runs/24857340131/job/72776289234) | 0 | 0s | 30m41s | 0% (0/3) | 3 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 38 | 14 | [4h18m](https://github.com/iree-org/iree/actions/runs/24857340131/job/72776289129) | 5 | 25s | 26m58s | 0% (0/5) | 4 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 16 | 13 | [5h43m](https://github.com/iree-org/iree/actions/runs/24845424353/job/72763239618) | 1 | 0s | 16m49s | — | 1 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 16 | 13 | [5h21m](https://github.com/iree-org/iree/actions/runs/24847371366/job/72766667317) | 0 | 0s | 15m34s | — | 1 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 16 | 4 | [4h18m](https://github.com/iree-org/iree/actions/runs/24857340131/job/72776289145) | 1 | 50s | 13m46s | 0% (0/4) | 3 |
| `macos-14` | github-hosted | 47 | 3 | [4h16m](https://github.com/iree-org/iree/actions/runs/24858194429/job/72776647073) | 5 | 2m13s | 10m41s | 0% (0/14) | 42 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 16 | 11 | [5h43m](https://github.com/iree-org/iree/actions/runs/24845424353/job/72763239390) | 0 | 0s | 10m24s | 50% (1/2) | 2 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 16 | 3 | [4h10m](https://github.com/iree-org/iree/actions/runs/24857352018/job/72777570910) | 3 | 2s | 8m31s | 0% (0/4) | 1 |
| `macos-15-intel` | github-hosted | 3 | 0 | — | 3 | 5s | 4m30s | — | 3 |
| `ubuntu-24.04-arm` | github-hosted | 45 | 0 | — | 2 | 3s | 4m02s | 0% (0/15) | 45 |
| `windows-2022` | github-hosted | 45 | 0 | — | 10 | 28s | 3m54s | 7% (1/14) | 45 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 64 | 3 | [4h10m](https://github.com/iree-org/iree/actions/runs/24857352018/job/72777570816) | 6 | 8s | 3m39s | 5% (1/20) | 61 |
| `Linux,X64,iree-w7900` | self-hosted | 16 | 13 | [5h43m](https://github.com/iree-org/iree/actions/runs/24845424353/job/72763239445) | 0 | 0s | 2m41s | — | 1 |
| `ubuntu-24.04` | github-hosted | 277 | 9 | [4h10m](https://github.com/iree-org/iree/actions/runs/24857352018/job/72777570689) | 18 | 2s | 2m37s | 3% (2/78) | 261 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 26 | 20 | [5h43m](https://github.com/iree-org/iree/actions/runs/24845424353/job/72763239448) | 1 | 0s | 2m29s | — | 2 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 2 | 0 | — | 2 | 1m59s | 2m06s | — | 2 |
| `azure-windows-scale` | ossci | 15 | 0 | — | 6 | 1s | 2m05s | 0% (0/3) | 15 |
| `ubuntu-latest` | github-hosted | 23 | 0 | — | 0 | 2s | 39s | 0% (0/10) | 23 |
| `azure-linux-scale` | ossci | 86 | 0 | — | 28 | 8s | 33s | 0% (0/23) | 86 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | 2 | 1s | 2s | 20% (1/5) | 16 |
| `Linux,X64,gfx1201` | self-hosted | 32 | 29 | [5h43m](https://github.com/iree-org/iree/actions/runs/24845424353/job/72763239706) | 0 | 0s | 0s | — | 1 |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 16 | 14 | [5h43m](https://github.com/iree-org/iree/actions/runs/24845424353/job/72763239770) | 0 | 0s | 0s | — | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, +2 more | 136 | 2% (2/133) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +7 more | 146 | 15% (22/143) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +2 more | 113 | 0% (0/109) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +5 more | 130 | 2% (3/126) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 45 | 0% (0/42) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job waiting 4h18m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 4h46m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 5h43m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 5h43m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 5h21m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 5h43m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 5h43m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 5h21m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 5h43m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job waiting 4h18m (> 2h00m)
- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job waiting 4h10m (> 2h00m)
- **[stale-queued]** `macos-14` oldest queued job waiting 4h16m (> 2h00m)
- **[stale-queued]** `nodai-amdgpu-mi308-x86-64` oldest queued job waiting 4h10m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 5h43m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 4h18m (> 2h00m)
- **[stale-queued]** `ubuntu-24.04` oldest queued job waiting 4h10m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds.
