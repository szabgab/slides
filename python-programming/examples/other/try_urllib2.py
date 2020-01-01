import urllib2

# f is like a filehand for http requests
f = urllib2.urlopen('http://python.org/')
html = f.read()   # is like a get() request
f.close()
print(html)


try:
    f = urllib2.urlopen('http://python.org/some_missing_page')
    html = f.read()
    f.close()
    print(html)
except urllib2.HTTPError as e:
    print(e)   # HTTP Error 404: OK
