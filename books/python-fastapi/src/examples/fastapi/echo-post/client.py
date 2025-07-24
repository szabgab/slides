import requests
res = requests.post('http://localhost:8000/',
    headers = {
        #'User-agent'  : 'Internet Explorer/2.0',
        'Content-type': 'application/json'
    },
    json = {"text": "Fast API"},
)
#print(res.headers['content-type'])
print(res.text)

