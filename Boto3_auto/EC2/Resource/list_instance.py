import boto3

ec2 = boto3.resource('ec2', 'ap-south-1')

print(list(ec2.instances.all()))