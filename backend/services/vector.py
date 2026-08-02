def vector_literal(vector):
    return "[" + ",".join(f"{x:.10f}" for x in vector) + "]"