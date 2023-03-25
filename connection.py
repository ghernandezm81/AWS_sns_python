import boto3
from dotenv import load_dotenv
from os import getenv

load_dotenv()


sns_client = boto3.client("sns", aws_access_key_id=getenv("AKIA3YYMPKBD5SOGRXNY"),
                          aws_secret_access_key=getenv(
                              "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"),
                          region_name=getenv("us-east-2"))
