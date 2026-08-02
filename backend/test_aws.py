import os
from pathlib import Path

import boto3
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

session = boto3.Session(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

print("Session region:", session.region_name)

sts = session.client("sts")

print(sts.get_caller_identity())