# iree-ci-monitor

_Updated: 2026-04-23 19:51 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 52 | 36 | [9h41m](https://github.com/iree-org/iree/actions/runs/24848088906/job/72741935655) | 2 | [0s](https://github.com/iree-org/iree/actions/runs/24857340131/job/72776288949) | [2h53m](https://github.com/iree-org/iree/actions/runs/24850230442/job/72749564892) | 0% (0/1) | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 30 | 16 | [8h53m](https://github.com/iree-org/iree/actions/runs/24850230442/job/72749564690) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24861685549/job/72791988688) | [2h21m](https://github.com/iree-org/iree/actions/runs/24849484323/job/72747011670) | 0% (0/2) | 2 |
| `Linux,X64,iree-r9700` | self-hosted | 30 | 11 | [8h53m](https://github.com/iree-org/iree/actions/runs/24850230442/job/72749564658) | 1 | [8s](https://github.com/iree-org/iree/actions/runs/24866704561/job/72804850608) | [2h17m](https://github.com/iree-org/iree/actions/runs/24849453891/job/72749710580) | 0% (0/4) | 1 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 30 | 14 | [8h00m](https://github.com/iree-org/iree/actions/runs/24852668845/job/72758160871) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24862703064/job/72792565206) | [2h03m](https://github.com/iree-org/iree/actions/runs/24849484323/job/72747011899) | 0% (0/4) | 1 |
| `Linux,X64,gfx1100` | self-hosted | 60 | 16 | [6h30m](https://github.com/iree-org/iree/actions/runs/24856591127/job/72771964649) | 3 | [11m48s](https://github.com/iree-org/iree/actions/runs/24851251242/job/72753263486) | [1h49m](https://github.com/iree-org/iree/actions/runs/24849453891/job/72749710796) | 0% (0/10) | 3 |
| `Linux,X64,gfx1201` | self-hosted | 60 | 41 | [9h41m](https://github.com/iree-org/iree/actions/runs/24848088906/job/72741935792) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24860904417/job/72786810797) | [1h38m](https://github.com/iree-org/iree/actions/runs/24851251242/job/72753263371) | 0% (0/2) | 1 |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 30 | 21 | [9h41m](https://github.com/iree-org/iree/actions/runs/24848088906/job/72741935678) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24858194412/job/72780172578) | [1h32m](https://github.com/iree-org/iree/actions/runs/24849487196/job/72747008974) | 0% (0/1) | 1 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 30 | 15 | [8h30m](https://github.com/iree-org/iree/actions/runs/24851251242/job/72753263438) | 2 | [0s](https://github.com/iree-org/iree/actions/runs/24866300244/job/72803732728) | [1h31m](https://github.com/iree-org/iree/actions/runs/24849484323/job/72747011965) | 0% (0/2) | 1 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 30 | 13 | [9h09m](https://github.com/iree-org/iree/actions/runs/24849487196/job/72747008902) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24866704561/job/72804850730) | [1h27m](https://github.com/iree-org/iree/actions/runs/24852057045/job/72756134846) | 67% (4/6) | 2 |
| `Linux,X64,rdna3` | self-hosted | 30 | 8 | [6h02m](https://github.com/iree-org/iree/actions/runs/24857340131/job/72776289234) | 0 | [7m48s](https://github.com/iree-org/iree/actions/runs/24866931477/job/72805571846) | [1h26m](https://github.com/iree-org/iree/actions/runs/24849487196/job/72747008987) | 0% (0/7) | 3 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 68 | 14 | [6h02m](https://github.com/iree-org/iree/actions/runs/24857340131/job/72776289129) | 5 | [9m22s](https://github.com/iree-org/iree/actions/runs/24848085290/job/72741815595) | [1h14m](https://github.com/iree-org/iree/actions/runs/24851251242/job/72753263257) | 0% (0/14) | 4 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 30 | 4 | [6h02m](https://github.com/iree-org/iree/actions/runs/24857340131/job/72776289145) | 1 | [7m55s](https://github.com/iree-org/iree/actions/runs/24860904417/job/72786810846) | [1h04m](https://github.com/iree-org/iree/actions/runs/24850230442/job/72749565051) | 0% (0/8) | 3 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 30 | 3 | [5h54m](https://github.com/iree-org/iree/actions/runs/24857352018/job/72777570910) | 3 | [2s](https://github.com/iree-org/iree/actions/runs/24866931477/job/72805571854) | [23m31s](https://github.com/iree-org/iree/actions/runs/24849484323/job/72747011930) | 0% (0/8) | 1 |
| `macos-14` | github-hosted | 108 | 3 | [6h00m](https://github.com/iree-org/iree/actions/runs/24858194429/job/72776647073) | 8 | [1m02s](https://github.com/iree-org/iree/actions/runs/24861766248/job/72788945949) | [8m52s](https://github.com/iree-org/iree/actions/runs/24849487191/job/72745969107) | 0% (0/26) | 103 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 120 | 3 | [5h54m](https://github.com/iree-org/iree/actions/runs/24857352018/job/72777570816) | 6 | [9s](https://github.com/iree-org/iree/actions/runs/24857340131/job/72776288980) | [8m34s](https://github.com/iree-org/iree/actions/runs/24848088906/job/72741935642) | 11% (4/36) | 117 |
| `macos-15-intel` | github-hosted | 7 | 0 | — | 6 | [14s](https://github.com/iree-org/iree/actions/runs/24848085220/job/72740704509) | [4m30s](https://github.com/iree-org/iree/actions/runs/24861766248/job/72788945917) | — | 7 |
| `ubuntu-24.04` | github-hosted | 562 | 9 | [5h54m](https://github.com/iree-org/iree/actions/runs/24857352018/job/72777570689) | 24 | [3s](https://github.com/iree-org/iree/actions/runs/24852057045/job/72756134900) | [4m25s](https://github.com/iree-org/iree/actions/runs/24849484323/job/72747011766) | 2% (3/139) | 545 |
| `windows-2022` | github-hosted | 102 | 0 | — | 10 | [28s](https://github.com/iree-org/iree/actions/runs/24856591150/job/72770959538) | [4m06s](https://github.com/iree-org/iree/actions/runs/24849487191/job/72745969153) | 4% (1/26) | 102 |
| `ubuntu-24.04-arm` | github-hosted | 102 | 0 | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/24851251241/job/72752093966) | [3m59s](https://github.com/iree-org/iree/actions/runs/24848235576/job/72741594009) | 0% (0/27) | 102 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 6 | 0 | — | 3 | [1m59s](https://github.com/iree-org/iree/actions/runs/24861766248/job/72788945893) | [2m10s](https://github.com/iree-org/iree/actions/runs/24853408896/job/72759790581) | — | 6 |
| `ubuntu-latest` | github-hosted | 50 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24867466329/job/72806569537) | [1m24s](https://github.com/iree-org/iree/actions/runs/24867333495/job/72806180933) | 0% (0/18) | 50 |
| `azure-windows-scale` | ossci | 34 | 0 | — | 6 | [1s](https://github.com/iree-org/iree/actions/runs/24867333933/job/72806179223) | [1m22s](https://github.com/iree-org/iree/actions/runs/24861685535/job/72788483318) | 0% (0/7) | 34 |
| `azure-linux-scale` | ossci | 194 | 0 | — | 28 | [9s](https://github.com/iree-org/iree/actions/runs/24849453899/job/72745713308) | [49s](https://github.com/iree-org/iree/actions/runs/24845424292/job/72745950908) | 0% (0/47) | 194 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 30 | 0 | — | 2 | [1s](https://github.com/iree-org/iree/actions/runs/24866300244/job/72803732671) | [2s](https://github.com/iree-org/iree/actions/runs/24860904417/job/72786810626) | 22% (2/9) | 30 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, +2 more | 142 | 1% (2/139) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 47 | 0% (0/44) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +2 more | 118 | 0% (0/114) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +5 more | 139 | 2% (3/135) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +7 more | 154 | 16% (24/151) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job waiting 6h02m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 6h30m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 8h30m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 9h41m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 8h53m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 8h53m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 9h09m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 8h00m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 9h41m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job waiting 6h02m (> 2h00m)
- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job waiting 5h54m (> 2h00m)
- **[stale-queued]** `macos-14` oldest queued job waiting 6h00m (> 2h00m)
- **[stale-queued]** `nodai-amdgpu-mi308-x86-64` oldest queued job waiting 5h54m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 9h41m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 6h02m (> 2h00m)
- **[stale-queued]** `ubuntu-24.04` oldest queued job waiting 5h54m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h04m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h49m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h31m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h38m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h21m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h03m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h26m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h53m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h14m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
