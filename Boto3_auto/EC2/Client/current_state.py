import boto3

client = boto3.client('ec2', 'ap-south-1')

describe = client.describe_instances(InstanceIds=['i-087ff19afeaeab573'])

# to check current state of the instance
print(describe['Reservations'][0]['Instances'][0]['State'])