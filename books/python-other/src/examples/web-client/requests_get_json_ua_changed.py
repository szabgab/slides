import requests

res = requests.get('http://httpbin.org/user-agent',
    headers = {'User-agent': 'Internet Explorer/2.0'})
# print(res.headers['content-type'])
# print(res.text)

data = res.json()
print(data)
print(data['user-agent'])
