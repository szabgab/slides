import requests
 
r = requests.get('http://httpbin.org/user-agent')
print(r.headers['content-type'])
print(r.text)
data = r.json()
print(data)
print(data['user-agent'])
