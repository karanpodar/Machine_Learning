import boto3

client = boto3.client('ec2', 'ap-south-1')

client.start_instances(InstanceIds=['i-087ff19afeaeab573'])