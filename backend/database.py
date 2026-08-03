from pathlib import Path
import os

import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL not found.")

# Psycopg expects a PostgreSQL URL
DATABASE_URL = DATABASE_URL.replace(
    "cockroachdb://",
    "postgresql://",
    1
)

def get_connection():
    return psycopg.connect(
        DATABASE_URL + "&sslrootcert=system",
        row_factory=dict_row
    )