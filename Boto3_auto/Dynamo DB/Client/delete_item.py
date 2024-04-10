import boto3

client = boto3.client('dynamodb', 'ap-south-1')

item_key = {
    'Title' : {'S' : 'The Matrix'},
    'Rating' : {'N' : '8'}
}


response = client.delete_item(
    TableName='Movies',
    Key=item_key,
    )

print(response)