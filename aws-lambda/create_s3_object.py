import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('s3')
    
    res = client.put_object(
        Bucket='szabgab',
        Key='abc.json',
        Body=json.dumps({"name": "Foo"}),
    )
    
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps({ 'res': res })
    }
