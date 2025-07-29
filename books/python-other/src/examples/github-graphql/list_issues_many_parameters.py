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
query($since:DateTime, $first:Int, $user:String!) {
  user(login: $user) {
    issues(first: $first, filterBy: {since: $since}) {
      totalCount
      edges {
        node {
          number, title, state, createdAt, url, repository {
            owner {
              login
            }
          }
        }
      }
    }
  }
}
'''

ts = datetime.datetime.now() - datetime.timedelta(days = 20)
variables = {
    "user": "szabgab",
    "since": ts.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "first": 30,
}

transport = AIOHTTPTransport(url=url, headers=headers)
client = Client(transport=transport, fetch_schema_from_transport=True)
result = client.execute(gql(query), variable_values=variables)

if output_file:
    with open(output_file, 'w') as fh:
        json.dump(result, fh, indent=4)
else:
    print(result)



