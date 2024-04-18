import boto3

client = boto3.client('s3')

with open('sample_s3_file.txt', 'w') as file:
    file.write('Hello this is the sample file for S3 bucket')

client.upload_file(Filename='sample_s3_file.txt',
                   Bucket='my-first-buck-boto',
                   Key='sample-s3-file')