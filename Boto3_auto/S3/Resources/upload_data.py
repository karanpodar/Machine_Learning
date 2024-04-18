import boto3

s3 = boto3.resource('s3')

bucket = s3.Bucket(name='my-first-buck-boto')

bucket.upload_file(Filename='sample_s3_file.txt',
                   Key='sample-s3-file')