import requests

res = requests.get('http://httpbin.org/user-agent')
#print(res.headers['content-type'])
#print(res.text)
data = res.json()
print(data)
print(data['user-agent'])
