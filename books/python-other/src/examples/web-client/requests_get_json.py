import requests

res = requests.get('http://httpbin.org/ip')
print(res.headers['content-type'])
print(res.text)
print()

data = res.json()
print(data)
print()
print(data['origin'])
