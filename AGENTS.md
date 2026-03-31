# AGENTS

This file defines how AI agents should work in this repository.

## Mission

Help the user create Blender animations quickly and safely using MCP-connected tools.

## Session startup checklist

1. Read `docs/ANIMATION_BRIEF.md`.
2. Read `docs/SHOT_LIST.md`.
3. Confirm Blender MCP connectivity before heavy actions:
   - Run `python3 scripts/mcp_healthcheck.py`.
   - If not reachable, ask user to open Blender and connect MCP on port `9876`.

## Workflow expectations

- Work one shot at a time (`S01`, `S02`, `S03`, etc).
- Propose small reversible steps, then execute.
- After each meaningful step, report exactly what changed.
- Update shot status in `docs/SHOT_LIST.md` when requested.

## Blender safety rules

- Avoid destructive actions unless user confirms.
- Prefer non-destructive editing and clear object/collection naming.
- Keep camera and animation adjustments incremental for easy rollback.

## Project conventions

- Canonical scene files live in `scenes/`.
- Track `*.blend` with Git LFS.
- Do not commit Blender rolling backups (`*.blend1`, `*.blend2`, etc).
- Keep docs and prompts in sync with scene changes.

## MCP config locations

- Codex: `.codex/config.toml`
- Claude: `.mcp.json` and `.claude/settings.json`
- OpenClaw: `openclaw.json`
