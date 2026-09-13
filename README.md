# iree-ci-monitor

_Updated: 2026-09-13 04:58 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528359) | [8s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528447) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528373) | [5s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528385) | — | 3 |
| `ubuntu-24.04` | github-hosted | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528371) | [3s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528374) | 0% (0/1) | 6 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528398) | [3s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528453) | — | 2 |
| `Linux,X64,gfx1201` | self-hosted | 1 | 1 | [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 1 | [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528447) | [8s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528447) | [8s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528447) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528359) | [7s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528359) | [7s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528359) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528373) | [5s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528373) | [5s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528373) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528385) | [5s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528385) | [5s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528385) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528362) | [4s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528362) | [4s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528362) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528374) | [3s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528374) | [3s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528374) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528453) | [3s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528453) | [3s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528453) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528375) | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528375) | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528375) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528371) | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528371) | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528371) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528426) | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528426) | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528426) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677509993) | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677509993) | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677509993) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528398) | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528398) | [2s](https://github.com/iree-org/iree/actions/runs/34739817131/job/103677528398) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34739791629/job/103677437119) | [2s](https://github.com/iree-org/iree/actions/runs/34739791629/job/103677437119) | [2s](https://github.com/iree-org/iree/actions/runs/34739791629/job/103677437119) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | 0s | 0s | 0s | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 254 | 8% (20/254) |  | 1d11h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 284 | 1% (4/284) |  | 1d11h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 214 | 1% (3/214) |  | 1d12h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 208 | 1% (2/208) |  | 1d12h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 2h00m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
