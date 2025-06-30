import os
import psycopg
from dotenv import load_dotenv

ENV_PATH = "../.env"


def load_environment_variables(env: str) -> None:
    if not os.path.exists(env):
        raise Exception(f"{env} does not exists")

    load_dotenv(env)


def main():
    load_environment_variables(ENV_PATH)


if __name__ == "__main__":
    main()
