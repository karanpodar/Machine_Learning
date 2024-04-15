import boto3

iam = boto3.client('iam')

print(iam.list_users())

result = iam.list_users()

print(result['Users'][0])
print(result['Users'][0]['UserName'])