import boto3

iam = boto3.client('iam')

iam.create_user(UserName='new-user-boto')