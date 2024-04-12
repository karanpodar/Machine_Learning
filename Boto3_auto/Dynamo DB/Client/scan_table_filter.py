import boto3

client = boto3.client('dynamodb', 'ap-south-1')

items = []

# we grab a key first
# this wont get all the keys for us
response = client.scan(
    TableName='Movies',
    FilterExpression='Rating >= :num',
    ExpressionAttributeValues={':num' : {'N' : '5'}}
    )

items.extend(response['Items'])

print(items)