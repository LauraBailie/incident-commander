from backend.database import get_connection

def store_embedding(incident_id, summary, vector):

    vector_literal = "[" + ",".join(map(str, vector)) + "]"

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO embeddings
                (incident_id, embedding, summary)

                VALUES (%s, %s::VECTOR, %s)
                """,
                (
                    incident_id,
                    vector_literal,
                    summary,
                ),
            )

        conn.commit()