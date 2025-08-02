import boto3

aws_profile = 'connect-prod-2'
aws_region = 'us-east-1'

session = boto3.Session(profile_name=aws_profile, region_name=aws_region)
client = session.client('s3')

response = client.get_object_acl(
    Bucket='ayushi_demo_bucket_1234'
)

print(response)