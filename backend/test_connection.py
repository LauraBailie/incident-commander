from database import get_connection

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT now();")
        print(cur.fetchone())