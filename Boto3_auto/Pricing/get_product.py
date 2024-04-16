import boto3

client = boto3.client('pricing', 'us-east-1')
result = client.get_products(ServiceCode='AmazonS3')

print(result)