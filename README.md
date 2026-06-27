# iree-ci-monitor

_Updated: 2026-06-26 18:18 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [18m26s](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447567) | [42m08s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940159) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [39m36s](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447582) | [40m00s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940116) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [1m20s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940078) | [37m02s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677931) | — | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [33m06s](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447529) | [36m07s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722678023) | — | `shark01-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [12m31s](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447579) | [35m06s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722678062) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [16m21s](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447517) | [28m28s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677743) | — | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [3m43s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722939968) | [25m42s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677951) | — | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [9m14s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940156) | [19m35s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722678031) | — | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 3 | 0 | — | — | 0 | [9m06s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722678038) | [18m02s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940135) | — | `iree-mi308-1` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [6m32s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940191) | [16m47s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940129) | — | `shark01-ci`, `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 12 | 0 | — | — | 0 | [3m04s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722939970) | [11m22s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940130) | — | 12 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [6m40s](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447555) | [9m03s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677943) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [6m45s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677821) | [8m06s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722939765) | — | `shark75-ci` |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [34s](https://github.com/iree-org/iree/actions/runs/28256204268/job/83719823481) | [4m47s](https://github.com/iree-org/iree/actions/runs/28256257540/job/83720229375) | — | 12 |
| `ubuntu-24.04` | github-hosted | 70 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447569) | [4m17s](https://github.com/iree-org/iree/actions/runs/28256241172/job/83720210109) | — | 70 |
| `azure-linux-scale` | ossci | 21 | 0 | — | — | 0 | [2m09s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83720191423) | [3m53s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83719826400) | — | 21 |
| `windows-2022` | github-hosted | 12 | 0 | — | — | 0 | [56s](https://github.com/iree-org/iree/actions/runs/28256204268/job/83719823468) | [2m26s](https://github.com/iree-org/iree/actions/runs/28256257540/job/83720229366) | — | 12 |
| `macos-14` | github-hosted | 12 | 0 | — | — | 0 | [36s](https://github.com/iree-org/iree/actions/runs/28256257540/job/83720229191) | [1m52s](https://github.com/iree-org/iree/actions/runs/28256241172/job/83720210099) | — | 12 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28256140516/job/83719584689) | [4s](https://github.com/iree-org/iree/actions/runs/28256140516/job/83719584692) | — | 3 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28256241172/job/83720210110) | [1s](https://github.com/iree-org/iree/actions/runs/28256257540/job/83720229693) | — | 4 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 3 | 3 | [6h59m](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447477) | 2026-06-26 18:17 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [6h59m](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447477) | 2026-06-26 18:17 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/scalable_distribution_tiling` | pull_request |
| [6h58m](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677804) | 2026-06-26 18:17 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/scalable_vector_level_tiling` | pull_request |
| [6h56m](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722939709) | 2026-06-26 18:17 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/overload_iree_tiling_interface_ops` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 3 | 3 | [6h59m](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447477) | 2026-06-26 18:17 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [27m59s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677954) | [42m08s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940159) | [42m08s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940159) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [39m36s](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447582) | [40m00s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940116) | [40m00s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940116) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [1m20s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940078) | [37m02s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677931) | [37m02s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677931) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [33m06s](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447529) | [36m07s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722678023) | [36m07s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722678023) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [24m45s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940108) | [35m06s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722678062) | [35m06s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722678062) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [8m00s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940174) | [29m19s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677947) | [29m19s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677947) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [16m21s](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447517) | [28m28s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677743) | [28m28s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677743) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [3m43s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722939968) | [25m42s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677951) | [25m42s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677951) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [13m53s](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447607) | [24m00s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940076) | [24m00s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940076) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [9m14s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940156) | [19m35s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722678031) | [19m35s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722678031) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 3 | 0 | — | — | [9m06s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722678038) | [18m02s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940135) | [18m02s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940135) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [15m13s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677980) | [16m47s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940129) | [16m47s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940129) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [10m57s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940085) | [15m04s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677894) | [15m04s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677894) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 3 | 0 | — | — | [11m22s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940130) | [12m13s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722678049) | [12m13s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722678049) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 3 | 0 | — | — | [3m04s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722939970) | [10m48s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677941) | [10m48s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677941) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [6m40s](https://github.com/iree-org/iree/actions/runs/28256257762/job/83722447555) | [9m03s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677943) | [9m03s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677943) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [6m45s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677821) | [8m06s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722939765) | [8m06s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722939765) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 3 | 0 | — | — | [1m18s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722677765) | [6m53s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722939760) | [6m53s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722939760) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [6m32s](https://github.com/iree-org/iree/actions/runs/28256203862/job/83722940191) | [6m50s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722678009) | [6m50s](https://github.com/iree-org/iree/actions/runs/28256241017/job/83722678009) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 119 | 0% (0/119) |  | 6h07m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 95 | 8% (8/95) |  | 6h17m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 91 | 0% (0/91) |  | 6h19m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 85 | 0% (0/85) |  | 6h21m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 26 | 0% (0/26) |  | 6h28m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 6h59m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
