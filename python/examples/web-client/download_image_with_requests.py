import requests

url = 'https://www.python.org/images/python-logo.gif'
filename = 'logo.gif'
res = requests.get(url)
print(res.status_code)
with open(filename, 'wb') as out:
    out.write(res.content)
