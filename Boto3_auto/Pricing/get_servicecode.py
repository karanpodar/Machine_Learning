import boto3

client = boto3.client('pricing', 'us-east-1')
paginator = client.get_paginator('describe_services')

for page in paginator.paginate():
    for service in page['Services']:
        print(service['ServiceCode'])