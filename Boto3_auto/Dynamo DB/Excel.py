import boto3
import csv

client = boto3.client('dynamodb', 'ap-south-1')

table_name = 'netflix_titles'

attributes = [
    {
        'AttributeName' : 'show_id',
        'AttributeType' : 'S'
    },
    {
        'AttributeName' : 'release_year',
        'AttributeType' : 'N'
    }
]

key_schema = [
    {
        'AttributeName' : 'show_id',
        'KeyType' : 'HASH'
    },
    {
        'AttributeName' : 'release_year',
        'KeyType' : 'RANGE'
    }
]

provisioned_throughput = {
    'ReadCapacityUnits' : 10,
    'WriteCapacityUnits' : 10
}

attributes.append({
    "AttributeName": "country", "AttributeType" : "S"
    })

response = client.create_table(TableName = table_name,
                               AttributeDefinitions = attributes,
                               KeySchema = key_schema,
                               ProvisionedThroughput = provisioned_throughput,
                               GlobalSecondaryIndexes=[
        {
            'IndexName': 'idx1',
            'KeySchema': [
               {
                  'AttributeName': 'country',
                  'KeyType': 'HASH'
               }
             ],
             'Projection': {
               'ProjectionType': 'ALL'
             },
             'ProvisionedThroughput': {
                  'ReadCapacityUnits': 10,
                  'WriteCapacityUnits': 10
             }
        }])


print(response)

data_list = []

with open(r'Boto3_auto\netflix_titles.csv', 'r', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        data_list.append(row)

data_list = data_list[:100]

items_to_upload = []

for item in data_list:
   
    put_request = {"PutRequest": {"Item": {}}}
    for key, value in item.items():
        
        if not value:  # Some fields are empty and dynamo db cannot handle empty fields for keys
            value = "None"

        try:
            float(value)
            put_request["PutRequest"]["Item"][key] = {'N': value}
        except ValueError:
            put_request["PutRequest"]["Item"][key] = {'S': value}
         
    items_to_upload.append(put_request)

    if len(items_to_upload) == 25:  # Upload the batch when it consists of 25 elements
        response = client.batch_write_item(RequestItems={
                                                table_name: items_to_upload  
                                            }
                                          )
        items_to_upload = []