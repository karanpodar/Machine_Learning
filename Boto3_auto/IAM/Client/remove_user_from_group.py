import boto3

iam = boto3.client('iam')

iam.remove_user_from_group(UserName='new-user-boto',
                           GroupName='new-group-boto')