import boto3

s3 = boto3.client('s3')

url = s3.generate_presigned_url(ClientMethod='get_object',
                                Params={
                                    'Bucket' : 'my-first-buck-boto',
                                    'Key' : 'sample-s3-file'
                                },
                                ExpiresIn=120)

print(url)