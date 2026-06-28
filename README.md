# iree-ci-monitor

_Updated: 2026-06-28 05:47 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463969) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463979) | — | 3 |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463965) | [3s](https://github.com/iree-org/iree/actions/runs/28321109256/job/83903093822) | 0% (0/1) | 10 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903596417) | [3s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584491) | — | 6 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463972) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463975) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463977) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463988) | — | 2 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 6 | [17h43m](https://github.com/iree-org/iree/actions/runs/28298636190/job/83843455562) | 2026-06-28 05:47 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [17h43m](https://github.com/iree-org/iree/actions/runs/28298636190/job/83843455562) | 2026-06-28 05:47 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/fill-buffer-1byte-edge` | pull_request |
| [17h25m](https://github.com/iree-org/iree/actions/runs/28299106146/job/83844610658) | 2026-06-28 05:47 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/copy-buffer-1byte-grid` | pull_request |
| [17h22m](https://github.com/iree-org/iree/actions/runs/28299121805/job/83844820560) | 2026-06-28 05:47 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/indirect-dispatch-stack-garbage` | pull_request |
| [17h19m](https://github.com/iree-org/iree/actions/runs/28299152490/job/83844978281) | 2026-06-28 05:47 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/staging-buffer-overflow` | pull_request |
| [17h18m](https://github.com/iree-org/iree/actions/runs/28299136794/job/83845041346) | 2026-06-28 05:47 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/export-name-lookup` | pull_request |
| [17h17m](https://github.com/iree-org/iree/actions/runs/28299177820/job/83845077655) | 2026-06-28 05:47 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `metal/indirect-dispatch-offset` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 6 | 6 | [17h43m](https://github.com/iree-org/iree/actions/runs/28298636190/job/83843455562) | 2026-06-28 05:47 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463967) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463967) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463967) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463969) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463969) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463969) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463979) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463979) | [5s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463979) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463974) | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463974) | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463974) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883450588) | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883450588) | [3s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883450588) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28313880526/job/83883403723) | [3s](https://github.com/iree-org/iree/actions/runs/28313880526/job/83883403723) | [3s](https://github.com/iree-org/iree/actions/runs/28313880526/job/83883403723) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28321109256/job/83903093822) | [3s](https://github.com/iree-org/iree/actions/runs/28321109256/job/83903093822) | [3s](https://github.com/iree-org/iree/actions/runs/28321109256/job/83903093822) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584491) | [3s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584491) | [3s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584491) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463965) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463965) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463965) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463988) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463988) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463988) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463977) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463977) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463977) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463975) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463975) | [2s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83883463975) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28321153273/job/83903205799) | [2s](https://github.com/iree-org/iree/actions/runs/28321153273/job/83903205799) | [2s](https://github.com/iree-org/iree/actions/runs/28321153273/job/83903205799) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584460) | [2s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584460) | [2s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584460) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584462) | [2s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584462) | [2s](https://github.com/iree-org/iree/actions/runs/28321293665/job/83903584462) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903584185) | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903584185) | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903584185) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903596417) | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903596417) | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903596417) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903596411) | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903596411) | [2s](https://github.com/iree-org/iree/actions/runs/28321293580/job/83903596411) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83903087528) | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83903087528) | [1s](https://github.com/iree-org/iree/actions/runs/28313896423/job/83903087528) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 149 | 0% (0/149) |  | 13h55m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 122 | 7% (9/122) |  | 15h04m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 110 | 0% (0/110) |  | 15h10m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 106 | 0% (0/106) |  | 15h18m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 33 | 0% (0/33) |  | 16h33m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 17h43m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
