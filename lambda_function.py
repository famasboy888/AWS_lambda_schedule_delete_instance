import boto3
import logging

boto3.set_stream_logger('', logging.DEBUG)

def lambda_handler(event, context):
    regions = [
    'ap-northeast-1',
    'ap-northeast-2',
    'ap-south-1',
    'ap-southeast-1',
    'ap-southeast-2',
    'ca-central-1',
    'eu-central-1',
    'eu-north-1',
    'eu-west-1',
    'eu-west-2',
    'eu-west-3',
    'sa-east-1',
    'us-east-1',
    'us-east-2',
    'us-west-1',
    'us-west-2'
    ]
    
    for region in regions:
        ec2_client = boto3.client('ec2', region)
        all_instances = ec2_client.describe_instances()
        if all_instances:
            print("List all instances:")
            for reservation in all_instances['Reservations']:
                for instance in reservation['Instances']:
                    print(instance['InstanceId'] + "-" + instance['State']['Name'])
                    
                    if instance['State']['Name'] == 'running':
                        print("Stopping ec2: " + instance['InstanceId'])
                        ec2_client.terminate_instances(InstanceIds=[instance['InstanceId']])
