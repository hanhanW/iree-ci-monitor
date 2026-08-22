# iree-ci-monitor

_Updated: 2026-08-22 06:02 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259625) | [7s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259518) | — | 3 |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/97022593147) | [4s](https://github.com/iree-org/iree/actions/runs/32569405589/job/97022606638) | 0% (0/1) | 10 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259570) | [3s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259567) | — | 2 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32569720185/job/97023379707) | [3s](https://github.com/iree-org/iree/actions/runs/32569491194/job/97022816137) | — | 9 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259542) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259574) | — | 2 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759524) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759599) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759660) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759688) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | — | 0 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759971) | 2026-08-19 00:07 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759524) | 2026-08-19 00:07 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759660) | 2026-08-19 00:07 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759599) | 2026-08-19 00:07 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759971) | 2026-08-19 00:07 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 1 | [14m13s](https://github.com/iree-org/iree/actions/runs/32223166720/job/95983759688) | 2026-08-19 00:07 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259518) | [7s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259518) | [7s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259518) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259625) | [6s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259625) | [6s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259625) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259533) | [4s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259533) | [4s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259533) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984237827) | [4s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984237827) | [4s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984237827) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32569405589/job/97022606638) | [4s](https://github.com/iree-org/iree/actions/runs/32569405589/job/97022606638) | [4s](https://github.com/iree-org/iree/actions/runs/32569405589/job/97022606638) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32569720887/job/97023367806) | [3s](https://github.com/iree-org/iree/actions/runs/32569491194/job/97022816137) | [3s](https://github.com/iree-org/iree/actions/runs/32569491194/job/97022816137) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/32569720887/job/97023367837) | [3s](https://github.com/iree-org/iree/actions/runs/32569491194/job/97022815980) | [3s](https://github.com/iree-org/iree/actions/runs/32569491194/job/97022815980) | 2 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259566) | [3s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259566) | [3s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259566) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259567) | [3s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259567) | [3s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259567) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32569468667/job/97022758871) | [3s](https://github.com/iree-org/iree/actions/runs/32569468667/job/97022758871) | [3s](https://github.com/iree-org/iree/actions/runs/32569468667/job/97022758871) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32569491194/job/97022816159) | [2s](https://github.com/iree-org/iree/actions/runs/32569720887/job/97023367720) | [2s](https://github.com/iree-org/iree/actions/runs/32569720887/job/97023367720) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/97022593147) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/97022593147) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/97022593147) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259520) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259520) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259520) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259549) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259549) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259549) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259511) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259511) | [2s](https://github.com/iree-org/iree/actions/runs/32553615346/job/96984259511) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 196 | 3% (5/195) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 208 | 1% (3/207) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 145 | 0% (0/144) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 150 | 0% (0/149) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
