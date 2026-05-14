---
name: iree-ci-monitor-beads
description: Use when working in the iree-ci-monitor repository and the task involves planning, tracking, triage, status handoff, or durable issue state with beads/br.
---

# iree-ci-monitor Beads

Use beads as the durable task layer for this repository. The dashboard data under
`data/` and the generated Markdown reports are product artifacts; beads are for
agent/human coordination about changes to the monitor itself.

## Start of Work

1. From the repo root, check that beads is available:
   ```bash
   br --version
   br where
   ```
2. If `.beads/beads.db` is missing in a fresh clone, hydrate it from the
   committed JSONL:
   ```bash
   br sync --import-only --db .beads/beads.db
   ```
3. Inspect current state before changing files:
   ```bash
   br ready
   br list --status open
   ```

## Working Rules

- Prefer one bead per coherent change or investigation.
- Create a bead before starting non-trivial work if no suitable bead exists.
- Keep the bead title outcome-oriented and specific to `iree-ci-monitor`.
- Use labels for lightweight grouping such as `collector`, `reporter`, `workflow`,
  `data`, `docs`, or `infra`.
- Record discoveries in bead comments when they affect later decisions.
- Do not store large JSONL excerpts, generated report dumps, tokens, or raw logs
  in bead text. Link files or summarize the relevant evidence instead.
- Keep bot refresh commits separate from human/agent task commits.

## Useful Commands

```bash
br create "Fix stale queued alert rendering" --type bug --priority 1 --labels reporter
br comments add <id> "Root cause: report aggregation used stale latest snapshot."
br update <id> --status in_progress
br dep add <blocked-id> <blocker-id>
br close <id> --reason fixed
br sync --status
br sync --flush-only
```

## Before Handoff

1. Run the verification required by `CLAUDE.md` for the files you changed.
2. Add a bead comment with the commands run and the important result.
3. Flush beads state before committing:
   ```bash
   br sync --flush-only
   git status --short
   ```
4. Leave the bead open if human review or follow-up is still needed; close it
   only when the task is actually complete.
