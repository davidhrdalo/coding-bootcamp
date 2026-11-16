// Check that every web reference solution passes its tests (and type-checks).
//
// This copies the web/ folder to a temporary folder, swaps each exercise file for its
// reference solution there, then runs Vitest and the TypeScript compiler. Your own exercise
// files are never touched.
//
// Needs `npm install --prefix web` first (python run.py setup-web).
// Run from the repo root:  node scripts/verify_web.mjs
import { cpSync, copyFileSync, existsSync, mkdtempSync, readdirSync, rmSync, statSync, symlinkSync } from "node:fs";
import { tmpdir } from "node:os";
import { basename, dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const web = join(root, "web");

if (!existsSync(join(web, "node_modules"))) {
  console.log("Web dependencies are not installed, so the web check was skipped. Run: python run.py setup-web");
  process.exit(0);
}

const work = mkdtempSync(join(tmpdir(), "bootcamp-web-"));
let status = 1;

try {
  cpSync(web, join(work, "web"), { recursive: true, filter: (src) => basename(src) !== "node_modules" });
  const copy = join(work, "web");
  // "junction" links work on Windows without administrator rights; on macOS and Linux it is a normal symlink.
  symlinkSync(join(web, "node_modules"), join(copy, "node_modules"), "junction");

  const exerciseFiles = new Map();
  const exercisesDir = join(copy, "exercises");
  for (const group of readdirSync(exercisesDir)) {
    const groupDir = join(exercisesDir, group);
    if (!statSync(groupDir).isDirectory()) continue;
    for (const file of readdirSync(groupDir)) exerciseFiles.set(file, join(groupDir, file));
  }

  for (const file of readdirSync(join(copy, "solutions")).sort()) {
    const target = exerciseFiles.get(file);
    if (!target) {
      console.error(`No exercise file found for solution ${file}`);
      process.exit(1);
    }
    copyFileSync(join(copy, "solutions", file), target);
  }

  const tests = spawnSync(
    process.execPath,
    [join(copy, "node_modules", "vitest", "vitest.mjs"), "run", "--reporter=dot"],
    { cwd: copy, stdio: "inherit" },
  );
  if (tests.status !== 0) {
    status = tests.status ?? 1;
  } else {
    const types = spawnSync(
      process.execPath,
      [join(copy, "node_modules", "typescript", "bin", "tsc"), "--noEmit", "-p", "."],
      { cwd: copy, stdio: "inherit" },
    );
    status = types.status ?? 1;
    console.log(status === 0 ? "Web solutions: tests passed and types check" : "Web solutions: TYPE ERRORS");
  }
} finally {
  rmSync(work, { recursive: true, force: true });
}
process.exitCode = status;
