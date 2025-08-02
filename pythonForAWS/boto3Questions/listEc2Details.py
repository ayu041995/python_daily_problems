import boto3
from botocore.exceptions import ProfileNotFound

def analyze_ec2_instances(aws_profile, aws_region):
    try:
        session = boto3.Session(profile_name=aws_profile, region_name=aws_region)
        ec2_client = session.client('ec2')
    except ProfileNotFound:
        print(f"Profile '{aws_profile}' not found.")
        return []

    response = ec2_client.describe_instances()
    print(response)


def main():
    # ⬇ Set AWS profile and region here
    aws_profile = 'connect-prod-2'
    aws_region = 'us-east-1'

    data = analyze_ec2_instances(aws_profile, aws_region)

if __name__ == "__main__":
    main()