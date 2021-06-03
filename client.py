import boto3
from botocore.config import Config

import secrets
import config

s3 = boto3.client(
    service_name='s3',
    endpoint_url=config.HOST,
    aws_access_key_id=secrets.access_key,
    aws_secret_access_key=secrets.secret_keys,
)


sns = boto3.client(
    service_name='sns',
    endpoint_url=config.HOST,
    region_name='',
    aws_access_key_id=secrets.access_key,
    aws_secret_access_key=secrets.secret_keys,
    config=Config(signature_version='s3')
)
