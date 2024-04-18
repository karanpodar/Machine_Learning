import boto3
import paramiko

ec2 = boto3.resource('ec2', 'ap-south-1')
client = boto3.client('ec2', 'ap-south-1')

instance = ec2.create_instances(
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    ImageId = 'ami-05a5bb48beb785bf1',  # Look up in console
    KeyName = 'new-boto-key',           # from ssh_key_pair.py in client
    SecurityGroupIds = 'group-id'       # from ssh_key_pair.py in client
)

print(instance)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddpolicy())
private_key = paramiko.RSAKey(filename='my-key-pair.pem')     # from ssh_key_pair.py in client

describe = client.describe_instances(InstanceIds=['i-087ff19afeaeab573'])

print(describe)

ip = describe['Reservations'][0]['Instances'][0]['PublicIpAddress']

print(ip)

ssh.connect(hostname=ip, username='ubuntu', pkey=private_key)

stdin, stdout, stderr = ssh.exec_command('mkdir TestDir')
stdin, stdout, stderr = ssh.exec_command('ls')

print(stdout.read()) 