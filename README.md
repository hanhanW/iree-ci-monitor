# iree-ci-monitor

_Updated: 2026-04-27 11:46 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | 0 | [17m55s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193624) | [29m57s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954068) | — | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 2 | 0 | — | 0 | [8m46s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193619) | [27m20s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954193) | — | `shark10-ci-2` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | 0 | [18m09s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193610) | [22m58s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954273) | — | `shark10-ci-2` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193550) | [22m26s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954043) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | 0 | [4m01s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193629) | [18m30s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954035) | — | `shark10-ci-2` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | 0 | [6m29s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954134) | [17m41s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193691) | — | `shark01-ci`, `shark10-ci-2`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | 0 | [4m10s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193700) | [17m03s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954027) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | 0 | [6m42s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193626) | [17m03s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954081) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193582) | [14m12s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954034) | — | `shark10-ci-2` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | 0 | [6m39s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193625) | [12m52s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193646) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | 0 | [5m22s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954091) | [8m47s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193628) | — | `shark10-ci-2`, `shark55-ci` |
| `azure-windows-scale` | ossci | 2 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24995028438/job/73189692700) | [6m10s](https://github.com/iree-org/iree/actions/runs/24985668927/job/73158235168) | — | 2 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m52s](https://github.com/iree-org/iree/actions/runs/24988571683/job/73168031432) | [1m52s](https://github.com/iree-org/iree/actions/runs/24988571683/job/73168031432) | 0% (0/1) | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193682) | [32s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193596) | — | 8 |
| `azure-linux-scale` | ossci | 12 | 0 | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/24995028438/job/73189692662) | [12s](https://github.com/iree-org/iree/actions/runs/24985668927/job/73158235155) | 0% (0/2) | 12 |
| `ubuntu-24.04` | github-hosted | 42 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/24985668900/job/73158205969) | [3s](https://github.com/iree-org/iree/actions/runs/24995028438/job/73193909479) | 0% (0/2) | 41 |
| `windows-2022` | github-hosted | 6 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24995028438/job/73189692611) | [3s](https://github.com/iree-org/iree/actions/runs/24995028438/job/73189692512) | — | 6 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24985668927/job/73158235022) | [3s](https://github.com/iree-org/iree/actions/runs/24995028438/job/73189692638) | — | 6 |
| `macos-14` | github-hosted | 7 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24995028438/job/73189692647) | [3s](https://github.com/iree-org/iree/actions/runs/24995028438/job/73189692602) | 0% (0/1) | 7 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/24988562703/job/73168001571) | [3s](https://github.com/iree-org/iree/actions/runs/24988562703/job/73168001571) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 2 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193575) | [2s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954032) | — | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193521) | [2s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954086) | — | `shark01-ci`, `shark10-ci-2` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193651) | [2s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954386) | — | `iree-mi308-1` |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 403 | 2% (7/399) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 435 | 14% (61/431) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 332 | 3% (9/327) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 317 | 0% (0/313) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 120 | 0% (0/117) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
