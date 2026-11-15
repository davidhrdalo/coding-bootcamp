"""Create a database file to experiment with.

    python sql/playground.py            # small sample data
    python sql/playground.py large      # the larger generated data
    sqlite3 sql/playground.db           # then type SQL, for example:  SELECT * FROM customers;

Useful sqlite3 commands: .tables  .schema customers  .headers on  .mode column  .quit
Delete sql/playground.db and run this again to reset it.
"""
import sqlite3
import sys
from pathlib import Path

import sql_support as support

dataset = sys.argv[1] if len(sys.argv) > 1 else "small"
if dataset not in support.DATASETS:
    sys.exit("usage: python sql/playground.py [small|large]")

target = Path(__file__).parent / "playground.db"
if target.exists():
    target.unlink()

memory = support.connect(dataset)
disk = sqlite3.connect(target)
memory.backup(disk)
disk.close()
print(f"Created {target} with the {dataset} data.")
print("Open it with:  sqlite3 sql/playground.db    (then try: .headers on, .mode column, SELECT * FROM customers;)")
