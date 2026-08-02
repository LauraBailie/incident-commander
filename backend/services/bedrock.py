import os
import json

import boto3

from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

client = boto3.client(
    "bedrock-runtime",
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

CHAT_MODEL = os.getenv("BEDROCK_CHAT_MODEL")

EMBED_MODEL = os.getenv("BEDROCK_EMBEDDING_MODEL")

def embed(text):

    body = {
        "inputText": text,
        "dimensions": 1024,
        "normalize": True
    }

    response = client.invoke_model(
        modelId=EMBED_MODEL,
        body=json.dumps(body)
    )

    result = json.loads(response["body"].read())

    return result["embedding"]

def chat(prompt):

    body = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = client.invoke_model(
        modelId=CHAT_MODEL,
        body=json.dumps(body)
    )

    result = json.loads(
        response["body"].read()
    )

    return result["output"]["message"]["content"][0]["text"]

def summarize_incident(title, description):

    prompt = f"""
You are an SRE incident commander.

Summarize this incident in 2 sentences.

Title:
{title}

Description:
{description}
"""

    return chat(prompt)