import json
import boto3


def lambda_handler(event, context):
    client = boto3.client('s3')

    res = client.get_object(
        Bucket='szabgab',
        Key='abc.json',
    )
    #obj = res["Body"] # botocore.response.StreamingBody
    content = res["Body"].read()
    data = json.loads(content)
    
    
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        #'body': json.dumps({ 'res': str(res) }),
        #'body': json.dumps({ 'res': str(content) }),
        'body': json.dumps({ 'res': data }),

    }
