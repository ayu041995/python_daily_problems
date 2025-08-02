import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='ayushi_demo_bucket_1234'
)