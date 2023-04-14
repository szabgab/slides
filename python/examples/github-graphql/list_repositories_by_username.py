import sys
import json
import os
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

token = os.environ.get('MY_GITHUB_TOKEN')
headers = {
    'Authorization': f'Bearer {token}',
}

url = "https://api.github.com/graphql"

query = '''
query {
  repositoryOwner(login: "cm-demo") {
    repositories(first: 5, privacy: PUBLIC) {
      totalCount
      edges {
        node {
          id, name, isPrivate, description
        }
      }
    }
  }
}
'''

transport = AIOHTTPTransport(url=url, headers=headers)
client = Client(transport=transport, fetch_schema_from_transport=True)
result = client.execute(gql(query))

if len(sys.argv) == 2:
    with open(sys.argv[1], 'w') as fh:
        json.dump(result, fh, indent=4)
else:
    print(result)

