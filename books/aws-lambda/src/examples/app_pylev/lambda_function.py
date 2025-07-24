import json
import sys

sys.path.insert(0, 'pypi')
import pylev

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

    distance = pylev.levenshtein(event['queryStringParameters']['a'], event['queryStringParameters']['b'])
    

    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps({
            'a' : event['queryStringParameters']['a'],
            'b' : event['queryStringParameters']['b'],
            'distance': distance,
        })
    }

