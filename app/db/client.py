import boto3
from app.core.config import settings


def get_dynamodb_resource():
    return boto3.resource(
        "dynamodb",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION,
    )
