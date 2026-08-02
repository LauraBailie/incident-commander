import json
from backend.services.search import similar_incidents
from backend.services.bedrock import chat


def investigate(question: str):

    incidents = similar_incidents(question)

    context = ""

    for incident in incidents:
        context += f"""
Title: {incident['title']}
Severity: {incident['severity']}
Status: {incident['status']}

Summary:
{incident['summary']}

-----------------------

"""

    prompt = f"""
You are an expert Site Reliability Engineer acting as an AI Incident Commander.

Current incident:

{question}

Relevant historical incidents:

{context}

Respond ONLY as valid JSON.

Use exactly this format:

{{
  "root_cause": "...",
  "immediate_actions": [
    "...",
    "..."
  ],
  "long_term_actions": [
    "...",
    "..."
  ],
  "confidence": 95
}}

Do not include markdown.
Do not wrap the JSON in ``` blocks.
"""

    response = chat(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    return json.loads(response)