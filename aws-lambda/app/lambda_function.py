import json

def lambda_handler(event, context):
    data = None
    if 'queryStringParameters' in event and 'file' in event['queryStringParameters']:
        file = event['queryStringParameters']['file'] + '.json'
        if file in ['a.json', 'b.json', 'c.json']:
            try:
                with open(file) as fh:
                    data = json.load(fh)
            except Exception:
                pass
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps({ 'data' : data })
    }

