import boto3

client = boto3.client('dynamodb', 'ap-south-1')

table_name = 'Movies'

attributes = [
    {
        'AttributeName' : 'Title',
        'AttributeType' : 'S'
    },
    {
        'AttributeName' : 'Rating',
        'AttributeType' : 'N'
    }
]

key_schema = [
    {
        'AttributeName' : 'Title',
        'KeyType' : 'HASH'
    },
    {
        'AttributeName' : 'Rating',
        'KeyType' : 'RANGE'
    }
]

provisioned_throughput = {
    'ReadCapacityUnits' : 5,
    'WriteCapacityUnits' : 5
}

response = client.create_table(TableName = table_name,
                               AttributeDefinitions = attributes,
                               KeySchema = key_schema,
                               ProvisionedThroughput = provisioned_throughput)

print(response)