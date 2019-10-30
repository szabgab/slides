import requests
 
r = requests.get('http://httpbin.org/user-agent',
    headers = {'User-agent': 'Internet Explorer/2.0'})
print(r.headers['content-type'])
print(r.text)
data = r.json()
print(data)
print(data['user-agent'])
