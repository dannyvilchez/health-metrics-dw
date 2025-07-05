import os
import psycopg
from psycopg import Connection
from dotenv import load_dotenv


ENV_PATH = os.path.abspath(".env")
MIGRATION_PATH = os.path.abspath("migrations/")


def load_environment_variables(env: str) -> None:
    if not os.path.exists(env):
        raise Exception(f"{env} does not exist")

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


def apply_migrations(conn: Connection, file_path: str) -> None:
    filename = os.path.splitext(os.path.basename(file_path))[0]
    with open(file_path, "r") as f:
        sql = f.read()
    with conn.cursor() as cur:
        cur.execute(sql)
        cur.execute(
            "INSERT INTO schema_migrations (Filename) VALUES (%s);",
            (filename,),
        )
        print(f"Applied {filename} to database")
    conn.commit()

def main():
    load_environment_variables(ENV_PATH)
    conn = connect_to_database()

    ensure_migrations_table_exists(conn)
    applied = get_applied_migrations(conn)
    print("Applied: ", applied)
    file_list = sorted(os.listdir(MIGRATION_PATH))
    print("file list: ", file_list)

    """
    This the main loop that applies the migrations to the database.
    I thought about abstracting this out to its own function but 
    decided against it because there's no major complexity here that 
    I want to develop or test separately. And there's no branching in it.
    """
    
    for file in file_list:
        if file.endswith(".sql") and file not in applied:
            apply_migrations(conn, os.path.join(MIGRATION_PATH, file))

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM schema_migrations")
        rows = cur.fetchall()
        print(rows)



if __name__ == "__main__":
    main()

