"""Cross-platform task runner: the same commands on macOS, Windows and Linux.

Usage (from the repo root):
    python run.py <task>        macOS / Linux:  python3 run.py <task>     Windows:  py run.py <task>
    python run.py               lists every task

It uses only the Python standard library, so it works before anything is installed.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)

VENV_PY = ROOT / ".venv" / ("Scripts" if os.name == "nt" else "bin") / ("python.exe" if os.name == "nt" else "python")
PY = str(VENV_PY) if VENV_PY.exists() else sys.executable
NODE_TEST = ["node", "--disable-warning=ExperimentalWarning", "--test", "--test-reporter=spec"]


def swift_test(*extra):
    return ["swift", "test", "--quiet", "--package-path", "swift", *extra]


TASKS = {
    "setup": ("Python: create .venv and install pytest", "setup"),
    "setup-ts": ("TypeScript: install the compiler (only needed for typecheck)", [["npm", "install"]]),
    "test": ("run all Python exercises", [[PY, "-m", "pytest"]]),
    "week0": ("Python week 0", [[PY, "-m", "pytest", "python/exercises/week0_data_types"]]),
    "week1": ("Python week 1", [[PY, "-m", "pytest", "python/exercises/week1_basics"]]),
    "week2": ("Python week 2", [[PY, "-m", "pytest", "python/exercises/week2_collections"]]),
    "week3": ("Python week 3", [[PY, "-m", "pytest", "python/exercises/week3_stacks_and_search"]]),
    "week4": ("Python week 4", [[PY, "-m", "pytest", "python/exercises/week4_linked_lists_and_trees"]]),
    "theory": ("theory exercises", [[PY, "-m", "pytest", "theory/exercises"]]),
    "ts": ("all TypeScript exercises (Node 22.18+)", [NODE_TEST + ["typescript/exercises/**/*.test.ts"]]),
    "ts0": ("TypeScript week 0", [NODE_TEST + ["typescript/exercises/week0_js_basics/*.test.ts"]]),
    "ts1": ("TypeScript week 1", [NODE_TEST + ["typescript/exercises/week1_algorithms/*.test.ts"]]),
    "ts2": ("TypeScript week 2", [NODE_TEST + ["typescript/exercises/week2_async_and_types/*.test.ts"]]),
    "typecheck": ("TypeScript compiler check (run setup-ts first)", [["npx", "tsc", "-p", "typescript/tsconfig.json"]]),
    "swift": ("all Swift exercises (needs a Swift toolchain)", [swift_test()]),
    "swift0": ("Swift week 0", [swift_test("--filter", "Week0BasicsTests")]),
    "swift1": ("Swift week 1", [swift_test("--filter", "Week1AlgorithmsTests")]),
    "swift2": ("Swift week 2", [swift_test("--filter", "Week2ConcurrencyTests")]),
    "sql": ("all SQL exercises", [[PY, "-m", "pytest", "sql"]]),
    "sql1": ("SQL block 1", [[PY, "-m", "pytest", "sql", "-k", "block1_select"]]),
    "sql2": ("SQL block 2", [[PY, "-m", "pytest", "sql", "-k", "block2_joins"]]),
    "sql3": ("SQL block 3", [[PY, "-m", "pytest", "sql", "-k", "block3_subqueries"]]),
    "sql4": ("SQL block 4", [[PY, "-m", "pytest", "sql", "-k", "block4_changing"]]),
    "verify": ("check the reference solutions pass (does not touch your files)", [
        [PY, "scripts/verify_solutions.py"],
        ["node", "scripts/verify_typescript.mjs"],
        [PY, "scripts/verify_swift.py"],
    ]),
}


def run(cmd):
    exe = shutil.which(cmd[0]) if cmd[0] != PY else cmd[0]
    if exe is None:
        print(f"'{cmd[0]}' is not installed or not on your PATH. See the README for what each track needs.")
        return 127
    return subprocess.call([exe, *cmd[1:]])


def setup():
    code = subprocess.call([sys.executable, "-m", "venv", ".venv"])
    if code:
        return code
    code = subprocess.call([str(VENV_PY), "-m", "pip", "install", "-r", "requirements.txt"])
    if code == 0:
        activate = r".venv\Scripts\activate" if os.name == "nt" else "source .venv/bin/activate"
        print(f"\nDone. run.py finds the .venv by itself; to use it in your own shell run: {activate}")
    return code


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else ""
    if name not in TASKS:
        print("Usage: python run.py <task>\n")
        for key, (desc, _) in TASKS.items():
            print(f"  {key:<10} {desc}")
        return 0 if not name else 2
    steps = TASKS[name][1]
    if steps == "setup":
        return setup()
    status = 0
    for cmd in steps:
        status = run(cmd) or status
    return status


if __name__ == "__main__":
    sys.exit(main())
