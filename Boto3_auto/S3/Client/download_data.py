import boto3

client = boto3.client('s3')

client.download_file(Bucket='my-first-buck-boto',
                    Key='sample-s3-file',
                    Filename='download_sample.txt')

with open('download_sample.txt', 'r') as file:
    print(file.read())