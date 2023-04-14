import sys
import json
import os
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

if 2 <= len(sys.argv) <= 3:
    query_filename = sys.argv[1]
    if len(sys.argv) == 3:
        output_file = sys.argv[2]
    else:
        output_file = None
else:
    exit(f"Usage: {sys.argv[0]} QUERY_FILE [OUTPUT_FILE]")

with open(query_filename) as fh:
    query = fh.read()

token = os.environ.get('MY_GITHUB_TOKEN')
headers = {
    'Authorization': f'Bearer {token}',
}


url = "https://api.github.com/graphql"


transport = AIOHTTPTransport(url=url, headers=headers)
client = Client(transport=transport, fetch_schema_from_transport=True)
result = client.execute(gql(query))

if output_file:
    with open(output_file, 'w') as fh:
        json.dump(result, fh, indent=4)
else:
    print(result)

