import os
import psycopg2
from dotenv import load_dotenv
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description="Apply DB migrations.")
parser.add_argument("--env", choices=["dev", "prod"], required=True)
args = parser.parse_args()

load_dotenv(f".env.{args.env}")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

MIGRATIONS_DIR = Path("migrations")


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASS
    )


def ensure_migrations_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS schema_migrations (
                id SERIAL PRIMARY KEY,
                filename TEXT UNIQUE NOT NULL,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
    conn.commit()


def get_applied_migrations(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT filename FROM schema_migrations;")
        return {row[0] for row in cur.fetchall()}


def apply_migration(conn, filename, sql):
    with conn.cursor() as cur:
        cur.execute(sql)
        cur.execute(
            "INSERT INTO schema_migrations (filename) VALUES (%s);", (filename,)
        )
    conn.commit()


def run():
    conn = get_db_connection()
    ensure_migrations_table(conn)
    applied = get_applied_migrations(conn)

    for file in sorted(MIGRATIONS_DIR.glob("*.sql")):
        if file.name not in applied:
            print(f"Applying migration: {file.name}")
            sql = file.read_text()
            try:
                apply_migration(conn, file.name, sql)
                print(f"✔ Applied {file.name}")
            except Exception as e:
                print(f"✖ Failed on {file.name}: {e}")
                conn.rollback()
                break

    conn.close()


# TODO: Create an error log table to log issues with migrations


if __name__ == "__main__":
    run()
