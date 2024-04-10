import boto3
from datetime import datetime, timedelta

client = boto3.client('ce')

start_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')
end_date = datetime.now().strftime('%Y-%m-%d')

print(start_date, end_date)

# CE finds cost based on Start date & End date

response = client.get_cost_and_usage(TimePeriod = {
    'Start' : start_date,
    'End' : end_date
}, Granularity = 'MONTHLY',
Metric = ['UnblendedCost'],
GroupBy = {
    'Type' : 'DIMENSION',
    'Key' : 'SERVICE'
})

print(response)

for item in response['ResultByTime']:
    print(item['TimePeriod'])
    for group in item['Groups']:
        service_name = group['Keys'][0]
        cost = group['Metrics']['unblended']['Amount']
        print(f'{service_name} : ${cost}')

        