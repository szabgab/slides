import datetime
import argparse
import json
import os
import datetime
import sys
import requests

query = '''
query ($organization: String!) {
  organization(login: $organization) {
    avatarUrl
    repositories(first: 2, after: null) {
      nodes {
        createdAt
        url
        pushedAt
        name
        watchers {
          totalCount
        }
        visibility
        updatedAt
        stargazers {
          totalCount
        }
      }
      totalCount
      pageInfo {
        endCursor
        hasNextPage
      }
    }
  }
}
'''

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

def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} ORGANIZATION")

    organization = sys.argv[1]
    results = run_query(query, organization=organization)
    with open("out.json", "w") as fh:
        json.dump(results, fh, indent=4)

main()
