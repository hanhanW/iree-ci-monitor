# iree-ci-monitor

_Updated: 2026-05-28 00:42 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [30m10s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341744) | [36m29s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235463973) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [17m32s](https://github.com/iree-org/iree/actions/runs/26549603749/job/78209396995) | [32m53s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041653) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [20m59s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041656) | [32m47s](https://github.com/iree-org/iree/actions/runs/26549603749/job/78209396984) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [21m43s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235463810) | [27m18s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341682) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [18m28s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235463920) | [22m04s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341730) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [12m38s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041658) | [22m03s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235463977) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [7m48s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341685) | [18m56s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041524) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [6m24s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041676) | [17m55s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341740) | 17% (1/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [6m46s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235463969) | [17m08s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341764) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [7m16s](https://github.com/iree-org/iree/actions/runs/26549603749/job/78209397082) | [16m10s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235464004) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 28 | 1 | [1h37m](https://github.com/iree-org/iree/actions/runs/26557770899/job/78233280316) | 2026-05-28 00:41 PDT | 0 | [8s](https://github.com/iree-org/iree/actions/runs/26549603727/job/78208803551) | [10m07s](https://github.com/iree-org/iree/actions/runs/26557770899/job/78233280070) | 0% (0/18) | 22 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [6m00s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041633) | [6m28s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341751) | 0% (0/3) | `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/26549603749/job/78209396989) | [8s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235463950) | 0% (0/12) | 16 |
| `windows-2022` | github-hosted | 17 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26557736495/job/78233126168) | [4s](https://github.com/iree-org/iree/actions/runs/26558657012/job/78236124490) | 0% (0/9) | 17 |
| `ubuntu-24.04` | github-hosted | 116 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26549352370/job/78208029415) | [3s](https://github.com/iree-org/iree/actions/runs/26557736495/job/78233126131) | 7% (4/59) | 110 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26557736495/job/78233126064) | [3s](https://github.com/iree-org/iree/actions/runs/26558657012/job/78236124482) | 0% (0/9) | 18 |
| `macos-14` | github-hosted | 17 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26557770899/job/78233279940) | [3s](https://github.com/iree-org/iree/actions/runs/26558657012/job/78236124495) | 0% (0/9) | 17 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041538) | [2s](https://github.com/iree-org/iree/actions/runs/26549603749/job/78209396832) | 0% (0/3) | 4 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235463958) | [2s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041655) | 33% (1/3) | `iree-mi308-1` |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26549603438/job/78208786266) | [2s](https://github.com/iree-org/iree/actions/runs/26549781614/job/78209323411) | 0% (0/9) | 15 |
| `azure-windows-scale` | ossci | 5 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26549603727/job/78208803561) | [1s](https://github.com/iree-org/iree/actions/runs/26557770899/job/78233280122) | 0% (0/3) | 5 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [1h37m](https://github.com/iree-org/iree/actions/runs/26557770899/job/78233280316) | 2026-05-28 00:41 PDT | `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | `add-rpi-gpu-config` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 5 | 1 | [1h37m](https://github.com/iree-org/iree/actions/runs/26557770899/job/78233280316) | 2026-05-28 00:41 PDT | [8s](https://github.com/iree-org/iree/actions/runs/26544747162/job/78194132507) | [9s](https://github.com/iree-org/iree/actions/runs/26549603727/job/78208803542) | [9s](https://github.com/iree-org/iree/actions/runs/26549603727/job/78208803542) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [30m10s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341744) | [36m29s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235463973) | [36m29s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235463973) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [30m12s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235464019) | [32m53s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041653) | [32m53s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041653) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [20m59s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041656) | [32m47s](https://github.com/iree-org/iree/actions/runs/26549603749/job/78209396984) | [32m47s](https://github.com/iree-org/iree/actions/runs/26549603749/job/78209396984) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [21m43s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235463810) | [27m18s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341682) | [27m18s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341682) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [18m28s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235463920) | [22m04s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341730) | [22m04s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341730) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [13m48s](https://github.com/iree-org/iree/actions/runs/26549603749/job/78209396996) | [22m03s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235463977) | [22m03s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235463977) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [10m44s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235463967) | [21m48s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041650) | [21m48s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041650) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [7m48s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341685) | [18m56s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041524) | [18m56s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041524) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [6m24s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041676) | [17m55s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341740) | [17m55s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341740) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [10m37s](https://github.com/iree-org/iree/actions/runs/26549603749/job/78209396981) | [17m08s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341764) | [17m08s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341764) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [11m07s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041670) | [16m36s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341822) | [16m36s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341822) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [7m16s](https://github.com/iree-org/iree/actions/runs/26549603749/job/78209397082) | [16m10s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235464004) | [16m10s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235464004) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [5m35s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341773) | [13m11s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235464011) | [13m11s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235464011) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [9m43s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78235464010) | [12m20s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341771) | [12m20s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341771) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 5 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/26549603727/job/78208803556) | [10m08s](https://github.com/iree-org/iree/actions/runs/26557770899/job/78233279933) | [10m08s](https://github.com/iree-org/iree/actions/runs/26557770899/job/78233279933) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 5 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/26549603727/job/78208803570) | [10m07s](https://github.com/iree-org/iree/actions/runs/26557770899/job/78233280070) | [10m07s](https://github.com/iree-org/iree/actions/runs/26557770899/job/78233280070) | 4 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 5 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78194133027) | [9m56s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78233245029) | [9m56s](https://github.com/iree-org/iree/actions/runs/26557770874/job/78233245029) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 5 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/26549603727/job/78208803551) | [9m54s](https://github.com/iree-org/iree/actions/runs/26557770899/job/78233280167) | [9m54s](https://github.com/iree-org/iree/actions/runs/26557770899/job/78233280167) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [6m00s](https://github.com/iree-org/iree/actions/runs/26544747176/job/78195041633) | [6m28s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341751) | [6m28s](https://github.com/iree-org/iree/actions/runs/26547819241/job/78204341751) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 287 | 2% (5/287) |  | 28m22s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 260 | 5% (13/260) |  | 50m57s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 220 | 2% (5/220) |  | 54m32s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 206 | 1% (2/206) |  | 54m34s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 69 | 1% (1/69) |  | 1h08m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
