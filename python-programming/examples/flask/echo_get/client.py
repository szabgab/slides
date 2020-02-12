import requests

res = requests.get('http://localhost:5000/')
print(res.status_code)
print(res.text)

res = requests.get('http://localhost:5000/echo?text=Hello World!')
print(res.status_code)
print(res.text)
