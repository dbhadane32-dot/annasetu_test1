import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
    "port": int(os.getenv("MYSQL_PORT", "3306")),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
    "database": os.getenv("MYSQL_DATABASE", "annasetu"),
    "autocommit": False,
    "connection_timeout": 10,
}


if os.getenv("MYSQL_SSL_DISABLED", "0") == "1":
    DB_CONFIG["ssl_disabled"] = True
if os.getenv("MYSQL_SSL_CA"):
    DB_CONFIG["ssl_ca"] = os.getenv("MYSQL_SSL_CA")


def connect():
    return mysql.connector.connect(**DB_CONFIG)


def row_dict(cursor, row):
    return dict(zip(cursor.column_names, row)) if row else None
