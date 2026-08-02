from backend.database import get_connection
from backend.services.memory import store_embedding
from backend.services.bedrock import embed, summarize_incident

def create_incident(title, description, severity, status, service):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                INSERT INTO incidents
                (title, description, severity, status, service)
                VALUES (%s,%s,%s,%s,%s)
                RETURNING id
            """, (
                title,
                description,
                severity,
                status,
                service
            ))

            incident_id = cur.fetchone()["id"]

        conn.commit()

    try:
        summary = summarize_incident(
            title,
            description
        )

        print(summary)
        
        vector = embed(summary)
        
        print(type(vector))
        print(len(vector))
        print(vector[:5])

        store_embedding(
            incident_id,
            summary,
            vector
        )
    except Exception as e:
        print("Embedding failed:", e)

    return incident_id

def get_incident(id):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                SELECT *
                FROM incidents
                WHERE id=%s
            """, (id,))

            return cur.fetchone()
        
def list_incidents():

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                SELECT *
                FROM incidents
                ORDER BY created_at DESC
            """)

            return cur.fetchall()

def update_status(id, status):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                UPDATE incidents

                SET status=%s

                WHERE id=%s
            """, (
                status,
                id
            ))

        conn.commit()

def add_note(incident_id, author, note):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                INSERT INTO notes

                (incident_id, author, note)

                VALUES (%s,%s,%s)
            """, (
                incident_id,
                author,
                note
            ))

        conn.commit()
        
def add_resolution(incident_id, resolution, resolved_by):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                INSERT INTO resolutions

                (incident_id, resolution, resolved_by)

                VALUES (%s,%s,%s)
            """, (
                incident_id,
                resolution,
                resolved_by
            ))

        conn.commit()
        
def log_action(user, action):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                INSERT INTO audit_log

                ("user", action)

                VALUES (%s,%s)
            """, (
                user,
                action
            ))

        conn.commit()
        
def delete_incident(id):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                DELETE FROM incidents
                WHERE id=%s
                """,
                (id,)
            )

        conn.commit()
        
def get_notes(incident_id):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT *
                FROM notes
                WHERE incident_id=%s
                ORDER BY created_at
                """,
                (incident_id,)
            )

            return cur.fetchall()
        
def get_resolutions(incident_id):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT *
                FROM resolutions
                WHERE incident_id=%s
                """,
                (incident_id,)
            )

            return cur.fetchall()
        
