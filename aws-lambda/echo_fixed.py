import json

def lambda_handler(event, context):
    if event['queryStringParameters'] == None or 'name' not in event['queryStringParameters']:
        return {
            'statusCode': 400,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps({ 'error': 'Missing "name" field' })
        }


    name = event['queryStringParameters']['name']

    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps({ 'message': 'Hello {}!'.format(name) })
    }
