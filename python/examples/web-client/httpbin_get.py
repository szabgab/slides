import requests

r = requests.get('http://httpbin.org/')
print(type(r))
print(r.status_code)
print(r.headers)
print(r.headers['content-type'])
# print(r.content)

