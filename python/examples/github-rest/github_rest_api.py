import requests
import os


def get_from_github(url, expected=0, pages=False):
    token = os.environ.get('MY_GITHUB_TOKEN')
    if not token:
        print('Missing MY_GITHUB_TOKEN. Not collecting data from Github')
        return

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {token}',
        'X-GitHub-Api-Version': '2022-11-28',
    }

    if pages:
        per_page = 100 # default is 30 max is 100
        page = 1
        all_data = []
        while True:
            real_url = f"{url}?per_page={per_page}&page={page}"
            print(f"Fetching from {real_url}")
            data = requests.get(real_url, headers=headers).json()
            all_data.extend(data)
            print(f"Received {len(data)} Total {len(all_data)} out of an expected {expected}")
            page += 1
            if len(data) < per_page:
                break
    else:
        print(f"Fetching from {url}")
        all_data = requests.get(url, headers=headers).json()

    return all_data


