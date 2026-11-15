"""Check that every reference solution passes its tests.

This copies the repo to a temporary folder, swaps each exercise file for its
reference solution there, and runs pytest. Your own exercise files are never touched.

Run from the repo root:  python scripts/verify_solutions.py
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

with tempfile.TemporaryDirectory() as tmp:
    work = Path(tmp) / "repo"
    shutil.copytree(
        ROOT,
        work,
        ignore=shutil.ignore_patterns(".git", ".venv", "__pycache__", ".pytest_cache", "node_modules", ".build"),
    )
    solution_dirs = (work / "python" / "solutions", work / "theory" / "solutions", work / "sql" / "solutions")
    for solutions in solution_dirs:
        for solution in sorted(p for p in solutions.iterdir() if p.suffix in (".py", ".sql")):
            targets = list(work.glob(f"**/exercises/**/{solution.name}"))
            if len(targets) != 1:
                sys.exit(f"Expected exactly one exercise file for {solution.name}, found {len(targets)}")
            shutil.copy(solution, targets[0])
    sys.exit(subprocess.call([sys.executable, "-m", "pytest", "-p", "no:cacheprovider"], cwd=work))
