import boto3

s3 = boto3.resource('s3')
list(s3.buckets.all())