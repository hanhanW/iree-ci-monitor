# iree-ci-monitor

_Updated: 2026-10-23 14:28 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [4m32s](https://github.com/iree-org/iree/actions/runs/39978153928/job/120508233344) | [30m53s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446571343) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [7m29s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628683) | [25m38s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446571317) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [18m08s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628753) | [20m53s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446570899) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [7m41s](https://github.com/iree-org/iree/actions/runs/39978153928/job/120508233572) | [20m05s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446571347) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [12m22s](https://github.com/iree-org/iree/actions/runs/39978153928/job/120508233531) | [19m41s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628570) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [12m51s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628803) | [14m47s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446570990) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446570815) | [8m26s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628650) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 20 | 0 | — | — | 0 | [31s](https://github.com/iree-org/iree/actions/runs/39975607072/job/120513782628) | [1m29s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214611) | 0% (0/7) | 20 |
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39978143902/job/120498077819) | [19s](https://github.com/iree-org/iree/actions/runs/39967118265/job/120459772951) | 0% (0/3) | 18 |
| `macos-15` | github-hosted | 9 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/39975607072/job/120513782011) | [17s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214387) | 0% (0/3) | 9 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/39962359052/job/120443374383) | [5s](https://github.com/iree-org/iree/actions/runs/39975607072/job/120513782058) | 33% (1/3) | 9 |
| `ubuntu-24.04` | github-hosted | 71 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39978153928/job/120508233792) | [3s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214484) | 4% (1/24) | 67 |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214588) | [3s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214540) | 0% (0/3) | 9 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214976) | [2s](https://github.com/iree-org/iree/actions/runs/39962359052/job/120443374769) | 0% (0/1) | 3 |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [4m32s](https://github.com/iree-org/iree/actions/runs/39978153928/job/120508233344) | [30m53s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446571343) | [30m53s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446571343) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [13m48s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628839) | [25m38s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446571317) | [25m38s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446571317) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [7m29s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628683) | [25m29s](https://github.com/iree-org/iree/actions/runs/39978153928/job/120508233874) | [25m29s](https://github.com/iree-org/iree/actions/runs/39978153928/job/120508233874) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [18m08s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628753) | [20m53s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446570899) | [20m53s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446570899) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [7m41s](https://github.com/iree-org/iree/actions/runs/39978153928/job/120508233572) | [20m05s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446571347) | [20m05s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446571347) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [18m16s](https://github.com/iree-org/iree/actions/runs/39978153928/job/120508233714) | [19m41s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628570) | [19m41s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628570) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [9m20s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446571265) | [15m13s](https://github.com/iree-org/iree/actions/runs/39978153928/job/120508234457) | [15m13s](https://github.com/iree-org/iree/actions/runs/39978153928/job/120508234457) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [12m51s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628803) | [14m47s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446570990) | [14m47s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446570990) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [8m18s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446570941) | [12m22s](https://github.com/iree-org/iree/actions/runs/39978153928/job/120508233531) | [12m22s](https://github.com/iree-org/iree/actions/runs/39978153928/job/120508233531) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [1m56s](https://github.com/iree-org/iree/actions/runs/39978153928/job/120508233998) | [8m26s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628650) | [8m26s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628650) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446570748) | [4m08s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628931) | [4m08s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628931) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 3 | 0 | — | — | [1m16s](https://github.com/iree-org/iree/actions/runs/39962359052/job/120443374365) | [1m29s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214972) | [1m29s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214972) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 2 | 0 | — | — | [1m15s](https://github.com/iree-org/iree/actions/runs/39962359052/job/120443374625) | [1m29s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214611) | [1m29s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214611) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 3 | 0 | — | — | [1m16s](https://github.com/iree-org/iree/actions/runs/39962359052/job/120443374723) | [1m22s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214864) | [1m22s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214864) | 3 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 3 | 0 | — | — | [1m09s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214977) | [1m17s](https://github.com/iree-org/iree/actions/runs/39962359052/job/120443374577) | [1m17s](https://github.com/iree-org/iree/actions/runs/39962359052/job/120443374577) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 3 | 0 | — | — | [17s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498215111) | [1m13s](https://github.com/iree-org/iree/actions/runs/39962359052/job/120443374904) | [1m13s](https://github.com/iree-org/iree/actions/runs/39962359052/job/120443374904) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39962962057/job/120445403257) | [22s](https://github.com/iree-org/iree/actions/runs/39967118265/job/120459772953) | [22s](https://github.com/iree-org/iree/actions/runs/39967118265/job/120459772953) | 4 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39962962057/job/120445403703) | [19s](https://github.com/iree-org/iree/actions/runs/39967118265/job/120459772951) | [19s](https://github.com/iree-org/iree/actions/runs/39967118265/job/120459772951) | 4 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 3 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/39962359052/job/120443374657) | [17s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214387) | [17s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214387) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 3 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214464) | [13s](https://github.com/iree-org/iree/actions/runs/39962359052/job/120443374357) | [13s](https://github.com/iree-org/iree/actions/runs/39962359052/job/120443374357) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 408 | 0% (0/408) |  | 5h02m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 338 | 2% (7/338) |  | 5h08m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
