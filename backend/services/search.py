from backend.database import get_connection
from backend.services.bedrock import embed

def similar_incidents(question, limit=5):

    vector = embed(question)
    
    vector_literal = "[" + ",".join(map(str, vector)) + "]"

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT
                    i.id,
                    i.title,
                    i.severity,
                    i.status,
                    e.summary,
                    e.embedding <=> %s::VECTOR AS distance

                FROM embeddings e
                JOIN incidents i
                ON e.incident_id = i.id

                ORDER BY distance

                LIMIT %s
                """,
                (
                    vector_literal,
                    limit
                ),
            )

            return cur.fetchall()