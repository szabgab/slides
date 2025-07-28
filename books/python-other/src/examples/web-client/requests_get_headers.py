import requests

res = requests.get('https://httpbin.org/headers')
print(res.text)

# {
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.3.0 CPython/2.7.12 Darwin/16.3.0"
#   }
# }

print()
data = res.json()
print(data)
#print(data['headers'])
