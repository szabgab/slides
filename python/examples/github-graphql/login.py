import json
import os
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport


token = os.environ.get('MY_GITHUB_TOKEN')
headers = {
    'Authorization': f'Bearer {token}',
}

query = '''
query {
  viewer {
    login
  }
}
'''

url = "https://api.github.com/graphql"
transport = AIOHTTPTransport(url=url, headers=headers)
client = Client(transport=transport, fetch_schema_from_transport=True)
result = client.execute(gql(query))

print(result)

with open('out.json', 'w') as fh:
    json.dump(result, fh)


