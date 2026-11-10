# iree-ci-monitor

_Updated: 2026-11-10 11:49 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 24 | 0 | — | — | 0 | [51m12s](https://github.com/iree-org/iree/actions/runs/42852657214/job/129963347909) | [2h00m](https://github.com/iree-org/iree/actions/runs/42838243138/job/129911946007) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 24 | 0 | — | — | 0 | [38m36s](https://github.com/iree-org/iree/actions/runs/42867031421/job/130015973897) | [1h58m](https://github.com/iree-org/iree/actions/runs/42835059073/job/129903818283) | 0% (0/8) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 24 | 0 | — | — | 0 | [45m38s](https://github.com/iree-org/iree/actions/runs/42862059569/job/129996130068) | [1h32m](https://github.com/iree-org/iree/actions/runs/42844465937/job/129934415194) | 0% (0/8) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [25m03s](https://github.com/iree-org/iree/actions/runs/42844465937/job/129934415217) | [1h11m](https://github.com/iree-org/iree/actions/runs/42835028164/job/129899721450) | 0% (0/4) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 24 | 0 | — | — | 0 | [13m12s](https://github.com/iree-org/iree/actions/runs/42862059569/job/129996130050) | [51m09s](https://github.com/iree-org/iree/actions/runs/42844465937/job/129934414620) | 0% (0/8) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 12 | 0 | — | — | 0 | [22m35s](https://github.com/iree-org/iree/actions/runs/42852657214/job/129963347013) | [44m30s](https://github.com/iree-org/iree/actions/runs/42827046081/job/129870835224) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [16m32s](https://github.com/iree-org/iree/actions/runs/42855175353/job/129971327224) | [38m29s](https://github.com/iree-org/iree/actions/runs/42824681792/job/129864091930) | 0% (0/4) | `shark75-ci` |
| `macos-15` | github-hosted | 39 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/42852657009/job/129959067756) | [3m01s](https://github.com/iree-org/iree/actions/runs/42828169383/job/129870971789) | 0% (0/12) | 39 |
| `windows-2022` | github-hosted | 39 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/42852657009/job/129959067869) | [2m43s](https://github.com/iree-org/iree/actions/runs/42828169383/job/129870971667) | 0% (0/12) | 39 |
| `ubuntu-24.04-arm` | github-hosted | 39 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/42827046154/job/129867237694) | [2m01s](https://github.com/iree-org/iree/actions/runs/42828169383/job/129870971227) | 0% (0/12) | 39 |
| `azure-linux-scale` | ossci | 82 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/42862059593/job/129990660038) | [1m28s](https://github.com/iree-org/iree/actions/runs/42844466098/job/129928216808) | 0% (0/28) | 82 |
| `ubuntu-24.04` | github-hosted | 268 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/42844465937/job/129934414583) | [1m17s](https://github.com/iree-org/iree/actions/runs/42844466098/job/129928215894) | 1% (1/78) | 261 |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/42836117715/job/129898667519) | [3s](https://github.com/iree-org/iree/actions/runs/42855180969/job/129966174459) | 0% (0/12) | 24 |
| `azure-windows-scale` | ossci | 13 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/42852657009/job/129959068370) | [2s](https://github.com/iree-org/iree/actions/runs/42837114621/job/129902307686) | 0% (0/4) | 13 |
| `Linux,X64,iree-w7900` | self-hosted | 12 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 12 | 0 | — | — | [53m03s](https://github.com/iree-org/iree/actions/runs/42862059569/job/129996130225) | [1h58m](https://github.com/iree-org/iree/actions/runs/42835059073/job/129903818283) | [2h04m](https://github.com/iree-org/iree/actions/runs/42843899130/job/129932936359) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 12 | 0 | — | — | [56m19s](https://github.com/iree-org/iree/actions/runs/42824681792/job/129864091278) | [1h37m](https://github.com/iree-org/iree/actions/runs/42844465937/job/129934414967) | [2h00m](https://github.com/iree-org/iree/actions/runs/42838243138/job/129911946007) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 12 | 0 | — | — | [49m57s](https://github.com/iree-org/iree/actions/runs/42838243138/job/129911946096) | [1h32m](https://github.com/iree-org/iree/actions/runs/42843899130/job/129932936961) | [2h10m](https://github.com/iree-org/iree/actions/runs/42828169597/job/129876250730) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 12 | 0 | — | — | [38m34s](https://github.com/iree-org/iree/actions/runs/42828169597/job/129876250684) | [1h29m](https://github.com/iree-org/iree/actions/runs/42843899130/job/129932936340) | [1h40m](https://github.com/iree-org/iree/actions/runs/42844465937/job/129934415477) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 12 | 0 | — | — | [46m39s](https://github.com/iree-org/iree/actions/runs/42843899130/job/129932937156) | [1h17m](https://github.com/iree-org/iree/actions/runs/42852657214/job/129963348026) | [1h32m](https://github.com/iree-org/iree/actions/runs/42844465937/job/129934415194) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 12 | 0 | — | — | [25m03s](https://github.com/iree-org/iree/actions/runs/42844465937/job/129934415217) | [1h11m](https://github.com/iree-org/iree/actions/runs/42835028164/job/129899721450) | [1h13m](https://github.com/iree-org/iree/actions/runs/42835059073/job/129903818122) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 12 | 0 | — | — | [33m04s](https://github.com/iree-org/iree/actions/runs/42828169597/job/129876250910) | [53m49s](https://github.com/iree-org/iree/actions/runs/42838243138/job/129911945911) | [1h26m](https://github.com/iree-org/iree/actions/runs/42844465937/job/129934414896) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 12 | 0 | — | — | [18m01s](https://github.com/iree-org/iree/actions/runs/42855175353/job/129971327215) | [51m09s](https://github.com/iree-org/iree/actions/runs/42844465937/job/129934414620) | [1h34m](https://github.com/iree-org/iree/actions/runs/42835059073/job/129903818308) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 12 | 0 | — | — | [22m35s](https://github.com/iree-org/iree/actions/runs/42852657214/job/129963347013) | [44m30s](https://github.com/iree-org/iree/actions/runs/42827046081/job/129870835224) | [1h41m](https://github.com/iree-org/iree/actions/runs/42824681792/job/129864091435) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 12 | 0 | — | — | [12m34s](https://github.com/iree-org/iree/actions/runs/42855175353/job/129971327237) | [40m38s](https://github.com/iree-org/iree/actions/runs/42844465937/job/129934415261) | [49m42s](https://github.com/iree-org/iree/actions/runs/42843899130/job/129932936092) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 12 | 0 | — | — | [16m32s](https://github.com/iree-org/iree/actions/runs/42855175353/job/129971327224) | [38m29s](https://github.com/iree-org/iree/actions/runs/42824681792/job/129864091930) | [42m19s](https://github.com/iree-org/iree/actions/runs/42827046081/job/129870835479) | 1 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 14 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/42843899263/job/129926216031) | [3m21s](https://github.com/iree-org/iree/actions/runs/42828169383/job/129870970962) | [4m14s](https://github.com/iree-org/iree/actions/runs/42835056728/job/129895093137) | 13 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 13 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/42837114621/job/129902307341) | [3m19s](https://github.com/iree-org/iree/actions/runs/42835056728/job/129895093191) | [3m31s](https://github.com/iree-org/iree/actions/runs/42828169383/job/129870971541) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 13 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/42862059593/job/129990659954) | [3m01s](https://github.com/iree-org/iree/actions/runs/42828169383/job/129870971789) | [3m11s](https://github.com/iree-org/iree/actions/runs/42835056728/job/129895093052) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 13 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42867031699/job/130008151173) | [2m50s](https://github.com/iree-org/iree/actions/runs/42828169383/job/129870971164) | [4m51s](https://github.com/iree-org/iree/actions/runs/42835056728/job/129895093744) | 13 |
| `.github/workflows/ci.yml` | linux_x64_clang_byollvm / linux_x64_clang_byollvm | `ubuntu-24.04` | 2 | 0 | — | — | [1m00s](https://github.com/iree-org/iree/actions/runs/42827046154/job/129867239190) | [2m42s](https://github.com/iree-org/iree/actions/runs/42828169383/job/129870971548) | [2m42s](https://github.com/iree-org/iree/actions/runs/42828169383/job/129870971548) | 2 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 13 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42862059593/job/129990659491) | [2m41s](https://github.com/iree-org/iree/actions/runs/42835056728/job/129895092695) | [3m37s](https://github.com/iree-org/iree/actions/runs/42828169383/job/129870970940) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 13 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/42855176475/job/129966331176) | [2m01s](https://github.com/iree-org/iree/actions/runs/42828169383/job/129870971227) | [2m52s](https://github.com/iree-org/iree/actions/runs/42835056728/job/129895093108) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 13 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/42862059593/job/129990659836) | [1m51s](https://github.com/iree-org/iree/actions/runs/42844466098/job/129928216398) | [2m02s](https://github.com/iree-org/iree/actions/runs/42835056728/job/129895093127) | 13 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 13 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/42835028164/job/129894983089) | [1m50s](https://github.com/iree-org/iree/actions/runs/42828169597/job/129870978368) | [6m21s](https://github.com/iree-org/iree/actions/runs/42867031421/job/130008161770) | 13 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 462 | 1% (6/462) |  | 1h17m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 359 | 1% (5/359) |  | 1h44m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h11m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h58m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
