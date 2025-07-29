import json
import sys

from github_rest_api import get_from_github

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} USERNAME")

username = sys.argv[1]

data = get_from_github(f"https://api.github.com/users/{username}")
with open("out.json", 'w') as fh:
    json.dump(data, fh, indent=4)
