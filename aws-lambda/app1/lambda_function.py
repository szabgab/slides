import json
from mymod import add

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps({ 'data' : add(19, 23) })
    }

