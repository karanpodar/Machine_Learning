import boto3

iam = boto3.client('iam')

iam.add_user_to_group(UserName='new-user-boto',
                      GroupName='new-group-boto')