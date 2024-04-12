import boto3
from boto3.dynamodb.conditions import Key, Attr
from decimal import Decimal

# print(dir(Attr))      # to print the attriubte condiiton used for comparison 

dynamodb = boto3.resource('dynamodb', 'ap-south-1')
table = dynamodb.Table('Movies')

response = table.scan(
    FilterExpression=Attr('Year').gte(2000)
)

# print(response)
print(response['Items'])

response = table.scan(
    FilterExpression=Attr('Rating').lte(Decimal(7.5))       # for decimal values
)

# print(response)
print(response['Items'])