# iree-ci-monitor

_Updated: 2026-05-02 05:35 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | 0 | [25m17s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989402) | [25m17s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989402) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | 0 | [24m31s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989396) | [24m31s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989396) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | 0 | [6m06s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989374) | [19m52s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989392) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 1 | 0 | — | 0 | [19m52s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989378) | [19m52s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989378) | 100% (1/1) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | 0 | [14m25s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989522) | [14m25s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989522) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | 0 | [7m28s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989370) | [12m42s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989379) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | 0 | [11m10s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989397) | [11m10s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989397) | 0% (0/1) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | 0 | [6m15s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989394) | [9m11s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989384) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 6 | 0 | — | 0 | [27s](https://github.com/iree-org/iree/actions/runs/25243903940/job/74024588238) | [35s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024590021) | 0% (0/6) | 6 |
| `ubuntu-24.04` | github-hosted | 27 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25245161066/job/74028078629) | [8s](https://github.com/iree-org/iree/actions/runs/25245161066/job/74028078633) | 0% (0/18) | 27 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989405) | [8s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989410) | 50% (2/4) | 4 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25250831528/job/74042560120) | [8s](https://github.com/iree-org/iree/actions/runs/25250755438/job/74042367080) | 0% (0/2) | 9 |
| `windows-2022` | github-hosted | 5 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25245161066/job/74028078638) | [5s](https://github.com/iree-org/iree/actions/runs/25243903940/job/74024588151) | 0% (0/3) | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25245161066/job/74028078607) | [3s](https://github.com/iree-org/iree/actions/runs/25243903940/job/74024588139) | 0% (0/3) | 6 |
| `macos-14` | github-hosted | 5 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25245161066/job/74028078627) | [3s](https://github.com/iree-org/iree/actions/runs/25243903940/job/74024588168) | 0% (0/3) | 5 |
| `Linux,X64,rdna3` | self-hosted | 1 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989388) | [2s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989388) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989328) | [1s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989328) | 0% (0/1) | `shark75-ci` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989330) | [1s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989330) | 0% (0/1) | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989347) | [1s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989347) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989375) | [1s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989375) | 0% (0/1) | `shark01-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989393) | [1s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989393) | 0% (0/1) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 1 | 0 | — | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25243903940/job/74024588222) | [0s](https://github.com/iree-org/iree/actions/runs/25243903940/job/74024588222) | 0% (0/1) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1044 | 5% (56/1043) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 905 | 3% (28/904) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 822 | 1% (11/822) |  | 7h17m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 610 | 6% (38/610) |  | 7h17m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 245 | 2% (5/245) |  | 7h37m ago |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 94 | 14% (13/94) |  | 4d15h ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
