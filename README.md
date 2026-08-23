# iree-ci-monitor

_Updated: 2026-08-22 19:01 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [5m33s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216550) | [24m53s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216639) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [16m09s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216536) | [21m20s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216580) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [17m16s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216581) | [17m16s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216581) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [17m02s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216490) | [17m02s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216490) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [17m01s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216479) | [17m01s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216479) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [11m19s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216511) | [11m19s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216511) | 0% (0/1) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [5m12s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216488) | [5m38s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216538) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216546) | [5m18s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216530) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949180) | [1m55s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97078950026) | 0% (0/6) | 6 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949080) | [4s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949127) | 0% (0/3) | 3 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/32592725691/job/97078924629) | [4s](https://github.com/iree-org/iree/actions/runs/32592725691/job/97078924451) | 0% (0/3) | 3 |
| `ubuntu-24.04` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216587) | [3s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949093) | 0% (0/18) | 18 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949086) | [3s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949117) | 0% (0/3) | 3 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949134) | [3s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949107) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949183) | [1s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949183) | 0% (0/1) | 1 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216484) | [1s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216484) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216494) | [1s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216494) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216526) | [1s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216526) | 0% (0/1) | `shark10-ci` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [24m53s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216639) | [24m53s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216639) | [24m53s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216639) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [21m20s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216580) | [21m20s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216580) | [21m20s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216580) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [17m16s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216581) | [17m16s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216581) | [17m16s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216581) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [17m02s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216490) | [17m02s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216490) | [17m02s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216490) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [17m01s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216479) | [17m01s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216479) | [17m01s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216479) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [16m09s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216536) | [16m09s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216536) | [16m09s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216536) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [11m19s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216511) | [11m19s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216511) | [11m19s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216511) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [5m38s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216538) | [5m38s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216538) | [5m38s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216538) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [5m33s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216550) | [5m33s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216550) | [5m33s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216550) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [5m18s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216530) | [5m18s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216530) | [5m18s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216530) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [5m12s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216488) | [5m12s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216488) | [5m12s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97080216488) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [1m55s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97078950026) | [1m55s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97078950026) | [1m55s](https://github.com/iree-org/iree/actions/runs/32592726340/job/97078950026) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m25s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949196) | [1m25s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949196) | [1m25s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949196) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [40s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949154) | [40s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949154) | [40s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949154) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949180) | [8s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949180) | [8s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949180) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949161) | [8s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949161) | [8s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949161) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949080) | [4s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949080) | [4s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949080) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949051) | [4s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949051) | [4s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949051) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949127) | [4s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949127) | [4s](https://github.com/iree-org/iree/actions/runs/32592726364/job/97078949127) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32592725691/job/97078924451) | [4s](https://github.com/iree-org/iree/actions/runs/32592725691/job/97078924451) | [4s](https://github.com/iree-org/iree/actions/runs/32592725691/job/97078924451) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 212 | 1% (3/211) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 153 | 0% (0/152) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 201 | 2% (5/200) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 148 | 0% (0/147) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
