import boto3

client = boto3.client('dynamodb', 'ap-south-1')

items = []

# we grab a key first
# this wont get all the keys for us
response = client.scan(TableName='Movies')
items.extend(response['Items'])


# then to fetch for all keys we do this
while 'LastEvaluatedKey' in response.keys():

    response = client.scan(TableName='Movies', ExclusiveStartKey=response['LastEvaluatedKey'])
    items.extend(response['Items'])


print(items)