import boto3

client = boto3.client('s3')

print(client.list_buckets())