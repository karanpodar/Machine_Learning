import boto3

s3 = boto3.client('s3')
waiter = s3.get_waiter('bucket_exists')

# This will run every 5 secs until a successful state is achieved. An error is return after 20 failed checks.
# to change the wait period -

wait_config = {'Delay' : 10,
               'MaxAttempts' : 30}

waiter.wait(Bucket='my-first-buck-boto', WaiterConfig=wait_config)