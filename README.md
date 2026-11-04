# iree-ci-monitor

_Updated: 2026-11-04 11:51 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 24 | 0 | — | — | 0 | [1h23m](https://github.com/iree-org/iree/actions/runs/41871683681/job/126725558606) | [3h28m](https://github.com/iree-org/iree/actions/runs/41846148312/job/126646682604) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 24 | 0 | — | — | 0 | [1h07m](https://github.com/iree-org/iree/actions/runs/41871683681/job/126725558819) | [3h20m](https://github.com/iree-org/iree/actions/runs/41842431950/job/126620944912) | 0% (0/4) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 24 | 0 | — | — | 0 | [40m58s](https://github.com/iree-org/iree/actions/runs/41846060824/job/126646213267) | [2h59m](https://github.com/iree-org/iree/actions/runs/41846148312/job/126646682283) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [23m02s](https://github.com/iree-org/iree/actions/runs/41865135135/job/126701995042) | [1h17m](https://github.com/iree-org/iree/actions/runs/41851409182/job/126655122353) | 0% (0/2) | `shark55-ci` |
| `macos-15` | github-hosted | 39 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/41871683244/job/126720303225) | [10m13s](https://github.com/iree-org/iree/actions/runs/41851409289/job/126650038029) | 0% (0/6) | 31 |
| `azure-linux-scale` | ossci | 82 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/41832826841/job/126584155763) | [3m16s](https://github.com/iree-org/iree/actions/runs/41857042738/job/126668547310) | 0% (0/15) | 82 |
| `ubuntu-24.04` | github-hosted | 260 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/41871683681/job/126725558170) | [2m08s](https://github.com/iree-org/iree/actions/runs/41836894553/job/126602911193) | 3% (1/37) | 253 |
| `ubuntu-24.04-arm` | github-hosted | 39 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/41871683244/job/126720303329) | [1m52s](https://github.com/iree-org/iree/actions/runs/41848495478/job/126652112248) | 17% (1/6) | 39 |
| `windows-2022` | github-hosted | 39 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/41846060883/job/126629867629) | [1m33s](https://github.com/iree-org/iree/actions/runs/41848495478/job/126652111623) | 0% (0/6) | 39 |
| `ubuntu-latest` | github-hosted | 36 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/41844396440/job/126624116669) | [46s](https://github.com/iree-org/iree/actions/runs/41846146698/job/126630057147) | 0% (0/6) | 36 |
| `azure-windows-scale` | ossci | 13 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/41857042738/job/126668547639) | [7s](https://github.com/iree-org/iree/actions/runs/41850308716/job/126644643425) | 0% (0/2) | 13 |
| `Linux,X64,iree-r9700` | self-hosted | 12 | 11 | [6h50m](https://github.com/iree-org/iree/actions/runs/41832827194/job/126588006647) | 2026-11-04 11:49 PST | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 12 | 11 | [6h50m](https://github.com/iree-org/iree/actions/runs/41832827194/job/126588006477) | 2026-11-04 11:49 PST | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201` | self-hosted | 24 | 22 | [6h50m](https://github.com/iree-org/iree/actions/runs/41832827194/job/126588006618) | 2026-11-04 11:49 PST | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 12 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [6h50m](https://github.com/iree-org/iree/actions/runs/41832827194/job/126588006477) | 2026-11-04 11:49 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `fix-webgpu-host-memory-files` | pull_request |
| [6h50m](https://github.com/iree-org/iree/actions/runs/41832827194/job/126588006618) | 2026-11-04 11:49 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `fix-webgpu-host-memory-files` | pull_request |
| [6h50m](https://github.com/iree-org/iree/actions/runs/41832827194/job/126588006647) | 2026-11-04 11:49 PST | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `fix-webgpu-host-memory-files` | pull_request |
| [6h50m](https://github.com/iree-org/iree/actions/runs/41832827194/job/126588006747) | 2026-11-04 11:49 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `fix-webgpu-host-memory-files` | pull_request |
| [6h21m](https://github.com/iree-org/iree/actions/runs/41836894553/job/126602911130) | 2026-11-04 11:49 PST | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `fix-webgpu-export-names` | pull_request |
| [6h21m](https://github.com/iree-org/iree/actions/runs/41836894553/job/126602911167) | 2026-11-04 11:49 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `fix-webgpu-export-names` | pull_request |
| [6h21m](https://github.com/iree-org/iree/actions/runs/41836894553/job/126602911339) | 2026-11-04 11:49 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `fix-webgpu-export-names` | pull_request |
| [6h21m](https://github.com/iree-org/iree/actions/runs/41836894553/job/126602911479) | 2026-11-04 11:49 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `fix-webgpu-export-names` | pull_request |
| [5h56m](https://github.com/iree-org/iree/actions/runs/41837507513/job/126615984196) | 2026-11-04 11:49 PST | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `integrates/llvm-20261103` | pull_request |
| [5h56m](https://github.com/iree-org/iree/actions/runs/41837507513/job/126615984242) | 2026-11-04 11:49 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `integrates/llvm-20261103` | pull_request |
| [5h56m](https://github.com/iree-org/iree/actions/runs/41837507513/job/126615984271) | 2026-11-04 11:49 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `integrates/llvm-20261103` | pull_request |
| [5h56m](https://github.com/iree-org/iree/actions/runs/41837507513/job/126615984456) | 2026-11-04 11:49 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `integrates/llvm-20261103` | pull_request |
| [5h47m](https://github.com/iree-org/iree/actions/runs/41842431950/job/126620944427) | 2026-11-04 11:49 PST | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `manewing/25034-globaloptimization-pass-ordering-keeps-im2col-convolutions-in-quantized-conv-models-from-lowering-to-integer-math` | pull_request |
| [5h47m](https://github.com/iree-org/iree/actions/runs/41842431950/job/126620944751) | 2026-11-04 11:49 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `manewing/25034-globaloptimization-pass-ordering-keeps-im2col-convolutions-in-quantized-conv-models-from-lowering-to-integer-math` | pull_request |
| [5h47m](https://github.com/iree-org/iree/actions/runs/41842431950/job/126620944779) | 2026-11-04 11:49 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `manewing/25034-globaloptimization-pass-ordering-keeps-im2col-convolutions-in-quantized-conv-models-from-lowering-to-integer-math` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 12 | 11 | [6h50m](https://github.com/iree-org/iree/actions/runs/41832827194/job/126588006647) | 2026-11-04 11:49 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 12 | 11 | [6h50m](https://github.com/iree-org/iree/actions/runs/41832827194/job/126588006477) | 2026-11-04 11:49 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 12 | 11 | [6h50m](https://github.com/iree-org/iree/actions/runs/41832827194/job/126588006618) | 2026-11-04 11:49 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 12 | 11 | [6h50m](https://github.com/iree-org/iree/actions/runs/41832827194/job/126588006747) | 2026-11-04 11:49 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 12 | 0 | — | — | [54m47s](https://github.com/iree-org/iree/actions/runs/41842431950/job/126620944647) | [3h35m](https://github.com/iree-org/iree/actions/runs/41846148312/job/126646682555) | [3h35m](https://github.com/iree-org/iree/actions/runs/41846148312/job/126646682555) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 12 | 0 | — | — | [1h40m](https://github.com/iree-org/iree/actions/runs/41851409182/job/126655122549) | [3h33m](https://github.com/iree-org/iree/actions/runs/41848495501/job/126657328188) | [3h33m](https://github.com/iree-org/iree/actions/runs/41848495501/job/126657328188) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 12 | 0 | — | — | [1h03m](https://github.com/iree-org/iree/actions/runs/41865135135/job/126701995510) | [3h27m](https://github.com/iree-org/iree/actions/runs/41846148312/job/126646682870) | [3h27m](https://github.com/iree-org/iree/actions/runs/41846148312/job/126646682870) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 12 | 0 | — | — | [1h23m](https://github.com/iree-org/iree/actions/runs/41871683681/job/126725558606) | [3h24m](https://github.com/iree-org/iree/actions/runs/41848495501/job/126657328700) | [3h24m](https://github.com/iree-org/iree/actions/runs/41848495501/job/126657328700) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 12 | 0 | — | — | [40m58s](https://github.com/iree-org/iree/actions/runs/41846060824/job/126646213267) | [2h59m](https://github.com/iree-org/iree/actions/runs/41846148312/job/126646682283) | [2h59m](https://github.com/iree-org/iree/actions/runs/41846148312/job/126646682283) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 12 | 0 | — | — | [1h32m](https://github.com/iree-org/iree/actions/runs/41842431950/job/126620944785) | [2h57m](https://github.com/iree-org/iree/actions/runs/41848495501/job/126657328703) | [3h04m](https://github.com/iree-org/iree/actions/runs/41846148312/job/126646682616) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 12 | 0 | — | — | [23m02s](https://github.com/iree-org/iree/actions/runs/41865135135/job/126701995042) | [1h17m](https://github.com/iree-org/iree/actions/runs/41851409182/job/126655122353) | [1h50m](https://github.com/iree-org/iree/actions/runs/41846148312/job/126646682316) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 13 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/41846148476/job/126630595333) | [15m39s](https://github.com/iree-org/iree/actions/runs/41851409289/job/126650037740) | [15m39s](https://github.com/iree-org/iree/actions/runs/41851409289/job/126650037740) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 13 | 0 | — | — | [1m08s](https://github.com/iree-org/iree/actions/runs/41850308716/job/126644643423) | [10m13s](https://github.com/iree-org/iree/actions/runs/41851409289/job/126650038029) | [10m13s](https://github.com/iree-org/iree/actions/runs/41851409289/job/126650038029) | 12 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 3 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/41846060883/job/126629868470) | [3m57s](https://github.com/iree-org/iree/actions/runs/41837507707/job/126600333663) | [3m57s](https://github.com/iree-org/iree/actions/runs/41837507707/job/126600333663) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 12 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/41857042952/job/126675555859) | [2m18s](https://github.com/iree-org/iree/actions/runs/41846148312/job/126646682804) | [2m26s](https://github.com/iree-org/iree/actions/runs/41836894553/job/126602911233) | 12 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 13 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/41836894338/job/126598122182) | [2m09s](https://github.com/iree-org/iree/actions/runs/41851409289/job/126650037916) | [2m16s](https://github.com/iree-org/iree/actions/runs/41837507707/job/126600332772) | 13 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 13 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/41871683244/job/126720303785) | [2m03s](https://github.com/iree-org/iree/actions/runs/41837507707/job/126600333042) | [4m21s](https://github.com/iree-org/iree/actions/runs/41857042738/job/126668547045) | 13 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 13 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/41846148476/job/126630596122) | [1m59s](https://github.com/iree-org/iree/actions/runs/41837507707/job/126600333303) | [3m16s](https://github.com/iree-org/iree/actions/runs/41857042738/job/126668547310) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 13 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/41842432051/job/126617339210) | [1m54s](https://github.com/iree-org/iree/actions/runs/41848495478/job/126652111632) | [6m39s](https://github.com/iree-org/iree/actions/runs/41837507707/job/126600332984) | 13 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 13 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/41851409289/job/126650038867) | [1m52s](https://github.com/iree-org/iree/actions/runs/41857042738/job/126668547376) | [3m23s](https://github.com/iree-org/iree/actions/runs/41837507707/job/126600333318) | 13 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 561 | 2% (9/561) |  | 1h11m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 399 | 1% (5/399) |  | 1d01h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job observed waiting 6h50m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 6h50m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job observed waiting 6h50m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 3h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 3h28m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h59m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
