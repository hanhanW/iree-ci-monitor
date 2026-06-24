# iree-ci-monitor

_Updated: 2026-06-24 06:06 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [14m55s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261714) | [34m08s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554303) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189553827) | [30m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097812) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [15m34s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261770) | [28m12s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097782) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [11m35s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261707) | [25m40s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554191) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [13m37s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139098024) | [25m19s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097849) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [7m02s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097970) | [21m03s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554179) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [9m05s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261653) | [19m20s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097852) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [8m15s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139098052) | [17m46s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554210) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [9m11s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261803) | [16m40s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097974) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261734) | [10m09s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097759) | 50% (1/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [3m58s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261814) | [7m36s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554108) | 0% (0/1) | `shark01-ci`, `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 12 | 0 | — | — | 0 | [19s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261647) | [2m23s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097876) | 0% (0/4) | 12 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m28s](https://github.com/iree-org/iree/actions/runs/28091828575/job/83171474390) | [1m28s](https://github.com/iree-org/iree/actions/runs/28091828575/job/83171474390) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/28079587977/job/83131285389) | [1m14s](https://github.com/iree-org/iree/actions/runs/28090664452/job/83178150313) | 0% (0/3) | 12 |
| `macos-14` | github-hosted | 12 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869754) | [42s](https://github.com/iree-org/iree/actions/runs/28096680186/job/83187846485) | 0% (0/3) | 12 |
| `azure-linux-scale` | ossci | 18 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/28090664452/job/83178150400) | [37s](https://github.com/iree-org/iree/actions/runs/28096680186/job/83187846616) | 0% (0/8) | 18 |
| `ubuntu-24.04` | github-hosted | 73 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/28091828384/job/83171473527) | [4s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261715) | 14% (3/22) | 73 |
| `windows-2022` | github-hosted | 11 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28090664452/job/83178150311) | [4s](https://github.com/iree-org/iree/actions/runs/28096680186/job/83187846536) | 0% (0/3) | 11 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28095981924/job/83185471572) | [3s](https://github.com/iree-org/iree/actions/runs/28095981924/job/83185471581) | 0% (0/3) | 12 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/28091803077/job/83171386382) | [3s](https://github.com/iree-org/iree/actions/runs/28091803077/job/83171386382) | — | 1 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261701) | [2s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554150) | 0% (0/1) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28090664452/job/83178150488) | [1s](https://github.com/iree-org/iree/actions/runs/28096680186/job/83187846582) | 0% (0/1) | 3 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 6 | [21h50m](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257221) | 2026-06-24 06:06 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [21h50m](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257221) | 2026-06-24 06:06 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [16h28m](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409541) | 2026-06-24 06:06 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/bjacob/cpu-ukernel-pipeline-test` | pull_request |
| [16h15m](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990411) | 2026-06-24 06:06 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/bjacob/cpu-ukernel-bodies` | pull_request |
| [5h47m](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097808) | 2026-06-24 06:06 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `fix-24624-raise-special-ops-memref-crash` | pull_request |
| [1h41m](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261695) | 2026-06-24 06:06 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `flow_empty_fold` | pull_request |
| [1h00m](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554091) | 2026-06-24 06:06 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 6 | 6 | [21h50m](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257221) | 2026-06-24 06:06 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [14m55s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261714) | [34m08s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554303) | [34m08s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554303) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189553827) | [30m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097812) | [30m22s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097812) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [15m34s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261770) | [28m12s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097782) | [28m12s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097782) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [11m35s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261707) | [25m40s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554191) | [25m40s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554191) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [16m48s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554189) | [25m19s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097849) | [25m19s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097849) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [7m02s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097970) | [21m03s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554179) | [21m03s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554179) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [9m05s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261653) | [19m20s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097852) | [19m20s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097852) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [8m24s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261818) | [17m46s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554210) | [17m46s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554210) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [9m11s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261803) | [16m40s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097974) | [16m40s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097974) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [13m37s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139098024) | [15m37s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261825) | [15m37s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261825) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [12m46s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261732) | [13m18s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554227) | [13m18s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554227) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [4m42s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554219) | [10m09s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097759) | [10m09s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097759) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [8m15s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139098052) | [9m19s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554121) | [9m19s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554121) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [3m58s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261814) | [7m36s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554108) | [7m36s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554108) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261734) | [4m36s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554134) | [4m36s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554134) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 3 | 0 | — | — | [2m23s](https://github.com/iree-org/iree/actions/runs/28072661834/job/83139097876) | [3m13s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261817) | [3m13s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261817) | 3 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83178151668) | [1m35s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83187851478) | [1m35s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83187851478) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 3 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28096680186/job/83187846463) | [1m29s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869744) | [1m29s](https://github.com/iree-org/iree/actions/runs/28072661843/job/83137869744) | 3 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m28s](https://github.com/iree-org/iree/actions/runs/28091828575/job/83171474390) | [1m28s](https://github.com/iree-org/iree/actions/runs/28091828575/job/83171474390) | [1m28s](https://github.com/iree-org/iree/actions/runs/28091828575/job/83171474390) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 113 | 4% (5/113) |  | 22m19s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 113 | 0% (0/113) |  | 29m54s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 143 | 0% (0/143) |  | 34m37s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 100 | 0% (0/100) |  | 38m45s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 32 | 0% (0/32) |  | 50m40s ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 21h50m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
