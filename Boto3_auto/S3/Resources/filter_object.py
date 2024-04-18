import boto3

s3 = boto3.resource('s3')

bucket = s3.Bucket(name='my-first-buck-boto')
print(bucket.objects.filter(Prefix='sam'))      #prefix of the key