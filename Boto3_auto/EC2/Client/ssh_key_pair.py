import boto3

client = boto3.client('ec2', 'ap-south-1')

key_pair = client.create_key_pair(KeyName='new-boto-key')   # to pass key name in creation of new instance

private_key = key_pair['KeyMaterial']

with open('my-key-pair.pem', 'w') as f:
    f.write(private_key)

security_groups = client.describe_security_groups()
print(security_groups['SecurityGroups'])            # to pass security group id in creation of new instance