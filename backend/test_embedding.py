from services.bedrock import embed

response = embed(
    "Payment API returning HTTP 500 errors."
)

vector = response["embedding"]

print(type(vector))
print(len(vector))