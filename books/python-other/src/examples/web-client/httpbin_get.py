import requests

res = requests.get('https://httpbin.org/get')
print(type(res))
print(res.status_code)
print()
print(res.headers)
print()
#print(res.content)
print()
print(res.json())
data = res.json()
print(type(data))

