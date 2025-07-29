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
query($username:String!, $from:DateTime, $to:DateTime, $first:Int) {
  user(login: $username) {
    contributionsCollection(from: $from, to: $to) {
      pullRequestContributions(first: $first) {
        nodes {
          pullRequest {
            title, url, createdAt, state, repository { name }
          }
        }
      }
    }
  }
}
'''

ts = datetime.datetime.now() - datetime.timedelta(days = 20)
variables = {
    "username": "szabgab",
    "first": 30,
    "from": "2013-04-20T00:00:00Z",
    "to": "2014-04-20T00:00:00Z"
}

transport = AIOHTTPTransport(url=url, headers=headers)
client = Client(transport=transport, fetch_schema_from_transport=True)
result = client.execute(gql(query), variable_values=variables)

if output_file:
    with open(output_file, 'w') as fh:
        json.dump(result, fh, indent=4)
else:
    print(result)



