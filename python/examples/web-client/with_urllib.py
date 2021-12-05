import urllib.request

# fh is like a filehandle
with urllib.request.urlopen('https://python.org/') as fh:
    html = fh.read()

print(html)
