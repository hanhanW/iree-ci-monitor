# iree-ci-monitor

_Updated: 2026-09-01 14:05 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 5 | 0 | — | — | 0 | [30m07s](https://github.com/iree-org/iree/actions/runs/33538087916/job/99961343480) | [44m37s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99933012399) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 10 | 0 | — | — | 0 | [14m59s](https://github.com/iree-org/iree/actions/runs/33538087916/job/99961344001) | [34m02s](https://github.com/iree-org/iree/actions/runs/33529594729/job/99931596789) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [23m42s](https://github.com/iree-org/iree/actions/runs/33529594729/job/99931596672) | [29m14s](https://github.com/iree-org/iree/actions/runs/33505312909/job/99913607938) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 5 | 0 | — | — | 0 | [14m36s](https://github.com/iree-org/iree/actions/runs/33529594729/job/99931596710) | [23m38s](https://github.com/iree-org/iree/actions/runs/33505312909/job/99913608129) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 5 | 0 | — | — | 0 | [13m35s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99933012256) | [22m56s](https://github.com/iree-org/iree/actions/runs/33529594729/job/99931596575) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [8m51s](https://github.com/iree-org/iree/actions/runs/33524814253/job/99916214391) | [22m55s](https://github.com/iree-org/iree/actions/runs/33529594729/job/99931596745) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 5 | 0 | — | — | 0 | [18m47s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99933012358) | [21m51s](https://github.com/iree-org/iree/actions/runs/33505312909/job/99913607906) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [8m07s](https://github.com/iree-org/iree/actions/runs/33524814253/job/99916214472) | [16m47s](https://github.com/iree-org/iree/actions/runs/33505312909/job/99913608053) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 10 | 0 | — | — | 0 | [4m28s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99933012422) | [12m24s](https://github.com/iree-org/iree/actions/runs/33538087916/job/99961343857) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 10 | 0 | — | — | 0 | [5m54s](https://github.com/iree-org/iree/actions/runs/33538087916/job/99961343695) | [12m13s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99933012330) | 0% (0/4) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 10 | 0 | — | — | 0 | [4m51s](https://github.com/iree-org/iree/actions/runs/33524814253/job/99916214522) | [11m41s](https://github.com/iree-org/iree/actions/runs/33524814253/job/99916214835) | 0% (0/4) | `shark10-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 27 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/33538087959/job/99957327477) | [2m18s](https://github.com/iree-org/iree/actions/runs/33524814253/job/99912912963) | 0% (0/12) | 27 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33529980743/job/99930480666) | [5s](https://github.com/iree-org/iree/actions/runs/33505312904/job/99910240466) | 0% (0/6) | 15 |
| `ubuntu-24.04` | github-hosted | 99 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33529980617/job/99930389244) | [4s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99933011937) | 0% (0/38) | 99 |
| `windows-2022` | github-hosted | 15 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33505312904/job/99910239984) | [4s](https://github.com/iree-org/iree/actions/runs/33505312904/job/99910240410) | 0% (0/6) | 15 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33505312904/job/99910240077) | [4s](https://github.com/iree-org/iree/actions/runs/33505312904/job/99910240471) | 0% (0/6) | 15 |
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33538697805/job/99959331907) | [4s](https://github.com/iree-org/iree/actions/runs/33517889306/job/99889445471) | 0% (0/6) | 18 |
| `azure-windows-scale` | ossci | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33505312904/job/99910240506) | [2s](https://github.com/iree-org/iree/actions/runs/33538087959/job/99957327341) | 0% (0/2) | 5 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 5 | 0 | — | — | [30m07s](https://github.com/iree-org/iree/actions/runs/33538087916/job/99961343480) | [44m37s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99933012399) | [44m37s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99933012399) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [19m28s](https://github.com/iree-org/iree/actions/runs/33538087916/job/99961343566) | [34m02s](https://github.com/iree-org/iree/actions/runs/33529594729/job/99931596789) | [34m02s](https://github.com/iree-org/iree/actions/runs/33529594729/job/99931596789) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 5 | 0 | — | — | [23m42s](https://github.com/iree-org/iree/actions/runs/33529594729/job/99931596672) | [29m14s](https://github.com/iree-org/iree/actions/runs/33505312909/job/99913607938) | [29m14s](https://github.com/iree-org/iree/actions/runs/33505312909/job/99913607938) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 5 | 0 | — | — | [14m36s](https://github.com/iree-org/iree/actions/runs/33529594729/job/99931596710) | [23m38s](https://github.com/iree-org/iree/actions/runs/33505312909/job/99913608129) | [23m38s](https://github.com/iree-org/iree/actions/runs/33505312909/job/99913608129) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [14m59s](https://github.com/iree-org/iree/actions/runs/33538087916/job/99961344001) | [23m24s](https://github.com/iree-org/iree/actions/runs/33524814253/job/99916214660) | [23m24s](https://github.com/iree-org/iree/actions/runs/33524814253/job/99916214660) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 5 | 0 | — | — | [13m35s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99933012256) | [22m56s](https://github.com/iree-org/iree/actions/runs/33529594729/job/99931596575) | [22m56s](https://github.com/iree-org/iree/actions/runs/33529594729/job/99931596575) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 5 | 0 | — | — | [8m51s](https://github.com/iree-org/iree/actions/runs/33524814253/job/99916214391) | [22m55s](https://github.com/iree-org/iree/actions/runs/33529594729/job/99931596745) | [22m55s](https://github.com/iree-org/iree/actions/runs/33529594729/job/99931596745) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 5 | 0 | — | — | [18m47s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99933012358) | [21m51s](https://github.com/iree-org/iree/actions/runs/33505312909/job/99913607906) | [21m51s](https://github.com/iree-org/iree/actions/runs/33505312909/job/99913607906) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 5 | 0 | — | — | [8m07s](https://github.com/iree-org/iree/actions/runs/33524814253/job/99916214472) | [16m47s](https://github.com/iree-org/iree/actions/runs/33505312909/job/99913608053) | [16m47s](https://github.com/iree-org/iree/actions/runs/33505312909/job/99913608053) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [9m00s](https://github.com/iree-org/iree/actions/runs/33529594729/job/99931596958) | [12m24s](https://github.com/iree-org/iree/actions/runs/33538087916/job/99961343857) | [12m24s](https://github.com/iree-org/iree/actions/runs/33538087916/job/99961343857) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [10m03s](https://github.com/iree-org/iree/actions/runs/33505312909/job/99913608173) | [12m13s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99933012330) | [12m13s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99933012330) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 5 | 0 | — | — | [3m15s](https://github.com/iree-org/iree/actions/runs/33529594729/job/99931596934) | [11m41s](https://github.com/iree-org/iree/actions/runs/33524814253/job/99916214835) | [11m41s](https://github.com/iree-org/iree/actions/runs/33524814253/job/99916214835) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [3m09s](https://github.com/iree-org/iree/actions/runs/33524814253/job/99916214795) | [11m02s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99933012345) | [11m02s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99933012345) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [5m48s](https://github.com/iree-org/iree/actions/runs/33529594729/job/99931596864) | [8m18s](https://github.com/iree-org/iree/actions/runs/33524814253/job/99916214570) | [8m18s](https://github.com/iree-org/iree/actions/runs/33524814253/job/99916214570) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 5 | 0 | — | — | [5m00s](https://github.com/iree-org/iree/actions/runs/33505312909/job/99913608060) | [7m47s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99933012130) | [7m47s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99933012130) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 5 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/33529980743/job/99930481503) | [2m19s](https://github.com/iree-org/iree/actions/runs/33524814070/job/99912905354) | [2m19s](https://github.com/iree-org/iree/actions/runs/33524814070/job/99912905354) | 5 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 5 | 0 | — | — | [1m03s](https://github.com/iree-org/iree/actions/runs/33529980919/job/99930492874) | [2m18s](https://github.com/iree-org/iree/actions/runs/33524814253/job/99912912963) | [2m18s](https://github.com/iree-org/iree/actions/runs/33524814253/job/99912912963) | 5 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 5 | 0 | — | — | [21s](https://github.com/iree-org/iree/actions/runs/33529594798/job/99929121639) | [2m17s](https://github.com/iree-org/iree/actions/runs/33524814070/job/99912905286) | [2m17s](https://github.com/iree-org/iree/actions/runs/33524814070/job/99912905286) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 5 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/33529594798/job/99929121689) | [1m38s](https://github.com/iree-org/iree/actions/runs/33538087959/job/99957327385) | [1m38s](https://github.com/iree-org/iree/actions/runs/33538087959/job/99957327385) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 5 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/33529980743/job/99930481277) | [1m28s](https://github.com/iree-org/iree/actions/runs/33538087959/job/99957327227) | [1m28s](https://github.com/iree-org/iree/actions/runs/33538087959/job/99957327227) | 5 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 294 | 0% (1/294) |  | 2h45m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 215 | 0% (1/215) |  | 2h56m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 241 | 4% (10/241) |  | 2h58m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 203 | 0% (0/203) |  | 3h07m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
