import json
import os
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import datetime
import sys

if len(sys.argv) == 2:
    output_file = sys.argv[1]
else:
    output_file = None


token = os.environ.get('MY_GITHUB_TOKEN')
headers = {
    'Authorization': f'Bearer {token}',
}

url = "https://api.github.com/graphql"


query = '''
query($username:String!, $last:Int) {
  user(login: $username) {
    pullRequests(last: $last) {
      totalCount
      edges {
        node {
          number, title, state, createdAt, author { login }, url
        }
      }
    }
  }
}
'''

ts = datetime.datetime.now() - datetime.timedelta(days = 20)
variables = {
    "username": "szabgab",
    "last": 30,
}

transport = AIOHTTPTransport(url=url, headers=headers)
client = Client(transport=transport, fetch_schema_from_transport=True)
result = client.execute(gql(query), variable_values=variables)

if output_file:
    with open(output_file, 'w') as fh:
        json.dump(result, fh, indent=4)
else:
    print(result)



