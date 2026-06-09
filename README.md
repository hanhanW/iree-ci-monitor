# iree-ci-monitor

_Updated: 2026-06-09 06:19 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [11m15s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467489) | [33m51s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720702) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [22m05s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720412) | [24m16s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315047) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [22m27s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276314995) | [23m27s](https://github.com/iree-org/iree/actions/runs/27195011646/job/80287893581) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [17m19s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276314986) | [22m33s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467551) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [15m02s](https://github.com/iree-org/iree/actions/runs/27195011646/job/80287893475) | [21m48s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467563) | 50% (1/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [10m54s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720506) | [16m12s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720618) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [14m36s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467499) | [15m48s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315014) | 0% (0/1) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [10m18s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720451) | [11m59s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315126) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [6m03s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720419) | [11m26s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315016) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [5m48s](https://github.com/iree-org/iree/actions/runs/27195011646/job/80287893468) | [10m48s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467480) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m40s](https://github.com/iree-org/iree/actions/runs/27199888844/job/80300918918) | [1m40s](https://github.com/iree-org/iree/actions/runs/27199888844/job/80300918918) | 0% (0/1) | 1 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27204090772/job/80315252910) | [1m29s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772388) | 0% (0/3) | 15 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/27195011777/job/80284352058) | [1m11s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772350) | 0% (0/3) | 15 |
| `azure-linux-scale` | ossci | 25 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/27195011777/job/80284352593) | [1m01s](https://github.com/iree-org/iree/actions/runs/27204090772/job/80315253004) | 0% (0/8) | 25 |
| `windows-2022` | github-hosted | 14 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772334) | [50s](https://github.com/iree-org/iree/actions/runs/27204090772/job/80315252881) | 0% (0/3) | 14 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467474) | [19s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315333) | 0% (0/4) | 16 |
| `ubuntu-24.04` | github-hosted | 92 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27195011240/job/80284314030) | [4s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467532) | 18% (4/22) | 92 |
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27203218224/job/80312199140) | [3s](https://github.com/iree-org/iree/actions/runs/27203218224/job/80312199157) | 0% (0/3) | 18 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27199845654/job/80300772154) | [3s](https://github.com/iree-org/iree/actions/runs/27199845654/job/80300772154) | 100% (1/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720342) | [2s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467337) | 100% (1/1) | 4 |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720388) | [2s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467367) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27195011777/job/80284352858) | [1s](https://github.com/iree-org/iree/actions/runs/27204090772/job/80315252986) | 0% (0/1) | 4 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27195011646/job/80287893484) | [1s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720503) | 0% (0/1) | `iree-mi308-1` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [24m30s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315187) | [33m51s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720702) | [33m51s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720702) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [22m05s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720412) | [24m16s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315047) | [24m16s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315047) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [22m27s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276314995) | [23m27s](https://github.com/iree-org/iree/actions/runs/27195011646/job/80287893581) | [23m27s](https://github.com/iree-org/iree/actions/runs/27195011646/job/80287893581) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [17m19s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276314986) | [22m33s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467551) | [22m33s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467551) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [11m15s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467489) | [22m23s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720511) | [22m23s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720511) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [17m37s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315028) | [21m48s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467563) | [21m48s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467563) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [15m02s](https://github.com/iree-org/iree/actions/runs/27195011646/job/80287893475) | [20m16s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467466) | [20m16s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467466) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [15m53s](https://github.com/iree-org/iree/actions/runs/27195011646/job/80287893618) | [16m12s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720618) | [16m12s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720618) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [14m36s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467499) | [15m48s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315014) | [15m48s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315014) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [10m18s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720451) | [11m59s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315126) | [11m59s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315126) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [10m54s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720506) | [11m32s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467472) | [11m32s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467472) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [6m03s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720419) | [11m26s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315016) | [11m26s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315016) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [5m48s](https://github.com/iree-org/iree/actions/runs/27195011646/job/80287893468) | [10m48s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467480) | [10m48s](https://github.com/iree-org/iree/actions/runs/27188475787/job/80266467480) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [6m21s](https://github.com/iree-org/iree/actions/runs/27204090791/job/80316720601) | [7m15s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315110) | [7m15s](https://github.com/iree-org/iree/actions/runs/27192246864/job/80276315110) | 2 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27204090772/job/80315252827) | [1m51s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772271) | [1m51s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772271) | 4 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m40s](https://github.com/iree-org/iree/actions/runs/27199888844/job/80300918918) | [1m40s](https://github.com/iree-org/iree/actions/runs/27199888844/job/80300918918) | [1m40s](https://github.com/iree-org/iree/actions/runs/27199888844/job/80300918918) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 4 | 0 | — | — | [1m11s](https://github.com/iree-org/iree/actions/runs/27195011777/job/80284352068) | [1m37s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772429) | [1m37s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772429) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 4 | 0 | — | — | [50s](https://github.com/iree-org/iree/actions/runs/27204090772/job/80315252891) | [1m29s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772388) | [1m29s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772388) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27192246801/job/80275057683) | [1m17s](https://github.com/iree-org/iree/actions/runs/27195011777/job/80284352293) | [1m17s](https://github.com/iree-org/iree/actions/runs/27195011777/job/80284352293) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 4 | 0 | — | — | [1m11s](https://github.com/iree-org/iree/actions/runs/27188475789/job/80262772350) | [1m11s](https://github.com/iree-org/iree/actions/runs/27192246801/job/80275057710) | [1m11s](https://github.com/iree-org/iree/actions/runs/27192246801/job/80275057710) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 351 | 1% (5/351) |  | 41m17s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 295 | 4% (13/295) |  | 53m26s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 280 | 1% (4/280) |  | 57m14s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 257 | 0% (0/257) |  | 59m39s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 83 | 0% (0/83) |  | 1h10m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
