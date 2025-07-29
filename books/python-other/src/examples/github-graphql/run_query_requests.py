import sys
import json
import os
import requests

def run_query(query):
    token = os.environ.get('MY_GITHUB_TOKEN')
    headers = {
        'Authorization': f'Bearer {token}',
    }

    url = "https://api.github.com/graphql"
    res = requests.post(url, json={"query": query}, headers=headers)
    # print(res.status_code)
    if res.status_code == 200:
        return res.json()
    print(f"Request failed with status_code: {res.status_code}")
    print(res.data)

if __name__ == "__main__":
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
    result = run_query(query)

    if output_file:
        with open(output_file, 'w') as fh:
            json.dump(result, fh, indent=4)
    else:
        print(result)

