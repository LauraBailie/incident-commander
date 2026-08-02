from pathlib import Path
import os

import psycopg
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

url = os.getenv("DATABASE_URL")

# SQLAlchemy URLs use the cockroachdb:// scheme.
# Psycopg expects a PostgreSQL scheme.
url = (
    url.replace("cockroachdb+psycopg://", "postgresql://")
       .replace("cockroachdb://", "postgresql://")
)

with psycopg.connect(url) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT now();")
        print("Connected!")
        print(cur.fetchone())

        cur.execute("SELECT version();")
        print(cur.fetchone())