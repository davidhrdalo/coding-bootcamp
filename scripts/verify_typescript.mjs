// Check that every TypeScript reference solution passes its tests.
//
// This copies the repo to a temporary folder, swaps each exercise file for its reference
// solution there, and runs the tests. Your own exercise files are never touched.
//
// Run from the repo root:  node scripts/verify_typescript.mjs
import { cpSync, copyFileSync, mkdtempSync, readdirSync, rmSync, statSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname, basename } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const work = mkdtempSync(join(tmpdir(), "bootcamp-ts-"));
const skip = new Set([".git", ".venv", "node_modules", "__pycache__", ".pytest_cache"]);

try {
  cpSync(root, work, { recursive: true, filter: (src) => !skip.has(basename(src)) });

  const exercisesDir = join(work, "typescript", "exercises");
  const solutionsDir = join(work, "typescript", "solutions");
  const exerciseFiles = new Map();
  for (const week of readdirSync(exercisesDir)) {
    const weekDir = join(exercisesDir, week);
    if (!statSync(weekDir).isDirectory()) continue;
    for (const file of readdirSync(weekDir)) exerciseFiles.set(file, join(weekDir, file));
  }

  for (const file of readdirSync(solutionsDir).sort()) {
    const target = exerciseFiles.get(file);
    if (!target) {
      console.error(`No exercise file found for solution ${file}`);
      process.exit(1);
    }
    copyFileSync(join(solutionsDir, file), target);
  }

  const result = spawnSync(
    process.execPath,
    [
      "--disable-warning=ExperimentalWarning",
      "--test",
      "--test-reporter=dot",
      "typescript/exercises/**/*.test.ts",
    ],
    { cwd: work, stdio: "inherit" },
  );
  process.exitCode = result.status ?? 1;
} finally {
  rmSync(work, { recursive: true, force: true });
}
