import json
import sys

sys.path.insert(0, 'pypi')
import requests

def lambda_handler(event, context):
    if 'queryStringParameters' not in event:
        return {
            'statusCode': 500,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps({ 'error': 'Missing queryStringParameters' })
        }
        
    
    if event['queryStringParameters'] == None or 'url' not in event['queryStringParameters']:
        return {
            'statusCode': 400,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps({ 'error': 'Missing field' })
        }

    r = requests.get(event['queryStringParameters']['url'])

    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps({
            'url' : event['queryStringParameters']['url'],
            'content': r.text,
        })
    }

