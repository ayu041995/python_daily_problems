import boto3

# Initialize a session using your specific region
region = 'your-region'  # e.g., 'us-west-2'
ec2 = boto3.client('ec2', region_name=region)

# Describe EC2 instances
response = ec2.describe_instances()

# Define instance types smaller than or equal to m5.large
allowed_instance_types = [
    't2.nano', 't2.micro', 't2.small', 't2.medium',
    't3.nano', 't3.micro', 't3.small', 't3.medium',
    't4g.micro', 't4g.small', 't4g.medium', 't4g.large',
    'm4.large', 'm4.xlarge', 'm4.2xlarge', 'm4.4xlarge',
    'm4.10xlarge', 'm4.16xlarge',
    'm5.large', 'm5.xlarge', 'm5.2xlarge', 'm5.4xlarge',
    'm5.12xlarge', 'm5.24xlarge'
]

# Process and print instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_type = instance['InstanceType']
        if instance_type in allowed_instance_types:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            name = None
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Name':
                    name = tag['Value']
            print(f"Instance ID: {instance_id}, Type: {instance_type}, State: {state}, Name: {name}")

