#!/usr/bin/env node
"use strict";

// Launcher for the Outdoor Norway marketing plugins.
// Run it with: npx github:Sameersexy/outdoornorway <command>
// Node built-ins only. It writes no files itself. "install" and "update" print the
// Claude Code commands and run them only when you pass --run. "skills pack" calls
// tools/pack_skills.py, which writes zip files only into its --out folder.

const fs = require("fs");
const path = require("path");
const { spawn, spawnSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const MARKETPLACE = "Sameersexy/outdoornorway";
const DEFAULT_MARKETPLACE_NAME = "outdoornorway";
const DEFAULT_PLUGIN = "outdoornorway-marketing";
// The umbrella already carries these seventeen skills. Installed next to it, each shows up twice.
const OVERLAP_PLUGIN = "outdoornorway-copy-skills";
const SOURCE_ENV = "OUTDOORNORWAY_MARKETPLACE";
const UMBRELLA_SKILLS = ".claude/skills";
const SKILL_SOURCES = [UMBRELLA_SKILLS, "account-skills"];
// Skills that tools/pack_skills.py leaves out: they need the validator and tours.json.
const PLUGIN_ONLY = ["scriptcraft"];
// Marketplace entry fields that list plugin components.
const COMPONENT_KEYS = ["skills", "commands", "agents", "hooks", "mcpServers", "lspServers", "outputStyles"];
// What the Claude Code CLI says, or older versions exit non-zero with, when a step is already done.
const ALREADY_DONE = /already (added|exists|installed|on disk)/i;

const TEST_STEPS = [
  ["python3", ["-I", ".claude/skills/scriptcraft/scripts/test_script_check.py"]],
  ["python3", ["-I", "tools/test_repo_integrity.py"]],
];
const ADQUILL_TEST = ["python3", ["-I", "adquill/skills/adquill/scripts/test_slop_lint.py"]];

const HELP = `Outdoor Norway marketing tools

Usage: outdoornorway <command> [options]

Commands
  list                 List the plugins in the marketplace with their install lines.
  install [NAME|all]   Show how to install a plugin. NAME is one of the names from
                       "list", default ${DEFAULT_PLUGIN}. "all" means every plugin
                       except ${OVERLAP_PLUGIN}, which the default already covers.
                       Add --run to run the steps.
  update [NAME|all]    Show how to update a plugin, same names as install.
                       Add --run to run the steps.
  skills list          List every skill, the plugin that ships it and its folder.
  skills pack [--out DIR] [--list] [NAME...]
                       Zip skills for upload to claude.ai, one zip per skill.
                       Default folder dist/skills. Needs python3.
  doctor               Check Node, Python 3, the Claude Code CLI, the repo files and
                       every marketplace entry.
  test                 Run the validator tests and the repo integrity tests.
                       Add --all to include the adquill tests.
  version              Print the package version.
  help                 Show this text.

Environment
  ${SOURCE_ENV}   Marketplace source for install. Default ${MARKETPLACE}.
                       Set it to a fork or a local folder. The Claude Code marketplace
                       called outdoornorway then points there. update ignores it.

From GitHub, without cloning:
  npx github:${MARKETPLACE} list
  npx github:${MARKETPLACE} install
  npx github:${MARKETPLACE} install all --run
`;

function readJson(relative) {
  return JSON.parse(fs.readFileSync(path.join(ROOT, relative), "utf8"));
}

function isInside(target) {
  const relative = path.relative(ROOT, target);
  return relative === "" || (relative !== ".." && !relative.startsWith(".." + path.sep) && !path.isAbsolute(relative));
}

function toPosix(relative) {
  return relative.split(path.sep).join("/") || ".";
}

// The marketplace file, checked just enough that the commands can rely on it.
function loadMarketplace() {
  const data = readJson(".claude-plugin/marketplace.json");
  if (!data || !Array.isArray(data.plugins) || data.plugins.length === 0) {
    throw new Error("it lists no plugins");
  }
  const bad = data.plugins.findIndex((entry) => !entry || typeof entry.name !== "string" || entry.name === "");
  if (bad !== -1) {
    throw new Error("plugin entry " + (bad + 1) + " has no name");
  }
  const name = typeof data.name === "string" && data.name ? data.name : DEFAULT_MARKETPLACE_NAME;
  return { name, plugins: data.plugins };
}

// Returns the marketplace, or null after printing why it could not be read.
function marketplaceOrReport() {
  try {
    return loadMarketplace();
  } catch (error) {
    console.error("Could not read .claude-plugin/marketplace.json: " + error.message);
    return null;
  }
}

function marketplaceSource() {
  const value = (process.env[SOURCE_ENV] || "").trim();
  if (!value) {
    return { source: MARKETPLACE, custom: false };
  }
  // A path typed relative to where the person is standing, not to the repo.
  const source = /^\.{1,2}([\\/]|$)/.test(value) ? path.resolve(value) : value;
  return { source, custom: true };
}

// Name of the frontmatter field "name" in a SKILL.md, or null.
function skillName(skillFile) {
  const text = fs.readFileSync(skillFile, "utf8").replace(/\r\n?/g, "\n");
  if (!text.startsWith("---\n")) {
    return null;
  }
  const end = text.indexOf("\n---", 4);
  const block = end === -1 ? "" : text.slice(4, end);
  const match = /^name:[ \t]*(.*)$/m.exec(block);
  return match ? match[1].trim().replace(/^(["'])(.*)\1$/, "$2") : null;
}

function have(command) {
  const result = spawnSync(command, ["--version"], { encoding: "utf8" });
  return !result.error && result.status === 0;
}

function show(step) {
  return step[0] + " " + step[1].join(" ");
}

// A step may carry a third item, { tolerateAlready: true }. Its output is then read, so a
// non-zero exit that only says "already added" or "already installed" counts as success.
function runSteps(steps, cwd) {
  for (const step of steps) {
    console.log("> " + show(step));
    const tolerate = Boolean(step[2] && step[2].tolerateAlready);
    const result = spawnSync(step[0], step[1], tolerate ? { cwd, encoding: "utf8" } : { cwd, stdio: "inherit" });
    if (result.error) {
      console.error("Could not run " + step[0] + ": " + result.error.message);
      return 1;
    }
    let status = result.status === null ? 1 : result.status;
    if (tolerate) {
      const stdout = result.stdout || "";
      const stderr = result.stderr || "";
      if (stdout) {
        process.stdout.write(stdout.endsWith("\n") ? stdout : stdout + "\n");
      }
      if (stderr) {
        process.stderr.write(stderr.endsWith("\n") ? stderr : stderr + "\n");
      }
      if (status !== 0 && ALREADY_DONE.test(stdout + stderr)) {
        console.log("Already in place, continuing.");
        status = 0;
      }
    }
    if (status !== 0) {
      return status;
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

  let pkgVersion = null;
  try {
    pkgVersion = readJson("package.json").version;
    const plugin = readJson(".claude-plugin/plugin.json").version;
    if (pkgVersion === plugin) {
      line("ok", "plugin.json version matches package.json (" + pkgVersion + ")");
    } else {
      failed = true;
      line("fail", "versions differ: package " + pkgVersion + ", plugin.json " + plugin);
    }
  } catch (error) {
    failed = true;
    line("fail", "could not read package.json or plugin.json: " + error.message);
  }

  let market = null;
  try {
    market = loadMarketplace();
  } catch (error) {
    failed = true;
    line("fail", "could not read .claude-plugin/marketplace.json: " + error.message);
  }
  if (market) {
    const seen = new Set();
    for (const entry of market.plugins) {
      if (seen.has(entry.name)) {
        failed = true;
        line("fail", "marketplace entry name used twice: " + entry.name);
      }
      seen.add(entry.name);
      if (checkEntry(entry, pkgVersion, line)) {
        failed = true;
      }
    }
  }

  console.log(failed ? "\nSome checks failed." : "\nAll required checks passed.");
  return failed ? 1 : 0;
}

// Checks one marketplace entry. Prints a line per check and returns true when one failed.
function checkEntry(entry, pkgVersion, line) {
  let failed = false;
  const label = entry.name;
  const fail = (text) => {
    failed = true;
    line("fail", label + ": " + text);
  };

  let sourceDir = null;
  if (typeof entry.source !== "string" || entry.source === "") {
    fail("source must be a folder path inside this repo");
  } else {
    const resolved = path.resolve(ROOT, entry.source);
    if (!isInside(resolved)) {
      fail("source " + entry.source + " is outside the repo");
    } else if (!fs.existsSync(resolved) || !fs.statSync(resolved).isDirectory()) {
      fail("source folder " + entry.source + " does not exist");
    } else if (!isInside(fs.realpathSync(resolved))) {
      fail("source " + entry.source + " resolves outside the repo");
    } else {
      sourceDir = resolved;
      line("ok", label + ": source " + entry.source + " exists inside the repo");
    }
  }

  if (Array.isArray(entry.skills)) {
    let good = 0;
    for (const item of entry.skills) {
      const shown = String(item);
      if (typeof item !== "string" || sourceDir === null) {
        fail("skill path " + shown + " cannot be checked");
        continue;
      }
      const folder = path.resolve(sourceDir, item);
      const skillFile = path.join(folder, "SKILL.md");
      if (!isInside(folder)) {
        fail("skill path " + shown + " is outside the repo");
        continue;
      }
      if (!fs.existsSync(skillFile)) {
        fail("skill path " + shown + " has no SKILL.md");
        continue;
      }
      let name = null;
      try {
        name = skillName(skillFile);
      } catch (error) {
        name = null;
      }
      if (name !== path.basename(folder)) {
        fail("skill path " + shown + " has name " + (name === null ? "(none)" : name) + " in SKILL.md, not " + path.basename(folder));
        continue;
      }
      good += 1;
    }
    if (good === entry.skills.length) {
      line("ok", label + ": " + good + " skill" + (good === 1 ? "" : "s") + ", each with a SKILL.md whose name matches its folder");
    }
  }

  if (entry.version === pkgVersion && pkgVersion !== null) {
    line("ok", label + ": version " + entry.version + " matches package.json");
  } else {
    fail("version " + entry.version + " does not match package.json (" + pkgVersion + ")");
  }

  const listed = COMPONENT_KEYS.filter((key) => Object.prototype.hasOwnProperty.call(entry, key));
  const atRoot = typeof entry.source === "string" && path.resolve(ROOT, entry.source) === ROOT;
  if (atRoot && entry.strict === false && listed.length > 0) {
    fail("source ./ with strict false and " + listed.join(", ") + " conflicts with .claude-plugin/plugin.json (Claude Code fails to load it)");
  }
  return failed;
}

// Builds the steps for install and update. Returns null after printing why it cannot.
function planSteps(kind, args) {
  const flags = args.filter((arg) => arg.startsWith("-"));
  const names = args.filter((arg) => !arg.startsWith("-"));
  const unknown = flags.filter((flag) => flag !== "--run");
  if (unknown.length > 0 || names.length > 1) {
    console.error(unknown.length > 0 ? "Unknown option: " + unknown[0] : "Give one plugin name or all, not " + names.length + ".");
    console.error("Usage: outdoornorway " + kind + " [NAME|all] [--run]");
    return null;
  }
  const market = marketplaceOrReport();
  if (!market) {
    return null;
  }
  const requested = names[0] || DEFAULT_PLUGIN;
  let chosen = requested === "all" ? market.plugins : market.plugins.filter((entry) => entry.name === requested);
  if (chosen.length === 0) {
    console.error("Unknown plugin: " + requested);
    console.error("Valid names: " + market.plugins.map((entry) => entry.name).join(", ") + ", all");
    return null;
  }
  // Both plugins at once would list the same seventeen skills twice.
  const overlap = requested === "all" && kind === "install" && chosen.some((entry) => entry.name === DEFAULT_PLUGIN);
  const skipped = overlap ? chosen.filter((entry) => entry.name === OVERLAP_PLUGIN) : [];
  chosen = chosen.filter((entry) => !skipped.includes(entry));
  const where = marketplaceSource();
  const steps = [];
  if (kind === "install") {
    steps.push(["claude", ["plugin", "marketplace", "add", where.source], { tolerateAlready: true }]);
    for (const entry of chosen) {
      steps.push(["claude", ["plugin", "install", entry.name + "@" + market.name], { tolerateAlready: true }]);
    }
  } else {
    steps.push(["claude", ["plugin", "marketplace", "update", market.name]]);
    for (const entry of chosen) {
      steps.push(["claude", ["plugin", "update", entry.name + "@" + market.name]]);
    }
  }
  return { steps, chosen, skipped, where, marketName: market.name, all: requested === "all", run: flags.includes("--run") };
}

function install(kind, args) {
  const plan = planSteps(kind, args);
  if (!plan) {
    return 1;
  }
  const verb = kind === "install" ? "Install" : "Update";
  const what = plan.all ? "all " + plan.chosen.length + " plugins" : plan.chosen[0].name;
  console.log(verb + " " + what + " with these Claude Code commands:\n");
  for (const step of plan.steps) {
    console.log("  " + show(step));
  }
  console.log("\nThen restart Claude Code.");
  if (kind === "install" && plan.where.custom) {
    console.log("\nMarketplace source: " + plan.where.source + " (from " + SOURCE_ENV + ").");
    console.log("This changes where the Claude Code marketplace called " + plan.marketName + " points.");
  }
  if (plan.skipped.length > 0) {
    console.log("\nLeft out: " + OVERLAP_PLUGIN + ". " + DEFAULT_PLUGIN + " already has the same seventeen skills, and with both installed each skill is listed twice.");
    console.log("To add it alone: outdoornorway install " + OVERLAP_PLUGIN);
  }
  if (!plan.run) {
    console.log("\nThese steps were not run. Add --run to run them now.");
    return 0;
  }
  console.log("");
  if (!have("claude")) {
    console.error("The Claude Code CLI was not found. Install it first: https://code.claude.com/docs/en/quickstart");
    return 1;
  }
  return runSteps(plan.steps, ROOT);
}

function list() {
  const market = marketplaceOrReport();
  if (!market) {
    return 1;
  }
  console.log("Plugins in the " + market.name + " marketplace:\n");
  for (const entry of market.plugins) {
    console.log(entry.name + "  " + (entry.version || "(no version)"));
    if (entry.description) {
      console.log("  " + entry.description);
    }
    console.log("  claude plugin install " + entry.name + "@" + market.name + "\n");
  }
  console.log("Install one with: outdoornorway install NAME [--run]. \"install all\" covers every plugin except " + OVERLAP_PLUGIN + ", which " + DEFAULT_PLUGIN + " already includes.");
  return 0;
}

// Skill folders with a SKILL.md, as posix paths relative to the repo.
function skillFolders() {
  const found = [];
  for (const base of SKILL_SOURCES) {
    let names = [];
    try {
      names = fs.readdirSync(path.join(ROOT, base)).sort();
    } catch (error) {
      names = [];
    }
    for (const name of names) {
      if (fs.existsSync(path.join(ROOT, base, name, "SKILL.md"))) {
        found.push(base + "/" + name);
      }
    }
  }
  return found;
}

function skillsList() {
  const market = marketplaceOrReport();
  if (!market) {
    return 1;
  }
  // folder -> plugin names that ship it
  const shippedBy = new Map();
  const add = (folder, plugin) => {
    if (!shippedBy.has(folder)) {
      shippedBy.set(folder, []);
    }
    if (plugin && !shippedBy.get(folder).includes(plugin)) {
      shippedBy.get(folder).push(plugin);
    }
  };
  for (const folder of skillFolders()) {
    add(folder, null);
  }
  for (const entry of market.plugins) {
    if (typeof entry.source !== "string") {
      continue;
    }
    const sourceDir = path.resolve(ROOT, entry.source);
    if (Array.isArray(entry.skills)) {
      for (const item of entry.skills) {
        if (typeof item === "string") {
          add(toPosix(path.relative(ROOT, path.resolve(sourceDir, item))), entry.name);
        }
      }
    } else if (sourceDir === ROOT) {
      for (const folder of skillFolders()) {
        if (folder.startsWith(UMBRELLA_SKILLS + "/")) {
          add(folder, entry.name);
        }
      }
    }
  }
  const folders = skillFolders();
  const rows = Array.from(shippedBy.entries()).map(([folder, plugins]) => {
    const name = folder.split("/").pop();
    const packable = folders.includes(folder) && !PLUGIN_ONLY.includes(name);
    return { name, folder, plugins: plugins.length ? plugins.join(", ") : "(no plugin)", zip: packable ? "zip" : "plugin only" };
  });
  rows.sort((a, b) => (a.name === b.name ? a.folder.localeCompare(b.folder) : a.name.localeCompare(b.name)));
  const header = { name: "skill", plugins: "plugins", folder: "folder", zip: "zip" };
  const widths = { name: 0, plugins: 0, folder: 0 };
  for (const row of rows.concat([header])) {
    for (const key of Object.keys(widths)) {
      widths[key] = Math.max(widths[key], row[key].length);
    }
  }
  const format = (row) => "  " + [row.name.padEnd(widths.name), row.plugins.padEnd(widths.plugins), row.folder.padEnd(widths.folder), row.zip].join("  ");
  console.log("Skills in this repo:\n");
  console.log(format(header));
  for (const row of rows) {
    console.log(format(row));
  }
  const packable = rows.filter((row) => row.zip === "zip").length;
  console.log("\n\"skills pack\" can package " + packable + " of " + rows.length + " skills as zip files. Plugin only: " + PLUGIN_ONLY.join(", ") + " (it needs the validator and tours.json).");
  return 0;
}

function skillsPack(args) {
  if (!have("python3")) {
    console.error("python3 not found. Install Python 3 from https://www.python.org/downloads/");
    return 1;
  }
  // No folder change: a relative --out and the default dist/skills resolve against where you run this.
  const result = spawnSync("python3", ["-I", path.join(ROOT, "tools", "pack_skills.py")].concat(args), { stdio: "inherit" });
  if (result.error) {
    console.error("Could not run python3: " + result.error.message);
    return 1;
  }
  return result.status === null ? 1 : result.status;
}

function skills(args) {
  switch (args[0]) {
    case "list":
      return skillsList();
    case "pack":
      return skillsPack(args.slice(1));
    default:
      console.error(args[0] ? "Unknown skills command: " + args[0] : "Missing skills command.");
      console.error("Usage: outdoornorway skills list\n       outdoornorway skills pack [--out DIR] [--list] [NAME...]");
      return 1;
  }
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
    case "list":
      return list();
    case "install":
      return install("install", args);
    case "update":
      return install("update", args);
    case "skills":
      return skills(args);
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
