import json
import boto3
import os
from urllib.request import urlopen, Request


def lambda_handler(event, context):
    
    unauthorized_instances = []
    reqired_image_id = os.environ['required_ami_id']
    launched_instances = event['detail']['responseElements']['instancesSet']['items']
    user_name = event['detail']['userIdentity']['userName']
    for i in launched_instances:
        image_id = i['imageId']
        if image_id != reqired_image_id:
            unauthorized_instances.append(i['instanceId'])
    if unauthorized_instances != []:
        region = os.environ['region']
        ec2 = boto3.client('ec2', region_name=region)
        ec2.terminate_instances(InstanceIds=unauthorized_instances)
        print('terminated your instances: ' + str(unauthorized_instances))
        CHIME_HOOK_URL = os.environ['chime_hook_url']
        user_login = os.environ['user_login']
        message = {"Content": 'user {0} @{1}, you used the unauthorized AMI, please use the Amazon Linux 2!'.format(user_name, user_login)}
        req = Request(CHIME_HOOK_URL, json.dumps(message).encode('ascii'))
        with urlopen(req) as response:
            json_response = json.load(response)
    
    return {
        'statusCode': 200,
        'body': json.dumps('lambda Succeeded')
    }
