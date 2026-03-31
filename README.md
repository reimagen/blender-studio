# blender-starter

Starter project for Blender animation workflows with MCP, designed to work with Claude, Codex, and OpenClaw.

## Goal

Use AI as an animation copilot: plan shots, build/adjust scenes in Blender, and iterate quickly.

## What this repo includes

- Project-scoped Codex MCP config in `.codex/config.toml`
- Project-scoped Claude MCP config in `.mcp.json`
- Project-scoped OpenClaw MCP config in `openclaw.json`
- Shared Claude permissions in `.claude/settings.json`
- Animation planning templates in `docs/`
- A prompt starter in `prompts/`
- A Blender MCP bridge smoke test in `scripts/mcp_healthcheck.py`

All MCP clients use the same local Blender bridge on `localhost:9876`.

## Prerequisites

- Blender installed
- Blender MCP bridge/add-on running and listening on `127.0.0.1:9876`
- Python 3 available as `python3`
- Git LFS installed (`git lfs install`)

## Quick start

1. Start Blender.
2. Enable/run your Blender MCP bridge so port `9876` is listening.
3. In this repo, run:
   - `python3 scripts/mcp_healthcheck.py`
4. Open this project in Claude, Codex, or OpenClaw and run a simple scene-info tool call.
5. Fill out `docs/ANIMATION_BRIEF.md` and `docs/SHOT_LIST.md`.
6. Use `prompts/START_SESSION.md` to kick off an AI-assisted build session.

## Client notes

- `Codex`: reads `.codex/config.toml` when the project is trusted.
- `Claude`: uses `.mcp.json` for project MCP server definitions.
- `OpenClaw`: reads `openclaw.json` and its `mcp.servers` block.

## Suggested repo workflow

- Keep canonical scene files as `*.blend` (tracked with Git LFS).
- Ignore local Blender rolling backups (`*.blend1`, `*.blend2`, ...).
- Commit often at milestone points: blocking, lighting pass, animation pass, render pass.

## Troubleshooting

- If MCP calls fail with connection errors, Blender is usually not listening on `9876`.
- If `python3` is missing, install Python or update command paths in config files.
- If one client works and another does not, reload/restart that client to refresh MCP config.
