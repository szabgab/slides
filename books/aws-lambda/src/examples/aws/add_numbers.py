import json

def lambda_handler(event, context):
    if 'queryStringParameters' not in event:
        return {
            'statusCode': 500,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps({ 'error': 'Missing queryStringParameters' })
        }
        
    
    if event['queryStringParameters'] == None or 'a' not in event['queryStringParameters'] or 'b' not in event['queryStringParameters']:
        return {
            'statusCode': 400,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps({ 'error': 'Missing field' })
        }
        
    result = int(event['queryStringParameters']['a']) + int(event['queryStringParameters']['b'])

    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps({
            'a' : event['queryStringParameters']['a'],
            'b' : event['queryStringParameters']['b'],
            'op' : '+',
            'result': result,
        })
    }

