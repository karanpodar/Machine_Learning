import boto3

ec2 = boto3.resource('ec2', 'ap-south-1')

instance = ec2.create_instances(
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    ImageId = 'ami-05a5bb48beb785bf1'  # Look up in console
)

print(instance)