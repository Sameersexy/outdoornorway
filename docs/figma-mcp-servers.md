# Figma MCP servers

This repo's `.mcp.json` lists three community Figma MCP servers next to `scrapling`. The owner chose to add them, although two of them only do useful work on a Mac with Figma open. This page says what each one does, when to use it, and how to set it up.

## Use the official Figma connector first

The official Figma MCP server (the Figma connector) is the default for all Figma work in this repo. It is the only one that works in cloud sessions, and the Figma skills use it. Reach for a community server only when you are on your own Mac and need something the official one does not give you.

| Server in `.mcp.json` | What it does | Use it when | Needs on a Mac |
|---|---|---|---|
| `TalkToFigma` ([grab/cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp)) | Reads and edits the file you have open in Figma through a plugin: selection, nodes, text, annotations, instance overrides, exports. 40 tools. | You want quick live edits in an open file, such as bulk text replacement or annotations. | Bun, Figma open with its plugin running, and its WebSocket server running in a terminal. No token. |
| `figma-console` ([southleft/figma-console-mcp](https://github.com/southleft/figma-console-mcp)) | Talks to the Figma desktop app through its Desktop Bridge plugin: console logs, screenshots, variables and tokens, components, design system audits, and running Figma plugin code. 121 tools. | You debug a Figma plugin, or manage variables and design tokens in a file. | Node 18 or newer, the Figma desktop app, the Desktop Bridge plugin and a Figma personal access token in `FIGMA_ACCESS_TOKEN`. |
| `framelink-figma` ([GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP), npm package `figma-developer-mcp`) | Reads a Figma file, frame or group from a link and returns trimmed layout and styling data, and downloads images. Read only. 2 tools. | You turn a design into code and want smaller, simpler design data. | Node and a Figma personal access token in `FIGMA_API_KEY`. No desktop app, no plugin. |

All three are MIT licensed. The npm package `cursor-talk-to-figma-mcp` has no licence field, but its repo has an MIT `LICENSE` file.

Each server is pinned to an exact npm version in `.mcp.json` (0.3.5, 1.41.5 and 0.13.2). To update one, check the new version's README and changelog, then change the number.

## How the token gets in

No token is stored in this repo, and none may be: the repo is public. `.mcp.json` reads the token from your environment with Claude Code's variable expansion, for example `"FIGMA_ACCESS_TOKEN": "${FIGMA_ACCESS_TOKEN:-}"`. When the variable is not set it expands to an empty string, so Claude Code shows no warning and the server starts without a token.

`framelink-figma` also sets `FRAMELINK_TELEMETRY` to `off`, which turns off the usage reports the package sends by default.

## Set up on a Mac

1. Create a Figma personal access token. Figma's help page [Manage personal access tokens](https://help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens) shows how. The figma-console README asks for these scopes: File content (read), File versions (read), Variables (read) and Comments (read and write).
2. Put the token in your shell profile, for example `~/.zshrc`, never in a repo file:

   ```bash
   export FIGMA_ACCESS_TOKEN=your-token
   export FIGMA_API_KEY="$FIGMA_ACCESS_TOKEN"
   ```

   Open a new terminal so the variables are set, then start Claude Code from this repo. You can skip either line if you do not use that server.
3. Claude Code asks once before it starts each project server. Approve only the ones you want, and check them with `/mcp`.

### TalkToFigma

1. Install Bun, as the README says: `curl -fsSL https://bun.sh/install | bash`.
2. Start the WebSocket server. It is not in the npm package, so clone the repo somewhere outside this one, then run `bun install` and `bun socket` in that folder. Leave that terminal open. It listens on port 3055. You do not need the README's `bun setup` step: it installs the same dependencies and writes MCP config files for Cursor and Claude Code, and this repo's `.mcp.json` already has the server.
3. Install the Figma plugin from its [Figma community page](https://www.figma.com/community/plugin/1485687494525374295/cursor-talk-to-figma-mcp-plugin), open your file in Figma and run the plugin.
4. In Claude Code, ask it to join the channel the plugin shows (the `join_channel` tool). Then it can read and edit the file.

Nothing in this repo starts the WebSocket server for you.

### figma-console

1. Set `FIGMA_ACCESS_TOKEN` (step 2 above) and use the Figma desktop app, not the web app.
2. Start Claude Code once, so the server copies its plugin files to `~/.figma-console-mcp/plugin/`. `npx figma-console-mcp --print-path` prints the exact path.
3. In Figma, go to Plugins, Development, Import plugin from manifest, and pick `manifest.json` in that folder.
4. Run the Desktop Bridge plugin in your file. It finds the server on a port from 9223 to 9232 and connects by itself. No separate process is needed.

After an update, re-import the plugin only when the figma-console release notes say so.

### framelink-figma

1. Set `FIGMA_API_KEY` (step 2 above).
2. Paste a Figma link into Claude Code and ask for the design data. Nothing else to install.

Images it downloads go to the folder Claude Code started it in, which is the repo root, unless you name a folder. Do not commit them.

## In cloud sessions

The three servers fail harmlessly in a cloud session, because there is no Figma app, no plugin and no token there. Use the official Figma connector instead. This is what a test in a cloud container showed, with no token set:

- `TalkToFigma` starts, answers the MCP handshake and lists its 40 tools, then logs that it cannot reach `ws://localhost:3055` and retries every 2 seconds. Its tools cannot reach Figma.
- `figma-console` starts, answers the handshake and lists its 121 tools, opens its own bridge on port 9223 and waits for the plugin, which never connects. It writes its plugin files to `~/.figma-console-mcp/` in the container.
- `framelink-figma` stops at once with "Either FIGMA_API_KEY or FIGMA_OAUTH_TOKEN is required", so `/mcp` shows it as failed. With a placeholder key it starts and lists its 2 tools.

`TalkToFigma` also needs Bun, so it fails to start on any machine without it.
