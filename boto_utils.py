import json
import boto3
from dotenv import load_dotenv

import os

def get_bucket_list():

    load_dotenv()

    aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    bucket_name = os.getenv("BUCKET_NAME")

    # Now you can use these variables in your code
    print(f"AWS Access Key: {aws_access_key}")
    print(f"AWS Secret Key: {aws_secret_key}")
    print(f"Bucket Name: {bucket_name}")

    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )
    
    response = s3_client.list_objects(Bucket=bucket_name)

    # print(response)

    for obj in response.get('Contents', []):
        print(obj['Key'])