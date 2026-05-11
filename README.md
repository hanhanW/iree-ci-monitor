# iree-ci-monitor

_Updated: 2026-05-11 12:00 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `azure-windows-scale` | ossci | 24 | 0 | — | 1 | [1m22s](https://github.com/iree-org/iree/actions/runs/25673868080/job/75366216470) | [1h19m](https://github.com/iree-org/iree/actions/runs/25660883101/job/75321265346) | 0% (0/2) | 22 |
| `Linux,X64,gfx1201` | self-hosted | 44 | 9 | [3h00m](https://github.com/iree-org/iree/actions/runs/25680866201/job/75393915280) | 0 | [17m05s](https://github.com/iree-org/iree/actions/runs/25687840553/job/75417643099) | [1h07m](https://github.com/iree-org/iree/actions/runs/25680865848/job/75393910227) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 22 | 1 | [2m33s](https://github.com/iree-org/iree/actions/runs/25690379188/job/75426499316) | 0 | [18m55s](https://github.com/iree-org/iree/actions/runs/25687840553/job/75417642862) | [1h05m](https://github.com/iree-org/iree/actions/runs/25682993130/job/75404013579) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 21 | 6 | [3h00m](https://github.com/iree-org/iree/actions/runs/25680866201/job/75393915357) | 0 | [15m35s](https://github.com/iree-org/iree/actions/runs/25678235394/job/75387284294) | [48m09s](https://github.com/iree-org/iree/actions/runs/25664812496/job/75335555776) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 22 | 5 | [52m17s](https://github.com/iree-org/iree/actions/runs/25687840553/job/75417642996) | 1 | [16m55s](https://github.com/iree-org/iree/actions/runs/25668777375/job/75349230524) | [39m46s](https://github.com/iree-org/iree/actions/runs/25667829692/job/75346179123) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 22 | 3 | [52m17s](https://github.com/iree-org/iree/actions/runs/25687840553/job/75417643062) | 0 | [12m05s](https://github.com/iree-org/iree/actions/runs/25668777375/job/75349230605) | [37m43s](https://github.com/iree-org/iree/actions/runs/25680866201/job/75393915055) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 22 | 2 | [50m48s](https://github.com/iree-org/iree/actions/runs/25687967528/job/75417907631) | 0 | [6m32s](https://github.com/iree-org/iree/actions/runs/25680865848/job/75393910161) | [31m17s](https://github.com/iree-org/iree/actions/runs/25684915768/job/75407346137) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 22 | 1 | [2m33s](https://github.com/iree-org/iree/actions/runs/25690379188/job/75426499198) | 1 | [5m34s](https://github.com/iree-org/iree/actions/runs/25687840553/job/75417642987) | [27m24s](https://github.com/iree-org/iree/actions/runs/25687967528/job/75417907559) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 44 | 5 | [39m36s](https://github.com/iree-org/iree/actions/runs/25683382564/job/75419855192) | 0 | [8m21s](https://github.com/iree-org/iree/actions/runs/25660883155/job/75322507295) | [24m48s](https://github.com/iree-org/iree/actions/runs/25687967528/job/75417907580) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 22 | 2 | [39m36s](https://github.com/iree-org/iree/actions/runs/25683382564/job/75419855131) | 0 | [12m20s](https://github.com/iree-org/iree/actions/runs/25684915768/job/75407346379) | [24m47s](https://github.com/iree-org/iree/actions/runs/25682993130/job/75404013600) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 22 | 1 | [2m33s](https://github.com/iree-org/iree/actions/runs/25690379188/job/75426499259) | 1 | [6m40s](https://github.com/iree-org/iree/actions/runs/25680865848/job/75393910020) | [24m02s](https://github.com/iree-org/iree/actions/runs/25683382564/job/75419854931) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 44 | 3 | [17m28s](https://github.com/iree-org/iree/actions/runs/25689673361/job/75423819438) | 0 | [9m03s](https://github.com/iree-org/iree/actions/runs/25678235394/job/75387284347) | [22m38s](https://github.com/iree-org/iree/actions/runs/25684915768/job/75407346342) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 22 | 1 | [2m33s](https://github.com/iree-org/iree/actions/runs/25690379188/job/75426499383) | 0 | [3m50s](https://github.com/iree-org/iree/actions/runs/25689673361/job/75423819460) | [13m07s](https://github.com/iree-org/iree/actions/runs/25684915768/job/75407346363) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 22 | 0 | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/25660883155/job/75322507318) | [11m11s](https://github.com/iree-org/iree/actions/runs/25660985947/job/75322893874) | 0% (0/2) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 88 | 0 | — | 4 | [9s](https://github.com/iree-org/iree/actions/runs/25687840553/job/75417642889) | [5m57s](https://github.com/iree-org/iree/actions/runs/25678239481/job/75387713518) | 0% (0/8) | 88 |
| `macos-14` | github-hosted | 73 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25689673334/job/75422516088) | [2m18s](https://github.com/iree-org/iree/actions/runs/25673868080/job/75366216360) | 0% (0/7) | 71 |
| `windows-2022` | github-hosted | 72 | 0 | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/25690379182/job/75424983632) | [1m52s](https://github.com/iree-org/iree/actions/runs/25678239464/job/75382248813) | 0% (0/6) | 72 |
| `ubuntu-24.04-arm` | github-hosted | 72 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25687967545/job/75416585213) | [1m27s](https://github.com/iree-org/iree/actions/runs/25687840577/job/75416632990) | 0% (0/6) | 72 |
| `azure-linux-scale` | ossci | 126 | 0 | — | 5 | [10s](https://github.com/iree-org/iree/actions/runs/25690379182/job/75424983711) | [1m22s](https://github.com/iree-org/iree/actions/runs/25680866492/job/75391722578) | 0% (0/13) | 122 |
| `ubuntu-24.04` | github-hosted | 439 | 0 | — | 9 | [4s](https://github.com/iree-org/iree/actions/runs/25667829692/job/75346178955) | [1m02s](https://github.com/iree-org/iree/actions/runs/25687967528/job/75417907557) | 0% (0/35) | 439 |
| `ubuntu-latest` | github-hosted | 28 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25678492764/job/75383140439) | [18s](https://github.com/iree-org/iree/actions/runs/25674883776/job/75369875797) | 0% (0/4) | 28 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 22 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25673868123/job/75424968943) | [4s](https://github.com/iree-org/iree/actions/runs/25690379188/job/75426499215) | 100% (2/2) | 22 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25664519709/job/75333431199) | [4s](https://github.com/iree-org/iree/actions/runs/25664519709/job/75333431199) | 0% (0/1) | 1 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 1 | [8h34m](https://github.com/iree-org/iree/actions/runs/25664551860/job/75333540077) | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,shark01-ci` | self-hosted | 1 | 1 | [50m48s](https://github.com/iree-org/iree/actions/runs/25687967528/job/75417907634) | 0 | 0s | 0s | — | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 733 | 2% (13/731) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 278 | 2% (6/276) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 1012 | 8% (85/1008) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1077 | 4% (48/1074) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 851 | 3% (24/848) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 3h00m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 3h00m (> 2h00m)
- **[stale-queued]** `ah-ubuntu_22_04-c7g_4x-50` oldest queued job waiting 8h34m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h07m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h05m (> 1h00m)
- **[queue-starved]** `azure-windows-scale` p95 queue 1h19m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
