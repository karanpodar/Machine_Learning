import boto3

client = boto3.client('dynamodb', 'ap-south-1')

print(client.describe_table(TableName='Movies'))