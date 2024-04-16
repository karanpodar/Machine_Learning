import boto3

iam = boto3.client('iam')

# make sure user is not attached to any group
iam.delete_user(UserName='new-user-boto')