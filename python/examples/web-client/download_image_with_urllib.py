import urllib.request

url = 'https://www.python.org/images/python-logo.gif'
with urllib.request.urlopen(url) as fh:
    with open('logo.gif', 'wb') as out:
        out.write(fh.read())
