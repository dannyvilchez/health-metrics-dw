import os
import psycopg
from psycopg import Connection
from dotenv import load_dotenv


ENV_FILENAME = ".env"
ENV_PATH = os.path.abspath(ENV_FILENAME)

PG_HOST = print(os.getenv("PG_HOST"))
PG_PORT = print(os.getenv("PG_PORT"))
PG_NAME = print(os.getenv("PG_NAME"))
PG_USER = print(os.getenv("PG_USER"))
PG_PASSWORD = print(os.getenv("PG_PASSWORD"))


def load_environment_variables(env: str) -> None:
    if not os.path.exists(env):
        raise Exception(f"{env} does not exists")

    load_dotenv(env)

def connect_to_database() -> Connection:
    return psycopg.connect(
        host = PG_HOST,
        port = PG_PORT,
        dbname = PG_NAME,
        user = PG_USER,
        password = PG_PASSWORD
    )

def main():
    load_environment_variables(ENV_PATH)
    conn = connect_to_database()
    
    with conn.cursor() as cur:
        cur.exectue("SELECT * FROM test_table;")
        rows = cur.fetchall()
        print(rows)


if __name__ == "__main__":
    main()
