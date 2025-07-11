import json

def lambda_handler(event, context):
    with open('a.json') as fh:
       data = json.load(fh)
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps({ 'data' : data })
    }

