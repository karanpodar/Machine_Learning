import boto3

client = boto3.client('s3')

client.delete_bucket(Bucket='my-first-buck-boto')