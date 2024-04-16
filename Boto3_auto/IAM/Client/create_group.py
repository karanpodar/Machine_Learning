import boto3

iam = boto3.client('iam')

iam.create_group(GroupName='new-group-boto')