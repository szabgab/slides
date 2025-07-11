import json
import mymodule

def lambda_handler(event, context):
    if 'queryStringParameters' not in event:
        return {
            'statusCode': 500,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps({ 'error': 'Missing queryStringParameters' })
        }
        
    
    if event['queryStringParameters'] == None or 'a' not in event['queryStringParameters'] or 'b' not in event['queryStringParameters'] or 'operation' not in event['queryStringParameters']:
        return {
            'statusCode': 400,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps({ 'error': 'Missing field' })
        }

    operation = event['queryStringParameters']['operation']
    if operation == 'add':
        result = mymodule.add(int(event['queryStringParameters']['a']), int(event['queryStringParameters']['b']))
        op = '+'
    elif operation == 'multiply':
        result = mymodule.multiply(int(event['queryStringParameters']['a']), int(event['queryStringParameters']['b']))
        op = '*'
    else:
        return {
            'statusCode': 400,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps({ 'error': 'Unsupported operation: "{}"'.format(operation) })
        }

    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps({
            'a' : event['queryStringParameters']['a'],
            'b' : event['queryStringParameters']['b'],
            'op' : op,
            'result': result,
        })
    }

