import os
import psycopg
from psycopg import Connection
from dotenv import load_dotenv


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
                filename TEXT UNIQUE NOT NULL,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
    conn.commit()


def main():
    load_environment_variables(ENV_PATH)

    conn = connect_to_database()

    ensure_migrations_table_exists(conn)

    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO schema_migrations (filename) VALUES ('test_file');
        """)
        cur.execute("SELECT * FROM schema_migrations")
        rows = cur.fetchall()
        print(rows)


if __name__ == "__main__":
    main()
