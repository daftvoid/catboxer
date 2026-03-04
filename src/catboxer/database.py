import sqlite3
from pathlib import Path

dbpath = Path.home() / '.catboxer' / 'database.db'

def init():
    dbpath.parent.mkdir(parents=True, exist_ok=True)

    print(f"Path: {dbpath}")

    conn = sqlite3.connect(dbpath)

    print("Database connected")

    conn.close()

init()