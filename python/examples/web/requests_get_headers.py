import requests
 
r = requests.get('http://httpbin.org/headers')
print(r.text)

# {
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.3.0 CPython/2.7.12 Darwin/16.3.0"
#   }
# }
