#!/usr/bin/env node
"use strict";

// Launcher for the Outdoor Norway marketing plugin.
// Run it with: npx github:Sameersexy/outdoornorway <command>
// Node built-ins only. It never writes files; "install" and "update" print the
// Claude Code commands, and run them only when you pass --run.

const fs = require("fs");
const path = require("path");
const { spawn, spawnSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const MARKETPLACE = "Sameersexy/outdoornorway";
const PLUGIN = "outdoornorway-marketing@outdoornorway";

const PLUGIN_STEPS = [
  ["claude", ["plugin", "marketplace", "add", MARKETPLACE]],
  ["claude", ["plugin", "install", PLUGIN]],
];
const UPDATE_STEPS = [
  ["claude", ["plugin", "marketplace", "update", "outdoornorway"]],
  ["claude", ["plugin", "update", PLUGIN]],
];
const TEST_STEPS = [
  ["python3", ["-I", ".claude/skills/scriptcraft/scripts/test_script_check.py"]],
  ["python3", ["-I", "tools/test_repo_integrity.py"]],
];
const ADQUILL_TEST = ["python3", ["-I", "adquill/skills/adquill/scripts/test_slop_lint.py"]];

const HELP = `Outdoor Norway marketing tools

Usage: outdoornorway <command> [options]

Commands
  doctor           Check Node, Python 3, the Claude Code CLI and the repo files.
  install          Show how to install the plugin. Add --run to run the steps.
  update           Show how to update the plugin. Add --run to run the steps.
  test             Run the validator tests and the repo integrity tests.
                   Add --all to include the adquill tests.
  version          Print the package version.
  help             Show this text.

From GitHub, without cloning:
  npx github:${MARKETPLACE} doctor
  npx github:${MARKETPLACE} install
`;

function readJson(relative) {
  return JSON.parse(fs.readFileSync(path.join(ROOT, relative), "utf8"));
}

function have(command) {
  const result = spawnSync(command, ["--version"], { encoding: "utf8" });
  return !result.error && result.status === 0;
}

function show(step) {
  return step[0] + " " + step[1].join(" ");
}

function runSteps(steps, cwd) {
  for (const step of steps) {
    console.log("> " + show(step));
    const result = spawnSync(step[0], step[1], { cwd, stdio: "inherit" });
    if (result.error) {
      console.error("Could not run " + step[0] + ": " + result.error.message);
      return 1;
    }
    if (result.status !== 0) {
      return result.status === null ? 1 : result.status;
    }
  }
  return 0;
}

// The test suites do not depend on each other, so they all start at once.
// Output still appears in step order: the first suite streams as it runs and each
// later suite is held back until the ones before it have ended. The first failure
// in that order sets the exit status, and nothing from later suites is shown.
function runTogether(steps, cwd) {
  return new Promise((resolve) => {
    // Child output goes through pipes here, so ask for the colour a terminal would get.
    const env = process.stderr.isTTY ? Object.assign({ FORCE_COLOR: "1" }, process.env) : process.env;
    const runs = steps.map((step) => ({ step, held: [], opened: false, ended: false, status: 0, child: null }));
    let current = 0;
    let settled = false;

    function settle(status) {
      settled = true;
      for (const run of runs) {
        if (!run.ended && run.child) {
          run.child.kill();
        }
      }
      resolve(status);
    }

    function advance() {
      while (!settled && current < runs.length) {
        const run = runs[current];
        if (!run.opened) {
          console.log("> " + show(run.step));
          run.opened = true;
        }
        for (const piece of run.held.splice(0)) {
          piece.stream.write(piece.data);
        }
        if (!run.ended) {
          return;
        }
        if (run.status !== 0) {
          settle(run.status);
          return;
        }
        current += 1;
      }
      if (!settled) {
        settle(0);
      }
    }

    function listen(run, stream) {
      return (data) => {
        if (runs[current] === run) {
          stream.write(data);
        } else {
          run.held.push({ stream, data });
        }
      };
    }

    for (const run of runs) {
      const child = spawn(run.step[0], run.step[1], { cwd, env, stdio: ["ignore", "pipe", "pipe"] });
      run.child = child;
      child.stdout.on("data", listen(run, process.stdout));
      child.stderr.on("data", listen(run, process.stderr));
      child.on("error", (error) => {
        if (run.ended) {
          return;
        }
        run.held.push({ stream: process.stderr, data: "Could not run " + run.step[0] + ": " + error.message + "\n" });
        run.ended = true;
        run.status = 1;
        advance();
      });
      child.on("close", (code) => {
        if (run.ended) {
          return;
        }
        run.ended = true;
        run.status = code === null ? 1 : code;
        advance();
      });
    }
    advance();
  });
}

function doctor() {
  let failed = false;
  const line = (state, text) => console.log("[" + state + "] " + text);

  const major = Number(process.versions.node.split(".")[0]);
  line(major >= 18 ? "ok" : "warn", "Node " + process.versions.node + " (the launcher needs 18 or newer)");

  if (have("python3")) {
    line("ok", "python3 found (the validator and tests run on it)");
  } else {
    failed = true;
    line("fail", "python3 not found. Install Python 3 from https://www.python.org/downloads/");
  }

  if (have("claude")) {
    line("ok", "Claude Code CLI found");
  } else {
    line("warn", "Claude Code CLI not found. Install it from https://code.claude.com/docs/en/quickstart");
  }

  const required = [
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    ".claude/commands",
    ".claude/agents",
    ".claude/skills/scriptcraft/SKILL.md",
    "campaigns/ski-meta-ads/tours.json",
  ];
  for (const item of required) {
    if (fs.existsSync(path.join(ROOT, item))) {
      line("ok", item);
    } else {
      failed = true;
      line("fail", "missing " + item);
    }
  }

  try {
    const pkg = readJson("package.json").version;
    const plugin = readJson(".claude-plugin/plugin.json").version;
    const market = readJson(".claude-plugin/marketplace.json").plugins[0].version;
    if (pkg === plugin && plugin === market) {
      line("ok", "versions match (" + pkg + ")");
    } else {
      failed = true;
      line("fail", "versions differ: package " + pkg + ", plugin " + plugin + ", marketplace " + market);
    }
  } catch (error) {
    failed = true;
    line("fail", "could not read the version files: " + error.message);
  }

  console.log(failed ? "\nSome checks failed." : "\nAll required checks passed.");
  return failed ? 1 : 0;
}

function install(args, steps, title) {
  console.log(title + "\n");
  for (const step of steps) {
    console.log("  " + show(step));
  }
  console.log("\nThen restart Claude Code.");
  if (!args.includes("--run")) {
    console.log("\nThese steps were not run. Add --run to run them now.");
    return 0;
  }
  console.log("");
  if (!have("claude")) {
    console.error("The Claude Code CLI was not found. Install it first: https://code.claude.com/docs/en/quickstart");
    return 1;
  }
  return runSteps(steps, ROOT);
}

function test(args) {
  const steps = TEST_STEPS.slice();
  if (args.includes("--all")) {
    steps.push(ADQUILL_TEST);
  }
  if (!have("python3")) {
    console.error("python3 not found. Install Python 3 from https://www.python.org/downloads/");
    return 1;
  }
  return runTogether(steps, ROOT);
}

function main(argv) {
  const command = argv[0] || "help";
  const args = argv.slice(1);
  switch (command) {
    case "doctor":
      return doctor();
    case "install":
      return install(args, PLUGIN_STEPS, "Install the plugin with these Claude Code commands:");
    case "update":
      return install(args, UPDATE_STEPS, "Update the plugin with these Claude Code commands:");
    case "test":
      return test(args);
    case "version":
    case "--version":
    case "-v":
      console.log(readJson("package.json").version);
      return 0;
    case "help":
    case "--help":
    case "-h":
      console.log(HELP);
      return 0;
    default:
      console.error("Unknown command: " + command + "\n");
      console.error(HELP);
      return 1;
  }
}

Promise.resolve(main(process.argv.slice(2))).then((code) => {
  process.exitCode = code;
});
