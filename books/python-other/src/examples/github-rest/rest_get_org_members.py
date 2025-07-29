import json

from github_rest_api import get_from_github

orgid = 'github'
data = get_from_github(f"https://api.github.com/orgs/{orgid}/members")
with open("out.json", 'w') as fh:
    json.dump(data, fh, indent=4)
print(data)
