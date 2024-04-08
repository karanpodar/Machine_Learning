import boto3
from datetime import datetime, timedelta

client = boto3.client('ce')

start_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
end_date = (datetime.now() + timedelta(days=32)).strftime('%Y-%m-%d')

print(start_date, end_date)

# CE finds cost based on Start date & End date

response = client.get_cost_forecast(TimePeriod = {
    'Start' : start_date,
    'End' : end_date
}, Granularity = 'MONTHLY',
Metric = 'UNBLENDED_COST')

print(response)