import json
import boto3


def lambda_handler(event, context):
    client = boto3.client('s3')
    response = client.list_objects(
        Bucket='szabgab',
    )
    objects = [ o['Key'] for o in response['Contents'] ]
    
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps({ 'objects': objects, 'res': str(response) })
    }
