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
query($since:DateTime) {
  user(login: "szabgab") {
    issues(first: 1, filterBy: {since: $since}) {
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

variables = {
    "since": "2023-04-10T00:00:00Z"
}

transport = AIOHTTPTransport(url=url, headers=headers)
client = Client(transport=transport, fetch_schema_from_transport=True)
result = client.execute(gql(query), variable_values=variables)
print(result)



