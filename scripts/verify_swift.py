"""Check that every Swift reference solution passes its tests.

Copies the Swift package to a temporary folder, swaps each exercise file for its
reference solution there, and runs `swift test`. Your own files are never touched.

Run from the repo root:  python scripts/verify_swift.py
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

swift = shutil.which("swift")
if swift is None:
    print("Swift is not installed here, so the Swift check was skipped.")
    sys.exit(0)

with tempfile.TemporaryDirectory() as tmp:
    work = Path(tmp) / "swift"
    work.mkdir()
    shutil.copy(ROOT / "swift" / "Package.swift", work)
    shutil.copytree(ROOT / "swift" / "Sources", work / "Sources")
    shutil.copytree(ROOT / "swift" / "Tests", work / "Tests")
    for target_dir in sorted((ROOT / "swift" / "Solutions").iterdir()):
        if target_dir.is_dir():
            for solution in sorted(target_dir.glob("*.swift")):
                shutil.copy(solution, work / "Sources" / target_dir.name / solution.name)

    result = subprocess.run([swift, "test"], cwd=work, capture_output=True, text=True, encoding="utf-8", errors="replace")
    lines = (result.stdout + result.stderr).splitlines()
    for line in lines:
        if "error:" in line or "✘" in line or "Test run with" in line or "Executed" in line:
            print(line)
    print("Swift solutions: all tests passed" if result.returncode == 0 else f"Swift solutions: FAILED (exit {result.returncode})")
    sys.exit(result.returncode)
