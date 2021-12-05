import requests

res = requests.get('https://python.org/')
print(type(res))
print(res.status_code)
print(res.headers)
print(res.headers['content-type'])
# print(res.content)

