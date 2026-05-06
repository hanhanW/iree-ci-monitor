# iree-ci-monitor

_Updated: 2026-05-06 05:58 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 15 | 2 | [21m12s](https://github.com/iree-org/iree/actions/runs/25435309899/job/74612856709) | 0 | [21m27s](https://github.com/iree-org/iree/actions/runs/25433015907/job/74604898471) | [41m16s](https://github.com/iree-org/iree/actions/runs/25414480014/job/74543695135) | 17% (1/6) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 30 | 2 | [21m12s](https://github.com/iree-org/iree/actions/runs/25435309899/job/74612856688) | 1 | [16m14s](https://github.com/iree-org/iree/actions/runs/25414453644/job/74543495079) | [40m47s](https://github.com/iree-org/iree/actions/runs/25414480014/job/74543695178) | 0% (0/12) | `shark75-ci` |
| `azure-linux-scale` | ossci | 79 | 0 | — | 8 | [32s](https://github.com/iree-org/iree/actions/runs/25435872003/job/74613631820) | [38m37s](https://github.com/iree-org/iree/actions/runs/25426615835/job/74581869021) | 0% (0/33) | 72 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 15 | 1 | [9m16s](https://github.com/iree-org/iree/actions/runs/25435872002/job/74614891796) | 0 | [15m42s](https://github.com/iree-org/iree/actions/runs/25419265247/job/74558231050) | [37m05s](https://github.com/iree-org/iree/actions/runs/25414480014/job/74543695033) | 0% (0/6) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 15 | 1 | [9m16s](https://github.com/iree-org/iree/actions/runs/25435872002/job/74614892056) | 0 | [17m46s](https://github.com/iree-org/iree/actions/runs/25433015907/job/74604898244) | [35m45s](https://github.com/iree-org/iree/actions/runs/25419265247/job/74558231081) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 30 | 1 | [9m16s](https://github.com/iree-org/iree/actions/runs/25435872002/job/74614891961) | 1 | [11m16s](https://github.com/iree-org/iree/actions/runs/25414480014/job/74543695163) | [31m23s](https://github.com/iree-org/iree/actions/runs/25419265247/job/74558231104) | 0% (0/12) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 15 | 2 | [21m12s](https://github.com/iree-org/iree/actions/runs/25435309899/job/74612856512) | 0 | [20m33s](https://github.com/iree-org/iree/actions/runs/25417850768/job/74553696703) | [27m35s](https://github.com/iree-org/iree/actions/runs/25419800066/job/74560010082) | 0% (0/6) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 15 | 2 | [21m12s](https://github.com/iree-org/iree/actions/runs/25435309899/job/74612856373) | 0 | [19m09s](https://github.com/iree-org/iree/actions/runs/25414480014/job/74543694896) | [27m22s](https://github.com/iree-org/iree/actions/runs/25415140705/job/74545545294) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 15 | 0 | — | 1 | [4m43s](https://github.com/iree-org/iree/actions/runs/25414480014/job/74543694923) | [27m13s](https://github.com/iree-org/iree/actions/runs/25417850768/job/74553696670) | 0% (0/6) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 15 | 2 | [21m12s](https://github.com/iree-org/iree/actions/runs/25435309899/job/74612856519) | 0 | [19m52s](https://github.com/iree-org/iree/actions/runs/25417850768/job/74553696800) | [24m45s](https://github.com/iree-org/iree/actions/runs/25414480014/job/74543695056) | 0% (0/6) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 15 | 1 | [9m16s](https://github.com/iree-org/iree/actions/runs/25435872002/job/74614891990) | 0 | [10m08s](https://github.com/iree-org/iree/actions/runs/25414453644/job/74543495092) | [16m46s](https://github.com/iree-org/iree/actions/runs/25415140705/job/74545545464) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 15 | 0 | — | 1 | [6m11s](https://github.com/iree-org/iree/actions/runs/25426615835/job/74589390597) | [14m58s](https://github.com/iree-org/iree/actions/runs/25414453644/job/74543495151) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 30 | 3 | [21m12s](https://github.com/iree-org/iree/actions/runs/25435309899/job/74612856661) | 0 | [4m12s](https://github.com/iree-org/iree/actions/runs/25414480014/job/74543695099) | [11m14s](https://github.com/iree-org/iree/actions/runs/25414480014/job/74543695037) | 0% (0/12) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 15 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25419800066/job/74560010063) | [8m00s](https://github.com/iree-org/iree/actions/runs/25414480014/job/74543695156) | 0% (0/6) | `iree-mi308-1` |
| `macos-14` | github-hosted | 45 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25435309976/job/74611662295) | [2m51s](https://github.com/iree-org/iree/actions/runs/25419265250/job/74557457176) | 0% (0/16) | 45 |
| `azure-windows-scale` | ossci | 14 | 0 | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/25419800350/job/74559134862) | [2m24s](https://github.com/iree-org/iree/actions/runs/25414480015/job/74542970689) | 0% (0/5) | 13 |
| `windows-2022` | github-hosted | 44 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25425572355/job/74578006713) | [1m41s](https://github.com/iree-org/iree/actions/runs/25419265250/job/74557457246) | 0% (0/15) | 44 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m32s](https://github.com/iree-org/iree/actions/runs/25428734466/job/74589028159) | [1m32s](https://github.com/iree-org/iree/actions/runs/25428734466/job/74589028159) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 45 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25435309976/job/74611661971) | [1m21s](https://github.com/iree-org/iree/actions/runs/25419265250/job/74557457151) | 0% (0/15) | 45 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 60 | 0 | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/25417850768/job/74553696770) | [1m12s](https://github.com/iree-org/iree/actions/runs/25419800066/job/74560010072) | 17% (4/24) | 53 |
| `ubuntu-24.04` | github-hosted | 279 | 0 | — | 3 | [4s](https://github.com/iree-org/iree/actions/runs/25424262785/job/74573637297) | [1m00s](https://github.com/iree-org/iree/actions/runs/25419265250/job/74557457125) | 1% (1/100) | 257 |
| `ubuntu-latest` | github-hosted | 17 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25430400629/job/74594848570) | [9s](https://github.com/iree-org/iree/actions/runs/25430618579/job/74595643903) | 0% (0/10) | 17 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25428720443/job/74588980113) | [3s](https://github.com/iree-org/iree/actions/runs/25428720443/job/74588980113) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 15 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25435309899/job/74612856381) | [2s](https://github.com/iree-org/iree/actions/runs/25433015907/job/74604898339) | 0% (0/6) | 14 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 738 | 1% (6/736) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1051 | 4% (42/1047) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 904 | 6% (54/902) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 838 | 2% (14/835) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 248 | 1% (3/246) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
