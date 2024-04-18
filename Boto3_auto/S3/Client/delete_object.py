import boto3

client = boto3.client('s3')

client.delete_object(Bucket='my-first-buck-boto',
                     Key='sample-s3-file')