"""Create the Annasetu tables in the database named by your environment variables.
Works on hosted MySQL (where you cannot CREATE DATABASE) as well as locally.
Usage: python init_db.py && python seed.py
"""
import os
import re
from db import connect

SCHEMA = os.path.join(os.path.dirname(__file__), "..", "database", "schema.sql")


def main():
    sql = open(SCHEMA, encoding="utf-8").read()
    sql = re.sub(r"(?im)^\s*(CREATE DATABASE|USE)\b.*?;\s*$", "", sql)
    cn = connect(); cur = cn.cursor()
    for stmt in [s.strip() for s in sql.split(";") if s.strip()]:
        cur.execute(stmt)
    cn.commit(); cur.close(); cn.close()
    print("Tables ready.")


if __name__ == "__main__":
    main()
