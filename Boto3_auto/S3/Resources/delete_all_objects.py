import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('my-first-buck-boto')

bucket.objects.all().delete()