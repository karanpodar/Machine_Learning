import boto3

s3 = boto3.resource('s3')

bucket = s3.Bucket(name='my-first-buck-boto')

bucket.download_file(Key='sample-s3-file',
                    Filename='download_sample.txt')

with open('download_sample.txt', 'r') as file:
    print(file.read())