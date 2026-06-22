import boto3


ec2 = boto3.client('ec2')

# EC2 Instance ID
INSTANCE_ID = 'i-064f9bcb577af7c60'


def lambda_handler(event, context):

    response = ec2.start_instances(
        InstanceIds=[INSTANCE_ID]
    )

    return {
        'statusCode': 200,
        'body': 'Self-Healing Triggered: EC2 Instance Restarted'
    }
