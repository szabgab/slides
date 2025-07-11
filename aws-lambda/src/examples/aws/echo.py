import json

def lambda_handler(event, context):
    name = event['queryStringParameters']['name']
    
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps({ 'message': 'Hello {}!'.format(name) })
    }

