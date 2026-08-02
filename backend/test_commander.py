from backend.services.commander import investigate

response = investigate(
    "Payment API returning HTTP 500 after deployment."
)

print(response)