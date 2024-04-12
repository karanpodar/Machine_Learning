import boto3

client = boto3.client('dynamodb', 'ap-south-1')

entry = {
    'Title' : {'S' : 'The Matrix1'},
    'Director' : {'S' : 'Lana'},
    'Year' : {'N' : '1998'},
    'Rating' : {'N' : '8'}
}

response = client.put_item(TableName='Movies', Item=entry)

print(response)