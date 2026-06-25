# iree-ci-monitor

_Updated: 2026-06-24 18:19 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28107886109/job/83236316185) | [2s](https://github.com/iree-org/iree/actions/runs/28107886210/job/83236524279) | 50% (1/2) | 2 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 6 | [13h55m](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261695) | 2026-06-24 18:19 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [13h55m](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261695) | 2026-06-24 18:19 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `flow_empty_fold` | pull_request |
| [13h14m](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554091) | 2026-06-24 18:19 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [11h39m](https://github.com/iree-org/iree/actions/runs/28102210744/job/83208735459) | 2026-06-24 18:19 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [11h33m](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184300) | 2026-06-24 18:19 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/bjacob/cpu-ukernel-bodies` | pull_request |
| [10h48m](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582315) | 2026-06-24 18:19 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `fix-24624-raise-special-ops-memref-crash` | pull_request |
| [10h13m](https://github.com/iree-org/iree/actions/runs/28107886109/job/83228908779) | 2026-06-24 18:19 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 6 | 6 | [13h55m](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261695) | 2026-06-24 18:19 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28107886210/job/83236524279) | [2s](https://github.com/iree-org/iree/actions/runs/28107886210/job/83236524279) | [2s](https://github.com/iree-org/iree/actions/runs/28107886210/job/83236524279) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28107886109/job/83236316185) | [2s](https://github.com/iree-org/iree/actions/runs/28107886109/job/83236316185) | [2s](https://github.com/iree-org/iree/actions/runs/28107886109/job/83236316185) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 87 | 7% (6/87) |  | 9h41m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 76 | 0% (0/76) |  | 9h49m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 111 | 0% (0/111) |  | 9h53m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 86 | 0% (0/86) |  | 9h56m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 24 | 0% (0/24) |  | 10h03m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 13h55m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
