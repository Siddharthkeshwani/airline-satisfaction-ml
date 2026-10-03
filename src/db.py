import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


PROJECT_ROOT = Path(__file__).resolve().parent.parent
TABLE_NAME = "airline_passenger_satisfaction"

REQUIRED_SETTINGS = ["DB_USER","DB_PASSWORD","DB_HOST","DB_PORT","DB_NAME"]


def get_engine():
    load_dotenv(PROJECT_ROOT / ".env", override=True)

    missing = [name for name in REQUIRED_SETTINGS if not os.getenv(name)]
    if missing:
        raise ValueError(
            f"These settings are missing or empty in the .env file: {missing}. "
              "open .env, fill them in, save it, and try again."
        )    


    url = URL.create(
    "postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME"),
)

    return create_engine(url,pool_pre_ping=True)


def run_query(sql, engine=None, params=None):
    engine = engine or get_engine()
    return pd.read_sql(text(sql), engine, params=params)


def fetch_table(engine=None, table=TABLE_NAME):
    return run_query(f"select * from {table} ORDER BY id", engine=engine)


if __name__== "__main__":
    engine = get_engine()
    count = run_query(f"select count(*) as n from {TABLE_NAME}", engine)["n"][0]
    print(f"Connected. Rows in {TABLE_NAME}: {count}")


