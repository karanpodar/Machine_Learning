import boto3

s3 = boto3.client('s3')
paginator = s3.get_paginator('list_objects_v2')

results = paginator.paginate(Bucket='my-first-buck-boto')

print(list(results))

# to print all the Contents of each object
for item in results.search('Contents'):
    print(item)

# to print all the Keys of Contents of each object
for item in results.search('Contents'):
    print(item['Key'])