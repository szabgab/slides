import requests

res = requests.get('http://localhost:5000/')
print(res.status_code)
print(res.text)


res = requests.post('http://localhost:5000/echo', data={"text": "Hello World!"})
print(res.status_code)
print(res.text)
