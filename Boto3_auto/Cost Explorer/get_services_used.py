import boto3
from datetime import datetime, timedelta

client = boto3.client('ce')

start_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')
end_date = datetime.now().strftime('%Y-%m-%d')

print(start_date, end_date)

response = client.get_dimension_values(TimePeriod={
    'Start' : start_date,
    'End' : end_date
}, Dimension = 'SERVICE')

print(response)

for service in response['DimensionValues']:
    print(service['Value'])