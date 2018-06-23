import json
import boto3


def lambda_handler(event, context):
    client = boto3.client('s3')

    res = client.get_object(
        Bucket=event["Records"][0]['s3']['bucket']['name'],
        Key=event["Records"][0]['s3']['object']['key'],
    )
    content = res["Body"].read()
    data = json.loads(content)
    
    res = client.put_object(
        Bucket='szabgab',
        Key='out.json',
        Body=json.dumps({"data" : data, "event": event}),
    )

