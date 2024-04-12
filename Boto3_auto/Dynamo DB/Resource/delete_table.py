import boto3

dynamodb = boto3.resource('dynamodb', 'ap-south-1')
table = dynamodb.Table('Movies')

table.delete()