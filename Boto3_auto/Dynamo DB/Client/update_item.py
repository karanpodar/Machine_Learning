import boto3

client = boto3.client('dynamodb', 'ap-south-1')

item_key = {
    'Title' : {'S' : 'The Matrix'},
    'Rating' : {'N' : '8'}
}

update = 'SET Director = :r'    # search 'update expressions' in documentation to know the syntax

response = client.update_item(
    TableName='Movies',
    Key=item_key,
    UpdateExpression=update,
    ExpressionAttributeValues={':r' : {'S' : 'Lana and Lilly'}}    
    )

print(response)