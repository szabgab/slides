import urllib

# f is like a filehand for http requests, but it cannot be user "with"
# Only works in Python 2
f = urllib.urlopen('http://python.org/')
html = f.read()   # is like a get() request
f.close()

print(html)


# retrieve a file and save it locally:
urllib.urlretrieve('http://www.python.org/images/python-logo.gif', 'logo.gif')
