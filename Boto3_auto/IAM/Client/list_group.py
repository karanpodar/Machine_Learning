import boto3

iam = boto3.client('iam')

print(iam.list_groups())

result = iam.list_users()

print(result)