from services.search import similar_incidents
from services.bedrock import embed

vector = embed("Payment service returning HTTP 500")

print(type(vector))
print(vector[:5])

results = similar_incidents(
    "Payment service returning HTTP 500"
)

for row in results:
    print(row)