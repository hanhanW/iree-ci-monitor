# iree-ci-monitor

_Updated: 2026-04-25 18:08 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 2 | 1 | [6m02s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312700) | 0 | [23m43s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432504) | [23m43s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432504) | — | `shark10-ci-2` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 1 | [6m02s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312703) | 0 | [14m19s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432500) | [14m19s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432500) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | 1 | [9m29s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432514) | [13m03s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432503) | — | `shark01-ci`, `shark10-ci-2`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 1 | [6m02s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312711) | 1 | [4m36s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312706) | [12m24s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432501) | — | `shark01-ci`, `shark10-ci-2`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 1 | [6m02s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312695) | 0 | [9m03s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432502) | [9m03s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432502) | — | `shark10-ci-2` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 1 | [6m02s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312664) | 0 | [6m04s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432481) | [6m04s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432481) | — | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 1 | [6m02s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312687) | 1 | [0s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432512) | [5m28s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312694) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312617) | [3m31s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432461) | — | `shark01-ci`, `shark10-ci-2` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | 2 | [8s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432403) | [2m51s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432499) | — | 8 |
| `azure-linux-scale` | ossci | 14 | 0 | — | 3 | [8s](https://github.com/iree-org/iree/actions/runs/24939265366/job/73030106036) | [2m45s](https://github.com/iree-org/iree/actions/runs/24939265366/job/73030106069) | — | 14 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 2 | 0 | — | 1 | [1m40s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73043998090) | [1m59s](https://github.com/iree-org/iree/actions/runs/24939265366/job/73030106049) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24939265366/job/73030106038) | [38s](https://github.com/iree-org/iree/actions/runs/24939265366/job/73030106040) | — | 6 |
| `ubuntu-latest` | github-hosted | 4 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24944671074/job/73043947727) | [4s](https://github.com/iree-org/iree/actions/runs/24944671074/job/73043947737) | — | 4 |
| `ubuntu-24.04` | github-hosted | 38 | 0 | — | 4 | [2s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432486) | [3s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432488) | — | 38 |
| `macos-14` | github-hosted | 8 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73043998076) | [3s](https://github.com/iree-org/iree/actions/runs/24939265366/job/73030106080) | — | 8 |
| `macos-15-intel` | github-hosted | 2 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73043998130) | [3s](https://github.com/iree-org/iree/actions/runs/24939265366/job/73030106075) | — | 2 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 1 | [6m02s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312666) | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432387) | [2s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432387) | — | `shark01-ci` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 2 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432395) | [2s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312592) | — | 2 |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432458) | [2s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312594) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312704) | [2s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432517) | — | `shark10-ci-2`, `shark55-ci` |
| `windows-2022` | github-hosted | 6 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24939265366/job/73030106044) | [2s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73043998077) | — | 6 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432407) | [1s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312699) | — | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 2 | 0 | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/24939265366/job/73030106084) | [1s](https://github.com/iree-org/iree/actions/runs/24944671533/job/73043998102) | — | 2 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 1 | [6m02s](https://github.com/iree-org/iree/actions/runs/24944671545/job/73044312696) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432498) | [0s](https://github.com/iree-org/iree/actions/runs/24939265377/job/73030432498) | — | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 298 | 0% (0/293) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 373 | 2% (7/368) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 313 | 3% (9/307) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 114 | 0% (0/110) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 403 | 14% (56/398) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
