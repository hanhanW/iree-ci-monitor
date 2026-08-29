# iree-ci-monitor

_Updated: 2026-08-29 00:10 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090337) | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090372) | — | 3 |
| `ubuntu-24.04` | github-hosted | 13 | 7 | [4h28m](https://github.com/iree-org/iree/actions/runs/32985622770/job/98231128361) | 2026-08-26 13:05 PDT | 2 | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090341) | [3s](https://github.com/iree-org/iree/actions/runs/33235631932/job/99056003516) | 0% (0/1) | 6 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090377) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090379) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090403) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090413) | — | 2 |
| `ubuntu-latest` | github-hosted | 9 | 9 | [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028102) | 2026-08-26 13:05 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028102) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | `refs/pull/24852/head` | dynamic |
| [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028148) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | `refs/pull/24852/head` | dynamic |
| [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028155) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | `refs/pull/24852/head` | dynamic |
| [4h28m](https://github.com/iree-org/iree/actions/runs/32985518325/job/98231089680) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | `refs/pull/24851/head` | dynamic |
| [4h28m](https://github.com/iree-org/iree/actions/runs/32985518325/job/98231089764) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | `refs/pull/24851/head` | dynamic |
| [4h28m](https://github.com/iree-org/iree/actions/runs/32985518325/job/98231089780) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | `refs/pull/24851/head` | dynamic |
| [4h28m](https://github.com/iree-org/iree/actions/runs/32985622770/job/98231128361) | 2026-08-26 13:05 PDT | `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | `users/egebeysel/scalable-dist-4-pack-distribution-hints` | pull_request |
| [4h27m](https://github.com/iree-org/iree/actions/runs/32985674221/job/98231234420) | 2026-08-26 13:05 PDT | `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | `users/egebeysel/scalable-dist-5-distribution-tiling-tests` | pull_request |
| [4h27m](https://github.com/iree-org/iree/actions/runs/32985693175/job/98231275534) | 2026-08-26 13:05 PDT | `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | `users/egebeysel/scalable-dist-2-distribution-tile-sizes` | pull_request |
| [4h27m](https://github.com/iree-org/iree/actions/runs/32985674146/job/98231288233) | 2026-08-26 13:05 PDT | `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | `users/egebeysel/scalable-dist-5-distribution-tiling-tests` | pull_request |
| [4h26m](https://github.com/iree-org/iree/actions/runs/32985715581/job/98231323412) | 2026-08-26 13:05 PDT | `.github/workflows/clang_tidy.yml` | clang-tidy | `ubuntu-24.04` | `users/egebeysel/scalable-dist-1-vscale-range-target-field` | pull_request |
| [4h26m](https://github.com/iree-org/iree/actions/runs/32985518655/job/98231324540) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | `refs/pull/24850/head` | dynamic |
| [4h26m](https://github.com/iree-org/iree/actions/runs/32985518655/job/98231324643) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | `refs/pull/24850/head` | dynamic |
| [4h26m](https://github.com/iree-org/iree/actions/runs/32985518655/job/98231324649) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | `refs/pull/24850/head` | dynamic |
| [4h26m](https://github.com/iree-org/iree/actions/runs/32985698522/job/98231380998) | 2026-08-26 13:05 PDT | `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | `users/egebeysel/scalable-dist-5-distribution-tiling-tests` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 3 | [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028148) | 2026-08-26 13:05 PDT | 0s | 0s | 0s | 0 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 3 | [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028102) | 2026-08-26 13:05 PDT | 0s | 0s | 0s | 0 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 3 | [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028155) | 2026-08-26 13:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 1 | [4h28m](https://github.com/iree-org/iree/actions/runs/32985622770/job/98231128361) | 2026-08-26 13:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | 2 | 2 | [4h27m](https://github.com/iree-org/iree/actions/runs/32985674221/job/98231234420) | 2026-08-26 13:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 2 | 2 | [4h27m](https://github.com/iree-org/iree/actions/runs/32985674146/job/98231288233) | 2026-08-26 13:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/clang_tidy.yml` | clang-tidy | `ubuntu-24.04` | 1 | 1 | [4h26m](https://github.com/iree-org/iree/actions/runs/32985715581/job/98231323412) | 2026-08-26 13:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | 1 | 1 | [4h26m](https://github.com/iree-org/iree/actions/runs/32985698522/job/98231380998) | 2026-08-26 13:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090372) | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090372) | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090372) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090336) | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090336) | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090336) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090337) | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090337) | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090337) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090377) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090377) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090377) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090379) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090379) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090379) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090413) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090413) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090413) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33235631932/job/99056003516) | [3s](https://github.com/iree-org/iree/actions/runs/33235631932/job/99056003516) | [3s](https://github.com/iree-org/iree/actions/runs/33235631932/job/99056003516) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090339) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090339) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090339) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090360) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090360) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090360) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090341) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090341) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090341) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090460) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090460) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090460) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056070342) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056070342) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056070342) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 307 | 1% (2/307) |  | 12h38m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 265 | 3% (8/265) |  | 14h20m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 219 | 0% (1/219) |  | 14h21m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 215 | 0% (0/215) |  | 14h29m ago |

## Alerts

- **[stale-queued]** `ubuntu-24.04` oldest queued job observed waiting 4h28m (> 2h00m)
- **[stale-queued]** `ubuntu-latest` oldest queued job observed waiting 4h29m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
