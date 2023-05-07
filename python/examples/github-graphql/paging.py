import datetime
import argparse
import json
import os
import datetime
import sys
import requests

query = '''
query($after:String) {
  viewer {
    repositories(first: 100, after: $after, privacy: PUBLIC) {
      pageInfo {
        hasNextPage
        endCursor
      }
      nodes {
        name
        releases(last:1) {
          totalCount
          nodes {
            name
            publishedAt
            url
          }
        }
      }
    }
  }
}
'''

#    query = '''
#    query($username:String!, $from:DateTime, $to:DateTime, $first:Int) {
#      user(login: $username) {
#        contributionsCollection(from: $from, to: $to) {
#          issueContributions(first: $first) {
#            nodes {
#              issue {
#                title, url, createdAt, state, repository { name }
#              }
#            }
#          }
#        }
#      }
#    }
#    '''
#
#    ts = datetime.datetime.now() - datetime.timedelta(days = 20)
#    variables = {
#        "username": useranem,
#        "first": 30,
#        "from": start_date,
#        "to": end_date,
#    }
#
#    transport = AIOHTTPTransport(url=url, headers=headers)
#    client = Client(transport=transport, fetch_schema_from_transport=True)
#    result = client.execute(gql(query), variable_values=variables)
#
#    return result


def run_query(query, **variables):

    token = os.environ.get('MY_GITHUB_TOKEN')
    headers = {
        'Authorization': f'Bearer {token}',
    }

    #print(query)
    url = "https://api.github.com/graphql"
    res = requests.post(url, json={"query": query, "variables": variables}, headers=headers)
    # print(res.status_code)
    if res.status_code == 200:
        return res.json()
    print(f"Request failed with status_code: {res.status_code}")
    print(res.data)

def run_query_all(query):
    cursor = None
    nodes = []
    while True:
        results = run_query(query, after=cursor)
        # print(results)
        # print("------")
        nodes.extend(results['data']['viewer']['repositories']['nodes'])
        if not results['data']['viewer']['repositories']['pageInfo']['hasNextPage']:
            break
        cursor = results['data']['viewer']['repositories']['pageInfo']['endCursor']
    return nodes

def main():
    #args = get_args()
    today = datetime.date.today()
    #print(today)
    #print(today.weekday())
    #now = datetime.datetime.now()
    #print(now)
    end_ts = today - datetime.timedelta(days=today.weekday())
    start_ts = end_ts - datetime.timedelta(days=7)
    #print(end_ts)
    #print(start_ts)
    #username = "szabgab"
    #results = get_data(usernamem start_ts, end_ts)

    results = run_query_all(query)
    with open("out.json", "w") as fh:
        json.dump(results, fh, indent=4)

main()
