import os
import re
import psycopg
from psycopg import Connection
from dotenv import load_dotenv
from datetime import datetime


ENV_FILENAME = ".env"
ENV_PATH = os.path.abspath(ENV_FILENAME)


def load_environment_variables(env: str) -> None:
    if not os.path.exists(env):
        raise Exception(f"{env} does not exists")

    load_dotenv(env)


def connect_to_database() -> Connection:
    return psycopg.connect(
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT"),
        dbname=os.getenv("PG_NAME"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD"),
    )


def ensure_migrations_table_exists(conn: Connection) -> None:
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS schema_migrations (
                MigrationID BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                Filename TEXT UNIQUE NOT NULL,
                AppliedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
    conn.commit()


def get_applied_migrations(conn: Connection) -> set[str]:
    with conn.cursor() as cur:
        cur.execute("SELECT filename FROM schema_migrations;")
        return {row[0] for row in cur.fetchall()}


def apply_migrations(conn: Connection, file_path) -> None:
    filename = parse_filename(os.path.basename(file_path))
    with open(file_path, "r") as f:
        sql = f.read()
    with conn.cursor() as cur:
        cur.execute(sql)
        cur.execute(
            "INSERT INTO schema_migrations (Filename) VALUES (%s);",
            (filename),
        )
    cur.commit()


def parse_filename(filename: str) -> str:
    match = re.match(r"^(\d{8}_.+)\.sql$", filename)

    if not match:
        raise ValueError(
            f"Filename '{filename}' is not in the expected format: YYYYMMDD_filename.sql"
        )

    filename = match.group(1)

    return filename


def main():
    load_environment_variables(ENV_PATH)
    conn = connect_to_database()

    ensure_migrations_table_exists(conn)
    applied = get_applied_migrations(conn)
    file_list = sorted(os.listdir("migrations"))

    """
    This the main loop that applies the migrations to the database.
    I thought about abstracting this out to its own function but 
    decided against it because there's no major complexity here that 
    I want to develop or test separately. And there's no branching in it.
    """
    for file in all_files:
        if file.endswith(".sql") and file not in applied:
            apply_migrations(conn, os.path.join("migrations", file))

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM schema_migrations")
        rows = cur.fetchall()
        print(rows)

    print(applied)


if __name__ == "__main__":
    main()
